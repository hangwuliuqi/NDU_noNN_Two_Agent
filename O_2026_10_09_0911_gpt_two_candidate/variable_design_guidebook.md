# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0024-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.35],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={s2:u}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:d}
confidence=0.84
note=At the fixed 115/50-mm matched baseline, raising s2 from 4.00 toward about 4.35 mm usually deepens both fixed-target S11 values; the low valley shifts slightly upward in several variants while the high valley stays near 4.52-4.54 GHz. Matching is locally non-monotonic, especially at some intermediate s2 values.



rule=r-0024-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,40.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:s}
confidence=0.74
note=At the fixed matched baseline, increasing l3 from 35 toward 37.5-40 mm repeatedly lowers the low resonance and makes 2.45-GHz S11 much shallower; the high resonance remains near 4.5 GHz, with 4.50-GHz S11 generally slightly shallower. Evidence is limited to these controlled l3 variants.



rule=r-0024-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.80],l2:[15.00,15.00],l3:[35.00,35.30],s1:[0.78,0.80],s2:[4.00,4.30],s3:[0.50,0.55],f_l:[10.90,11.00]}
var_change={l1:u,l3:u,s1:d,s2:u,s3:u,f_l:d}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:s}
confidence=0.25
note=One nearby joint variant with longer l1/l3, narrower s1, wider s2/s3, and shorter feed line moved both detected valleys lower and made both fixed-target S11 values shallower relative to the close baseline. This is an unisolated single comparison, so use only as a low-confidence local interaction hypothesis.
