"""Regression tests for zero, single, and dual-resonance detection."""

from pathlib import Path

import numpy as np

from find_resonance_points import find_two_resonances


def test_uploaded_resonance_detector_is_kept_as_a_standalone_module() -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "find_resonance_points.py").read_text(encoding="utf-8")
    assert "def find_two_resonances(" in text
    assert "min_saddle_rise_db" in text
    assert '"resonance_count": 1' in text
    assert "resonance_freq_1_ghz" in text
    assert "resonance_freq_2_ghz" in text


def test_detector_returns_zero_one_or_two_resonances_with_zero_sentinels() -> None:
    frequency = np.linspace(1.5, 5.5, 801)

    no_resonance = find_two_resonances(frequency, np.full_like(frequency, -1.0))
    assert no_resonance["resonance_count"] == 0
    assert no_resonance["resonance_freq_1_ghz"] == 0.0
    assert no_resonance["resonance_s11_1_db"] == 0.0
    assert no_resonance["resonance_freq_2_ghz"] == 0.0
    assert no_resonance["resonance_s11_2_db"] == 0.0

    single_curve = -1.0 - 19.0 / (1.0 + ((frequency - 2.45) / 0.06) ** 2)
    single = find_two_resonances(frequency, single_curve)
    assert single["resonance_count"] == 1
    assert single["resonance_freq_1_ghz"] == 2.45
    assert single["resonance_s11_1_db"] < -10.0
    assert single["resonance_freq_2_ghz"] == 0.0
    assert single["resonance_s11_2_db"] == 0.0

    dual_curve = single_curve - 19.0 / (1.0 + ((frequency - 4.50) / 0.07) ** 2)
    dual = find_two_resonances(frequency, dual_curve)
    assert dual["resonance_count"] == 2
    assert dual["is_dual_resonance"]
    assert dual["resonance_freq_1_ghz"] == 2.45
    assert dual["resonance_freq_2_ghz"] == 4.5
