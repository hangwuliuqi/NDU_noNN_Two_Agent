# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0003-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,14.50],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:k}
confidence=0.57
note=In the repeated local slice, increasing l2 from 14.0-14.5 mm toward 15.0 mm consistently deepened S11 at 2.45 GHz and raised the high resonance, while low-resonance movement and 4.50 GHz depth were inconsistent across the two nearby comparisons.



rule=r-0003-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[13.00,14.00],l3:[34.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:h,s11_at_4_50:d}
confidence=0.53
note=Within the narrow nearby sweep, jointly increasing l2 and l3 was associated with a higher high resonance and deeper 4.50 GHz S11, but a lower low resonance and shallower 2.45 GHz S11. The evidence comes from few comparisons and cannot separate the individual l2 and l3 contributions.
