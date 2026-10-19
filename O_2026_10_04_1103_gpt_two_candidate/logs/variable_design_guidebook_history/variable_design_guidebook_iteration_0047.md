# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0047-01
domain={l3:[34.25,34.70],s3:[0.30,0.40]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:s}
confidence=0.69
note=From the lower l3 and s3 region, jointly increasing both toward the observed central region is generally associated with a lower low resonance, higher high resonance, deeper S11 at 2.45 GHz, and shallower S11 at 4.50 GHz. Nearby samples support the frequency and low-band trends, while the high-band depth is variable and the two changes are confounded.



rule=r-0047-02
domain={l3:[35.00,35.30],s3:[0.45,0.50]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:k}
confidence=0.65
note=Within the higher l3 and s3 region, jointly decreasing both toward the observed lower region generally raises the low resonance, lowers the high resonance, and makes S11 at 2.45 GHz shallower. The 4.50 GHz depth does not show a consistent directional change, and l3 and s3 remain confounded.



rule=r-0047-03
domain={l3:[35.00,35.00],s3:[0.43,0.55]}
var_change={l3:k,s3:u}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:h,s11_at_4_50:k}
confidence=0.53
note=With l3 held at 35.00 mm, increasing s3 across the observed interval is repeatedly associated with a higher high resonance. The low resonance and both fixed-target S11 responses remain mixed, so this is a weak local trend.
