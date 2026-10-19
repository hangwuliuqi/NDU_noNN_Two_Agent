"""Regression tests for runtime prompt rendering and candidate normalization."""

import logging
from pathlib import Path

from llmo.agents import ExperienceSummaryAgent, SamplingGuidanceAgent
from llmo.config import load_config
from llmo.intervals import variable_specs_from_config
from llmo.llm_client import LlmConnectionError
from llmo.prompts import compact_sample_line

root = Path(__file__).resolve().parents[1]


class FakeClient:
    def __init__(self, response: dict) -> None:
        self.response = response
        self.prompt = ""

    def complete_json(self, prompt: str, iteration: int, mock_factory=None) -> dict:
        self.prompt = prompt
        return self.response


class HistoryFakeClient:
    def __init__(self, responses: list[dict]) -> None:
        self.responses = iter(responses)
        self.calls: list[dict] = []

    def complete_json(
        self,
        prompt: str,
        iteration: int,
        mock_factory=None,
        history_messages=None,
    ) -> dict:
        self.calls.append(
            {
                "prompt": prompt,
                "iteration": iteration,
                "history_messages": history_messages,
            }
        )
        return next(self.responses)


class SamplingRetryFakeClient:
    """Return a scripted response for each semantic sampling turn."""

    def __init__(self, responses: list[object]) -> None:
        self.responses = iter(responses)
        self.calls: list[dict] = []
        self.last_response_text = None
        self.last_error = None

    def complete_json(
        self,
        prompt: str,
        iteration: int,
        mock_factory=None,
        history_messages=None,
        attempt_limit=None,
    ) -> object:
        self.calls.append(
            {
                "prompt": prompt,
                "iteration": iteration,
                "history_messages": history_messages,
                "attempt_limit": attempt_limit,
            }
        )
        response = next(self.responses)
        if isinstance(response, Exception):
            # Model a low-level client that received a response body but could
            # not parse it as JSON. The agent should preserve that body in the
            # next conversation history pair.
            self.last_response_text = "not-json-response"
            self.last_error = response
            raise response
        self.last_response_text = None
        self.last_error = None
        return response


def sample_summary() -> dict:
    return {
        "rank": 1,
        "sample_id": "real_001",
        "source": "hfss",
        "variables": {
            "a": 125.0,
            "b": 60.0,
            "l1": 30.0,
            "l2": 10.0,
            "l3": 30.0,
            "s1": 1.0,
            "s2": 6.0,
            "s3": 0.9,
            "f_l": 10.0,
        },
        "score": 0.65,
        "s11_at_2_45": -12.0,
        "s11_at_4_50": -11.0,
        "resonance_count": 2,
        "is_dual_resonance": True,
        "low_resonance_point": 2.47,
        "s11_at_low_resonance": -14.0,
        "high_resonance_point": 4.46,
        "s11_at_high_resonance": -13.0,
        "iteration": 3,
    }


def candidate(index: int) -> dict:
    return {
        "variables": {
            "a": 999.0 if index == 0 else 125.123,
            "b": 60.123,
            "l1": 30.123,
            "l2": 10.123,
            "l3": 30.123,
            "s1": 1.123,
            "s2": 6.123,
            "s3": 0.923,
            "f_l": 10.123,
        },
        "rationale": "Expected to improve on the best historical sample.\nThis remains a hypothesis.",
        "rules_used": ["r-example"],
    }


