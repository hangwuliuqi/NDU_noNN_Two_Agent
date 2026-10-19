# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0021-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.60],f_l:[11.00,11.00]}
var_change={l2:u,s3:k}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.76
note=In the repeated local family, increasing l2 toward 15.00 mm while keeping s3 approximately unchanged generally shifts both detected resonances higher and deepens S11 at both fixed targets; evidence is local and partially confounded by small s3 changes.



rule=r-0021-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.49,0.61],f_l:[11.00,11.00]}
var_change={s3:u}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:k,s11_at_4_50:d}
confidence=0.40
note=Within the repeated l2=15.00 mm family, larger s3 is weakly associated with deeper 4.50 GHz S11 overall, while resonance positions and 2.45 GHz S11 show no consistent direction; the response is non-monotonic and tightly local.
