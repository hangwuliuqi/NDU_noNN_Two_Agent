"""Regression tests for variable bounds, rounding, and invalid-value repair."""

import logging
from pathlib import Path

import numpy as np
import pytest

from llmo.config import load_config
from llmo.models import CandidateProposal
from llmo.optimizer import OptimizationEngine
from llmo.pools import SamplePools
from llmo.intervals import (
    annotate_variables,
    repair_candidate_variables,
    variable_specs_from_config,
)

root = Path(__file__).resolve().parents[1]


def test_summary_annotation_keeps_continuous_values_without_regions() -> None:
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)
    annotated = annotate_variables(
        {name: 0.5 * (spec.minimum + spec.maximum) for name, spec in specs.items()},
        specs,
        decimal_places=2,
    )
    assert annotated["a"] == 125.0
    assert annotated["s1"] == 1.0
    assert all(isinstance(value, float) for value in annotated.values())


def test_one_proposal_per_iteration_is_valid_configuration() -> None:
    conf = load_config(
        root / "project.conf",
        overrides=[
            "optimization.proposals_per_iteration=1",
            "optimization.mock_sampling_global_proposal_count=1",
        ],
    )
    engine = OptimizationEngine.__new__(OptimizationEngine)
    engine.conf = conf
    engine.specs = variable_specs_from_config(conf)
    engine._validate_config()


def test_summary_pool_size_must_cover_top_k_and_top_q() -> None:
    conf = load_config(
        root / "project.conf",
        overrides=["optimization.summary_pool_size=20"],
    )
    engine = OptimizationEngine.__new__(OptimizationEngine)
    engine.conf = conf
    engine.specs = variable_specs_from_config(conf)

    with pytest.raises(ValueError, match="summary_pool_size"):
        engine._validate_config()


def test_all_variable_names_are_lowercase() -> None:
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)
    assert set(specs) == {"a", "b", "l1", "l2", "l3", "s1", "s2", "s3", "f_l"}
    assert specs["s2"].minimum == 2.0
    assert specs["s2"].maximum == 10.0


def test_out_of_range_candidate_values_are_randomly_repaired_and_rounded() -> None:
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)
    raw = {
        "a": 999.0,
        "b": 60.1234,
        "l1": 30.555,
        "l2": 10.0,
        "l3": 30.0,
        "s1": 1.0,
        "s2": -7.0,
        "s3": 0.9,
        "f_l": 10.0,
    }
    repairs = []
    result = repair_candidate_variables(
        raw,
        specs,
        np.random.default_rng(42),
        decimal_places=2,
        on_repair=lambda name, old, new: repairs.append((name, old, new)),
    )
    assert {item[0] for item in repairs} == {"a", "s2"}
    assert specs["a"].minimum <= result["a"] <= specs["a"].maximum
    assert specs["s2"].minimum <= result["s2"] <= specs["s2"].maximum
    assert result["b"] == 60.12
    assert result["l1"] == 30.55


def test_duplicate_candidates_are_perturbed_and_kept_for_ranking(tmp_path: Path) -> None:
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)
    base = {name: 0.5 * (spec.minimum + spec.maximum) for name, spec in specs.items()}
    first = CandidateProposal(dict(base), "first", candidate_index=1, original_variables=dict(base))
    duplicate = CandidateProposal(dict(base), "duplicate", candidate_index=2, original_variables=dict(base))
    engine = OptimizationEngine.__new__(OptimizationEngine)
    engine.conf = conf
    engine.specs = specs
    engine.pools = SamplePools(tmp_path / "runtime", specs)
    engine.logger = logging.getLogger("test")

    repaired = engine._repair_duplicate_proposals([first, duplicate], iteration=3)

    assert len(repaired) == 2
    assert not repaired[0].duplicate_with_history_or_round
    assert repaired[1].duplicate_with_history_or_round
    assert repaired[1].perturbation_random_numbers
    assert repaired[1].variables != base


def test_duplicate_perturbation_alpha_is_read_from_config(tmp_path: Path) -> None:
    def perturb(alpha: float, directory: str) -> tuple[dict[str, float], dict[str, float]]:
        conf = load_config(
            root / "project.conf",
            [f"optimization.duplicate_perturbation_alpha={alpha}"],
        )
        specs = variable_specs_from_config(conf)
        base = {
            name: 0.5 * (spec.minimum + spec.maximum)
            for name, spec in specs.items()
        }
        engine = OptimizationEngine.__new__(OptimizationEngine)
        engine.conf = conf
        engine.specs = specs
        engine.pools = SamplePools(tmp_path / directory, specs)
        engine.logger = logging.getLogger("test")
        proposals = [
            CandidateProposal(dict(base), "first", candidate_index=1),
            CandidateProposal(dict(base), "duplicate", candidate_index=2),
        ]
        result = engine._repair_duplicate_proposals(proposals, iteration=3)[1]
        return base, result.variables

    base, small = perturb(0.05, "small")
    _, large = perturb(0.20, "large")
    assert any(abs(large[name] - base[name]) > abs(small[name] - base[name]) for name in base)