def test_sampling_prompt_uses_runtime_config_and_repairs_candidates() -> None:
    conf = load_config(root / "project.conf", overrides=["optimization.proposals_per_iteration=2"])
    specs = variable_specs_from_config(conf)
    count = conf.get_int("optimization.proposals_per_iteration")
    client = FakeClient({"proposals": [candidate(index) for index in range(count)]})
    agent = SamplingGuidanceAgent(conf, specs, client, root, logging.getLogger("test"))
    top_sample = sample_summary()
    top_sample.pop("iteration")
    proposals = agent.propose(
        [top_sample],
        "# test guidebook",
        iteration=4,
        allowed_rule_ids={"r-example"},
    )
    assert len(proposals) == count
    assert f"generate exactly {count} legal candidate designs" in client.prompt
    assert "current variable design guidebook" in client.prompt
    assert "extracted design experience" not in client.prompt
    assert "one at 2.45 ghz and one at 4.50 ghz" in client.prompt
    threshold = conf.get_float("antenna.targets.s11_threshold_db")
    assert f"no higher than {threshold:.2f} db" in client.prompt
    assert '"top_sample_count": 1' in client.prompt
    assert "i(s11_at_2_45 > -10.00)" not in client.prompt
    assert "`s2`: [2.00, 10.00] mm" in client.prompt
    assert "compact sample contract" in client.prompt
    assert "{geom:{a:125.00,b:60.00" in client.prompt
    assert "{n_res:2} + {res:[[2.47,-14.00],[4.46,-13.00]]}" in client.prompt
    assert "{target_s11:{2.45:-12.00,4.50:-11.00}}" in client.prompt
    assert 'source:"hfss"' not in client.prompt
    assert '{rank:1}' in client.prompt
    assert "`n_res:1`" in client.prompt
    assert "n_res:0" in client.prompt
    assert "`rank:1` is the highest-ranked sample" in client.prompt
    assert "ranking-only score" in client.prompt
    assert "geom={a:value,b:value" in client.prompt
    assert "target_s11" in client.prompt
    assert "R is not a success condition" in client.prompt
    assert "example rule:" in client.prompt
    assert "# test guidebook" in client.prompt
    assert "variable design guidebook format:" in client.prompt
    assert "complete rule example:" in client.prompt
    assert "domain=global" in client.prompt
    assert "`u`=increase, `d`=decrease, and `k`=keep" in client.prompt
    assert "r-example" in client.prompt
    assert '"variable_design_guidebook"' not in client.prompt
    assert '"variable_ranges"' not in client.prompt
    excellent_s11 = conf.get_float("score.excellent_s11_db")
    assert f"q_band(s)=clip((-s)/abs({excellent_s11:.2f}),0,1)" in client.prompt
    assert "only the code decides whether optimization stops" not in client.prompt
    assert "exploration_type" not in client.prompt
    assert '"iteration"' not in client.prompt
    assert "exploration_type" not in proposals[0].__dict__
    assert proposals[0].rationale == (
        "Expected to improve on the best historical sample. This remains a hypothesis."
    )
    assert "{{" not in client.prompt
    assert 100.0 <= proposals[0].variables["a"] <= 150.0
    assert proposals[1].variables["a"] == 125.12
    assert proposals[1].variables["s2"] == 6.12


def test_sampling_prompt_and_parser_support_one_configured_candidate() -> None:
    conf = load_config(
        root / "project.conf",
        overrides=["optimization.proposals_per_iteration=1"],
    )
    specs = variable_specs_from_config(conf)
    client = FakeClient({"proposals": [candidate(1)]})
    agent = SamplingGuidanceAgent(conf, specs, client, root, logging.getLogger("test"))

    proposals = agent.propose(
        [sample_summary()],
        "# test guidebook",
        iteration=4,
        allowed_rule_ids={"r-example"},
    )

    assert len(proposals) == 1
    assert "generate exactly 1 legal candidate designs" in client.prompt
    assert "the array length must be exactly 1" in client.prompt.lower()


