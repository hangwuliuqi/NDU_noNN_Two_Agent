# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0017-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.35],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={s2:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:d}
confidence=0.87
note=Within the tightly matched baseline, increasing s2 across approximately 4.00 to 4.35 generally deepens S11 at both fixed targets while the low resonance remains about 2.45 to 2.46 GHz and the high resonance about 4.52 to 4.53 GHz; the response is locally non-monotonic and should not be extrapolated.



rule=r-0017-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:s}
confidence=0.72
note=From the matched baseline, increasing l3 from 35 toward 37.5 to 40 mm consistently moves the low resonance lower and generally makes both fixed-target S11 values shallower, while the high resonance stays near 4.5 GHz; evidence is limited to a small local comparison with other variables held fixed.
