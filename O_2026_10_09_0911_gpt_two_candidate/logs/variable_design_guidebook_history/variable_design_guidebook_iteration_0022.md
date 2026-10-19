# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0022-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.35],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={s2:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:d}
confidence=0.86
note=At the matched baseline, increasing s2 from 4.00 toward 4.35 mm usually deepens S11 at both fixed targets while the two detected resonances remain near 2.45 to 2.46 GHz and 4.53 to 4.54 GHz; the response is locally beneficial but non-monotonic.



rule=r-0022-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,37.50],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:s}
confidence=0.64
note=In matched local samples, increasing l3 from 35 mm toward 37.5 to 40 mm lowers the low resonance and generally makes both fixed-target S11 values shallower; the high-resonance frequency change is not consistent.



rule=r-0022-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.35],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l1:u,l3:u,s1:d,s2:u,s3:u,f_l:d}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:l,s11_at_4_50:s}
confidence=0.35
note=A small number of nearby variants with longer l1 and l3, narrower s1, wider s2 and s3, and shorter f_l produced a high resonance near 4.00 GHz and shallower 4.50 GHz S11 while retaining a low resonance near 2.45 GHz; a and b also changed, so the coordinated effect is strongly confounded.
