"""Regression tests for the optimizer-to-HFSS Parquet exchange contract."""

import json
import logging
from pathlib import Path

import pandas as pd

from llmo.config import allocate_run_directory, load_config, resolve_run_directory
from llmo.hfss_runner import add_design_variables, load_optimization_request
from llmo.intervals import variable_specs_from_config
from llmo.parquet_package import EVALUATED_SAMPLE_COLUMNS, read_evaluated_sample_package, write_evaluated_sample_package
from llmo.simulator import HfssSimulator

root = Path(__file__).resolve().parents[1]


def test_run_directory_uses_timestamp_and_avoids_same_minute_overwrite(tmp_path: Path) -> None:
    from datetime import datetime

    timestamp = datetime(2026, 8, 31, 17, 42)
    first = allocate_run_directory(tmp_path / "runtime", timestamp)
    second = allocate_run_directory(tmp_path / "runtime", timestamp)
    assert first.name == "runtime_0831_1742"
    assert second.name == "runtime_0831_1742_01"


def test_named_output_and_resume_directories_are_explicit_and_safe(tmp_path: Path) -> None:
    output, resuming = resolve_run_directory(
        tmp_path, Path("runtime"), "experiment_a", None
    )
    assert output == tmp_path / "experiment_a"
    assert output.is_dir()
    assert not resuming

    resumed, resuming = resolve_run_directory(
        tmp_path, Path("runtime"), None, "experiment_a"
    )
    assert resumed == output
    assert resuming

    try:
        resolve_run_directory(tmp_path, Path("runtime"), "experiment_a", None)
    except FileExistsError:
        pass
    else:
        raise AssertionError("a new run must not overwrite an existing output directory")


def candidate_variables() -> dict[str, float]:
    return {
        "a": 125.0,
        "b": 60.0,
        "l1": 30.0,
        "l2": 10.0,
        "l3": 32.0,
        "s1": 1.1,
        "s2": 5.5,
        "s3": 0.8,
        "f_l": 11.0,
    }


def test_optimizer_request_injects_exactly_nine_hfss_variables(tmp_path: Path) -> None:
    request_path = tmp_path / "iteration_0007.json"
    output_path = tmp_path / "iteration_0007.parquet"
    request_path.write_text(
        json.dumps(
            {
                "iteration": 7,
                "variables": candidate_variables(),
                "expected_output_parquet": str(output_path),
            }
        ),
        encoding="utf-8",
    )

    iteration, variables, expected_output = load_optimization_request(request_path)
    assert iteration == 7
    assert variables == candidate_variables()
    assert expected_output == output_path

    fake_hfss: dict[str, str] = {}
    add_design_variables(fake_hfss, variables)
    assert fake_hfss["a"] == "125.00mm"
    assert fake_hfss["b"] == "60.00mm"
    assert fake_hfss["L1"] == "30.00mm"
    assert fake_hfss["L2"] == "10.00mm"
    assert fake_hfss["L3"] == "32.00mm"
    assert fake_hfss["S1"] == "1.10mm"
    assert fake_hfss["S2"] == "5.50mm"
    assert fake_hfss["S3"] == "0.80mm"
    assert fake_hfss["f_l"] == "11.00mm"

    # These are fixed values from the uploaded, locally validated script.
    assert fake_hfss["h_sub"] == "1.6mm"
    assert fake_hfss["S"] == "3.0mm"
    assert fake_hfss["G"] == "0.42mm"
    assert fake_hfss["t"] == "0.035mm"
    assert fake_hfss["wave_length"] == "150.0mm"
    assert fake_hfss["port_w"] == "S + 2*G + 12mm"
    assert fake_hfss["port_h"] == "h_sub + 10mm"


def test_pyaedt_mode_builds_bundled_runner_command_without_launching_hfss(
    tmp_path: Path,
) -> None:
    conf = load_config(
        root / "project.conf",
        [
            f'project.runtime_dir="{tmp_path.as_posix()}/runtime"',
            f'simulation.request_dir="{tmp_path.as_posix()}/requests"',
            f'simulation.response_dir="{tmp_path.as_posix()}/responses"',
            f'simulation.pyaedt.project_dir="{tmp_path.as_posix()}/projects"',
            "simulation.pyaedt.non_graphical=true",
        ],
    )
    simulator = HfssSimulator(
        conf,
        tmp_path / "runtime",
        variable_specs_from_config(conf),
        logging.getLogger("test"),
    )
    command = simulator._build_pyaedt_command(
        tmp_path / "requests" / "iteration_0001.json",
        tmp_path / "responses" / "iteration_0001.parquet",
    )
    assert command[1:3] == ["-m", "llmo.hfss_runner"]
    assert "--config" not in command
    assert "--request-json" in command
    assert "--output-parquet" in command
    assert "--project-dir" in command
    assert command[command.index("--version") + 1] == "2023.2"
    assert "--solve" not in command
    assert "--non-graphical" in command
    assert "--close" not in command


