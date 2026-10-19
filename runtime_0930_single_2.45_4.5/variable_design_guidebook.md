# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0002-01
domain={a:[110.00,115.00],b:[50.00,65.00],l1:[22.50,30.00],l2:[7.00,15.00],l3:[17.50,35.00],s1:[0.80,1.10],s2:[3.80,4.00],s3:[0.50,0.60],f_l:[5.00,11.00]}
var_change={b:d,l1:d,l2:u,l3:u,s1:d,s3:d,f_l:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.35
note=In the top-ranked local domain (a 110-115 mm, b 50-65 mm), the rank5-to-rank1/2/3 comparison supports decreasing b/l1/s1/s3 while increasing l2/l3/f_l; this moved the low resonance lower toward 2.45 GHz, raised the upper resonance toward 4.5 GHz, and deepened both fixed-target S11 values. Evidence is sparse and confounded by simultaneous changes.



rule=r-0002-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.50,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[3.80,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,s2:u}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.45
note=Within the rank1-3 cluster (a=115, b=50, l1=22.5, l3=35, s1=0.8, s3=0.5, f_l=11), increasing l2 from 14.5 toward 15.0 and s2 from 3.8 toward 4.0 raised both detected resonances and deepened S11 at 2.45 and 4.50 GHz. The comparisons are close but small; the high-target improvement is based mainly on rank3-to-rank1/2.



rule=r-0002-03
domain={a:[145.00,145.00],b:[45.00,45.00],l1:[15.00,15.00],l2:[6.00,6.00],l3:[22.50,25.00],s1:[1.40,1.50],s2:[6.00,7.00],s3:[0.70,1.00],f_l:[13.00,15.00]}
var_change={l3:u,s1:d,s2:u,s3:d,f_l:d}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:l,s11_at_4_50:d}
confidence=0.20
note=Narrowed from the previous rule to one clearly comparable nearby pair (rank23 to rank17). Increasing l3 and s2 while decreasing s1/s3/f_l moved both detected resonances lower and deepened both fixed-target S11 values. This is a single confounded comparison and should be treated as weak.
