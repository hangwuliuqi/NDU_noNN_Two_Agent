# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0008-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.50,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:k}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:s}
confidence=0.58
note=Near the repeated 115 by 50 mm local design, increasing l2 from about 14.5 toward 15 mm while keeping l3 near 35 mm generally lowers the low resonance, raises the high resonance, and deepens 2.45 GHz S11; 4.50 GHz S11 tends to become slightly shallower. Small nonmonotonic differences limit confidence.



rule=r-0008-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[13.00,14.50],l3:[34.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.34
note=In the lower portion of the local cluster, jointly increasing l2 and l3 is associated with higher high-resonance frequency and deeper matching at both fixed targets. The low-resonance direction is inconsistent across nearby comparisons, so it is treated as unclear; evidence is sparse and confounded.