def test_sampling_correction_retries_accumulate_only_this_call_history() -> None:
    conf = load_config(
        root / "project.conf",
        overrides=["llm.max_connection_attempts=4", "optimization.proposals_per_iteration=2"],
    )
    specs = variable_specs_from_config(conf)
    count = conf.get_int("optimization.proposals_per_iteration")
    client = SamplingRetryFakeClient(
        [
            # First response has too few proposals.
            {"proposals": [candidate(1)]},
            # Second response has the right array length but one malformed item.
            {"proposals": [candidate(1), {"variables": {}, "rationale": "bad"}]},
            # Third response is valid and should end the correction loop.
            {"proposals": [candidate(1), candidate(1)]},
        ]
    )
    agent = SamplingGuidanceAgent(
        conf,
        specs,
        client,
        root,
        logging.getLogger("test"),
    )

    proposals = agent.propose(
        [sample_summary()],
        "# guidebook",
        iteration=11,
        allowed_rule_ids={"r-example"},
    )

    assert len(proposals) == count
    assert len(client.calls) == 3
    # Each failed semantic turn contributes exactly one user/assistant pair;
    # the third request therefore receives both previous pairs, but no older
    # iteration's conversation.
    assert client.calls[0]["history_messages"] is None
    assert len(client.calls[1]["history_messages"]) == 2
    assert len(client.calls[2]["history_messages"]) == 4
    assert client.calls[1]["history_messages"][0]["role"] == "user"
    assert client.calls[1]["history_messages"][1]["role"] == "assistant"
    assert "proposals" in client.calls[1]["history_messages"][1]["content"]
    assert "fewer candidates" in client.calls[1]["prompt"]
    assert f"TOP-{conf.get_int('optimization.top_k')}" in client.calls[1]["prompt"]
    assert f"exactly {count}" in client.calls[1]["prompt"]
    assert "schema" in client.calls[2]["prompt"]
    assert f"exactly {count}" in client.calls[2]["prompt"]
    # The low-level client receives one request per semantic turn, so it does
    # not hide invalid answers behind its own same-prompt retry loop.
    assert [call["attempt_limit"] for call in client.calls] == [1, 1, 1]


def test_sampling_malformed_json_response_is_added_verbatim_to_history() -> None:
    conf = load_config(
        root / "project.conf",
        overrides=["llm.max_connection_attempts=2", "optimization.proposals_per_iteration=2"],
    )
    specs = variable_specs_from_config(conf)
    count = conf.get_int("optimization.proposals_per_iteration")
    client = SamplingRetryFakeClient(
        [
            LlmConnectionError("response was not JSON"),
            {"proposals": [candidate(1), candidate(1)]},
        ]
    )
    agent = SamplingGuidanceAgent(
        conf,
        specs,
        client,
        root,
        logging.getLogger("test"),
    )

    proposals = agent.propose([sample_summary()], "# guidebook", iteration=12)

    assert len(proposals) == count
    assert len(client.calls) == 2
    history = client.calls[1]["history_messages"]
    assert len(history) == 2
    assert history[1] == {
        "role": "assistant",
        "content": "not-json-response",
    }
    assert "not one usable JSON object" in client.calls[1]["prompt"]
    assert f"TOP-{conf.get_int('optimization.top_k')}" in client.calls[1]["prompt"]


def test_sampling_transport_failure_retries_without_fabricating_history() -> None:
    conf = load_config(
        root / "project.conf",
        overrides=["llm.max_connection_attempts=2", "optimization.proposals_per_iteration=2"],
    )
    specs = variable_specs_from_config(conf)
    count = conf.get_int("optimization.proposals_per_iteration")

    class TransportThenSuccess(SamplingRetryFakeClient):
        def complete_json(
            self,
            prompt,
            iteration,
            mock_factory=None,
            history_messages=None,
            attempt_limit=None,
        ):
            self.calls.append(
                {
                    "prompt": prompt,
                    "iteration": iteration,
                    "history_messages": history_messages,
                    "attempt_limit": attempt_limit,
                }
            )
            if len(self.calls) == 1:
                self.last_response_text = None
                self.last_error = ConnectionError("gateway unavailable")
                raise LlmConnectionError("gateway unavailable")
            return {"proposals": [candidate(1), candidate(1)]}

    client = TransportThenSuccess([])
    agent = SamplingGuidanceAgent(
        conf,
        specs,
        client,
        root,
        logging.getLogger("test"),
    )
    proposals = agent.propose([sample_summary()], "# guidebook", iteration=13)

    assert len(proposals) == count
    assert len(client.calls) == 2
    assert client.calls[0]["prompt"] == client.calls[1]["prompt"]
    assert client.calls[1]["history_messages"] is None


