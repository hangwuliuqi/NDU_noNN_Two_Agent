# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0006-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],s1:[0.80,0.80],s2:[4.00,4.00],f_l:[11.00,11.00],l2:[14.50,15.00],l3:[34.50,35.50],s3:[0.40,0.60]}
var_change={l2:u,l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:s}
confidence=0.47
note=Within the narrow top-ranked 115 by 50 mm cluster, increasing l2 while decreasing l3 and s3 is associated with higher low and high resonance frequencies, deeper 2.45 GHz S11, and shallower 4.50 GHz S11. The evidence comes from a few nearby but confounded comparisons and is not established outside this local domain.



rule=r-0006-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],s1:[0.80,0.80],s2:[4.00,4.00],f_l:[11.00,11.00],l2:[15.00,15.00],l3:[34.50,35.50],s3:[0.40,0.50]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:d}
confidence=0.46
note=Near the local top-ranked design, jointly reducing l3 and s3 is associated with a higher low resonance, lower high resonance, shallower 2.45 GHz S11, and deeper 4.50 GHz S11. The revised low-band depth direction follows the measured target values in ranks 3 to 5, but the comparison is sparse and non-monotonic.
