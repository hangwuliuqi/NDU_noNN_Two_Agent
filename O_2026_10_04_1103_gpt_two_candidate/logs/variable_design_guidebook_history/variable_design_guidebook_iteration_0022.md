# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0022-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],l3:[34.00,34.50],s3:[0.20,0.30],f_l:[11.00,11.00]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:k}
confidence=0.73
note=Within the local 115/50 geometry, jointly increasing l3 and s3 from the 34.0-34.5 mm and 0.20-0.30 mm region toward l3 near 35 mm and s3 near 0.45-0.50 mm generally lowers the low resonance, deepens 2.45 GHz S11, and raises the high resonance; high-band S11 is mixed.



rule=r-0022-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],l3:[35.00,35.30],s3:[0.45,0.50],f_l:[11.00,11.00]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:l,s11_at_4_50:k}
confidence=0.61
note=Starting from the locally strong l3 near 35.0-35.3 mm and s3 near 0.45-0.50 mm region, jointly decreasing both toward the observed 34.0-34.5 mm and 0.20-0.30 mm region generally raises the low resonance, shallows 2.45 GHz S11, and lowers the high resonance; high-band S11 has no stable direction.



rule=r-0022-03
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],l3:[35.00,35.00],s3:[0.43,0.50],f_l:[11.00,11.00]}
var_change={l3:k,s3:u}
effect={low_resonance_point:k,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.58
note=With l3 held at 35.0 mm in the dense local cluster, increasing s3 across roughly 0.43-0.50 mm is associated mainly with deeper 2.45 GHz S11; the detected resonance-frequency directions and 4.50 GHz S11 are not consistently resolved by the nearby samples.
