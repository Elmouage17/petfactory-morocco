# Note de Calcul — Dimensionnement des Citernes d'Eau
## Water Tank Sizing Analysis
**Project:** PetFactory Morocco — Sidi Bouathmane, Benguerir  
**Supplier:** FAMSUN (5T/H Pet Food Line)  
**Reference documents:** PCI Synoptique Surpresseur (INGenios), NSI ERT 0003311-NSI-YB (BCAT/Soufiane Incendie), Fang Kuai 3t Boiler Quotation, FAMSUN Chiller Solution V08, Condensate Return Rate Calculation  
**Date:** 2026-09-21  
**Prepared by:** Claude AI / Sam Aribi  

---

## 1. Plant Overview & Water Sources

| Parameter | Value |
|---|---|
| Production line | FAMSUN 5 TPH pet food (dry kibble) |
| Location | ZI Sidi Bouathmane, Benguerir, Province Rhamna |
| Total building area | 5,180 m² |
| Operating schedule | 16 h/day (2 shifts), ~300 days/year |
| Max occupancy (NSI ERT) | 559 persons |
| Typical production staff | ~200 persons/shift |
| Water supply — primary | Private well (forage) on site |
| Water supply — backup | ONEE (Office National de l'Électricité et de l'Eau potable) |
| ONEE water cost | 8.50 MAD/m³ |
| Well water cost (pumping only) | ~1.50 MAD/m³ (electricity + maintenance) |

### Dual Water Supply Strategy: Well + ONEE

The factory has **two independent water sources:**

**1. Private well (forage) — Primary supply**

The site at ZI Sidi Bouathmane will have a private borehole well. The Benguerir region sits on the **Bahira plain** aquifer (nappe de la Bahira), part of the Oum Er-Rbia basin. Typical characteristics for this region:

| Parameter | Typical Range (Benguerir area) |
|---|---|
| Aquifer type | Alluvial / Plio-Quaternary |
| Static water level | 15–40 m below ground |
| Well depth | 40–80 m |
| Expected yield | 3–10 m³/h (depending on location) |
| Water quality | Moderate hardness (200–400 mg/L CaCO₃), suitable for industrial use after treatment |
| TDS | 500–1,500 mg/L |

**Regulatory requirements for private well in Morocco:**
- Authorization from the Agence du Bassin Hydraulique de l'Oum Er-Rbia (ABHOER)
- Loi 36-15 sur l'eau (Water Law) — permit required for any groundwater extraction
- Annual declaration of volumes pumped
- Meter installation mandatory
- Water quality analysis (initial + annual)

**2. ONEE municipal supply — Backup**

