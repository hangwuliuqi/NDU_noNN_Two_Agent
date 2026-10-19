# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0007-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.50,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:k}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:s}
confidence=0.57
note=Near this fixed background, increasing l2 from about 14.5 to 15 mm generally lowers the low resonance, raises the high resonance, and deepens 2.45 GHz S11; 4.50 GHz S11 is mixed or slightly shallower. Small, nonmonotonic steps limit the evidence.



rule=r-0007-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[13.00,14.50],l3:[34.00,35.50],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:h,s11_at_4_50:d}
confidence=0.47
note=Within the lower local cluster, jointly increasing l2 and l3 is associated with a lower low resonance, a higher high resonance, shallower 2.45 GHz S11, and deeper 4.50 GHz S11. This is based on sparse, confounded nearby comparisons.



rule=r-0007-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.50,15.00],l3:[35.00,36.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:k,l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:h,s11_at_4_50:k}
confidence=0.45
note=With l2 near 14.5-15 mm in the local background, increasing l3 is associated with a lower low resonance and shallower 2.45 GHz S11; the high resonance shifts slightly higher while 4.50 GHz S11 is nearly unchanged. Evidence is limited to a few nearby samples.
