# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0014-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],f_l:[11.00,11.00],l3:[34.00,35.50],s3:[0.20,0.50]}
var_change={l3:d,s3:d}
effect={low_resonance_point:h,s11_at_2_45:s,high_resonance_point:k,s11_at_4_50:k}
confidence=0.74
note=In the repeated local cluster, jointly decreasing l3 and s3 generally raises the low resonance and makes S11 at 2.45 GHz shallower. High-resonance frequency and 4.50 GHz S11 vary without a stable direction; l3 and s3 remain partly confounded.



rule=r-0014-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[15.00,15.00],s1:[0.80,0.80],s2:[4.00,4.00],f_l:[11.00,11.00],l3:[34.75,35.25],s3:[0.40,0.45]}
var_change={l3:u,s3:k}
effect={low_resonance_point:l,s11_at_2_45:d,high_resonance_point:l,s11_at_4_50:d}
confidence=0.81
note=For nearby samples with s3 approximately 0.4-0.45, increasing l3 from about 34.75-35.0 toward 35.1-35.25 repeatedly lowers both detected resonance points and deepens S11 at both fixed targets. The rule is local and does not establish behavior outside this geometry cluster.
