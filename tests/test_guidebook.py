"""Regression tests for rule-schema validation and snapshot replacement."""

import json
from pathlib import Path

import pytest

from llmo.config import load_config
from llmo.guidebook import GuidebookManager, GuidebookValidationError
from llmo.intervals import variable_specs_from_config

root = Path(__file__).resolve().parents[1]


def make_payload(
    lower: float,
    upper: float,
    confidence: float = 0.68,
) -> dict:
    return {
        "summary": "evidence-bounded current rule snapshot",
        "rules": [
            {
                "domain": {
                    "l1": {"min": lower, "max": upper},
                    "s1": {"min": 0.80, "max": 1.10},
                },
                "var_change": {"l1": "u", "s1": "d"},
                "effect": {
                    "low_resonance_point": "h",
                    "s11_at_2_45": "d",
                    "high_resonance_point": "l",
                    "s11_at_4_50": "s",
                },
                "confidence": confidence,
                "note": f"interaction for l1 between {lower} and {upper}",
            }
        ],
    }


def make_manager(tmp_path: Path, max_rules: int = 8) -> GuidebookManager:
    conf = load_config(root / "project.conf")
    return GuidebookManager(
        tmp_path,
        variable_specs_from_config(conf),
        max_active_rules=max_rules,
    )


def test_llm_rule_snapshot_replaces_previous_snapshot_immediately(tmp_path: Path) -> None:
    manager = make_manager(tmp_path)
    first = manager.replace_with_llm_rules(
        make_payload(25.0, 34.0, 0.61), 1, ["sample_1"]
    )
    assert len(first) == 1
    assert first[0].confidence == 0.61
    assert "rule=r-0001-01" in manager.text()

    second = manager.replace_with_llm_rules(
        make_payload(30.0, 39.0, 0.74), 2, ["sample_2"]
    )
    history = json.loads(manager.rules_path.read_text(encoding="utf-8"))
    assert len(second) == 1
    assert len(history) == 1
    assert history[0]["rule"] == "r-0002-01"
    assert history[0]["domain"]["l1"] == {"min": 30.0, "max": 39.0}
    assert history[0]["confidence"] == 0.74
    assert history[0]["source"] == ["sample_2"]
    assert "r-0001-01" not in manager.text()
    assert "confidence=0.74" in manager.text()


def test_each_successful_iteration_archives_a_guidebook_snapshot(
    tmp_path: Path,
) -> None:
    manager = make_manager(tmp_path)
    manager.replace_with_llm_rules(
        make_payload(25.0, 34.0, 0.61), 1, ["sample_1"]
    )
    first_path = manager.history_dir / "variable_design_guidebook_iteration_0001.md"
    first_text = first_path.read_text(encoding="utf-8")

    manager.replace_with_llm_rules(
        make_payload(30.0, 39.0, 0.74), 2, ["sample_2"]
    )
    second_path = manager.history_dir / "variable_design_guidebook_iteration_0002.md"
    second_text = second_path.read_text(encoding="utf-8")

    assert "rule=r-0001-01" in first_text
    assert first_path.read_text(encoding="utf-8") == first_text
    assert "rule=r-0002-01" in second_text
    assert manager.text() == second_text

    restarted = make_manager(tmp_path)
    assert restarted.text() == second_text
    assert sorted(path.name for path in restarted.history_dir.glob("*.md")) == [
        "variable_design_guidebook_iteration_0001.md",
        "variable_design_guidebook_iteration_0002.md",
    ]


def test_empty_rule_snapshot_is_also_archived(tmp_path: Path) -> None:
    manager = make_manager(tmp_path)
    manager.replace_with_llm_rules(
        {"summary": "no supported rules", "rules": []},
        3,
        ["sample_1"],
    )

    history_path = manager.history_dir / "variable_design_guidebook_iteration_0003.md"
    assert "active_rules=none" in history_path.read_text(encoding="utf-8")
    assert manager.text() == history_path.read_text(encoding="utf-8")


def test_code_only_validates_and_rounds_llm_confidence(tmp_path: Path) -> None:
    manager = make_manager(tmp_path)
    rules = manager.replace_with_llm_rules(
        make_payload(25.0, 34.0, 0.678), 3, ["sample_1", "sample_1"]
    )
    stored = manager.active_rules()[0]
    assert rules[0].confidence == 0.68
    assert stored["confidence"] == 0.68
    assert stored["source"] == ["sample_1"]
    assert "status" not in stored
    assert "version" not in stored
    assert "evidence" not in stored
    assert "last_updated_iteration" not in stored


@pytest.mark.parametrize("confidence", [-0.01, 1.01, float("nan")])
def test_invalid_llm_confidence_is_rejected(tmp_path: Path, confidence: float) -> None:
    manager = make_manager(tmp_path)
    with pytest.raises(ValueError, match="confidence"):
        manager.replace_with_llm_rules(
            make_payload(25.0, 34.0, confidence), 1, ["sample_1"]
        )


def test_effect_symbols_are_checked_by_metric_type(tmp_path: Path) -> None:
    manager = make_manager(tmp_path)
    wrong_resonance = make_payload(25.0, 34.0)
    wrong_resonance["rules"][0]["effect"]["low_resonance_point"] = "d"
    with pytest.raises(ValueError, match="resonance-point effects"):
        manager.replace_with_llm_rules(wrong_resonance, 1, ["sample_1"])

    wrong_s11 = make_payload(25.0, 34.0)
    wrong_s11["rules"][0]["effect"]["s11_at_2_45"] = "h"
    with pytest.raises(ValueError, match="s11 effects"):
        manager.replace_with_llm_rules(wrong_s11, 1, ["sample_1"])


def test_rule_count_cannot_exceed_configured_snapshot_limit(tmp_path: Path) -> None:
    manager = make_manager(tmp_path, max_rules=1)
    payload = make_payload(25.0, 34.0)
    payload["rules"].append(make_payload(30.0, 39.0)["rules"][0])
    with pytest.raises(ValueError, match="maximum is 1"):
        manager.replace_with_llm_rules(payload, 1, ["sample_1"])


def test_all_out_of_range_domains_are_reported_together(tmp_path: Path) -> None:
    manager = make_manager(tmp_path)
    payload = make_payload(25.0, 34.0)
    payload["rules"][0]["domain"] = {
        "l2": {"min": 14.5, "max": 15.5},
        "s3": {"min": 0.1, "max": 1.7},
    }

    with pytest.raises(GuidebookValidationError) as caught:
        manager.replace_with_llm_rules(payload, 1, ["sample_1"])

    message = str(caught.value)
    assert "domain l2=[14.5,15.5] is outside [5.0,15.0]" in message
    assert "domain s3=[0.1,1.7] is outside [0.2,1.6]" in message
