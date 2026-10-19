# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0002-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],s1:[0.80,0.80],s2:[4.00,4.00],f_l:[11.00,11.00],l2:[14.50,15.00],l3:[34.50,35.50],s3:[0.40,0.60]}
var_change={l2:u,l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.40
note=Within the three closely related top-ranked designs, increasing l2 while decreasing l3 and s3 is associated overall with higher low and high resonance frequencies and deeper fixed-target S11, especially at 2.45 GHz. The relationship is based on a very narrow local cluster with some high-band variation.



rule=r-0002-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],s1:[0.80,0.80],s2:[4.00,4.00],f_l:[11.00,11.00],l2:[15.00,15.00],l3:[34.50,35.50],s3:[0.40,0.50]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:k}
confidence=0.29
note=Among the nearby designs with l2 fixed at 15.0, increasing l3 is associated with a lower low resonance and a slightly higher high resonance, while the 2.45 GHz target S11 generally deepens; the 4.50 GHz depth has no consistent direction. Evidence is limited to a few local comparisons.
