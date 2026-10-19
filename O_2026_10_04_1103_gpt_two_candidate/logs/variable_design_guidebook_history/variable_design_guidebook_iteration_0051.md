# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0051-01
domain={l3:[34.25,34.90],s3:[0.30,0.40]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:k}
confidence=0.57
note=In the lower sampled l3 and s3 region, jointly increasing both variables is generally associated with a lower low resonance, deeper 2.45 GHz S11, and a higher high resonance. The 4.50 GHz S11 response is mixed, and direct comparisons are confounded by sparse nearby geometry combinations.



rule=r-0051-02
domain={l3:[35.00,35.00],s3:[0.35,0.52]}
var_change={l3:k,s3:u}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:h,s11_at_4_50:k}
confidence=0.50
note=With l3 held at 35.00 mm, increasing s3 across the sampled local interval is associated mainly with a modest upward shift of the high resonance. The low resonance and both fixed-target S11 depths remain broadly mixed or locally saturated, so the earlier claim of deeper S11 at both targets is not retained.
