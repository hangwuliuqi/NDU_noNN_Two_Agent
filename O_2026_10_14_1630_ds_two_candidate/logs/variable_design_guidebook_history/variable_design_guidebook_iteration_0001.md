# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0001-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,23.50],l2:[15.00,15.00],l3:[34.50,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l1:d,l3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.70
note=In the exact a=115,b=50,l2=15,s1=0.8,s2=4,s3=0.5,f_l=11 region, decreasing l1 from about 23.5 to 22.5 while increasing l3 from about 34.5 to 35.0 moved the lower resonance from 2.52 to 2.45, moved the upper resonance from 4.25 to 4.53, and deepened both fixed-target S11 values; supported by the three nearby samples ranked 1, 2, and 4.



rule=r-0001-02
domain={a:[145.00,145.00],b:[45.00,45.00],l1:[15.00,15.00],l2:[6.00,6.00],l3:[22.50,25.00],s1:[1.40,1.50],s2:[6.00,7.00],s3:[0.70,1.00],f_l:[13.00,15.00]}
var_change={l3:u,s1:d,s2:u,s3:d,f_l:d}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:l,s11_at_4_50:d}
confidence=0.25
note=For two samples in this a=145,b=45,l1=15,l2=6 domain, increasing l3 while decreasing s1, s3, and f_l and increasing s2 moved both detected resonances lower and deepened both fixed-target S11 values; only two samples support this and many variables changed together, so confidence is low.



rule=r-0001-03
domain={a:[105.00,105.00],b:[80.00,80.00],l1:[17.50,45.00],l2:[10.00,13.00],l3:[27.50,45.00],s1:[0.60,0.90],s2:[3.00,5.00],s3:[0.20,0.50],f_l:[5.00,9.00]}
var_change={l1:u,l2:u,l3:d,s1:u,s2:u,s3:d,f_l:d}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:l,s11_at_4_50:d}
confidence=0.20
note=In two a=105,b=80 samples, the coordinated change toward larger l1, l2, s1, and s2 with smaller l3, s3, and f_l was associated with lower detected resonance frequencies and deeper fixed-target S11 at both 2.45 and 4.50 GHz; evidence is sparse and heavily confounded.
