"""Regression tests for durable full-pool and ranked-summary-pool behavior."""

import json
from pathlib import Path

from llmo.config import load_config
from llmo.intervals import normalized_vector, variable_specs_from_config
from llmo.models import AntennaMetrics, CurveData, SampleRecord
from llmo.json_utils import dumps_readable
from llmo.pools import SamplePools

root = Path(__file__).resolve().parents[1]


def test_readable_json_keeps_vectors_horizontal_and_objects_indented() -> None:
    text = dumps_readable({"frequency_ghz": [1, 2, 3], "records": [{"score": 0.5}]})
    assert '"frequency_ghz": [1, 2, 3]' in text
    assert '"records": [\n' in text
    assert json.loads(text)["frequency_ghz"] == [1, 2, 3]


def make_record(
    sample_id: str,
    score: float,
    iteration: int,
    variable_overrides: dict[str, float] | None = None,
) -> SampleRecord:
    variables = {
        "a": 125.0,
        "b": 60.0,
        "l1": 30.0,
        "l2": 10.0,
        "l3": 30.0,
        "s1": 1.0,
        "s2": 5.0,
        "s3": 0.9,
        "f_l": 10.0,
    }
    variables.update(variable_overrides or {})
    metrics = AntennaMetrics(
        s11_at_2_45=-12.0,
        s11_at_4_50=-12.0,
        resonance_count=2,
        is_dual_resonance=True,
        low_resonance_point=2.45,
        s11_at_low_resonance=-12.0,
        high_resonance_point=4.5,
        s11_at_high_resonance=-12.0,
        score=score,
    )
    return SampleRecord(sample_id, variables, CurveData([2.0, 5.0], [-1.0, -1.0]), metrics, iteration, "test")


def test_experience_summaries_method_removed_from_public_pool_api(tmp_path: Path) -> None:
    """The experience view must preserve elites and add samples from outside them.

    All variables use their configured ranges when distance is calculated.  The
    elite is at the centre of the design space, while the two extreme ``a``
    values are equally far from it.  Their scores deliberately break the first
    max-min tie; after the first extreme is selected, the opposite extreme is
    still farther away than the centre-near candidate.
    """
    conf = load_config(root / "project.conf")
    pools = SamplePools(tmp_path, variable_specs_from_config(conf))
    pools.add_many(
        [
            make_record("elite", 1.0, 1),
            make_record("far_low", 0.10, 2, {"a": 100.0}),
            make_record("far_high", 0.80, 3, {"a": 150.0}),
            make_record("near", 0.70, 4, {"a": 126.0}),
        ]
    )

    assert not hasattr(pools, "experience_summaries")


def test_ranked_summaries_clamps_to_available_samples(tmp_path: Path) -> None:
    conf = load_config(root / "project.conf")
    pools = SamplePools(tmp_path, variable_specs_from_config(conf))
    pools.add(make_record("only", 0.5, 0))

    selected = pools.ranked_summaries(limit=10)
    assert [item["sample_id"] for item in selected] == ["only"]


def test_ranked_summaries_returns_only_requested_top_q(tmp_path: Path) -> None:
    conf = load_config(root / "project.conf")
    pools = SamplePools(tmp_path, variable_specs_from_config(conf))
    pools.add_many([make_record("one", 0.9, 0), make_record("two", 0.8, 0)])

    selected = pools.ranked_summaries(limit=1, exclude_iteration=True)

    assert [item["sample_id"] for item in selected] == ["one"]
    assert "iteration" not in selected[0]


def test_ranked_summaries_does_not_add_extra_geometry(tmp_path: Path) -> None:
    """A repeated evaluation remains one of the ordinary ranked summaries."""
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)
    pools = SamplePools(tmp_path, specs)
    pools.add_many(
        [
            make_record("elite", 1.0, 1),
            # Same nine variable values as the elite, but a different sample ID
            # and score. It remains an ordinary ranked record.
            make_record("elite_repeat", 0.95, 2),
            make_record("far", 0.10, 3, {"a": 150.0}),
        ]
    )

    selected = pools.ranked_summaries(limit=1)
    assert [item["sample_id"] for item in selected] == ["elite"]


def test_ranked_summaries_keeps_score_order_for_repeated_geometries(
    tmp_path: Path,
) -> None:
    """Repeated evaluations of one non-elite design count as one region."""
    conf = load_config(root / "project.conf")
    pools = SamplePools(tmp_path, variable_specs_from_config(conf))
    pools.add_many(
        [
            make_record("elite", 1.0, 1),
            make_record("far_a_1", 0.20, 2, {"a": 100.0}),
            make_record("far_a_2", 0.19, 3, {"a": 100.0}),
            make_record("far_b", 0.18, 4, {"a": 150.0}),
        ]
    )

    selected = pools.ranked_summaries(limit=3)
    assert [item["sample_id"] for item in selected] == ["elite", "far_a_1", "far_a_2"]


def test_design_distance_normalizes_each_configured_variable_range() -> None:
    """A full-range change has equal normalized scale in every dimension."""
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)
    centre = {
        name: (spec.minimum + spec.maximum) / 2.0
        for name, spec in specs.items()
    }
    a_high = dict(centre)
    a_high["a"] = specs["a"].maximum
    s1_high = dict(centre)
    s1_high["s1"] = specs["s1"].maximum

    centre_vector = normalized_vector(centre, specs)
    a_vector = normalized_vector(a_high, specs)
    s1_vector = normalized_vector(s1_high, specs)
    a_distance = sum((left - right) ** 2 for left, right in zip(centre_vector, a_vector))
    s1_distance = sum((left - right) ** 2 for left, right in zip(centre_vector, s1_vector))

    assert a_distance == s1_distance == 0.25


