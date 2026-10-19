"""Regression test for importing and recomputing the initial HFSS Parquet data."""

from pathlib import Path

import pandas as pd
import pytest

from llmo.config import load_config
from llmo.initial_data import import_initial_parquet
from llmo.intervals import variable_specs_from_config
from llmo.models import AntennaMetrics, CurveData, SampleRecord
from llmo.pools import SamplePools

root = Path(__file__).resolve().parents[1]


def test_initial_parquet_imports_40_rows_and_recomputes_metrics(tmp_path: Path) -> None:
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)
    source = root / "data" / "initial_samples" / "Sample_40_with_results.parquet"
    pools = SamplePools(tmp_path / "runtime", specs)

    assert import_initial_parquet(source, conf, specs, pools) == 40
    assert len(pools.records) == 40
    assert {record.source for record in pools.records} == {"initial_parquet"}
    assert {len(record.curve.frequency_ghz) for record in pools.records} == {401}
    assert {len(record.curve.s11_db) for record in pools.records} == {401}
    assert all(record.metrics.resonance_count in {0, 1, 2} for record in pools.records)
    assert len(pools.summary_path.read_text(encoding="utf-8").split("\n")) > 1


def make_remote_candidate() -> SampleRecord:
    return SampleRecord(
        sample_id="iteration_0001_01",
        variables={
            "a": 125.0,
            "b": 60.0,
            "l1": 30.0,
            "l2": 10.0,
            "l3": 30.0,
            "s1": 1.0,
            "s2": 5.0,
            "s3": 0.9,
            "f_l": 10.0,
        },
        curve=CurveData([2.0, 5.0], [-10.0, -11.0]),
        metrics=AntennaMetrics(
            s11_at_2_45=-10.0,
            s11_at_4_50=-11.0,
            resonance_count=2,
            is_dual_resonance=True,
            low_resonance_point=2.45,
            s11_at_low_resonance=-12.0,
            high_resonance_point=4.50,
            s11_at_high_resonance=-13.0,
            score=2.0,
        ),
        iteration=1,
        source="remote_hfss",
        metadata={"remote": {"task_id": "test-task"}},
    )


def test_resume_keeps_remote_candidates_and_does_not_reimport_initial_rows(
    tmp_path: Path,
) -> None:
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)
    source = root / "data" / "initial_samples" / "Sample_40_with_results.parquet"
    pools = SamplePools(tmp_path / "runtime", specs)
    assert import_initial_parquet(source, conf, specs, pools) == 40
    pools.add(make_remote_candidate())

    assert import_initial_parquet(source, conf, specs, pools) == 0

    assert len(pools.records) == 41
    assert {record.source for record in pools.records} == {
        "initial_parquet",
        "remote_hfss",
    }
    assert any(record.sample_id == "iteration_0001_01" for record in pools.records)


def test_changed_initial_parquet_is_rejected_without_mutating_pools(
    tmp_path: Path,
) -> None:
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)
    source = root / "data" / "initial_samples" / "Sample_40_with_results.parquet"
    pools = SamplePools(tmp_path / "runtime", specs)
    import_initial_parquet(source, conf, specs, pools)
    pools.add(make_remote_candidate())

    changed_source = tmp_path / "changed_initial.parquet"
    frame = pd.read_parquet(source)
    a_column = next(column for column in frame.columns if str(column).lower() == "a")
    first_index = frame.index[0]
    frame.at[first_index, a_column] = float(frame.at[first_index, a_column]) + 0.01
    frame.to_parquet(changed_source, index=False)

    full_before = pools.full_path.read_bytes()
    summary_before = pools.summary_path.read_bytes()
    with pytest.raises(ValueError, match="does not match the resumed sample pool"):
        import_initial_parquet(changed_source, conf, specs, pools)

    assert pools.full_path.read_bytes() == full_before
    assert pools.summary_path.read_bytes() == summary_before
    assert len(pools.records) == 41
