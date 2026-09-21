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
| Municipal water supply | ONEE (Office National de l'Électricité et de l'Eau potable) |
| Water cost | 8.50 MAD/m³ |

### Water supply from ONEE
The factory connects to the ONEE network at the ZI Sidi Bouathmane industrial zone. In Moroccan industrial zones, ONEE supply can experience:
- Scheduled maintenance shutdowns (24–72 h notice)
- Pressure drops during peak demand (summer)
- Occasional unplanned interruptions (pipe breaks, pump failures)

**Design philosophy:** Size raw water storage for **3–5 days autonomy** to protect production against supply disruptions.

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
**Annual cost:** 13,920 × 8.50 = **~118,320 MAD/year**

### With flash steam recovery vessel (recommended):
| | Daily Peak | Daily Average |
|---|---|---|
| Boiler makeup reduction | -4.2 m³/day | -3.4 m³/day |
| **Revised total** | **42.2 m³/day** | **36.8 m³/day** |
| Annual saving | ~1,260 m³/year | = ~10,710 MAD/year |

---

## 4. Water Tank Inventory — Sizing

### 4.1 Tank A — Raw Water Storage (Citerne d'eau brute)

**Purpose:** Main buffer between ONEE municipal supply and plant water treatment system.

| Design parameter | Value | Basis |
|---|---|---|
| Design daily demand | 46.4 m³/day | Peak day (Section 3) |
| Fire water reserve | 35 m³ | Dedicated tank (Section 4.5) |
| Target autonomy | 3–5 days | ONEE supply risk at Benguerir ZI |
| Minimum volume (3 days) | 46.4 × 3 = **139 m³** | |
| Recommended volume (4 days) | 46.4 × 4 = **186 m³** | |
| Safety margin (10%) | +19 m³ | |
| **Design volume** | **200 m³** | Rounded commercial size |

**Recommended configuration:**

| Option | Description | Cost Estimate | Pros | Cons |
|---|---|---|---|---|
| **Option 1 (Recommended)** | 2 × 100 m³ PEHD/béton | ~220,000 MAD | Redundancy: maintenance possible on one tank while other operates; phased installation | Higher total cost |
| Option 2 | 1 × 200 m³ béton enterré | ~180,000 MAD | Single foundation; lower cost | No redundancy; all-or-nothing maintenance |
| Option 3 | 1 × 200 m³ acier aérien | ~250,000 MAD | Easy inspection; fast install | Higher cost; thermal gain in summer |

**Construction details (Option 1):**
- Material: Reinforced concrete (béton armé), waterproofed with epoxy lining
- Location: Near ONEE connection point, ideally at low elevation on site
- ONEE connection: DN80 minimum (per industrial zone standard)
- Level control: Float valve on ONEE supply + level transmitter (LT) + low-level alarm
- Overflow: DN100 to storm drain
- Drain: DN80 at bottom for cleaning
- Ventilation: Screened vent pipe to prevent contamination
- Access: Manhole 600×600 mm minimum

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
| **A — Raw water storage** | **200 m³** (2×100) | Béton armé enterré | **TO BUILD** | Critical |
| **B — Boiler feedwater** | **3 m³** | SS insulated (Fang Kuai) | Included in boiler package | — |
| **C — Process water** | **15 m³** | PEHD/PRFV food-grade | **TO BUILD** (or upgrade existing 10 m³) | High |
| **D — Softened water buffer** | **2 m³** | SS or PEHD | **TO BUILD** | Medium |
| **E — Fire water reserve** | **35 m³** | Béton armé | Designed (INGenios) | Critical |
| **TOTAL** | **255 m³** | | | |

---

## 5. Water Treatment Chain

