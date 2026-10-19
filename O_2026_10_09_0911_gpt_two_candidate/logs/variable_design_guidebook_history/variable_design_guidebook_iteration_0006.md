# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0006-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00],l3:[35.00,40.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:k}
confidence=0.73
note=In the tightly matched 115.00 by 50.00 mm family, increasing l3 from 35.00 toward 37.50-40.00 mm repeatedly lowered the low resonance and made 2.45 GHz S11 shallower; high-band frequency and target S11 changes were mixed.



rule=r-0006-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s3:[0.50,0.50],f_l:[11.00,11.00],s2:[4.00,4.20]}
var_change={s2:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:d}
confidence=0.76
note=Across the nearby 115.00 by 50.00 mm samples with l3=35.00 mm, increasing s2 from 4.00 to 4.10 and 4.20 mm deepened both fixed-target S11 values while both detected resonance frequencies remained effectively stable; the comparison range is narrow.



rule=r-0006-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[10.80,11.00]}
var_change={f_l:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:s}
confidence=0.45
note=In one otherwise matched comparison, reducing f_l from 11.00 to 10.80 mm moved the low resonance slightly higher and made both fixed-target S11 values shallower while the high resonance frequency remained unchanged; evidence is limited to one perturbation.
