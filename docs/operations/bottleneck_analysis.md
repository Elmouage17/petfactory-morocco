# Bottleneck Detection: PetFactory Morocco — Kibble Production Line (5 TPH Famsun)

**Profile:** `manufacturing`  
**Findings:** 3

## 1. [MEDIUM] Slow stage: Drying (Belt Dryer GZDH2200, 4 zones)

- **Rule:** `R1`
- **Detail:** P50 35 min vs value-add mean 13.7 min (ratio 2.6x).
- **Hypothesis:** Stage runs much longer than the typical value-add step; common causes: batched approvals, single approver, missing self-service, or unclear acceptance criteria.
- **Recommended action:** Decompose the stage; check if approval can be parallelized or made conditional. If wait-state, apply Kanban WIP limit or remove the handoff.
- **Impact (P50 minutes):** 35

## 2. [MEDIUM] Slow stage: Raw Material Receiving & QC

- **Rule:** `R1`
- **Detail:** P50 30 min vs value-add mean 13.7 min (ratio 2.2x).
- **Hypothesis:** Stage runs much longer than the typical value-add step; common causes: batched approvals, single approver, missing self-service, or unclear acceptance criteria.
- **Recommended action:** Decompose the stage; check if approval can be parallelized or made conditional. If wait-state, apply Kanban WIP limit or remove the handoff.
- **Impact (P50 minutes):** 30

## 3. [MEDIUM] Process has excessive rework

- **Rule:** `R3`
- **Detail:** Rework accounts for 11% of total P50, vs 10% profile threshold.
- **Hypothesis:** Defects escape upstream stages. Six-Sigma canon: rework is always an upstream-quality problem, never a downstream one.
- **Recommended action:** Add a poka-yoke (error-proofing) check at the earliest stage that can detect the defect; do not add inspection downstream.
- **Impact (P50 minutes):** 20

