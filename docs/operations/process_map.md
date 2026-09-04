# Process Map: PetFactory Morocco — Kibble Production Line (5 TPH Famsun)

**Stages:** 14  
**Total P50:** 182.0 min  
**Total P90:** 330.0 min

## Swim Lanes

```
+----------------------+------------------------------------------------------------------------+
| OWNER                | STAGES (in process order)                                              |
+----------------------+------------------------------------------------------------------------+
| Warehouse / QC       | #1 [V] Raw Material Receiving & QC (p50=30m)                           |
+----------------------+------------------------------------------------------------------------+
| Production Ops       | #2 [V] Batch Weighing & Grinding (p50=15m) -> #3 [W] Wait for          |
|                      | Preconditioner Availabi (p50=5m) -> #4 [V] Preconditioner (Steam +     |
|                      | Water Mi (p50=3m) -> #5 [V] Extrusion (Twin-Screw SJPS165, 2 (p50=2m)  |
|                      | -> #6 [W] Wait — Dryer Belt Queue (p50=8m) -> #7 [V] Drying (Belt      |
|                      | Dryer GZDH2200, 4 z (p50=35m) -> #8 [V] Cooling (p50=12m) -> #9 [V]    |
|                      | Fat Coating & Palatant Applicati (p50=5m) -> #13 [R] Rework — Moisture |
|                      | or Density Out (p50=20m)                                               |
+----------------------+------------------------------------------------------------------------+
| Packaging            | #10 [W] Wait — Packaging Line Queue (p50=12m) -> #11 [V] Packaging     |
|                      | (14-head weigher, seal (p50=10m)                                       |
+----------------------+------------------------------------------------------------------------+
| QC                   | #12 [V] QC Final Check & Release (p50=15m)                             |
+----------------------+------------------------------------------------------------------------+
| Warehouse            | #14 [V] Palletizing & Warehouse (p50=10m)                              |
+----------------------+------------------------------------------------------------------------+
```

Legend: `[V]` value-add  `[W]` wait  `[R]` rework

## Linear sequence

| # | Stage | Owner | Type | P50 (min) | P90 (min) |
|---|-------|-------|------|-----------|-----------|
| 1 | Raw Material Receiving & QC | Warehouse / QC | value-add | 30.0 | 60.0 |
| 2 | Batch Weighing & Grinding | Production Ops | value-add | 15.0 | 25.0 |
| 3 | Wait for Preconditioner Availability | Production Ops | wait | 5.0 | 15.0 |
| 4 | Preconditioner (Steam + Water Mixing) | Production Ops | value-add | 3.0 | 4.0 |
| 5 | Extrusion (Twin-Screw SJPS165, 203 kW) | Production Ops | value-add | 2.0 | 3.0 |
| 6 | Wait — Dryer Belt Queue | Production Ops | wait | 8.0 | 20.0 |
| 7 | Drying (Belt Dryer GZDH2200, 4 zones) | Production Ops | value-add | 35.0 | 45.0 |
| 8 | Cooling | Production Ops | value-add | 12.0 | 15.0 |
| 9 | Fat Coating & Palatant Application | Production Ops | value-add | 5.0 | 8.0 |
| 10 | Wait — Packaging Line Queue | Packaging | wait | 12.0 | 30.0 |
| 11 | Packaging (14-head weigher, seal, label) | Packaging | value-add | 10.0 | 15.0 |
| 12 | QC Final Check & Release | QC | value-add | 15.0 | 30.0 |
| 13 | Rework — Moisture or Density Out of Spec | Production Ops | rework | 20.0 | 45.0 |
| 14 | Palletizing & Warehouse | Warehouse | value-add | 10.0 | 15.0 |

