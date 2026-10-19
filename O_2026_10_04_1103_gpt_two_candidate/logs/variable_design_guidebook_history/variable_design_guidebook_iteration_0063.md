# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0063-01
domain={l3:[34.25,34.80],s3:[0.30,0.43]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:k,s11_at_4_50:k}
confidence=0.65
note=Within the sampled l3=34.25-34.80 mm and s3=0.30-0.43 mm region, jointly increasing l3 and s3 is generally associated with a lower low resonance and deeper S11 at 2.45 GHz; high-resonance frequency and 4.50 GHz S11 remain mixed, and the variables are partly confounded.



rule=r-0063-02
domain={l3:[34.95,35.05],s3:[0.40,0.52]}
var_change={s3:u,l3:k}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:h,s11_at_4_50:k}
confidence=0.56
note=Near l3=35.00 mm, increasing s3 across the sampled 0.40-0.52 mm region is weakly associated with a higher high resonance, while the low resonance and both fixed-target S11 responses show no consistent directional change; the high-frequency effect is modest and partly confounded by small l3 variation.
