# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0041-01
domain={l3:[34.00,34.50],s3:[0.20,0.30]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.78
note=For starting designs near l3=34.0-34.5 mm and s3=0.2-0.3 mm, jointly increasing l3 and s3 toward l3=35.0-35.3 mm and s3=0.45-0.50 mm is associated with a lower low resonance, a higher high resonance, and deeper S11 at both targets. The evidence is local and l3 and s3 are confounded.



rule=r-0041-02
domain={l3:[35.00,35.30],s3:[0.45,0.50]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:s}
confidence=0.77
note=For starting designs near l3=35.0-35.3 mm and s3=0.45-0.50 mm, jointly decreasing l3 and s3 toward l3=34.0-34.5 mm and s3=0.2-0.3 mm is associated with a higher low resonance, a lower high resonance, and generally shallower S11 at both targets. The reverse trend is locally supported, but the variables cannot be isolated.



rule=r-0041-03
domain={l3:[35.00,35.10],s3:[0.43,0.50]}
var_change={l3:k,s3:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.34
note=With l3 approximately fixed near 35.0-35.1 mm, increasing s3 within the observed 0.43-0.50 mm neighborhood is weakly associated with deeper S11 at 2.45 GHz, while resonance positions and 4.50 GHz S11 show no consistent direction. Comparisons are local, noisy, and partly confounded.
