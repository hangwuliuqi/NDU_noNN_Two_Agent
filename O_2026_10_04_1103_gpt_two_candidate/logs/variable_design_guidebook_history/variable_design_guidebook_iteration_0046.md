# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0046-01
domain={l3:[34.25,34.70],s3:[0.30,0.40]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.67
note=From the observed lower l3 and s3 region, jointly increasing both toward approximately l3 34.9-35.1 mm and s3 0.43-0.50 mm is generally associated with a lower low resonance, higher high resonance, and deeper fixed-target S11. The trend is supported by nearby samples but remains confounded within one geometry family.



rule=r-0046-02
domain={l3:[35.00,35.30],s3:[0.45,0.50]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:s}
confidence=0.64
note=Within the observed l3 35.0-35.3 mm and s3 0.45-0.50 mm region, jointly decreasing both toward approximately l3 34.3-34.7 mm and s3 0.30-0.40 mm generally raises the low resonance, lowers the high resonance, and makes both fixed-target S11 values shallower. The reverse trend is locally repeated but the variables remain confounded.



rule=r-0046-03
domain={l3:[35.00,35.00],s3:[0.43,0.55]}
var_change={l3:k,s3:u}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:h,s11_at_4_50:k}
confidence=0.52
note=With l3 held at 35.0 mm, increasing s3 across the observed 0.43-0.55 mm interval is associated with a generally higher high resonance. The low resonance and both fixed-target S11 responses are mixed, so this is a local weak trend from repeated nearby samples.
