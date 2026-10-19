# runtime variable design guidebook

this file is the direct, code-validated rule snapshot returned by the experience llm. confidence is the experience llm's evidence assessment, not a probability calculated or upgraded by code. every rule is a trend, not a universal physical law.

## active rules



rule=r-0002-01
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[14.00,14.50],l3:[35.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u}
effect={low_resonance_point:h,s11_at_2_45:d,high_resonance_point:h,s11_at_4_50:d}
confidence=0.69
note=Within the repeated local slice, increasing l2 from 14.00-14.50 mm toward 15.00 mm raised the high resonance, shifted the low resonance higher on net, and generally deepened S11 at both fixed targets. The low-frequency shift and high-target depth were not perfectly monotonic, so extrapolation should remain local.



rule=r-0002-02
domain={a:[115.00,115.00],b:[50.00,50.00],l1:[22.50,22.50],l2:[13.00,14.00],l3:[34.00,35.00],s1:[0.80,0.80],s2:[4.00,4.00],s3:[0.50,0.50],f_l:[11.00,11.00]}
var_change={l2:u,l3:u}
effect={low_resonance_point:k,s11_at_2_45:k,high_resonance_point:h,s11_at_4_50:d}
confidence=0.55
note=Across the nearby l2/l3 sweep, increasing both variables was associated with a higher high resonance and deeper 4.50 GHz S11. Low-band frequency and 2.45 GHz depth were mixed, and the l3 contribution is confounded with the first joint step.
