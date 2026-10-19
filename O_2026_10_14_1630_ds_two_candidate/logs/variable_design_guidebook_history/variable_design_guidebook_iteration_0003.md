# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0003-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,23.50],l2:[15.00,15.00],l3:[34.50,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l1:u,l3:d}
effect={low_resonance_point:k,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:s}
confidence=0.55
note=In the high-ranked a=115,b=50 cluster with l2=15,s1=0.80,s2=4.00,s3=0.50,f_l=11, increasing l1 while decreasing l3 tends to move the high resonance numerically lower and make S11 at both fixed targets shallower; the low resonance shows no clear systematic movement. Most comparable top-cluster samples support the high-resonance and target-S11 trends, but the low-resonance effect is mixed.



rule=r-0003-02
domain={a:[145.00,145.00],b:[45.00,45.00],l1:[15.00,15.00],l2:[6.00,6.00],l3:[22.50,25.00],s1:[1.40,1.50],s2:[6.00,7.00],s3:[0.70,1.00],f_l:[13.00,15.00]}
var_change={l3:d,s1:u,s2:d,s3:u,f_l:u}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:h,s11_at_4_50:s}
confidence=0.38
note=Within the same a=145,b=45,l1=15,l2=6 domain, decreasing l3 and s2 while increasing s1,s3,f_l moves both detected resonances numerically higher and makes both fixed-target S11 values shallower. Supported by one paired comparison, so confidence is low.



rule=r-0003-03
domain={a:[105.00,105.00],b:[80.00,80.00],l1:[17.50,45.00],l2:[10.00,13.00],l3:[27.50,45.00],s1:[0.60,0.90],s2:[3.00,5.00],s3:[0.20,0.50],f_l:[5.00,9.00]}
var_change={l1:d,l2:d,l3:u,s1:d,s2:d,s3:u,f_l:u}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:h,s11_at_4_50:s}
confidence=0.35
note=In the a=105,b=80 paired comparison, jointly decreasing l1,l2,s1,s2 and increasing l3,s3,f_l moves both detected resonances higher and makes both fixed-target S11 values shallower. Evidence is limited to one pair, so use with caution.



rule=r-0003-04
domain={a:[140.00,140.00],b:[50.00,60.00],l1:[37.50,37.50],l2:[10.00,12.00],l3:[32.50,42.50],s1:[1.10,1.30],s2:[7.00,8.00],s3:[1.10,1.50],f_l:[9.00,14.00]}
var_change={b:u,l2:u,l3:u,s1:d,s2:d,s3:u,f_l:d}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:d}
confidence=0.33
note=Within the a=140,l1=37.5 pair, jointly increasing b,l2,l3,s3 and decreasing s1,s2,f_l moves both detected resonances numerically lower, makes S11 at 2.45 shallower, and makes S11 at 4.50 deeper. Single paired comparison, so low confidence.
