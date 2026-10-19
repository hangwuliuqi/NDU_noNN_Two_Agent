# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0061-01
domain={l3:[34.25,34.80],s3:[0.30,0.40]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.55
note=In the sampled lower-l3, lower-s3 region, jointly increasing l3 and s3 is generally associated with a lower low resonance and deeper S11 at 2.45 GHz, while the high resonance and 4.50 GHz S11 remain mixed; comparisons are sparse and joint changes are confounded.



rule=r-0061-02
domain={l3:[34.95,35.05],s3:[0.35,0.52]}
var_change={s3:u,l3:k}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:h,s11_at_4_50:k}
confidence=0.61
note=Near l3=35.00 mm with the other geometry fixed, increasing s3 across the sampled range is most consistently associated with a higher high resonance, while the low resonance and both fixed-target S11 responses show mixed variation.
