# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0049-01
domain={l3:[34.25,34.90],s3:[0.30,0.40]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:k}
confidence=0.62
note=Within the lower observed l3 and s3 region, jointly increasing l3 and s3 is generally associated with a lower low resonance, deeper S11 at 2.45 GHz, and a higher high resonance. The 4.50 GHz response is mixed, and the variables are confounded by sparse nearby comparisons.



rule=r-0049-02
domain={l3:[34.70,35.30],s3:[0.45,0.50]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:k}
confidence=0.59
note=In the higher l3 and s3 region, jointly decreasing both is generally associated with a higher low resonance, shallower S11 at 2.45 GHz, and a lower high resonance. The fixed 4.50 GHz response has no consistent direction, and l3 and s3 remain confounded.



rule=r-0049-03
domain={l3:[35.00,35.00],s3:[0.43,0.55]}
var_change={l3:k,s3:u}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:h,s11_at_4_50:s}
confidence=0.50
note=With l3 held at 35.00 mm, increasing s3 across the sampled interval weakly raises both detected resonance points and makes both fixed-target S11 responses shallower. The low-resonance and target changes are small relative to local variation, so this is a low-confidence local trend.
