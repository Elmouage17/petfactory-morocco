# Utilization Analysis

**Verdict:** UNBALANCED

**Headline:** Load spread of 32 percentage points across team — some are red while others are blue.

## Team Stats
- Mean utilization: 78.9%
- Median utilization: 82.5%
- Stdev: 10.2pp
- Spread (max - min): 32.0pp
- Counts: RED 5 / AMBER 4 / GREEN 3 / BLUE 0

## Member Detail

| Name | Role | Utilization | Light | Notes |
|---|---|---|---|---|
| Shift A Lead | Production Supervisor | 82% | AMBER | Within tolerable band but no surge capacity. |
| Shift A Op 1 | Extruder Operator | 88% | RED | Throughput collapse risk per queueing theory (>85% sustained). |
| Shift A Op 2 | Dryer Operator | 85% | RED | Throughput collapse risk per queueing theory (>85% sustained). |
| Shift A Op 3 | Packaging Operator | 92% | RED | Throughput collapse risk per queueing theory (>85% sustained). |
| Shift A Op 4 | Raw Material Handler | 65% | GREEN | — |
| Shift A QC | QC Technician | 70% | AMBER | Within tolerable band but no surge capacity. |
| Shift B Lead | Production Supervisor | 78% | AMBER | Within tolerable band but no surge capacity. |
| Shift B Op 1 | Extruder Operator | 86% | RED | Throughput collapse risk per queueing theory (>85% sustained). |
| Shift B Op 2 | Dryer Operator | 83% | AMBER | Within tolerable band but no surge capacity. |
| Shift B Op 3 | Packaging Operator | 90% | RED | Throughput collapse risk per queueing theory (>85% sustained). |
| Shift B Op 4 | Raw Material Handler | 60% | GREEN | — |
| Shift B QC | QC Technician | 68% | GREEN | — |

## Recommendations
- Rebalance load — investigate whether reds need different skills, specialization, or just more hands at their queue.

## Canon
- Reinertsen, *Principles of Product Development Flow*, principle 7.
- Little (1961), *A Proof for the Queuing Formula L = λW*.
- Goldratt, *The Goal* — bottleneck subordination.
