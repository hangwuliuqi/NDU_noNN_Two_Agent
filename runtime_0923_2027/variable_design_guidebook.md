# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0019-01
domain={a:[115.00,115.00],b:[50.00,51.20],l1:[22.50,22.60],l2:[14.90,15.00],l3:[35.00,35.20],s1:[0.80,0.80],s2:[3.50,4.30],s3:[0.40,0.75],f_l:[11.00,11.00]}
var_change={s2:u,s3:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:d}
confidence=0.80
note=In the a=115 compact cluster, jointly increasing s2 and s3 from about 3.5/0.4 mm toward 4.3/0.75 mm leaves both resonance frequencies nearly unchanged while strongly deepening S11 at the fixed 2.45 and 4.50 GHz targets. This is the strongest repeated local pattern in the supplied evidence.



rule=r-0019-02
domain={a:[115.00,115.00],b:[50.00,51.20],l1:[22.50,22.60],l2:[14.90,15.00],l3:[35.00,35.20],s1:[0.80,0.80],s2:[3.90,4.30],s3:[0.50,0.75],f_l:[11.00,11.00]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:d}
confidence=0.55
note=Within the a=115 cluster, increasing l3 from about 35.0 mm toward 35.1-35.2 mm while increasing s3 from about 0.5 mm toward 0.70-0.75 mm tends to lower the low resonance slightly and deepen S11 at both fixed targets; the high resonance stays near 4.49-4.54 GHz. The low-resonance shift is small and confounded by s2 variation.



rule=r-0019-03
domain={a:[115.00,115.00],b:[50.00,51.50],l1:[22.50,22.75],l2:[14.75,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.10],s3:[0.50,0.55],f_l:[11.00,11.00]}
var_change={b:u,l1:u,l2:d}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:l,s11_at_4_50:s}
confidence=0.38
note=For a=115 designs with l3=35.0, s2 near 4.0-4.1, and s3 near 0.50-0.55, jointly increasing b while increasing l1 and decreasing l2 leaves the low resonance near 2.45 GHz and low-target depth essentially unchanged, but moves the high resonance lower and makes S11 at 4.50 GHz shallower. Supported by very few nearby comparisons, so confidence is low.
