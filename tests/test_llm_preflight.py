"""Regression tests for the optional short LLM connectivity preflight."""

import json
import logging
from pathlib import Path
from types import SimpleNamespace

import pytest

from llmo.config import load_config
from llmo.llm_client import LlmClient
from llmo.run_logging import InteractionLogger

root = Path(__file__).resolve().parents[1]


def test_mock_preflight_is_logged_before_the_formal_llm_request(tmp_path: Path) -> None:
    conf = load_config(
        root / "project.conf",
        [
            'llm.sampling.provider="mock"',
            "llm.preflight.enabled=true",
            "llm.preflight.block_on_failure=true",
        ],
    )
    interactions = InteractionLogger(tmp_path / "llm_interactions.json")
    client = LlmClient("sampling", conf, interactions, logging.getLogger("test"))

    client.preflight_once(iteration=0)
    result = client.complete_json(
        "formal prompt",
        iteration=3,
        mock_factory=lambda: {"proposals": []},
    )
    second = client.complete_json(
        "formal prompt 2",
        iteration=4,
        mock_factory=lambda: {"proposals": []},
    )

    rows = json.loads(interactions.path.read_text(encoding="utf-8"))
    assert result == {"proposals": []}
    assert second == {"proposals": []}
    assert interactions.path.read_text(encoding="utf-8").startswith("[\n  {")
    assert [row["module"] for row in rows] == [
        "sampling_preflight",
        "sampling",
        "sampling",
    ]
    assert rows[0]["status"] == "success"
    assert rows[0]["response"] == '{"status":"ok"}'


def test_preflight_can_be_disabled(tmp_path: Path) -> None:
    conf = load_config(
        root / "project.conf",
        [
            'llm.sampling.provider="mock"',
            "llm.preflight.enabled=false",
        ],
    )
    interactions = InteractionLogger(tmp_path / "llm_interactions.json")
    client = LlmClient("sampling", conf, interactions, logging.getLogger("test"))

    client.complete_json("formal prompt", iteration=3, mock_factory=lambda: {"proposals": []})

    rows = json.loads(interactions.path.read_text(encoding="utf-8"))
    assert [row["module"] for row in rows] == ["sampling"]


class _FakeChat:
    def __init__(self, responses: list[object]) -> None:
        self.responses = iter(responses)

    def create(self, **_: object) -> object:
        return next(self.responses)


class _FakeClient:
    def __init__(self, responses: list[object]) -> None:
        self.chat = SimpleNamespace(completions=_FakeChat(responses))


def _response(
    content: str | None,
    *,
    finish_reason: str = "stop",
    reasoning_content: str | None = None,
    refusal: str | None = None,
    choices: list[object] | None = None,
) -> object:
    if choices is not None:
        return SimpleNamespace(
            id="resp-test",
            model="test-model",
            choices=choices,
            usage=None,
        )
    message = SimpleNamespace(
        content=content,
        reasoning_content=reasoning_content,
        refusal=refusal,
    )
    choice = SimpleNamespace(
        index=0,
        finish_reason=finish_reason,
        message=message,
    )
    return SimpleNamespace(
        id="resp-test",
        model="test-model",
        choices=[choice],
        usage=None,
    )


def _real_client(tmp_path: Path, overrides: list[str], fake: _FakeClient) -> tuple[LlmClient, Path]:
    conf = load_config(root / "project.conf", overrides)
    log_path = tmp_path / "llm_interactions.json"
    interactions = InteractionLogger(log_path)
    client = LlmClient("sampling", conf, interactions, logging.getLogger("test"))
    client._create_client = lambda *_args, **_kwargs: fake  # type: ignore[method-assign]
    return client, log_path


def test_preflight_retries_with_shared_attempt_limit(tmp_path: Path) -> None:
    fake = _FakeClient([
        _response(None),
        _response("   "),
        _response('{"status":"ok"}'),
    ])
    client, path = _real_client(
        tmp_path,
        [
            'llm.sampling.provider="openai"',
            'llm.sampling.api_key="test-key"',
            "llm.max_connection_attempts=3",
            "llm.retry_delay_seconds=0",
        ],
        fake,
    )

    client.preflight_once()
    rows = json.loads(path.read_text(encoding="utf-8"))
    assert [row["attempt"] for row in rows] == [1, 2, 3]
    assert [row["status"] for row in rows] == ["failed", "failed", "success"]
    assert rows[0]["diagnostics"]["content_state"] == "null"
    assert rows[1]["diagnostics"]["content_state"] == "blank"


def test_preflight_empty_content_fails_after_all_attempts(tmp_path: Path) -> None:
    fake = _FakeClient([_response(None), _response(None)])
    client, path = _real_client(
        tmp_path,
        [
            'llm.sampling.provider="openai"',
            'llm.sampling.api_key="test-key"',
            "llm.max_connection_attempts=2",
            "llm.retry_delay_seconds=0",
        ],
        fake,
    )

    with pytest.raises(Exception, match="after 2 attempts"):
        client.preflight_once()
    rows = json.loads(path.read_text(encoding="utf-8"))
    assert len(rows) == 2
    assert rows[-1]["diagnostics"]["content_is_none"] is True
    assert rows[-1]["diagnostics"]["content_length"] == 0


@pytest.mark.parametrize(
    ("response", "message", "diagnostic_key", "diagnostic_value"),
    [
        (
            _response(None, reasoning_content="hidden reasoning"),
            "reasoning_content is present",
            "reasoning_content_state",
            "nonempty",
        ),
        (
            _response("", finish_reason="length"),
            "may be truncated",
            "finish_reason",
            "length",
        ),
        (
            _response(None, refusal="not allowed"),
            "refusal",
            "refusal_state",
            "nonempty",
        ),
    ],
)
def test_preflight_diagnostic_variants(
    tmp_path: Path,
    response: object,
    message: str,
    diagnostic_key: str,
    diagnostic_value: str,
) -> None:
    fake = _FakeClient([response])
    client, path = _real_client(
        tmp_path,
        [
            'llm.sampling.provider="openai"',
            'llm.sampling.api_key="test-key"',
            "llm.max_connection_attempts=1",
        ],
        fake,
    )

    with pytest.raises(Exception, match=message):
        client.preflight_once()
    row = json.loads(path.read_text(encoding="utf-8"))[0]
    assert row["diagnostics"][diagnostic_key] == diagnostic_value


def test_preflight_empty_choices_is_diagnosed(tmp_path: Path) -> None:
    fake = _FakeClient([_response(None, choices=[])])
    client, path = _real_client(
        tmp_path,
        [
            'llm.sampling.provider="openai"',
            'llm.sampling.api_key="test-key"',
            "llm.max_connection_attempts=1",
        ],
        fake,
    )

    with pytest.raises(Exception, match="contains no choices"):
        client.preflight_once()
    row = json.loads(path.read_text(encoding="utf-8"))[0]
    assert row["diagnostics"]["choices_count"] == 0
