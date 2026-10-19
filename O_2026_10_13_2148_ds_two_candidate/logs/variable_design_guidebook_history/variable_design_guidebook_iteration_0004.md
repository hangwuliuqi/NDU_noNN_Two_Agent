# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0004-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[30.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.68
note=In this fixed compact domain, increasing l3 from 30 to 35 mm lowers the low resonance, e.g. from about 2.92 to 2.42 GHz at l2=14 mm, and deepens S11 at 2.45 from about -4.45 to -19.46 dB. High resonance near 4.35-4.55 GHz and S11 at 4.50 GHz are not clearly changed. Supported by nearby l3 comparisons, with l2 variation between 14 and 15 mm adding some high-band scatter.



rule=r-0004-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.72
note=With l3 fixed at 35 mm, increasing l2 from 14.0 to 14.8-15.0 mm moves the high resonance from about 4.35 GHz up to 4.50-4.53 GHz and deepens S11 at 4.50 GHz from about -13.27 dB to about -15.3 to -16.2 dB. The low resonance moves slightly higher, from about 2.42 to 2.44-2.46 GHz, while S11 at 2.45 GHz deepens. Supported by repeated nearby samples; the low-frequency shift is small.



rule=r-0004-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,15.00],l3:[30.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.72
note=Coordinated joint increase from about l2=14/l3=30 to l2=15/l3=35 moves the low resonance down from about 2.92 toward 2.45 GHz and strongly deepens S11 at 2.45, while moving the high resonance up from about 4.35 to 4.53 GHz and deepening S11 at 4.50 GHz. Supported by multiple nearby samples in this compact domain; residual l2/l3 coupling is present but the trend is clear.
