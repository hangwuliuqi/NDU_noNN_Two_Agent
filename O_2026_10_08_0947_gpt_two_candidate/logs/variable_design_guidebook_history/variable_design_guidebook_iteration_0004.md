# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0004-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,14.75],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.62
note=Within the narrow local sweep, increasing l2 generally deepened S11 at both fixed targets and raised the high resonance. Low-resonance movement was mixed, and the 4.50 GHz depth showed a small reversal at the final step, so the rule is limited to this exact geometry slice.



rule=r-0004-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[13.00,14.00],l3:[34.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:h,s11_at_4_50:d}
confidence=0.62
note=Across several nearby comparisons starting near l2=13.0-14.0 and l3=34.0-35.0, jointly increasing l2 and l3 consistently raised the high resonance, lowered the low resonance, and deepened S11 at 4.50 GHz; 2.45 GHz S11 was shallower in most comparisons but reversed in the largest step. Individual l2 and l3 effects cannot be separated.
