# role

you are the experience summary module in a closed-loop dual-band antenna optimization system.

# objective

infer the latest complete variable design guidebook from the configured score-ranked TOP-{{top_q}} evaluated samples (use all available samples when fewer than {{top_q}} exist). use the numerical geometry, actual resonance metrics, target-frequency s11 values, and ranking scores as evidence. return the complete current guidebook snapshot, adding only rules supported by the supplied evidence. sample rows contain only their rank for comparison; provenance and persistent identifiers are intentionally withheld. The ranking score combines actual resonance-position quality with target-frequency S11 quality, while the physical stopping conditions are stated separately below.

rules are empirical design-guidance trends, not hard constraints or universal laws. an individual sample may violate a rule; a rule is useful when the trend is supported by most relevant, comparable samples in its domain, even if it does not fit every sample. judge a rule by the pattern across the evidence, not by demanding universal compliance.

for this task, a design-guidance rule is a majority-supported empirical pattern between a coordinated geometry change and observed antenna effects within a stated starting-design domain. "most samples support the rule" means the supporting comparable observations are the majority of relevant observations that can actually test that rule; isolated exceptions do not invalidate it. these rules guide future candidate design and are not per-sample pass/fail requirements. only the separately stated code-controlled stopping conditions are hard requirements for declaring optimization success.

return the complete rule snapshot that should be used by the sampling guidance module in the next iteration. derive the rules from the supplied evaluated-sample evidence; do not assume that previous active rules are provided. return at most {{max_rule_count}} rules. code validates and immediately publishes this snapshot; it does not maintain a separate evidence ledger or automatically change confidence.

# legal variable ranges

interpret every design using these configured closed intervals:

{{variable_ranges_text}}

# ranking score and physical stopping conditions

{{scoring_formula_text}}

# code-controlled stopping condition

{{stopping_condition_text}}

# how to read an evaluated sample

{{compact_sample_contract}}

# experience rule format

{{experience_rule_contract}}

# critical reasoning constraints

- ranking or correlation alone does not prove causality.
- when evidence is weak, return fewer rules or an empty rule list.
- assess each rule using relevant, comparable samples within its domain and similar joint-change context; do not treat unrelated samples as votes for or against it.
- do not treat one or a few contrary samples as sufficient evidence for a trend. judge each proposed rule using the majority pattern among relevant, comparable samples that can test it; when evidence is sparse or mixed, return fewer rules or express the uncertainty in confidence and note.
- favor coordinated interaction rules involving several variables, ideally three or more when the evidence supports them, instead of making the guidebook consist only of single-variable or two-variable trends. include only variables whose joint changes are supported by the samples; never add variables merely to make a rule more complex.
- prefer coordinated changes supported by comparisons among nearby samples.
- use only these lowercase variable names: `a`, `b`, `l1`, `l2`, `l3`, `s1`, `s2`, `s3`, `f_l`.
- `domain` is either `global` or an object that gives a continuous closed starting range for each relevant variable as `{"min":value,"max":value}`.
- domain boundaries must remain within the legal variable ranges and must be supported by the supplied continuous-valued evidence. do not recreate fixed low/mid/high partitions.
- `u`, `d`, and `k` mean increase, decrease, and keep approximately unchanged.
- for `low_resonance_point` and `high_resonance_point`, use only `l`, `h`, or `k`: `l` means the numerical resonance frequency moves lower, `h` means it moves higher, and `k` means no clear meaningful frequency movement.
- for `s11_at_2_45` and `s11_at_4_50`, use only `d`, `s`, or `k`: `d` means the fixed-target s11 becomes deeper/more negative, `s` means it becomes shallower/less negative, and `k` means no clear meaningful depth change.
- every rule must contain all four required effect metrics.
- missing resonance cannot be interpreted as `k`.
- confidence must be between 0 and 1; never use 1.00. this is your direct, evidence-bounded assessment, not a code-computed probability. use low values when comparisons are sparse or confounded; reserve high values for repeated, consistent, nearby real-hfss comparisons.
- returned rules are hypotheses. code assigns internal identifiers after the response; code does not calculate, upgrade, or downgrade confidence.
- infer trends only from the numerical geometry and measured metrics in the supplied score-ranked TOP-{{top_q}} sample lines; fewer may be present when fewer evaluations are available.
- derive every returned rule from patterns that can be tested using the supplied evaluated samples; do not claim to retain, revise, or reject an earlier rule that is not included in this prompt.

# TOP-{{top_q}} evaluated samples

each following line is one score-ranked evaluated sample from the configured TOP-{{top_q}} selection (or all available samples if fewer exist). persistent identifiers and provenance are intentionally omitted:

{{experience_samples_compact}}

# required output

return only one valid json object with this exact shape:

```json
{
  "summary": "short english evidence assessment",
  "rules": [
    {
      "domain": {
        "l1": {"min": 26.40, "max": 34.20},
        "s1": {"min": 0.55, "max": 0.88}
      },
      "var_change": {"l1": "u", "s1": "d"},
      "effect": {
        "low_resonance_point": "h",
        "s11_at_2_45": "d",
        "high_resonance_point": "l",
        "s11_at_4_50": "s"
      },
      "confidence": 0.68,
      "note": "short english statement of the observed coordinated effect and its evidence limits"
    }
  ]
}
```

do not include markdown fences or commentary outside the json object.

