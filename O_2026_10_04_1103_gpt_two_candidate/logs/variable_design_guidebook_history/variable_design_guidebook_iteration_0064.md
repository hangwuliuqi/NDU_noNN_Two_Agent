# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0064-01
domain={l3:[34.25,34.80],s3:[0.30,0.43]}
var_change={l3:u,s3:u}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:k}
confidence=0.62
note=In the sampled l3=34.25-34.80 mm and s3=0.30-0.43 mm region, jointly increasing l3 and s3 is generally associated with a lower low resonance and deeper S11 at 2.45 GHz; the high resonance tends higher, but 4.50 GHz S11 is mixed and the variables are confounded.



rule=r-0064-02
domain={l3:[34.95,35.05],s3:[0.40,0.52]}
var_change={s3:u,l3:k}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:h,s11_at_4_50:k}
confidence=0.57
note=Near l3=35.00 mm, increasing s3 across 0.40-0.52 mm is repeatedly associated with a higher high resonance, while the low resonance and both fixed-target S11 responses show no stable directional change; small l3 variation and mixed high-band matching limit confidence.
