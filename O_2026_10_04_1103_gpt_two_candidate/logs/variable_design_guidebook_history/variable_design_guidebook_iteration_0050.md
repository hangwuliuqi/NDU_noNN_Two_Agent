# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0050-01
domain={l3:[34.25,34.90],s3:[0.30,0.40]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:k}
confidence=0.58
note=Within the lower sampled l3 and s3 region, jointly increasing l3 and s3 is generally associated with a lower low resonance, deeper 2.45 GHz S11, and a higher high resonance; the 4.50 GHz response is mixed and the variables are confounded by sparse nearby comparisons.



rule=r-0050-02
domain={l3:[35.00,35.00],s3:[0.43,0.52]}
var_change={l3:k,s3:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:d}
confidence=0.55
note=With l3 held at 35.00 mm, increasing s3 across the sampled local interval generally deepens S11 at both fixed targets, while neither detected resonance shows a consistent meaningful frequency shift; the effect is local and modest.
