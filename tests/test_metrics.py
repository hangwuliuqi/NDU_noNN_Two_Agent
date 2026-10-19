"""Regression tests for real HFSS curve metrics and stopping conditions."""

from pathlib import Path

import numpy as np

from llmo.config import load_config
from llmo.metrics import calculate_real_sample_score, calculate_ranking_score, evaluate_curve, meets_design_goal
from llmo.models import AntennaMetrics

root = Path(__file__).resolve().parents[1]


def test_target_s11_quality_uses_only_two_target_frequency_depths() -> None:
    conf = load_config(root / "project.conf")
    both_match = calculate_real_sample_score(-12.0, -12.0, conf)
    one_misses = calculate_real_sample_score(-12.0, -8.0, conf)
    assert one_misses < both_match


def test_target_s11_quality_weights_are_runtime_configurable() -> None:
    low_focused = load_config(
        root / "project.conf",
        [
            "score.low_band_weight=9.0",
            "score.high_band_weight=1.0",
        ],
    )
    high_focused = load_config(
        root / "project.conf",
        [
            "score.low_band_weight=1.0",
            "score.high_band_weight=9.0",
        ],
    )
    assert calculate_real_sample_score(-20.0, -2.0, low_focused) > calculate_real_sample_score(
        -20.0, -2.0, high_focused
    )


def test_dual_target_curve_meets_goal() -> None:
    conf = load_config(root / "project.conf")
    frequency = np.linspace(1.5, 5.5, 801)
    s11 = -1.0 - 19.0 / (1.0 + ((frequency - 2.45) / 0.06) ** 2)
    s11 -= 19.0 / (1.0 + ((frequency - 4.50) / 0.07) ** 2)
    metrics = evaluate_curve(frequency, s11, conf)
    assert metrics.resonance_count == 2
    assert metrics.is_dual_resonance
    assert abs(metrics.low_resonance_point - 2.45) < 0.02
    assert abs(metrics.high_resonance_point - 4.50) < 0.02
    assert meets_design_goal(metrics, conf)


def test_single_and_zero_resonance_metrics_use_zero_sentinels_and_cannot_stop() -> None:
    conf = load_config(root / "project.conf")
    frequency = np.linspace(1.5, 5.5, 801)

    single_curve = -1.0 - 19.0 / (1.0 + ((frequency - 4.50) / 0.07) ** 2)
    single = evaluate_curve(frequency, single_curve, conf)
    assert single.resonance_count == 1
    assert single.low_resonance_point == 4.5
    assert single.s11_at_low_resonance < -10.0
    assert single.high_resonance_point == 0.0
    assert single.s11_at_high_resonance == 0.0
    assert not meets_design_goal(single, conf)

    no_resonance = evaluate_curve(frequency, np.full_like(frequency, -1.0), conf)
    assert no_resonance.resonance_count == 0
    assert no_resonance.low_resonance_point == 0.0
    assert no_resonance.s11_at_low_resonance == 0.0
    assert no_resonance.high_resonance_point == 0.0
    assert no_resonance.s11_at_high_resonance == 0.0
    assert not meets_design_goal(no_resonance, conf)


def test_stop_is_code_controlled_by_target_resonances_and_score() -> None:
    conf = load_config(root / "project.conf", overrides=["antenna.targets.s11_threshold_db=-12.0"])
    metrics = AntennaMetrics(
        s11_at_2_45=-12.0,
        s11_at_4_50=-12.0,
        resonance_count=2,
        is_dual_resonance=True,
        low_resonance_point=2.45,
        s11_at_low_resonance=-18.0,
        high_resonance_point=4.50,
        s11_at_high_resonance=-18.0,
        score=0.0,
    )
    assert meets_design_goal(metrics, conf)
    metrics.s11_at_2_45 = -8.0
    assert not meets_design_goal(metrics, conf)


def test_ranking_score_separates_equal_s11_by_resonance_position() -> None:
    conf = load_config(root / "project.conf")
    aligned = calculate_ranking_score(-25.0, -25.0, 2.45, 4.50, conf)
    offset = calculate_ranking_score(-25.0, -25.0, 2.43, 4.48, conf)
    assert aligned > offset


def test_non_dual_resonance_penalty_is_configurable_and_only_hits_missing_second_resonance() -> None:
    base = load_config(root / "project.conf", overrides=["score.non_dual_resonance_penalty=0.0"])
    penalized = load_config(
        root / "project.conf",
        overrides=["score.non_dual_resonance_penalty=0.75"],
    )
    dual_base = calculate_ranking_score(-12.0, -12.0, 2.45, 4.50, base)
    dual_penalized = calculate_ranking_score(-12.0, -12.0, 2.45, 4.50, penalized)
    single_base = calculate_ranking_score(-12.0, -12.0, 2.45, 0.0, base)
    single_penalized = calculate_ranking_score(-12.0, -12.0, 2.45, 0.0, penalized)

    assert dual_penalized == dual_base
    assert single_penalized == single_base - 0.75


def test_non_dual_resonance_penalty_rejects_negative_configuration() -> None:
    conf = load_config(
        root / "project.conf",
        overrides=["score.non_dual_resonance_penalty=-1.0"],
    )
    try:
        calculate_ranking_score(-12.0, -12.0, 2.45, 0.0, conf)
    except ValueError as exc:
        assert "non_dual_resonance_penalty" in str(exc)
    else:
        raise AssertionError("negative non-dual penalty must be rejected")
