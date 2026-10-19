# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0018-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],l3:[34.00,35.30],s3:[0.20,0.50],f_l:[11.00,11.00]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:k}
confidence=0.55
note=Within the repeated local cluster, jointly increasing l3 and s3 toward l3 about 35.0-35.3 mm generally lowers the low resonance and deepens S11 at 2.45 GHz, while the high resonance tends to rise. High-band S11 varies across nearby s3 values, so no consistent high-target depth direction is claimed.



rule=r-0018-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],l3:[34.00,35.30],s3:[0.20,0.50],f_l:[11.00,11.00]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:k}
confidence=0.48
note=In the same narrow cluster, jointly decreasing l3 and s3 generally raises the low resonance and makes 2.45 GHz S11 shallower, with the high resonance tending lower. The inverse high-band S11 depth is not consistent across nearby samples, and the two variable effects remain confounded.
