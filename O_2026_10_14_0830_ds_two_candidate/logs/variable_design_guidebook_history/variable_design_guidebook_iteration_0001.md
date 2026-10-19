# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0001-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.55
note=Clean rank-3 to rank-1 comparison with all other geometry equal: increasing l2 from 14 to 15 moved both detected resonances upward and deepened S11 at both fixed targets. Based on one real-HFSS pair, so confidence is moderate and limited to this narrow starting domain.



rule=r-0001-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[34.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.50
note=Clean rank-2 to rank-1 comparison with all other geometry equal: increasing l3 from 34 to 35 moved the lower resonance downward and strongly deepened S11 at 2.45 while the upper resonance and 4.50 target stayed approximately unchanged. Based on one near-duplicate pair.



rule=r-0001-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[34.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:h,s11_at_4_50:d}
confidence=0.42
note=Joint rank-3 to rank-2 comparison with l2 increased and l3 decreased: both resonances moved higher, the 2.45 target shallowed, and the 4.50 target deepened. This represents a local tradeoff observed in one real-HFSS pair.
