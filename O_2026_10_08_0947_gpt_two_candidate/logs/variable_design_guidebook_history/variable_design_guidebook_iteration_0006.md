# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0006-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:k}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.79
note=Within the fixed local background and l3 near 35 mm, increasing l2 generally keeps the low resonance near its prior position, raises the high resonance, and deepens S11 at both fixed targets; repeated nearby samples support the trend, with small-step nonmonotonicity limiting the domain.



rule=r-0006-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[13.00,14.50],l3:[34.00,35.50],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:u}
effect={low_resonance_point:l,s11_at_2_45:k,high_resonance_point:h,s11_at_4_50:d}
confidence=0.53
note=In the lower local cluster, jointly increasing l2 and l3 usually lowers the low resonance, raises the high resonance, and deepens S11 at 4.50 GHz; the 2.45 GHz depth response is mixed and the variables remain confounded across only a few nearby comparisons.



rule=r-0006-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.50,15.00],l3:[35.00,36.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:k,l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:k}
confidence=0.49
note=With l2 held near 14.5-15.0 mm in the same local background, increasing l3 lowers the low resonance and makes S11 at 2.45 GHz shallower, while the high resonance stays nearly unchanged and 4.50 GHz S11 is mixed; evidence is limited to two nearby comparisons.
