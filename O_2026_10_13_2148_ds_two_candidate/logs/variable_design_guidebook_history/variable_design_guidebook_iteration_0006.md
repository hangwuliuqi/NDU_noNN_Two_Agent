# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0006-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[30.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.66
note=Increasing l3 from 30 to 35 mm in this compact domain lowers the low resonance and deepens S11 at 2.45 GHz, while the high resonance near 4.35-4.55 GHz and S11 at 4.50 GHz remain nearly unchanged. Supported by l3 comparisons at l2=14 mm and l2=15 mm; small high-band variations leave high-band metrics approximately constant.



rule=r-0006-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.75
note=Increasing l2 from 14.0 toward 14.8-15.0 mm with l3 fixed at 35 mm moves the high resonance up from about 4.35 toward 4.50-4.53 GHz and deepens S11 at 4.50 GHz. The low resonance moves slightly higher and S11 at 2.45 GHz also deepens. Strongly supported by repeated nearby rank-1 to rank-6 samples.



rule=r-0006-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[30.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.72
note=Coordinated joint increase from approximately l2=14/l3=30 to l2=15/l3=35 lowers the low resonance toward 2.45 GHz and strongly deepens S11 at 2.45 GHz, while raising the high resonance toward 4.50 GHz and deepening S11 at 4.50 GHz. Supported by multiple nearby samples in this compact domain; residual l2-l3 coupling remains.
