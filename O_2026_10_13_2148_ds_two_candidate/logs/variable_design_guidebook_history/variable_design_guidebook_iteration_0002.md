# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0002-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[30.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.55
note=In this compact domain, increasing l3 from 30 to 35 mm moves the low resonance from about 2.92 to 2.45 GHz and deepens S11 at 2.45 from about -4.45 to -26.44 dB. High-resonance frequency stays near 4.35-4.55 GHz and S11 at 4.50 GHz is mixed between -13.18 and -15.46 dB, so those are treated as keep-unchanged. Evidence is from four nearby samples and is confounded by l2 variation between 14 and 15 mm.



rule=r-0002-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.45
note=In this compact domain with l3 fixed at 35 mm, increasing l2 from 14 to 15 mm moves the high resonance from about 4.35 to 4.53 GHz and deepens S11 at 4.50 from about -13.27 to -15.46 dB. The low resonance moves slightly higher from 2.42 to 2.45 GHz and S11 at 2.45 deepens strongly. Evidence is from only two nearby samples, so the small low-frequency movement is uncertain.
