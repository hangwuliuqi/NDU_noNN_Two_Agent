# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0009-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:s}
confidence=0.82
note=Within the matched 115.00 by 50.00 mm family, increasing l3 from 35.00 toward 37.50-40.00 mm repeatedly lowered the low resonance and made both fixed-target S11 values shallower, while the high resonance stayed near 4.5 GHz. Evidence is confined to this narrow geometry.



rule=r-0009-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={s2:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:d}
confidence=0.89
note=With the other variables matched, increasing s2 from 4.00 to 4.10-4.30 mm consistently deepened S11 at both fixed targets while the resonances remained close to 2.45 and 4.53 GHz. The tested interval is narrow.



rule=r-0009-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[10.80,11.00]}
var_change={f_l:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:s}
confidence=0.43
note=In the matched l3=35.00 mm geometry, reducing f_l from 11.00 to 10.80 mm slightly raised the low resonance and made both fixed-target S11 values shallower, with little high-resonance movement. This direction relies on one direct comparison.
