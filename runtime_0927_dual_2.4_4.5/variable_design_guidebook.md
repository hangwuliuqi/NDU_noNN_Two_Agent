# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0036-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.60],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[5.50,5.60],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.78
note=Starting from l3=35.0 mm in the 115x50 mm cluster with l1 22.5-22.6 mm and s2 5.5-5.6 mm, increasing l3 toward 35.25-35.55 mm lowers the low resonance and deepens S11 at 2.40 GHz in most comparable samples. High resonance and 4.50 GHz S11 show no consistent movement.



rule=r-0036-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.60],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[5.20,5.60],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={s2:u}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:k,s11_at_4_50:d}
confidence=0.58
note=Within l3=35.0 mm designs in the 115x50 mm cluster, increasing s2 from about 5.2 to 5.6 mm generally deepens S11 at 4.50 GHz in most comparable samples. Low and high resonance positions and 2.40 GHz S11 show no consistent trend, and the depth comparison is noisy with small l1 variations.



rule=r-0036-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.60],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[5.50,5.60],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l1:u}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:l,s11_at_4_50:k}
confidence=0.40
note=Only sparse direct comparisons within l3=35.0 mm and s2 5.5-5.6 mm; increasing l1 from about 22.5 to 22.6 mm is weakly associated with a lower high resonance, about 4.51 toward 4.49 GHz. Other metrics show no clear trend.



rule=r-0036-04
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.60],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[5.20,5.60],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u,s2:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:d}
confidence=0.55
note=Jointly increasing l3 from 35.0 mm and s2 from about 5.2-5.6 mm is associated with a lower low resonance, deeper 2.40 GHz S11, and generally deeper 4.50 GHz S11 in most comparable 115x50 mm cluster samples. The high resonance is unchanged; the 4.50 GHz depth is partly dominated by s2 and direct joint comparisons are sparse or confounded by small l1 variations.
