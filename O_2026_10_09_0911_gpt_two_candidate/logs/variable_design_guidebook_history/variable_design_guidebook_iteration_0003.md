# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0003-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,40.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[10.80,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:k}
confidence=0.66
note=In the tightly matched 115.00 by 50.00 mm family, increasing l3 from 35.00 toward 37.50-40.00 mm lowered the low resonance and made target S11 at 2.45 GHz shallower across the nearby comparisons; high-band frequency and target depth had no consistent direction.



rule=r-0003-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={s2:u}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:d}
confidence=0.49
note=For the otherwise identical rank 1 and rank 2 geometries, increasing s2 from 4.00 to 4.10 mm shifted the low resonance slightly higher and deepened both fixed-target S11 values, while the high resonance frequency was unchanged; evidence is limited to one nearby comparison.



rule=r-0003-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[10.80,11.00]}
var_change={f_l:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:s}
confidence=0.47
note=In the otherwise matched rank 1 and rank 3 geometries, reducing f_l from 11.00 to 10.80 mm shifted the low resonance higher but made S11 at both fixed targets shallower; the high resonance frequency remained near 4.53 GHz, and this direction is based on one direct comparison.
