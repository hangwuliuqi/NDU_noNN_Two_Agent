# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0004-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,23.50],l2:[15.00,15.00],l3:[34.50,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l1:u,l3:d}
effect={low_resonance_point:k,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:s}
confidence=0.62
note=In this top-ranked 115x50 mm domain with other slot dimensions fixed, increasing l1 while decreasing l3 lowers the high resonance and makes both fixed-target S11 values shallower. Low-resonance movement was small or mixed and became clearer only for the larger l1/l3 offset.



rule=r-0004-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,23.50],l2:[15.00,15.00],l3:[34.50,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l1:d,l3:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.55
note=The reverse l1/l3 adjustment in the same domain raises the high resonance and deepens both fixed-target S11 values in nearby comparisons, though the low-resonance shift is not clear enough to state consistently.
