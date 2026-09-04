# Capacity Model — PFM Production Crew (Benguerir 5 TPH Line)

**Risk band:** SAFE

**Recommendation:** Sized correctly at 12.0 FTE for P90 demand at 80% utilization. Headroom is healthy (402%).

## Inputs
- Current FTE: 12.0
- AHT: 22.0 min
- SLA target: 30.0 min
- Shrinkage: 20.0%
- Working hours / day: 16.0
- Demand P50 / P90 / P99: 40.0 / 52.0 / 60.0 tickets/day

## Sizing Scenarios (Erlang-C, sized to P90 demand)

| Target Util | Raw FTE | Loaded FTE (post-shrinkage) | P(SLA breach @ P50) | P(SLA breach @ P90) | P(SLA breach @ P99) |
|---|---|---|---|---|---|
| 70% | 2 | 2.5 | 6.6% | 14.8% | 23.9% |
| 80% | 2 | 2.5 | 6.6% | 14.8% | 23.9% |
| 90% | 2 | 2.5 | 6.6% | 14.8% | 23.9% |

## Headroom
- Extra tickets/day before SLA breaks: 209.0
- Headroom %: 402.0%

## Canon
- Erlang (1909), Little (1961), Cleveland *Call Center Mgmt on Fast Forward*, Reinertsen *Principles of Product Development Flow*.
