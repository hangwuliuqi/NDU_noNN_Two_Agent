# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0044-01
domain={l3:[34.00,34.50],s3:[0.20,0.30]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.78
note=Within the observed low-l3, low-s3 corner, jointly increasing l3 and s3 toward about 35.0-35.3 mm and 0.45-0.50 mm is associated with a lower low resonance, a higher high resonance, and deeper S11 at both fixed targets. Evidence is concentrated in one geometry family and the two changes are confounded.



rule=r-0044-02
domain={l3:[35.00,35.30],s3:[0.45,0.50]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:s}
confidence=0.73
note=Within the observed l3=35.0-35.3 mm and s3=0.45-0.50 mm region, jointly decreasing both variables toward l3=34.0-34.5 mm and s3=0.2-0.3 mm is associated with a higher low resonance, a lower high resonance, and generally shallower target S11. The reverse trend is locally supported, but l3 and s3 remain confounded.



rule=r-0044-03
domain={l3:[35.00,35.00],s3:[0.43,0.55]}
var_change={l3:k,s3:u}
effect={low_resonance_point:h,s11_at_2_45:k,high_resonance_point:h,s11_at_4_50:k}
confidence=0.46
note=With l3 held at approximately 35.0 mm, increasing s3 across the observed 0.43-0.55 mm neighborhood weakly corresponds to higher low and high resonance frequencies. Fixed-target S11 responses are mixed, and the frequency shift is modest within this local set.