The ONEE connection at the ZI Sidi Bouathmane industrial zone serves as a **backup** supply for:
- Well pump failure or maintenance
- Peak demand exceeding well capacity
- Well water quality issues (seasonal variations)
- Sanitary/drinking water (if well water doesn't meet potable standards)

ONEE supply risks in Moroccan industrial zones:
- Scheduled maintenance shutdowns (24–72 h notice)
- Pressure drops during peak demand (summer)
- Occasional unplanned interruptions (pipe breaks, pump failures)

**Design philosophy:** The well is the primary source, ONEE is the backup. Raw water storage is sized so that **either source alone** can sustain the factory for at least **2 days**, and both together provide **3+ days** of autonomy. This dual-source approach significantly reduces supply risk compared to ONEE-only.

---

## 2. Water Consumers — Detailed Demand Calculation

### 2.1 Boiler Feedwater Makeup

> Source: Condensate Return Rate Calculation (see `Boiler/Condensate_Return_Rate_Calculation.md`)

| Parameter | Current System | With Flash Recovery |
|---|---|---|
| Total steam consumption | 2.45 t/h | 2.45 t/h |
| Condensate return rate | 70% (1.708 t/h) | 80% (1.969 t/h) |
| **Makeup water required** | **0.742 t/h** | **0.481 t/h** |
| Daily (16 h production) | 11.9 m³/day | 7.7 m³/day |
| Blowdown (~3% of steam) | 0.074 t/h | 0.074 t/h |
| **Total boiler water demand** | **0.816 t/h** | **0.555 t/h** |
| Daily total | 13.1 m³/day | 8.9 m³/day |

**Boiler water must be softened** (Fang Kuai specification: dual-tank automatic water softener, 3 t/h capacity included in boiler package).

### 2.2 Process Water — Preconditioner

> Source: FAMSUN specifications, petfood_simulator (`models/preconditioner.py`)

| Parameter | Value |
|---|---|
| Water addition to preconditioner | 400 kg/h |
| Pre-heating temperature | ~60 °C |
| Steam injection (direct) | 0.225 t/h (30% of preconditioner steam) |
| **Net process water consumed** | **0.400 t/h** |
| Daily (16 h) | 6.4 m³/day |

This water is absorbed into the product — it is not recovered.

### 2.3 Cooling Water — Chiller System

> Source: FAMSUN Chiller Solution V08

| Parameter | Value |
|---|---|
| FAMSUN chiller capacity | 180 kW (8 ventilo-convectors FP-238) |
| VRV existing | 410 kW (2 × 205 kW) |
| Circuit type | Closed loop (water-glycol) |
| Main pipe | DN150, reduced to DN65 per floor |
| Makeup water (evaporation/leaks) | ~0.15 t/h (estimate) |
| Daily makeup | 2.4 m³/day |

The chiller operates on a **closed-loop** system; makeup water compensates for minor evaporation and periodic blowdown of cooling towers (if present) or system losses.

### 2.4 CIP / Washdown Water

| Operation | Frequency | Volume |
|---|---|---|
| Equipment rinsing (extruder, preconditioner, dryer) | Daily | 3.0 m³ |
| Floor washing (production areas) | Daily | 2.5 m³ |
| Fat system cleaning (daily tanks, enrobeuse) | Daily | 1.5 m³ |
| Packaging area cleaning | Daily | 1.0 m³ |
| Deep CIP (monthly full line cleaning) | Monthly | 15.0 m³ |
| **Daily average** | | **8.5 m³/day** |

### 2.5 Sanitary Water

| Category | Persons | Consumption | Volume |
|---|---|---|---|
| Production workers (showers, WC, drinking) | 200 | 50 L/person/day | 10.0 m³/day |
| Admin & visitors | 30 | 80 L/person/day | 2.4 m³/day |
| Kitchen/canteen | 230 | 10 L/person/day | 2.3 m³/day |
| **Total sanitary** | | | **14.7 m³/day** |

> Moroccan industrial standard: 50–80 L/worker/day (Norme Marocaine NM 03.7.001)

### 2.6 Miscellaneous

| Use | Volume |
|---|---|
| Green spaces/landscape | 0.5 m³/day |
| Lab/quality control | 0.3 m³/day |
| Truck washing area | 0.5 m³/day |
| **Total miscellaneous** | **1.3 m³/day** |

---

## 3. Total Water Balance Summary

| Consumer | Peak (m³/h) | Daily Peak (m³/day) | Daily Average (m³/day) |
|---|---|---|---|
| Boiler makeup (no flash recovery) | 0.816 | 13.1 | 10.5 |
| Process water (preconditioner) | 0.400 | 6.4 | 6.4 |
| Cooling water makeup | 0.150 | 2.4 | 1.8 |
| CIP / washdown | — | 8.5 | 8.5 |
| Sanitary water | — | 14.7 | 12.0 |
| Miscellaneous | — | 1.3 | 1.0 |
| **TOTAL (excl. fire)** | **~1.37** | **46.4** | **40.2** |

**Peak hourly demand (production hours):** ~3.5 m³/h (including CIP peaks)  
**Annual consumption:** 46.4 × 300 = **~13,920 m³/year**

### Annual cost comparison — Well vs ONEE:
| Source | Unit Cost | Annual Cost | Saving vs ONEE |
|---|---|---|---|
| ONEE only | 8.50 MAD/m³ | 118,320 MAD/year | — |
| Well only (pumping cost) | ~1.50 MAD/m³ | 20,880 MAD/year | **97,440 MAD/year** |
| Well primary + ONEE backup (90/10 split) | ~2.20 MAD/m³ avg | 30,624 MAD/year | **87,696 MAD/year** |

> The well saves approximately **87,000–97,000 MAD/year** in water costs. Well pumping cost includes electricity (~1.20 MAD/kWh × ~1 kWh/m³) + pump maintenance allocation.

### With flash steam recovery vessel (recommended):
| | Daily Peak | Daily Average |
|---|---|---|
| Boiler makeup reduction | -4.2 m³/day | -3.4 m³/day |
| **Revised total** | **42.2 m³/day** | **36.8 m³/day** |
| Additional annual saving | ~1,260 m³/year | = ~1,890 MAD/year (well) or ~10,710 MAD/year (ONEE) |

---

## 4. Water Tank Inventory — Sizing

### 4.1 Tank A — Raw Water Storage (Citerne d'eau brute)

**Purpose:** Main buffer fed by both the private well and the ONEE backup connection.

**Sizing rationale with dual supply:**

With a well as the primary source, the tank acts as a buffer between the well pump (intermittent cycling) and the continuous plant demand, and as a reserve if the well pump fails. The ONEE backup automatically activates on low tank level.

| Design parameter | Value | Basis |
|---|---|---|
| Design daily demand | 46.4 m³/day | Peak day (Section 3) |
| Well pump expected yield | 5–8 m³/h | Typical for Benguerir area (to confirm after drilling) |
| Well pump operating hours | 8–12 h/day | To meet 46.4 m³/day at 5–8 m³/h |
| Minimum buffer (pump failure) | 46.4 × 2 = 93 m³ | 2 days without well (ONEE backup activates) |
| Target autonomy (both sources down) | 2 days | Unlikely but conservative |
| Safety margin (15%) | +14 m³ | |
| **Design volume** | **120 m³** | Reduced from 200 m³ thanks to dual supply |

> With only ONEE, 200 m³ was needed for 4+ days autonomy. The well reduces this to **120 m³** because the dual supply makes a total loss of water very unlikely. If the well fails, ONEE kicks in immediately; if ONEE is interrupted, the well continues pumping. The 120 m³ reserve covers 2 days even if **both** sources fail simultaneously.

**Recommended configuration:**

| Option | Description | Cost Estimate | Pros | Cons |
|---|---|---|---|---|
| **Option 1 (Recommended)** | 2 × 60 m³ béton armé | ~160,000 MAD | Redundancy: one tank can be cleaned while other operates; well and ONEE can each feed a different tank | Slightly higher cost than single |
| Option 2 | 1 × 120 m³ béton armé | ~120,000 MAD | Single foundation; lower cost | No redundancy during maintenance |
| Option 3 | 1 × 100 m³ + 1 × 50 m³ | ~145,000 MAD | Flexibility: small tank can be dedicated to boiler circuit | Uneven volumes |

**Construction details (Option 1 — 2 × 60 m³):**
- Material: Reinforced concrete (béton armé), waterproofed with epoxy lining
- Location: Near the well head and boiler room, at low elevation on site
- Well pump discharge: PEHD DN63–DN80 into tanks
- ONEE backup connection: DN80 with automatic fill valve (opens on low-low level)
- Disconnection device on ONEE line: mandatory (anti-retour + disconnecteur BA)
- Level control per tank: Level transmitter (LT) + high/low/low-low alarms
- Low level → alarm + auto-switch to ONEE backup
- Low-low level → critical alarm + production shutdown interlock
- Overflow: DN100 to storm drain
- Drain: DN80 at bottom for cleaning
- Ventilation: Screened vent pipe to prevent contamination
- Access: Manhole 600×600 mm minimum per tank
- Inter-tank connection: DN80 with isolation valve (allows balancing or isolation)

### 4.1.1 Well Pump Station

| Parameter | Recommended |
|---|---|
| Pump type | Submersible borehole pump |
| Flow rate | 5–8 m³/h (confirm after pump test) |
| Head | ~50–70 m (static level + friction + elevation) |
| Power | ~3–5 kW |
| Control | VFD (variable frequency drive) recommended for energy saving |
| Level protection | Dry-run protection sensor in well |
| Operating mode | Automatic: starts on tank low level, stops on high level |
| Backup pump | Recommended (stored on-site spare, not installed) |
| Estimated cost | 35,000–50,000 MAD (pump + VFD + wellhead piping) |

### 4.1.2 ONEE Backup Connection

| Parameter | Value |
|---|---|
| Connection size | DN80 |
| Activation | Automatic: solenoid valve opens when tank level < 30% |
| Disconnection device | BA (disconnecteur à zone de pression réduite) — mandatory per ONEE regulations |
| Flow meter | Pulsed output meter for ONEE billing |
| Expected fill rate | 8–12 m³/h at 2.5–3.5 bar ONEE pressure |
| Annual ONEE usage (normal) | ~10% of total = ~1,400 m³/year = ~11,900 MAD/year |

### 4.2 Tank B — Boiler Feedwater Tank (Bâche alimentaire)

> Already specified by Fang Kuai Boiler Co., LTD

| Parameter | Value | Source |
|---|---|---|
| Volume | **3 m³** | Fang Kuai quotation item 9 |
| Material | Stainless steel, double-layer insulated | Circular design |
| Feed water temperature | 20 °C (makeup) + 85 °C (condensate) = ~65 °C blend | Condensate calculation |
| Feed water pumps | 2 × 4 m³/h, H=140m, P=4kW | Fang Kuai item 10 |
| Buffer time at peak | 3 m³ ÷ 0.816 m³/h = **3.7 hours** | |
| Buffer time at average | 3 m³ ÷ 0.555 m³/h = **5.4 hours** | |

**Assessment:** The 3 m³ tank provides adequate buffer for the boiler. The dual feed pumps (1 running + 1 standby) ensure reliability.

**Upstream requirements:**
- Water softener: Included in Fang Kuai package (dual-tank, automatic regeneration, 3 t/h)
- Softened water buffer: **2 m³** tank recommended between softener and feedwater tank

### 4.3 Tank C — Process Water Tank (Bâche d'eau traitée)

**Purpose:** Treated water buffer for production line (preconditioner, CIP, cooling makeup).

| Design parameter | Value | Basis |
|---|---|---|
| Consumers served | Preconditioner + CIP + cooling makeup | |
| Peak hourly demand | 0.4 + 1.5 (CIP peak) + 0.15 = 2.05 m³/h | |
| Daily demand | 6.4 + 8.5 + 2.4 = 17.3 m³/day | |
| Minimum buffer (4 hours) | 2.05 × 4 = 8.2 m³ | |
| CIP surge capacity | 5 m³ (single CIP batch) | |
| **Recommended volume** | **15 m³** | Round up from 8.2 + safety |

> Note: The PCI synoptic diagram shows a "Bâche à eau 10 m³." This may need to be increased to 15 m³ to accommodate CIP surges.

**Construction details:**
- Material: PEHD (polyethylene) or fiberglass (PRFV) food-grade
- Location: Near production line, ideally elevated (+4.00 m) for gravity feed to preconditioner
- Treatment upstream: Sand filter + activated carbon filter (from raw water tank)
- Level control: Level transmitter + automatic fill valve from raw water tank
- Temperature: Ambient (heated locally at preconditioner to 60°C)

### 4.4 Tank D — Softened Water Buffer

**Purpose:** Buffer between water softener output and boiler feedwater tank.

| Parameter | Value |
|---|---|
| Softener output | 3 t/h (Fang Kuai dual-tank) |
| Boiler demand | 0.555–0.816 t/h |
| Regeneration cycle downtime | ~30 min (one tank regenerates while other produces) |
| **Recommended volume** | **2 m³** |

> This tank ensures continuous supply during softener regeneration cycles.

### 4.5 Tank E — Fire Water Reserve (Réserve Incendie)

> Already designed by Soufiane Incendie / INGenios

| Parameter | Value | Source |
|---|---|---|
| **Volume** | **35 m³** | PCI Synoptique Surpresseur |
| Material | Reinforced concrete or steel | PCI drawing |
| Fill line | PEHD DN63 | PCI drawing |
| Fire pump (RIA network) | 1 booster set, twin pumps | DN80 output |
| Fire pump (PI network) | 1 booster set, twin pumps | DN100 output |
| Expansion vessels | 2 × 250 L | PCI drawing |
| Poteaux incendie (PI) | 3 exterior hydrants | NSI ERT Section 19 |
| RIA (robinets d'incendie armés) | 8 total across building | NSI ERT Section 19 |
| Fire safety category | Category A | NSI ERT |
| By-pass | DN65 | PCI drawing |

**Fire water verification:**

Moroccan regulation (Décret n°2-14-499, Livre N°104) for ERT Category A:

| Requirement | Calculation | Duration |
|---|---|---|
| RIA: 2 simultaneous | 2 × 45 L/min = 90 L/min = 5.4 m³/h | 1 hour |
| PI: 1 simultaneous (ext.) | 60 m³/h | 2 hours |
| **Required reserve** | max(5.4×1, 60×2) → governed by PI | |

> Note: The 35 m³ appears sized for the internal RIA network + 1 PI for a reduced duration, which is standard for industrial sites with ONEE-backed supply. The poteaux incendie extérieurs are typically served directly from the ONEE network under pressure. This should be confirmed with Soufiane Incendie.

**Critical:** The fire water reserve must be **permanently full** and **never used for process water.** Level monitoring with automatic refill from raw water tank and a low-level alarm connected to the fire alarm panel are required.

### 4.6 Summary — Complete Tank Inventory

| Tank | Volume | Type | Status | Priority |
|---|---|---|---|---|
| **A — Raw water storage** | **120 m³** (2×60) | Béton armé enterré | **TO BUILD** | Critical |
| **B — Boiler feedwater** | **3 m³** | SS insulated (Fang Kuai) | Included in boiler package | — |
| **C — Process water** | **15 m³** | PEHD/PRFV food-grade | **TO BUILD** (or upgrade existing 10 m³) | High |
| **D — Softened water buffer** | **2 m³** | SS or PEHD | **TO BUILD** | Medium |
| **E — Fire water reserve** | **35 m³** | Béton armé | Designed (INGenios) | Critical |
| **TOTAL** | **175 m³** | | | |

> Compared to ONEE-only scenario (255 m³ total with 200 m³ raw storage), the dual well+ONEE supply reduces raw water storage by **80 m³**, saving approximately **60,000 MAD** in tank construction.

---

## 5. Water Treatment Chain

```
  PRIVATE WELL (forage)          ONEE Municipal Supply (DN80)
  Submersible pump               Backup — auto-activates on low level
  5–8 m³/h                       8–12 m³/h at 2.5–3.5 bar
        │                               │
        │    PEHD DN63–DN80             │    DN80 + disconnecteur BA
        │                               │    + solenoid valve (auto)
        └───────────┬───────────────────┘
                    │
                    ▼
          ┌──────────────────────┐
          │   RAW WATER TANK     │
          │   120 m³ (2 × 60)    │─────────────────────────────────┐
          │   Citerne d'eau brute │                                 │
          └──────────┬───────────┘                                 │
                     │                                              │
              ┌──────┴──────┐                                      │
              │             │                                      │
              ▼             ▼                                      ▼
          ┌────────┐  ┌─────────────┐                      ┌───────────────┐
          │ Sand   │  │ Softener    │                      │ FIRE RESERVE  │
          │ Filter │  │ (Fang Kuai  │                      │  35 m³        │
          │        │  │  dual-tank) │                      │ Dedicated     │
          └───┬────┘  └──────┬──────┘                      └───────────────┘
              │              │
              ▼              ▼
          ┌────────┐  ┌──────────────┐
          │ Carbon │  │ SOFTENED     │
          │ Filter │  │ WATER BUFFER │
          │        │  │  2 m³        │
          └───┬────┘  └──────┬───────┘
              │              │
              ▼              ▼
        ┌─────────────┐  ┌──────────────────┐
        │ PROCESS     │  │ BOILER FEEDWATER  │
        │ WATER TANK  │  │ TANK 3 m³        │
        │ 15 m³       │  │ (+ condensate     │
        │             │  │  return at 85°C)  │
        └─────┬───────┘  └──────┬───────────┘
              │                 │
              ├──► Preconditioner (400 kg/h, heated to 60°C)
              ├──► CIP system
              ├──► Cooling makeup
              ├──► Sanitary (via direct line from raw tank)
              │                 │
              │                 └──► Feed pumps 2×4 m³/h ──► Boiler 3 t/h
              │
              └──► Floor washing / misc
```

---

## 6. Water Supply Sources & Fill Rates

### 6.1 Primary Source — Private Well (Forage)

| Parameter | Value |
|---|---|
| Well pump type | Submersible borehole pump (e.g. Grundfos SP or Pedrollo 4SR) |
| Expected flow rate | 5–8 m³/h (to confirm after pump test) |
| Total dynamic head | ~50–70 m (static level + friction + elevation to tanks) |
| Motor power | ~3–5 kW |
| Daily pumping hours | 8–12 h/day (to supply 46.4 m³/day) |
| Daily electricity cost | ~10–14 kWh × 1.20 MAD = **12–17 MAD/day** |
| Control | VFD recommended; auto start/stop on tank level |
| Dry-run protection | Electrode sensor or float at intake |
| Discharge pipe | PEHD DN63–DN80 to raw water tank |
| Annual pumped volume | ~12,500 m³ (90% of 13,920 m³) |
| Annual pumping cost | ~18,750 MAD |

**Well pump sizing note:** Final pump selection depends on the pump test results after drilling. The submersible pump must be sized to the confirmed well yield and static water level. A spare pump should be stored on-site for rapid replacement.

### 6.2 Backup Source — ONEE Municipal Supply

| Parameter | Value |
|---|---|
| ONEE connection size (recommended) | DN80 (minimum) |
| Expected ONEE pressure at site | 2.5–3.5 bar |
| Fill rate at 3 bar, DN80 | ~8–12 m³/h |
| Activation | Automatic: solenoid valve opens when tank level < 30% |
| Disconnection device | BA (disconnecteur à zone de pression réduite) — mandatory |
| ONEE billing meter | Pulsed output, DN80 Woltman-type |
| Expected annual ONEE usage (normal operation) | ~1,400 m³ (~10% of total) = **~11,900 MAD/year** |
| Time to fill 120 m³ from empty (ONEE alone) | 10–15 hours |
| Time to fill fire reserve (35 m³) | ~3–4 hours |

### 6.3 Combined Fill Capacity

| Scenario | Fill Rate | Time to Fill Raw Tank (120 m³) |
|---|---|---|
| Well only | 5–8 m³/h | 15–24 hours |
| ONEE only | 8–12 m³/h | 10–15 hours |
| Both simultaneously | 13–20 m³/h | 6–9 hours |

**Automatic switching logic:**
1. **Normal:** Well pump runs on tank level (start at 60%, stop at 90%)
2. **Low level (< 30%):** ONEE solenoid valve opens automatically, alarm raised
3. **Low-low level (< 15%):** Critical alarm, production shutdown interlock, both sources active
4. **Well failure:** ONEE sustains full plant demand indefinitely (at higher cost)
5. **ONEE failure:** Well sustains full plant demand if yield ≥ 5 m³/h

**Important:** Confirm ONEE connection capacity with local ONEE office (Direction Régionale de Marrakech-Safi). The industrial zone may have a DN100 main, but individual connections are typically DN80.

---

## 7. Moroccan Regulatory Requirements

### Private well (Loi 36-15 sur l'eau)
- **Authorization required** from Agence du Bassin Hydraulique de l'Oum Er-Rbia (ABHOER, Beni Mellal)
- Application file: geological study, estimated extraction volume, intended use, site plan
- **Water meter installation mandatory** — annual declaration of pumped volumes to ABHOER
- **Water quality analysis** — initial analysis at commissioning + annual follow-up (physical, chemical, bacteriological)
- **Redevance (annual fee)** — based on volume extracted, set by ABHOER (typically 0.20–0.50 MAD/m³)
- **Drilling permit** — separate authorization for the drilling works from local authorities
- Well must be > 50 m from any septic tank, waste pit, or contamination source
- Penalties for unauthorized extraction: fines per Art. 151 of Loi 36-15

### Drinking water storage (NM 03.7.001)
- Minimum 24h autonomy for industrial establishments
- Anti-contamination (disconnection device required at ONEE connection)
- Annual inspection and cleaning of storage tanks
- If well water is used for sanitary/drinking purposes, it must meet NM 03.7.001 potable water standards — periodic testing required

### Fire water (Décret n°2-14-499)
- Dedicated reserve — cannot be shared with process water
- Automatic refill with level monitoring
- Annual testing of fire pumps

### Industrial water discharge
- Treated effluent discharge per Loi 36-15 (Environmental Protection)
- CIP and washdown water requires oil/grease separator before discharge
- pH, COD, and BOD limits per Arrêté conjoint

### ONEE connection
- Disconnection device (clapet anti-retour + disconnecteur BA) required to prevent backflow into ONEE network
- Meter with remote reading recommended
- Declaration of industrial water use to ONEE
- ONEE may require verification that private well water cannot cross-contaminate the public network (disconnecteur BA meets this)

---

## 8. Cost Estimate

### 8.1 Well Infrastructure

| Item | Description | Estimated Cost (MAD) |
|---|---|---|
| Well drilling (forage) | 60–80 m depth, DN200 casing | 80,000–120,000 |
| Pump test (essai de pompage) | 72 h step-drawdown + constant rate | 15,000 |
| Submersible pump + motor | 5–8 m³/h, 50–70 m head, ~4 kW | 25,000–35,000 |
| VFD (variateur de fréquence) | For energy savings and soft start | 8,000 |
| Wellhead infrastructure | Concrete pad, sanitary seal, electrical panel | 15,000 |
| Discharge pipe (PEHD DN63) | Well to raw water tank, ~30–50 m | 5,000 |
| Water quality analysis (initial) | Physical + chemical + bacteriological | 3,000 |
| ABHOER authorization fees | Administrative + redevance first year | 5,000 |
| **Sub-total well** | | **156,000–206,000 MAD** |

### 8.2 Water Storage & Treatment

| Item | Description | Estimated Cost (MAD) |
|---|---|---|
| Raw water tank (2 × 60 m³ béton armé) | Including excavation, waterproofing, piping | 160,000 |
| Process water tank (15 m³ PEHD) | Including foundation, piping | 35,000 |
| Softened water buffer (2 m³ SS) | Including connections | 15,000 |
| Sand filter + carbon filter | Automatic backwash, DN80 | 45,000 |
| Transfer pumping station | 2 × 5 m³/h, H=25m (raw tank to treatment) | 25,000 |
| Level instrumentation (5 tanks) | Level transmitters + alarms + PLC | 35,000 |
| Piping network (PEHD/PVC) | Raw + treated + sanitary distribution | 55,000 |
| ONEE backup connection & meter | DN80, disconnecteur BA, solenoid valve | 30,000 |
| **Sub-total storage & treatment** | | **400,000 MAD** |

### 8.3 Total Water System Investment

| Category | Cost (MAD) |
|---|---|
| Well infrastructure | 156,000–206,000 |
| Water storage & treatment | 400,000 |
| **TOTAL (excl. fire & boiler packages)** | **556,000–606,000 MAD** |
| Fire water tank (35 m³) | Already in PCI budget (Soufiane Incendie) |
| Boiler feedwater tank (3 m³) | Included in Fang Kuai package |
| Water softener (dual-tank) | Included in Fang Kuai package |

### 8.4 Annual Operating Cost Comparison

| Scenario | Water Cost | Well Maintenance | ABHOER Fee | Total Annual |
|---|---|---|---|---|
| **ONEE only (no well)** | 118,320 MAD | — | — | **118,320 MAD** |
| **Well + ONEE backup (90/10)** | 30,624 MAD | 10,000 MAD | ~3,000 MAD | **~43,600 MAD** |
| **Annual saving with well** | | | | **~74,700 MAD** |

**Payback period for well investment:** 156,000–206,000 MAD ÷ 74,700 MAD/year = **2.1–2.8 years**

> Note: Fang Kuai boiler package already includes the feedwater tank (3 m³), feed pumps (2 × 4 m³/h), and water softener. These do not need separate procurement.

---

## 9. Recommendations

### Phase 1 — Well & Water Infrastructure (before production start)
1. **Drill the well (forage)** — engage a qualified drilling company (entreprise de forage agréée); obtain ABHOER authorization before drilling starts
2. **Conduct pump test (essai de pompage)** — minimum 72 hours; this determines actual yield and pump sizing
3. **Confirm ONEE backup connection** — contact ONEE Direction Régionale Marrakech-Safi for available pressure and flow at ZI Sidi Bouathmane
4. **Build raw water storage (2 × 60 m³)** — critical path item; production cannot start without adequate water storage
5. **Verify fire water tank (35 m³)** — confirm with Soufiane Incendie that poteaux incendie are served from ONEE direct pressure and the 35 m³ covers RIA network only
6. **Upgrade process water tank** from 10 m³ to 15 m³ (if not yet procured)
7. **Install well pump station** — submersible pump, VFD, wellhead, electrical panel, discharge pipe to raw water tanks

### Phase 2 — Design optimization
8. **Install flash steam recovery vessel** — saves 4.2 m³/day of boiler makeup water (see Condensate Return Rate Calculation)
9. **Install water meters on each circuit** — well output, ONEE input, boiler makeup, preconditioner, CIP, sanitary — to enable water balance monitoring and leak detection
10. **Well water quality monitoring** — establish baseline quality profile; install online TDS/conductivity monitor on well output for early warning of quality changes
11. **Rainwater harvesting** — consider collecting roof water (5,180 m² roof × 300 mm avg rainfall = ~1,554 m³/year) for landscape and floor washing. Payback: ~2 years at well water rates

### Phase 3 — Future consideration
12. **Second well (forage de secours)** — if the factory expands beyond 5 TPH or if the primary well yield declines, a second borehole provides redundancy
13. **Water recycling** — CIP rinse water from final rinse can be reused for first rinse of next cycle (saves ~30% of CIP water)
14. **Cooling tower blowdown recovery** — if evaporative cooling is added later, blowdown can be recovered for floor washing

---

## 10. References

- FAMSUN 5T/H Pet Food Line — Equipment water specifications
- Fang Kuai Boiler Co., LTD — 3 tons steam split condensing boiler quotation (16 June 2026)
- Soufiane Incendie / INGenios — Schema Synoptique Surpresseur (PCI Plan)
- BCAT — NSI ERT PET FACTORY MAROC, Dossier N° CAS-0003311-AK/23
- FAMSUN Chiller Solution V08 — Note de synthèse (6 May 2026)
- PetFactory Morocco — Condensate Return Rate Calculation
- Norme Marocaine NM 03.7.001 — Installations de production et distribution d'eau
- Décret n°2-14-499 — Règlement général de construction, sécurité incendie
- Loi 36-15 sur l'eau — Code de l'eau marocain (groundwater extraction authorization)
- ABHOER — Agence du Bassin Hydraulique de l'Oum Er-Rbia (well permit authority)
- ONEE — Conditions techniques de raccordement
