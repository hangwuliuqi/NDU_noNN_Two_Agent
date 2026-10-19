# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0003-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[30.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.60
note=In this compact domain, increasing l3 from 30 to 35 mm lowers the low resonance, e.g. from about 2.92 to 2.42 GHz when l2 is held at 14 mm, and deepens S11 at 2.45 from about -4.45 to -19.46 dB. High resonance near 4.35 GHz and S11 at 4.50 GHz are not clearly changed. Most comparable nearby samples support this, although l2 variation between 14 and 15 mm confounds high-band detail.



rule=r-0003-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.47
note=With l3 fixed at 35 mm, increasing l2 from 14 to 15 mm moves the high resonance from about 4.35 to 4.53 GHz and deepens S11 at 4.50 from about -13.27 to -15.46 dB. The low resonance moves slightly higher from 2.42 to 2.45 GHz and S11 at 2.45 deepens. Only two or three nearby samples support this, so the low-frequency movement is uncertain.



rule=r-0003-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[30.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.62
note=Coordinated joint increase from about l3=30/l2=14 to l3=35/l2=15 moves the lower resonance from about 2.92 down toward 2.45 GHz, strongly deepens S11 at 2.45, moves the upper resonance from about 4.35 up to 4.53 GHz, and deepens S11 at 4.50. This is supported by multiple nearby samples in this compact domain, though residual l2/l3 coupling is still confounded.
