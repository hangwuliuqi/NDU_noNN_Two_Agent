# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0015-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],f_l:[11.00,11.00],l3:[34.75,35.25],s3:[0.40,0.45]}
var_change={l3:u,s3:k}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:l,s11_at_4_50:d}
confidence=0.81
note=Within the repeated local cluster, increasing l3 while keeping s3 approximately 0.40-0.45 mm generally lowers both detected resonance frequencies and deepens S11 at 2.45 and 4.50 GHz. Evidence is local and l3 remains partly confounded with small geometry changes.



rule=r-0015-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],f_l:[11.00,11.00],l3:[34.00,35.50],s3:[0.20,0.50]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:k}
confidence=0.72
note=Across the broader repeated local cluster, jointly decreasing l3 and s3 generally raises the low resonance and makes fixed-target S11 at 2.45 GHz shallower. The high resonance and 4.50 GHz S11 show no stable direction, and l3 and s3 are confounded.
