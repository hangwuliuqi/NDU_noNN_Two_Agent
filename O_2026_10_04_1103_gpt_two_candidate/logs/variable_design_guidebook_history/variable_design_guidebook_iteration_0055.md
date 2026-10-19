# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0055-01
domain={l3:[34.25,34.85],s3:[0.30,0.40]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:k}
confidence=0.56
note=Within the sampled lower-l3 region, jointly increasing l3 and s3 is usually associated with a lower low resonance, deeper 2.45 GHz S11, and a modestly higher high resonance. The 4.50 GHz response is mixed, and l3 and s3 changes are partly confounded.



rule=r-0055-02
domain={l3:[34.95,35.05],s3:[0.35,0.52]}
var_change={l3:k,s3:u}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:h,s11_at_4_50:k}
confidence=0.57
note=Near l3=35.00 mm, increasing s3 across the observed interval is most consistently associated with a higher high resonance. The low resonance and both fixed-target S11 responses show no stable directional change, so this rule is restricted to the narrow sampled domain.
