# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0001-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],l3:[35.00,37.50],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:s}
confidence=0.55
note=In the compact cluster around the rank1 geometry, increasing l3 from 35.00 to 37.50 mm lowered the lower resonance from 2.45 to 2.30 GHz and made S11 at 2.40 GHz shallower; high resonance movement was small and S11 at 4.50 GHz became slightly shallower.



rule=r-0001-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,24.00],l2:[15.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l1:u}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:s}
confidence=0.45
note=In this same compact cluster, increasing l1 from 22.50 to 24.00 mm while keeping the rest fixed raised the lower resonance from 2.45 to 2.50 GHz and lowered the high resonance from 4.53 to 4.10 GHz; both fixed-target S11 values became shallower.



rule=r-0001-03
domain={a:[105.00,115.00],b:[50.00,75.00],l1:[17.50,22.50],l2:[10.00,15.00],l3:[35.00,35.00],s1:[0.80,0.90],s2:[3.00,4.00],s3:[0.50,1.30],f_l:[8.00,11.00]}
var_change={a:u,b:d,l1:u,l2:u,s1:d,s2:u,s3:d,f_l:u}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:l,s11_at_4_50:d}
confidence=0.28
note=A coordinated comparison between the rank11 and rank1 designs, which share l3=35 mm, shows this joint change moves a too-low low resonance upward and a too-high high resonance downward, deepening both target S11 values. Many variables changed simultaneously, so this is a low-confidence hypothesis.
