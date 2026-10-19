# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0001-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.60
note=In the nearest comparable pair, increasing l2 from 14.00 to 15.00 mm shifted both resonance valleys higher and deepened S11 at both fixed targets; evidence is a single local comparison and may not extrapolate outside this narrow slice.



rule=r-0001-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[13.00,15.00],l3:[34.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:u}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:h,s11_at_4_50:d}
confidence=0.52
note=Across the local sweep from lower l2/l3 values toward l2=14-15 mm and l3=35 mm, the high resonance moved higher and 4.50 GHz S11 deepened consistently, while low-band frequency and depth responses were mixed.
