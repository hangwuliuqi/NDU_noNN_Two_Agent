# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0043-01
domain={l3:[34.00,34.50],s3:[0.20,0.30]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.78
note=From starting designs near l3=34.0-34.5 mm and s3=0.2-0.3 mm, jointly increasing l3 and s3 toward approximately 35.0-35.3 mm and 0.45-0.50 mm is locally associated with a lower low resonance, a higher high resonance, and deeper S11 at both targets. The evidence is concentrated in one geometry family and the two changes remain confounded.



rule=r-0043-02
domain={l3:[35.00,35.30],s3:[0.45,0.50]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:s}
confidence=0.73
note=From starting designs near l3=35.0-35.3 mm and s3=0.45-0.50 mm, jointly decreasing l3 and s3 toward approximately 34.0-34.5 mm and 0.2-0.3 mm is associated with a higher low resonance, a lower high resonance, and generally shallower target S11. This is the locally observed reverse of the low-l3, low-s3 trend, with l3 and s3 confounded.



rule=r-0043-03
domain={l3:[35.00,35.00],s3:[0.43,0.50]}
var_change={l3:k,s3:u}
effect={low_resonance_point:h,s11_at_2_45:k,high_resonance_point:h,s11_at_4_50:k}
confidence=0.44
note=With l3 held at approximately 35.0 mm, increasing s3 across the observed 0.43-0.50 mm neighborhood weakly tends to move both resonance points higher. Fixed-target S11 changes are mixed and provide no reliable direction; comparisons remain local and the frequency trend is modest.
