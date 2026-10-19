# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0002-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,23.50],l2:[15.00,15.00],l3:[34.50,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l1:d,l3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.74
note=Within the top-ranked a=115,b=50,l2=15,s1=0.8,s2=4,s3=0.5,f_l=11 cluster, decreasing l1 while increasing l3 moved the low resonance lower toward 2.45, deepened S11 at 2.45, moved the high resonance higher toward 4.50, and deepened S11 at 4.50. Evidence is limited to five samples where only l1 and l3 varied materially.



rule=r-0002-02
domain={a:[145.00,145.00],b:[45.00,45.00],l1:[15.00,15.00],l2:[6.00,6.00],l3:[22.50,25.00],s1:[1.40,1.50],s2:[6.00,7.00],s3:[0.70,1.00],f_l:[13.00,15.00]}
var_change={l3:d,s2:d,s1:u,s3:u,f_l:u}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:h,s11_at_4_50:s}
confidence=0.26
note=In the small a=145,b=45,l1=15,l2=6 comparison, decreasing l3 and s2 while increasing s1, s3, and f_l moved both detected resonances higher and made S11 at both fixed targets shallower. Only two comparable samples support this and five variables changed together, so confidence is low.