def test_experience_prompt_uses_top_q_without_payload_block_or_previous_rules() -> None:
    conf = load_config(root / "project.conf", overrides=["optimization.top_q=7"])
    specs = variable_specs_from_config(conf)
    client = FakeClient({"summary": "insufficient evidence", "rules": []})
    agent = ExperienceSummaryAgent(conf, specs, client, root)
    top_sample = sample_summary()
    previous_rules = [{"rule": "r-0001-01", "confidence": 0.62}]
    agent.summarize(
        [top_sample],
        iteration=4,
        previous_active_rules=previous_rules,
    )
    assert "last_evaluated_sample" not in client.prompt
    assert "low_score_last" not in client.prompt
    assert "previous_active_rules" not in client.prompt
    assert "r-0001-01" not in client.prompt
    assert "# current evidence payload" not in client.prompt
    assert "payload_json" not in client.prompt
    assert '"source"' not in client.prompt
    assert "selected_rules_used" not in client.prompt
    assert "selected_design_rationale" not in client.prompt
    assert "return at most 8 rules" in client.prompt
    assert "low_resonance_point\": \"h\"" in client.prompt
    assert "s11_at_2_45\": \"d\"" in client.prompt
    assert '"confidence": 0.68' in client.prompt
    assert "separate evidence ledger" in client.prompt
    assert '"variable_ranges"' not in client.prompt
    assert "`s2`: [2.00, 10.00] mm" in client.prompt
    assert "R = 0.600000 * q_f + 0.400000 * q_s" in client.prompt
    assert "q_r1 = exp(-abs(r1 - 2.45) / 0.05)" in client.prompt
    assert "q_r2 = exp(-abs(r2 - 4.50) / 0.05)" in client.prompt
    assert "this placeholder is not a real resonance" in client.prompt
    assert "With one detected resonance, do not assume it belongs to the low band" in client.prompt
    assert "compact sample contract" in client.prompt
    assert '"top_q_sample_count": 1' not in client.prompt
    assert "diversity" not in client.prompt.lower()
    assert "top-k+m" not in client.prompt.lower()
    assert '"experience_evidence_count": 1' not in client.prompt
    assert "# TOP-7 evaluated samples" in client.prompt
    assert "TOP-Q" not in client.prompt
    assert "configured score-ranked TOP-7 evaluated samples" in client.prompt
    assert "supported by most relevant, comparable samples" in client.prompt
    assert "an individual sample may violate a rule" in client.prompt
    assert "ideally three or more" in client.prompt
    assert "diversity" not in client.prompt.lower()
    assert "top-k+m" not in client.prompt.lower()
    assert "experience guidebook rule contract:" in client.prompt
    assert "`domain` describes the starting-geometry region" in client.prompt
    assert "# last_evaluated_sample" not in client.prompt
    assert "{rank:none}" not in client.prompt
    assert "low_score_last" not in client.prompt
    assert "last_evaluated_sample_id" not in client.prompt
    assert '"source": ["sample_1"]' not in client.prompt
    assert "{geom:{a:125.00" in client.prompt
    assert "{{" not in client.prompt


def test_experience_correction_history_is_scoped_to_one_iteration() -> None:
    conf = load_config(root / "project.conf", overrides=["llm.max_connection_attempts=3"])
    specs = variable_specs_from_config(conf)
    client = HistoryFakeClient(
        [
            {"summary": "first", "rules": "wrong"},
            {"summary": "corrected", "rules": []},
            {"summary": "second iteration", "rules": []},
        ]
    )
    agent = ExperienceSummaryAgent(conf, specs, client, root)
    top_sample = sample_summary()

    agent.summarize([top_sample], iteration=4, previous_active_rules=[])
    assert len(client.calls) == 2
    assert client.calls[0]["history_messages"] is None
    assert len(client.calls[1]["history_messages"]) == 2
    assert "rules" in client.calls[1]["history_messages"][1]["content"]
    assert "JSON array" in client.calls[1]["prompt"]

    # A new summarize call starts a new iteration conversation. It must not
    # receive the previous iteration's correction pair.
    agent.summarize([top_sample], iteration=5, previous_active_rules=[])
    assert len(client.calls) == 3
    assert client.calls[2]["history_messages"] is None


