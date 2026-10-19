# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0071-01
domain={l3:[34.25,35.20],s3:[0.30,0.52]}
var_change={l3:u,s3:k}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:k}
confidence=0.77
note=Within the observed l3=34.25-35.20 mm and s3=0.30-0.52 mm region, increasing l3 is repeatedly associated with a lower low resonance, deeper 2.45 GHz S11, and a higher high resonance; 4.50 GHz S11 is mixed. Nearby samples vary s3 and do not fully isolate l3 causality.



rule=r-0071-02
domain={l3:[34.95,35.05],s3:[0.40,0.52]}
var_change={s3:u,l3:k}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:h,s11_at_4_50:k}
confidence=0.58
note=Near l3=35.00 mm, increasing s3 from approximately 0.40-0.52 mm is weakly associated with a higher high resonance, while the low resonance and both fixed-target S11 responses show no stable direction. Small l3 differences and local response variability limit confidence.
