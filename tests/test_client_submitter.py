"""Tests for the remote Client progress log contract."""

from __future__ import annotations

import logging
from types import SimpleNamespace

from client_submitter import report_progress


def test_report_progress_logs_all_remote_states(caplog) -> None:
    progress = SimpleNamespace(
        batch_id="llmo-iteration-0001",
        completed=11,
        total=12,
        success=11,
        running=1,
        pending=0,
        retry_waiting=0,
        failed=0,
        canceled=0,
        not_found=0,
        elapsed_seconds=3921.7,
    )

    with caplog.at_level(logging.INFO, logger="client_submitter"):
        report_progress(progress)

    assert caplog.messages == [
        "远程批次进度：batch_id=llmo-iteration-0001, done=11/12, "
        "success=11, running=1, pending=0, retry=0, failed=0, canceled=0, "
        "not_found=0, waiting=1, elapsed_seconds=3921.7"
    ]
