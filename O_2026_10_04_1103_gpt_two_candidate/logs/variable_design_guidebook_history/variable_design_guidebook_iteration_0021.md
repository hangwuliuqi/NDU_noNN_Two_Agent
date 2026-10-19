# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0021-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],l3:[34.00,34.50],s3:[0.20,0.30],f_l:[11.00,11.00]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:k}
confidence=0.72
note=Within the local 115/50 geometry, jointly increasing l3 from 34.0–34.5 mm and s3 from 0.20–0.30 mm toward the observed 35.0 mm and 0.45–0.50 mm region generally lowers the low resonance, deepens S11 at 2.45 GHz, and raises the high resonance; 4.50 GHz S11 is inconsistent and the comparison is confounded.



rule=r-0021-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],l3:[35.00,35.30],s3:[0.45,0.50],f_l:[11.00,11.00]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:k}
confidence=0.60
note=From the observed high-performing local region, jointly decreasing l3 and s3 toward 34.0–34.5 mm and 0.20–0.30 mm generally raises the low resonance, shallows S11 at 2.45 GHz, and lowers the high resonance; 4.50 GHz S11 has no stable direction.



rule=r-0021-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],l3:[35.00,35.00],s3:[0.30,0.50],f_l:[11.00,11.00]}
var_change={l3:k,s3:u}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:k}
confidence=0.83
note=With l3 held at 35.0 mm, increasing s3 from 0.30 toward 0.45–0.50 mm moves the low resonance higher toward 2.45 GHz, deepens S11 at 2.45 GHz, and shifts the high resonance upward; high-band target S11 is mixed across the upper s3 values.