def test_hfss_fixed_model_and_solve_parameters_match_pso_runner() -> None:
    text = (root / "llmo" / "hfss_runner.py").read_text(encoding="utf-8")
    conf = load_config(root / "project.conf")
    assert conf.get("simulation.pyaedt.geometry", None) is None
    assert conf.get("simulation.pyaedt.setup", None) is None
    assert "SUBSTRATE_THICKNESS_MM = 1.6" in text
    assert "CPW_SIGNAL_WIDTH_MM = 3.0" in text
    assert "CPW_GAP_MM = 0.42" in text
    assert "COPPER_THICKNESS_MM = 0.035" in text
    assert "AIRBOX_REFERENCE_WAVELENGTH_MM = 150.0" in text
    assert "SUBSTRATE_RELATIVE_PERMITTIVITY = 4.3" in text
    assert "SUBSTRATE_LOSS_TANGENT = 0.02" in text
    assert 'SETUP_NAME = "Setup_PSO"' in text
    assert 'SWEEP_NAME = "Sweep_PSO"' in text
    assert "SETUP_FREQUENCY_GHZ = 4.0" in text
    assert "MAXIMUM_PASSES = 30" in text
    assert "MAX_DELTA_S = 0.02" in text
    assert "SWEEP_START_GHZ = 2.0" in text
    assert "SWEEP_STOP_GHZ = 6.0" in text
    assert "SWEEP_STEP_GHZ = 0.01" in text
    assert 'integration_line=hfss.axis_directions.ZNeg' in text
    assert '"S1+S2+S3+f_l"' in text
    assert "validate_full_design" not in text
    assert "create_report" not in text
    main_body = text.split("def main() -> None:", 1)[1]
    first_save = main_body.index("hfss.save_project()")
    second_save = main_body.index("hfss.save_project()", first_save + 1)
    positions = [
        main_body.index("add_design_variables(hfss, optimized_variables)"),
        main_body.index("create_geometry(hfss)"),
        main_body.index("create_setup(hfss)"),
        first_save,
        main_body.index("hfss.analyze_setup(SETUP_NAME)"),
        second_save,
        main_body.index("frequency, s11 = export_s11(hfss)"),
        main_body.index("_release(hfss)"),
        main_body.index("write_evaluated_sample_package("),
    ]
    assert positions == sorted(positions)
    assert "👉" not in text
    assert "🎉" not in text
    assert "📊" not in text


def test_evaluated_sample_parquet_has_ordered_geometry_and_curve_vectors(tmp_path: Path) -> None:
    package_path = tmp_path / "iteration_0007.parquet"
    variables = candidate_variables()
    write_evaluated_sample_package(package_path, variables, [2.5, 2.0], [-12.0, -3.0])

    frame = pd.read_parquet(package_path)
    assert tuple(frame.columns) == EVALUATED_SAMPLE_COLUMNS
    assert len(frame) == 1
    assert all(frame.iloc[0][name] == variables[name] for name in EVALUATED_SAMPLE_COLUMNS[:9])
    assert list(frame.iloc[0]["Frequency_GHz"]) == [2.5, 2.0]
    assert list(frame.iloc[0]["S11_dB"]) == [-12.0, -3.0]

    stored_variables, curve = read_evaluated_sample_package(package_path, variables)
    assert stored_variables == variables
    assert curve.frequency_ghz == [2.0, 2.5]
    assert curve.s11_db == [-3.0, -12.0]


def test_mock_response_is_a_parquet_package_with_requested_geometry(tmp_path: Path) -> None:
    conf = load_config(
        root / "project.conf",
        [
            'simulation.mode="mock"',
            f'simulation.request_dir="{tmp_path.as_posix()}/requests"',
            f'simulation.response_dir="{tmp_path.as_posix()}/responses"',
        ],
    )
    simulator = HfssSimulator(
        conf,
        tmp_path / "runtime",
        variable_specs_from_config(conf),
        logging.getLogger("test"),
    )
    variables = candidate_variables()
    curve = simulator.simulate(variables, iteration=7)
    package_path = tmp_path / "responses" / "iteration_0007.parquet"
    frame = pd.read_parquet(package_path)
    assert tuple(frame.columns) == EVALUATED_SAMPLE_COLUMNS
    assert frame.iloc[0]["a"] == variables["a"]
    assert len(curve.frequency_ghz) == len(curve.s11_db) == conf.get_int("simulation.mock.frequency_points")