```
ONEE Municipal Supply (DN80)
        │
        ▼
┌──────────────────────┐
│   RAW WATER TANK     │
│   200 m³ (2 × 100)   │─────────────────────────────────────────┐
│   Citerne d'eau brute │                                         │
└──────────┬───────────┘                                         │
           │                                                      │
    ┌──────┴──────┐                                              │
    │             │                                              │
    ▼             ▼                                              ▼
┌────────┐  ┌─────────────┐                              ┌───────────────┐
│ Sand   │  │ Softener    │                              │ FIRE RESERVE  │
│ Filter │  │ (Fang Kuai  │                              │  35 m³        │
│        │  │  dual-tank) │                              │ Dedicated     │
└───┬────┘  └──────┬──────┘                              └───────────────┘
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

## 6. ONEE Connection & Fill Rates

| Parameter | Value |
|---|---|
| ONEE connection size (recommended) | DN80 (minimum) |
| Expected ONEE pressure at site | 2.5–3.5 bar |
| Fill rate at 3 bar, DN80 | ~8–12 m³/h |
| Time to fill 200 m³ from empty | 17–25 hours |
| Daily refill requirement | 46.4 m³ → ~4–6 hours of fill per day |
| Fire reserve refill | 35 m³ → ~3–4 hours |

**Important:** Confirm ONEE connection capacity with local ONEE office (Direction Régionale de Marrakech-Safi). The industrial zone may have a DN100 main, but individual connections are typically DN80.

---

## 7. Moroccan Regulatory Requirements

### Drinking water storage (NM 03.7.001)
- Minimum 24h autonomy for industrial establishments
- Anti-contamination (disconnection device required at ONEE connection)
- Annual inspection and cleaning of storage tanks

### Fire water (Décret n°2-14-499)
- Dedicated reserve — cannot be shared with process water
- Automatic refill with level monitoring
- Annual testing of fire pumps

### Industrial water discharge
- Treated effluent discharge per Loi 36-15 (Environmental Protection)
- CIP and washdown water requires oil/grease separator before discharge
- pH, COD, and BOD limits per Arrêté conjoint

### ONEE connection
- Disconnection device (clapet anti-retour + disconnecteur) required to prevent backflow
- Meter with remote reading recommended
- Declaration of industrial water use to ONEE

---

## 8. Cost Estimate

| Item | Description | Estimated Cost (MAD) |
|---|---|---|
| Raw water tank (2 × 100 m³ béton armé) | Including excavation, waterproofing, piping | 220,000 |
| Process water tank (15 m³ PEHD) | Including foundation, piping | 35,000 |
| Softened water buffer (2 m³ SS) | Including connections | 15,000 |
| Sand filter + carbon filter | Automatic backwash, DN80 | 45,000 |
| Pumping station (2 transfer pumps) | 2 × 5 m³/h, H=25m | 25,000 |
| Level instrumentation (5 tanks) | Level transmitters + alarms | 30,000 |
| Piping network (PEHD/PVC) | Raw + treated + sanitary distribution | 55,000 |
| ONEE connection & meter | DN80, including disconnecteur | 25,000 |
| **Sub-total water storage & treatment** | | **450,000 MAD** |
| Fire water tank (35 m³) | Already in PCI budget (Soufiane Incendie) | (separate budget) |
| Boiler feedwater tank (3 m³) | Included in Fang Kuai package | (included) |
| Water softener (dual-tank) | Included in Fang Kuai package | (included) |

> Note: Fang Kuai boiler package already includes the feedwater tank (3 m³), feed pumps (2 × 4 m³/h), and water softener. These do not need separate procurement.

---

## 9. Recommendations

### Immediate actions
1. **Confirm ONEE connection capacity** — contact ONEE Direction Régionale Marrakech-Safi for available pressure and flow at ZI Sidi Bouathmane
2. **Build raw water storage (200 m³)** — this is the critical path item; production cannot start without adequate water storage
3. **Verify fire water tank (35 m³)** — confirm with Soufiane Incendie that poteaux incendie are served from ONEE direct pressure and the 35 m³ covers RIA network only
4. **Upgrade process water tank** from 10 m³ to 15 m³ (if not yet procured)

### Design optimization
5. **Install flash steam recovery vessel** — saves 4.2 m³/day of boiler makeup water (see Condensate Return Rate Calculation)
6. **Install water meters on each circuit** — boiler makeup, preconditioner, CIP, sanitary — to enable water balance monitoring and leak detection
7. **Rainwater harvesting** — consider collecting roof water (5,180 m² roof × 300 mm avg rainfall = ~1,554 m³/year) for landscape and floor washing. Payback: ~3 years at current water rates

### Future consideration
8. **Water recycling** — CIP rinse water from final rinse can be reused for first rinse of next cycle (saves ~30% of CIP water)
9. **Cooling tower blowdown recovery** — if evaporative cooling is added later, blowdown can be recovered for floor washing

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
- ONEE — Conditions techniques de raccordement
