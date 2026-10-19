# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0032-01
domain={l3:[34.00,34.50],s3:[0.20,0.30]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.76
note=From the local l3=34.0-34.5 mm and s3=0.2-0.3 mm corner, jointly increasing l3 and s3 toward l3 near 35 mm and s3 near 0.45-0.50 mm generally lowers the low resonance, raises the high resonance, and deepens both fixed-target S11 values. Several nearby samples support this direction, but l3 and s3 changes are confounded.



rule=r-0032-02
domain={l3:[35.00,35.30],s3:[0.45,0.50]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:s}
confidence=0.68
note=Within the locally strong l3=35.0-35.3 mm and s3=0.45-0.50 mm region, jointly decreasing l3 and s3 toward l3=34.0-34.5 mm and s3=0.2-0.3 mm generally raises the low resonance, lowers the high resonance, and makes both target S11 values shallower. The inverse pattern is repeated locally, although the two variables cannot be separated causally.



rule=r-0032-03
domain={l3:[35.00,35.00],s3:[0.43,0.50]}
var_change={l3:k,s3:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.40
note=With l3 held near 35.0 mm, increasing s3 within the observed 0.43-0.50 mm neighborhood is more often associated with deeper 2.45 GHz target S11, while the resonance positions and 4.50 GHz target S11 show no stable direction. Evidence is local, small-step, and confounded by measurement variation.
