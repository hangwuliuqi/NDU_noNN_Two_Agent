# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0029-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],l3:[34.00,34.50],s3:[0.20,0.30],f_l:[11.00,11.00]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.84
note=From the local l3=34.0-34.5 mm and s3=0.2-0.3 mm corner, jointly increasing l3 and s3 toward l3 near 35 mm and s3 near 0.45-0.50 mm generally lowers the low resonance, raises the high resonance, and deepens both fixed-target S11 values. Repeated nearby samples support the coupled trend, although l3 and s3 are not independently isolated.



rule=r-0029-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],l3:[35.00,35.30],s3:[0.45,0.50],f_l:[11.00,11.00]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:s}
confidence=0.70
note=Within the locally strong l3=35.0-35.3 mm and s3=0.45-0.50 mm region, jointly decreasing l3 and s3 toward l3=34.0-34.5 mm and s3=0.2-0.3 mm generally raises the low resonance, lowers the high resonance, and makes both fixed-target S11 values shallower. The inverse pattern is repeated but remains confounded by coordinated changes.



rule=r-0029-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],l3:[35.00,35.00],s3:[0.43,0.50],f_l:[11.00,11.00]}
var_change={l3:k,s3:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.38
note=With l3 held near 35.0 mm, increasing s3 across approximately 0.43-0.50 mm is associated with deeper 2.45 GHz target S11, while both resonance positions and 4.50 GHz target S11 show no consistent directional change. Evidence is local, modest in magnitude, and partially confounded by nearby geometry differences.
