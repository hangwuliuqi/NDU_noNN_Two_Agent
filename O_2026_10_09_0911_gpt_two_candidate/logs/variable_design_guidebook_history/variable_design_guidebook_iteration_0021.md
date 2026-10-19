# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0021-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.35],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={s2:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:d}
confidence=0.86
note=At the matched baseline, increasing s2 across 4.00 to 4.35 mm usually deepens S11 at both fixed targets while the detected resonances remain near 2.45 and 4.53 GHz; the depth response is beneficial but non-monotonic and locally evidenced.



rule=r-0021-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,37.50],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:s}
confidence=0.64
note=In matched local comparisons, increasing l3 from 35 mm toward 37.5 to 40 mm shifts the low resonance lower and makes 2.45 GHz S11 shallower; 4.50 GHz S11 is generally shallower while high-resonance movement is unclear, with only a few controlled points.



rule=r-0021-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.35],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l1:u,l3:u,s1:d,s2:u,s3:u,f_l:d}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:l,s11_at_4_50:s}
confidence=0.45
note=Two nearby variants with longer l1 and l3, wider s2 and s3, narrower s1, and shorter f_l kept the low resonance near 2.45 GHz but moved the high resonance toward 4.0 GHz and made 4.50 GHz S11 much shallower; low-band depth was inconsistent and a,b also varied.