def test_summary_is_ranked_and_sampling_view_removes_iteration(tmp_path: Path) -> None:
    conf = load_config(root / "project.conf")
    pools = SamplePools(tmp_path, variable_specs_from_config(conf))
    pools.add(make_record("low", 0.2, 1))
    pools.add(make_record("high", 0.8, 2))
    ranked = pools.ranked(exclude_iteration=True)
    assert [item["sample_id"] for item in ranked] == ["high", "low"]
    assert "iteration" not in ranked[0]
    assert ranked[0]["variables"]["a"] == 125.0
    assert ranked[0]["source"] == "test"
    assert ranked[0]["resonance_count"] == 2


def test_complete_pool_keeps_all_records_while_summary_keeps_top_40(
    tmp_path: Path,
) -> None:
    conf = load_config(root / "project.conf")
    pools = SamplePools(
        tmp_path,
        variable_specs_from_config(conf),
        summary_pool_size=40,
    )
    pools.add_many(
        [make_record(f"sample_{index:03d}", float(index), index) for index in range(40)]
    )
    pools.add_many(
        [
            make_record("new_best", 100.0, 41),
            make_record("new_low", -1.0, 41),
        ]
    )

    complete = json.loads(pools.full_path.read_text(encoding="utf-8"))
    summary = json.loads(pools.summary_path.read_text(encoding="utf-8"))

    assert len(complete) == 42
    assert len(summary) == 40
    assert complete[0]["sample_id"] == "new_best"
    assert complete[-1]["sample_id"] == "new_low"
    assert summary[0]["sample_id"] == "new_best"
    assert "sample_000" not in {item["sample_id"] for item in summary}
    assert "new_low" not in {item["sample_id"] for item in summary}


def test_complete_and_summary_pool_use_sample_id_as_score_tiebreaker(
    tmp_path: Path,
) -> None:
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)
    pools = SamplePools(tmp_path, specs, summary_pool_size=2)
    pools.add_many(
        [
            make_record("tie_b", 0.8, 1),
            make_record("low", 0.1, 1),
            make_record("tie_a", 0.8, 1),
        ]
    )

    complete = json.loads(pools.full_path.read_text(encoding="utf-8"))
    summary = json.loads(pools.summary_path.read_text(encoding="utf-8"))
    assert [item["sample_id"] for item in complete] == ["tie_a", "tie_b", "low"]
    assert [item["sample_id"] for item in summary] == ["tie_a", "tie_b"]

    reloaded = SamplePools(tmp_path, specs, summary_pool_size=2)
    assert [record.sample_id for record in reloaded.records] == ["tie_a", "tie_b", "low"]


def test_refresh_ranking_scores_persists_formula_migration(tmp_path: Path) -> None:
    conf = load_config(root / "project.conf")
    pools = SamplePools(tmp_path, variable_specs_from_config(conf))
    pools.add(make_record("old", 0.2, 1))

    changed = pools.refresh_ranking_scores(lambda metrics: metrics.score + 0.5)

    assert changed == 1
    assert json.loads(pools.full_path.read_text(encoding="utf-8"))[0]["metrics"]["score"] == 0.7
    assert json.loads(pools.summary_path.read_text(encoding="utf-8"))[0]["score"] == 0.7


def test_refresh_ranking_scores_reorders_both_persisted_pools(tmp_path: Path) -> None:
    conf = load_config(root / "project.conf")
    pools = SamplePools(
        tmp_path,
        variable_specs_from_config(conf),
        summary_pool_size=1,
    )
    pools.add_many(
        [
            make_record("low", 0.2, 1),
            make_record("high", 0.8, 1),
        ]
    )

    changed = pools.refresh_ranking_scores(lambda metrics: 1.0 - metrics.score)

    assert changed == 2
    complete = json.loads(pools.full_path.read_text(encoding="utf-8"))
    summary = json.loads(pools.summary_path.read_text(encoding="utf-8"))
    assert [item["sample_id"] for item in complete] == ["low", "high"]
    assert [item["sample_id"] for item in summary] == ["low"]


def test_batch_write_preserves_metadata_only_in_complete_pool(tmp_path: Path) -> None:
    conf = load_config(root / "project.conf")
    pools = SamplePools(tmp_path, variable_specs_from_config(conf))
    first = make_record("first", 0.2, 0)
    second = make_record("second", 0.8, 0)
    first.metadata = {"original_field": {"solver": "hfss"}}
    pools.add_many([first, second])

    assert pools.full_path.name == "complete_information_pool.json"
    assert pools.summary_path.name == "sample_summary_pool.json"
    complete = json.loads(pools.full_path.read_text(encoding="utf-8"))
    summary = json.loads(pools.summary_path.read_text(encoding="utf-8"))
    assert len(complete) == len(summary) == 2
    full_text = pools.full_path.read_text(encoding="utf-8")
    assert full_text.startswith("[\n  {")
    complete_by_id = {item["sample_id"]: item for item in complete}
    assert complete_by_id["first"]["metadata"]["original_field"]["solver"] == "hfss"
    assert "metadata" not in summary[0]
    assert "curve" not in summary[0]


def test_complete_pool_requires_a_standard_json_array(tmp_path: Path) -> None:
    conf = load_config(root / "project.conf")
    pool_path = tmp_path / "complete_information_pool.json"
    pool_path.write_text(json.dumps(make_record("invalid", 0.3, 0).to_dict()), encoding="utf-8")
    try:
        SamplePools(tmp_path, variable_specs_from_config(conf))
    except TypeError as exc:
        assert "JSON array" in str(exc)
    else:
        raise AssertionError("complete pool must reject a non-array JSON document")