def test_experience_rule_repair_keeps_full_conversation_history() -> None:
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)
    client = HistoryFakeClient(
        [
            {"summary": "first", "rules": [{"domain": {"l2": {"min": 14.5, "max": 15.5}}}]},
            {"summary": "corrected", "rules": []},
            {"summary": "corrected again", "rules": []},
        ]
    )
    agent = ExperienceSummaryAgent(conf, specs, client, root)
    top_sample = sample_summary()
    agent.summarize([top_sample], 4, [])
    agent.repair_invalid_rules(
        [top_sample],
        4,
        [],
        ["rule 1 domain l2=[14.5,15.5] is outside [5.0,15.0]"],
    )

    assert len(client.calls) == 2
    repair_call = client.calls[1]
    history = repair_call["history_messages"]
    assert len(history) == 2
    assert history[0]["role"] == "user"
    assert history[1]["role"] == "assistant"
    assert "first" in history[1]["content"]
    assert "domain l2=[14.5,15.5]" in repair_call["prompt"]
    assert "Return only the corrected JSON object" in repair_call["prompt"]


def test_prompt_uses_one_pair_for_single_resonance_without_zero_slot() -> None:
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)
    count = conf.get_int("optimization.proposals_per_iteration")
    client = FakeClient({"proposals": [candidate(index) for index in range(count)]})
    agent = SamplingGuidanceAgent(conf, specs, client, root, logging.getLogger("test"))
    single_sample = {
        **sample_summary(),
        "resonance_count": 1,
        "is_dual_resonance": False,
        "low_resonance_point": 4.48,
        "s11_at_low_resonance": -15.25,
        "high_resonance_point": 0.0,
        "s11_at_high_resonance": 0.0,
    }
    single_sample.pop("iteration")
    agent.propose([single_sample], "# test guidebook", iteration=4)
    assert "{n_res:1} + {res:[[4.48,-15.25]]}" in client.prompt
    assert "{res:[[4.48,-15.25],[0.00,0.00]]}" not in client.prompt


def test_compact_sample_line_adapts_to_zero_one_and_two_resonances() -> None:
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)

    no_resonance = {
        **sample_summary(),
        "resonance_count": 0,
        "is_dual_resonance": False,
        "low_resonance_point": 0.0,
        "s11_at_low_resonance": 0.0,
        "high_resonance_point": 0.0,
        "s11_at_high_resonance": 0.0,
    }
    single_resonance = {
        **sample_summary(),
        "resonance_count": 1,
        "is_dual_resonance": False,
        "low_resonance_point": 4.48,
        "s11_at_low_resonance": -15.25,
        "high_resonance_point": 0.0,
        "s11_at_high_resonance": 0.0,
    }

    no_line = compact_sample_line(no_resonance, specs, conf)
    single_line = compact_sample_line(single_resonance, specs, conf)
    dual_line = compact_sample_line(sample_summary(), specs, conf)

    assert "{geom:{a:125.00" in no_line
    assert "{n_res:0} + {res:[]}" in no_line
    assert "{n_res:1} + {res:[[4.48,-15.25]]}" in single_line
    assert "{n_res:2} + {res:[[2.47,-14.00],[4.46,-13.00]]}" in dual_line
    for line in (no_line, single_line, dual_line):
        assert "is_dual_resonance" not in line
        assert "low_resonance_point" not in line
        assert "high_resonance_point" not in line


def test_compact_sample_line_rejects_out_of_range_geometry() -> None:
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)
    sample = sample_summary()
    sample["variables"]["a"] = 999.0

    try:
        compact_sample_line(sample, specs, conf)
    except ValueError as exc:
        assert "outside" in str(exc)
    else:
        raise AssertionError("out-of-range geometry must be rejected")


def test_compact_sample_line_rejects_invalid_count_and_resonance_order() -> None:
    conf = load_config(root / "project.conf")
    specs = variable_specs_from_config(conf)

    invalid_count = {**sample_summary(), "resonance_count": 3}
    reversed_resonances = {
        **sample_summary(),
        "low_resonance_point": 4.46,
        "s11_at_low_resonance": -13.0,
        "high_resonance_point": 2.47,
        "s11_at_high_resonance": -14.0,
    }

    for sample, expected_message in (
        (invalid_count, "must be 0, 1, or 2"),
        (reversed_resonances, "ordered by increasing frequency"),
    ):
        try:
            compact_sample_line(sample, specs, conf)
        except ValueError as exc:
            assert expected_message in str(exc)
        else:
            raise AssertionError("invalid compact sample data must be rejected")
