# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0033-01
domain={l3:[34.00,34.50],s3:[0.20,0.30]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.82
note=For starting designs near l3=34.0-34.5 mm and s3=0.2-0.3 mm, jointly increasing l3 and s3 toward l3 near 35 mm and s3 near 0.45-0.50 mm is repeatedly associated with a lower low resonance, a higher high resonance, and deeper S11 at both fixed targets. The variables remain confounded and the domain is local.



rule=r-0033-02
domain={l3:[35.00,35.30],s3:[0.45,0.50]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:s}
confidence=0.75
note=For starting designs near l3=35.0-35.3 mm and s3=0.45-0.50 mm, jointly decreasing l3 and s3 toward the observed 34.0-34.5 mm and 0.2-0.3 mm region generally raises the low resonance, lowers the high resonance, and makes both fixed-target S11 values shallower. Evidence is repeated but the two changes cannot be isolated.



rule=r-0033-03
domain={l3:[34.95,35.05],s3:[0.43,0.50]}
var_change={l3:k,s3:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.43
note=With l3 held near 35 mm, increasing s3 across the observed 0.43-0.50 mm neighborhood is more often associated with deeper 2.45 GHz target S11, while neither resonance position nor 4.50 GHz target S11 has a consistent direction. This is a small-step local trend with measurement and geometry confounding.
