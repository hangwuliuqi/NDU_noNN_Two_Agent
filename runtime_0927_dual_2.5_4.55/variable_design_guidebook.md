# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0038-01
domain={a:[115.00,116.02],b:[47.29,50.00],l1:[22.40,22.55],l2:[15.00,15.00],l3:[34.63,35.00],s1:[0.78,0.80],s2:[4.00,4.00],s3:[0.42,0.50],f_l:[10.70,11.00]}
var_change={l1:u}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:l,s11_at_4_50:k}
confidence=0.68
note=Within the dense a=115.00-116.02, b=47.29-50.00 cluster with l2=15, s2=4 and nearby slot/feed settings, increasing l1 from about 22.40 toward 22.55 tends to move the high resonance numerically lower. Low resonance and fixed-target S11 depths remain mixed across comparable samples; the high-resonance trend is clearest in the a=116.02,b=47.29 subset.



rule=r-0038-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.45,22.55],l2:[15.00,15.00],l3:[34.80,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:h,s11_at_4_50:s}
confidence=0.65
note=Within the a=115,b=50 family with l2=15, s1=0.8, s2=4, s3=0.5 and f_l=11, increasing l3 from about 34.80 toward 35.00 lowers the low resonance, raises the high resonance, and makes S11 at both fixed targets shallower.



rule=r-0038-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.45,22.55],l2:[15.00,15.00],l3:[34.80,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={a:u,b:d,l3:d,s3:d,f_l:d}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.60
note=From the a=115,b=50,l3=34.80-35.00,s3=0.50,f_l=11.0 source cluster, a coordinated shift toward a=116.02,b=47.29,l3=34.63,s3=0.42-0.48,f_l=10.70 is associated with a slightly higher low resonance and substantially deeper S11 at 2.50 GHz. High resonance and 4.55 GHz depth remain mixed.
