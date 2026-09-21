# Note de Calcul — Dimensionnement des Citernes d'Eau
## Water Tank Sizing Analysis
**Project:** PetFactory Morocco — Sidi Bouathmane, Benguerir  
**Production:** FAMSUN 5 TPH Dry Line + Wet Line (~2.5 TPH)  
**Steam system:** 2 × 4 t/h boilers (8 t/h total capacity)  
**Reference documents:** PCI Synoptique Surpresseur (INGenios), NSI ERT 0003311-NSI-YB (BCAT/Soufiane Incendie), FAMSUN Chiller Solution V08, Condensate Return Rate Calculation, FAMSUN Performance Guarantee Annex  
**Date:** 2026-09-21 (Rev. 2 — wet line + 2×4t/h boilers)  
**Prepared by:** Claude AI / Sam Aribi  

---

## 1. Plant Overview & Water Sources

| Parameter | Value |
|---|---|
| **Dry production line** | FAMSUN 5 TPH pet food (dry kibble) |
| **Wet production line** | ~2.5 TPH wet pet food (cans/pouches) — *capacity to confirm with supplier* |
| Location | ZI Sidi Bouathmane, Benguerir, Province Rhamna |
| Total building area | 5,180 m² (incl. Unité Humide 2,000 m²) |
| Operating schedule | 16 h/day (2 shifts), ~300 days/year |
| Max occupancy (NSI ERT) | 559 persons |
| Typical production staff | ~300 persons/shift (dry + wet lines) |
| **Steam system** | **2 × 4 t/h boilers (8 t/h total capacity)** |
| Water supply — primary | Private well (forage) on site |
| Water supply — backup | ONEE (Office National de l'Électricité et de l'Eau potable) |
| ONEE water cost | 8.50 MAD/m³ |
| Well water cost (pumping only) | ~1.50 MAD/m³ (electricity + maintenance) |

> **Note on wet line estimates:** The wet production line equipment has not been specified yet. Water demands for the wet line are estimated based on industry standards for a 2–3 TPH wet pet food line with batch retorts. These figures should be updated once the wet line supplier and equipment are confirmed.

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

> **Critical finding:** With the wet line, peak daily demand rises to ~116 m³/day. A single well at the low end of yield (3–5 m³/h) **cannot** sustain the plant alone — it would need 23+ hours of continuous pumping. Either the well must yield ≥ 8 m³/h, or **two wells** are needed, or the ONEE connection becomes a co-primary source rather than a pure backup. The pump test after drilling will determine the appropriate strategy.

**Regulatory requirements for private well in Morocco:**
- Authorization from the Agence du Bassin Hydraulique de l'Oum Er-Rbia (ABHOER)
- Loi 36-15 sur l'eau (Water Law) — permit required for any groundwater extraction
- Annual declaration of volumes pumped
- Meter installation mandatory
- Water quality analysis (initial + annual)

**2. ONEE municipal supply — Backup (or co-primary)**

The ONEE connection at the ZI Sidi Bouathmane industrial zone serves as a **backup** supply — or as a **co-primary** source if well yield is insufficient for the combined dry+wet plant:
- Well pump failure or maintenance
- Peak demand exceeding well capacity
- Well water quality issues (seasonal variations)
- Sanitary/drinking water (if well water doesn't meet potable standards)

ONEE supply risks in Moroccan industrial zones:
- Scheduled maintenance shutdowns (24–72 h notice)
- Pressure drops during peak demand (summer)
- Occasional unplanned interruptions (pipe breaks, pump failures)

**Design philosophy:** Raw water storage is sized so that **either source alone** can sustain the factory for at least **2 days**, and both together provide **3+ days** of autonomy. With the larger combined plant demand, the ONEE connection is upgraded to **DN100**.

---

## 2. Water Consumers — Detailed Demand Calculation

### 2.1 Steam System — 2 × 4 t/h Boilers

The factory replaces the original Fang Kuai 3 t/h boiler with **two 4 t/h steam boilers** to serve both production lines.

**Steam distribution (combined plant):**

| Equipment | Steam (t/h) | Line | Heat Exchange Type |
|---|---|---|---|
| Dryer | 1.40 | Dry | Indirect (shell & tube) |
| Preconditioner | 0.75 | Dry | Mixed: 30% direct + 70% jacket |
| Liquid fat daily tanks | 0.30 | Dry | Indirect coil |
| Retorts (2–3 batch units) | 2.00 | Wet | Indirect (steam jacket + spray) |
| Cooking kettles / mixers | 0.50 | Wet | Indirect (jacketed) |
| Sauce / gravy preparation | 0.30 | Wet | Indirect (jacketed) |
| CIP hot water + tracing | 0.25 | Wet | Heat exchanger / tracing |
| **Total — dry line** | **2.45** | | |
| **Total — wet line** | **3.05** | | |
| **Total plant peak** | **5.50** | | |

> **Boiler capacity utilization:** 5.50 / 8.00 = **69%** at peak (both lines at capacity). Average load ~4.50 t/h (56%). The 8 t/h capacity provides comfortable margin for retort heat-up surges, which can momentarily reach 7+ t/h.

### 2.2 Boiler Feedwater Makeup

**Condensate return analysis (combined plant):**

| Equipment | Steam In (t/h) | Return Rate | Basis | Condensate (t/h) |
|---|---|---|---|---|
| Dryer | 1.40 | 92% | All indirect | 1.288 |
| Preconditioner | 0.75 | 63% | 30% direct (lost) + 70% jacket @ 90% | 0.473 |
| Fat tanks | 0.30 | 85% | Closed coil | 0.255 |
| Retorts | 2.00 | 85% | Indirect, high recovery | 1.700 |
| Cooking kettles | 0.50 | 80% | Jacketed | 0.400 |
| Sauce prep | 0.30 | 80% | Jacketed | 0.240 |
| CIP/tracing | 0.25 | 60% | Mixed (some direct contact) | 0.150 |
| **Total** | **5.50** | | | **4.506** |

**Flash steam losses at traps (1 MPa → 0.1 MPa):** flash fraction = 15.3% (same as dry line calculation)

| Scenario | Condensate Returned | Return Rate | Makeup Water | Blowdown (3%) | Total Boiler Water |
|---|---|---|---|---|---|
| No flash recovery | 4.506 − 0.689 = **3.817 t/h** | **69.4%** | 1.683 t/h | 0.165 t/h | **1.848 t/h** |
| With flash recovery | 3.817 + 0.584 = **4.401 t/h** | **80.0%** | 1.099 t/h | 0.165 t/h | **1.264 t/h** |

| Parameter | No Flash Recovery | With Flash Recovery |
|---|---|---|
| Daily peak (16 h) | **29.6 m³/day** | **20.2 m³/day** |
| Daily average | 24.2 m³/day | 16.5 m³/day |

**Boiler water must be softened.** With 2 × 4 t/h boilers, the softener must be sized for the higher makeup rate — see Section 4.4.

### 2.3 Process Water — Dry Line (Preconditioner)

> Source: FAMSUN specifications, petfood_simulator (`models/preconditioner.py`)

| Parameter | Value |
|---|---|
| Water addition to preconditioner | 400 kg/h |
| Pre-heating temperature | ~60 °C |
| Steam injection (direct) | 0.225 t/h (30% of preconditioner steam) |
| **Net process water consumed** | **0.400 t/h** |
| Daily (16 h) | 6.4 m³/day |

This water is absorbed into the product — it is not recovered.

### 2.4 Process Water — Wet Line

> Source: Industry estimates for 2.5 TPH wet pet food line. *Update once equipment confirmed.*

Wet pet food is typically 70–80% moisture. Raw materials (meat, meals) already contain significant water, so net added process water is a fraction of product moisture content.

| Consumer | Flow (t/h) | Daily (16 h) | Notes |
|---|---|---|---|
| Recipe/formulation water (mixing, sauce, gravy) | 1.00 | 16.0 m³/day | Net added water into product (after accounting for water in raw materials) |
| Can/pouch rinsing | 0.20 | 3.2 m³/day | Pre-fill container rinse |
| **Total wet line process water** | **1.20** | **19.2 m³/day** | Consumed in product or discharged |

### 2.5 Cooling Water

#### Dry line — Chiller system
> Source: FAMSUN Chiller Solution V08

| Parameter | Value |
|---|---|
| FAMSUN chiller capacity | 180 kW (8 ventilo-convectors FP-238) |
| VRV existing | 410 kW (2 × 205 kW) |
| Circuit type | Closed loop (water-glycol) |
| Makeup water (evaporation/leaks) | ~0.15 t/h |
| Daily makeup | 2.4 m³/day |

#### Wet line — Retort cooling system

Batch retorts require rapid cooling of sterilized product after the hold phase. A **recirculating cooling system with cooling tower** is standard to minimize water consumption.

| Parameter | Value |
|---|---|
| Retort cooling circulation rate | 15–20 m³/h (through retorts during cooling phase) |
| Cooling tower type | Induced-draft, counterflow |
| Cooling from / to | 45 °C → 25 °C |
| Evaporation loss (cooling tower) | ~2–3% of circulation = 0.4–0.6 t/h |
| Blowdown (cooling tower) | ~0.2 t/h (to control TDS buildup) |
| **Total retort cooling makeup** | **~0.80 t/h** |
| Daily makeup (16 h) | **12.8 m³/day** |

> Without a recirculating cooling tower (once-through cooling), the retort would consume 15–20 m³/h of water directly — over 300 m³/day. **A cooling tower is essential** for the wet line.

**Combined cooling makeup:** 0.15 + 0.80 = **0.95 t/h** → **15.2 m³/day**

### 2.6 CIP / Washdown Water

#### Dry line CIP

| Operation | Frequency | Volume |
|---|---|---|
| Equipment rinsing (extruder, preconditioner, dryer) | Daily | 3.0 m³ |
| Floor washing (production areas) | Daily | 2.5 m³ |
| Fat system cleaning (daily tanks, enrobeuse) | Daily | 1.5 m³ |
| Packaging area cleaning | Daily | 1.0 m³ |
| Deep CIP (monthly full line cleaning) | Monthly | 15.0 m³ |
| **Daily average — dry line** | | **8.5 m³/day** |

#### Wet line CIP

Wet pet food production involves meat, protein, and fat — requiring **significantly more intensive cleaning** than dry kibble to meet food safety and HACCP standards.

| Operation | Frequency | Volume |
|---|---|---|
| Retort interior/basket cleaning | Daily | 3.0 m³ |
| Cooking kettles / mixer CIP | Daily | 3.0 m³ |
| Sauce preparation vessel CIP | Daily | 2.0 m³ |
| Filling/seaming machine CIP | Daily | 2.0 m³ |
| Wet line floor washing | Daily | 3.0 m³ |
| Deep CIP wet line (weekly, amortized) | Daily average | 3.0 m³ |
| **Daily average — wet line** | | **16.0 m³/day** |

**Combined CIP / washdown:** 8.5 + 16.0 = **24.5 m³/day**

### 2.7 Sanitary Water

| Category | Persons | Consumption | Volume |
|---|---|---|---|
| Production workers — dry line (showers, WC, drinking) | 150 | 50 L/person/day | 7.5 m³/day |
| Production workers — wet line | 150 | 50 L/person/day | 7.5 m³/day |
| Admin, lab & visitors | 40 | 80 L/person/day | 3.2 m³/day |
| Kitchen/canteen | 340 | 10 L/person/day | 3.4 m³/day |
| **Total sanitary** | | | **21.6 m³/day** |

> Moroccan industrial standard: 50–80 L/worker/day (Norme Marocaine NM 03.7.001)

### 2.8 Miscellaneous

| Use | Volume |
|---|---|
| Green spaces/landscape | 0.5 m³/day |
| Lab/quality control (both lines) | 0.5 m³/day |
| Truck washing area | 0.5 m³/day |
| Cooling tower chemical treatment water | 0.3 m³/day |
| **Total miscellaneous** | **1.8 m³/day** |

---

## 3. Total Water Balance Summary

| Consumer | Peak (m³/h) | Daily Peak (m³/day) | Daily Average (m³/day) |
|---|---|---|---|
| Boiler makeup — 2×4t/h (no flash) | 1.848 | 29.6 | 24.2 |
| Process water — dry preconditioner | 0.400 | 6.4 | 6.4 |
| Process water — wet line | 1.200 | 19.2 | 16.0 |
| Cooling — dry chiller makeup | 0.150 | 2.4 | 1.8 |
| Cooling — retort (recirculating makeup) | 0.800 | 12.8 | 10.0 |
| CIP / washdown — dry line | — | 8.5 | 8.5 |
| CIP / washdown — wet line | — | 16.0 | 14.0 |
| Sanitary water | — | 21.6 | 18.0 |
| Miscellaneous | — | 1.8 | 1.5 |
| **TOTAL (excl. fire)** | **~4.40** | **118.3** | **100.4** |

**Peak hourly demand (production hours):** ~7.5 m³/h (including CIP surges and retort batch peaks)  
**Annual consumption:** 118 × 300 = **~35,400 m³/year** (peak basis); 100 × 300 = **~30,100 m³/year** (average)

### Comparison: Dry-only vs Dry+Wet plant

| Parameter | Dry Line Only (Rev. 1) | Dry + Wet Lines (Rev. 2) | Increase |
|---|---|---|---|
| Daily peak demand | 46.4 m³/day | 118.3 m³/day | **+155%** |
| Daily average | 40.2 m³/day | 100.4 m³/day | **+150%** |
| Annual consumption | ~13,920 m³ | ~35,400 m³ | **+154%** |
| Peak steam demand | 2.45 t/h | 5.50 t/h | **+124%** |
| Boiler capacity | 3 t/h (1 boiler) | 8 t/h (2 boilers) | **+167%** |

### Annual cost comparison — Well vs ONEE:

| Source | Unit Cost | Annual Cost (at 35,400 m³) | Saving vs ONEE |
|---|---|---|---|
| ONEE only | 8.50 MAD/m³ | 300,900 MAD/year | — |
| Well only (pumping cost) | ~1.50 MAD/m³ | 53,100 MAD/year | **247,800 MAD/year** |
| Well primary + ONEE backup (80/20 split) | ~2.90 MAD/m³ avg | 102,660 MAD/year | **198,240 MAD/year** |

> With the larger combined plant, the well saves approximately **198,000–248,000 MAD/year**. The higher daily demand may require a higher well yield or two wells, which increases the ONEE backup share to 20%.

### With flash steam recovery vessel (recommended):

| | Daily Peak | Daily Average |
|---|---|---|
| Boiler makeup reduction | -9.4 m³/day | -7.7 m³/day |
| **Revised total** | **108.9 m³/day** | **92.7 m³/day** |
| Additional annual saving | ~2,820 m³/year | = ~4,230 MAD/year (well) or ~23,970 MAD/year (ONEE) |

---

## 4. Water Tank Inventory — Sizing

### 4.1 Tank A — Raw Water Storage (Citerne d'eau brute)

**Purpose:** Main buffer fed by both the private well and the ONEE backup connection.

**Sizing rationale with dual supply:**

With the combined dry+wet plant demand of ~118 m³/day, the raw water storage must be significantly larger than the dry-only plant.

| Design parameter | Value | Basis |
|---|---|---|
| Design daily demand | 118 m³/day | Peak day (Section 3) |
| Well pump required yield | 8–12 m³/h | To meet demand in 12–15 h/day |
| Minimum buffer (pump failure) | 118 × 2 = 236 m³ | 2 days autonomy (ONEE backup activates) |
| Safety margin (10%) | +24 m³ | |
| **Design volume** | **250 m³** | 2 × 125 m³ recommended |

> With only ONEE, this would need to be **400+ m³** for 3–4 days autonomy. The well reduces storage to 250 m³ because both sources can independently sustain the plant. If both fail simultaneously, the 250 m³ reserve covers **2+ days**.

**Recommended configuration:**

| Option | Description | Cost Estimate | Pros | Cons |
|---|---|---|---|---|
| **Option 1 (Recommended)** | 2 × 125 m³ béton armé | ~280,000 MAD | Redundancy: one tank cleaned while other operates; separate feed from well and ONEE | Higher cost |
| Option 2 | 1 × 250 m³ béton armé | ~220,000 MAD | Single foundation; lower cost | No redundancy during maintenance |
| Option 3 | 2 × 100 m³ + 1 × 50 m³ | ~260,000 MAD | Flexibility: 50 m³ tank dedicated to boiler circuit | Three foundations |

**Construction details (Option 1 — 2 × 125 m³):**
- Material: Reinforced concrete (béton armé), waterproofed with epoxy lining
- Location: Near the well head and boiler room, at low elevation on site
- Well pump discharge: PEHD DN80–DN100 into tanks
- ONEE backup connection: DN100 with automatic fill valve (opens on low level)
- Disconnection device on ONEE line: mandatory (anti-retour + disconnecteur BA)
- Level control per tank: Level transmitter (LT) + high/low/low-low alarms
- Low level → alarm + auto-switch to ONEE backup
- Low-low level → critical alarm + production shutdown interlock
- Overflow: DN150 to storm drain
- Drain: DN100 at bottom for cleaning
- Ventilation: Screened vent pipe to prevent contamination
- Access: Manhole 600×600 mm minimum per tank
- Inter-tank connection: DN100 with isolation valve (allows balancing or isolation)

### 4.1.1 Well Pump Station

| Parameter | Recommended |
|---|---|
| Pump type | Submersible borehole pump |
| Flow rate | 8–12 m³/h (confirm after pump test) |
| Head | ~50–70 m (static level + friction + elevation) |
| Power | ~5–8 kW |
| Control | VFD (variable frequency drive) recommended |
| Level protection | Dry-run protection sensor in well |
| Operating mode | Automatic: starts on tank low level, stops on high level |
| Backup pump | Recommended (stored on-site spare, not installed) |
| Estimated cost | 45,000–65,000 MAD (pump + VFD + wellhead piping) |

> **If the well yield is < 8 m³/h after pump test**, consider: (a) drilling a second well, or (b) upgrading the ONEE connection to co-primary status with DN100 and a higher contracted capacity.

### 4.1.2 ONEE Backup Connection

| Parameter | Value |
|---|---|
| Connection size | **DN100** (upgraded from DN80 for higher demand) |
| Activation | Automatic: solenoid valve opens when tank level < 40% |
| Disconnection device | BA (disconnecteur à zone de pression réduite) — mandatory |
| Flow meter | Pulsed output meter for ONEE billing |
| Expected fill rate | 12–18 m³/h at 2.5–3.5 bar ONEE pressure |
| Annual ONEE usage (normal) | ~20% of total = ~7,100 m³/year = ~60,350 MAD/year |

### 4.2 Tank B — Boiler Feedwater Tank (Bâche alimentaire)

With **2 × 4 t/h boilers**, the feedwater system must be sized accordingly. The previous Fang Kuai 3 t/h package (3 m³ tank, 2 × 4 m³/h pumps) is **no longer adequate**.

| Parameter | Value | Basis |
|---|---|---|
| Boiler total capacity | 2 × 4 = 8 t/h | |
| Peak steam consumption | 5.50 t/h | Section 2.1 |
| Makeup water flow (no flash) | 1.848 t/h | Section 2.2 |
| Condensate return (hot, ~85°C) | 3.817 t/h | Section 2.2 |
| Total feedwater flow at peak | 5.665 t/h | Makeup + condensate |
| **Recommended tank volume** | **10 m³** | Shared between both boilers |
| Buffer time at peak | 10 ÷ 1.848 = **5.4 hours** | Time before makeup runs out |
| Material | Stainless steel, insulated | Standard for boiler feedwater |
| Feed water pumps | 2 × 8 m³/h per boiler (1+1 standby) | 4 pumps total |

> The 10 m³ tank provides a shared feedwater reservoir for both boilers. Each boiler has its own feed pump set (2 × 8 m³/h, 1 running + 1 standby). A common header allows either boiler to draw from the tank.

**Upstream requirements:**
- Water softener: Must handle 1.85 t/h makeup — see Section 4.4
- Deaerator: Recommended for 2 × 4 t/h boilers (removes dissolved O₂, reduces corrosion)

### 4.3 Tank C — Process Water Tank (Bâche d'eau traitée)

**Purpose:** Treated water buffer for both production lines (preconditioner, wet line process, CIP, cooling makeup).

| Design parameter | Value | Basis |
|---|---|---|
| Consumers served | Preconditioner + wet line process + CIP (both lines) + dry cooling makeup | |
| Peak hourly demand | 0.4 + 1.2 + 2.5 (CIP peak) + 0.15 = **4.25 m³/h** | |
| Daily demand | 6.4 + 19.2 + 24.5 + 2.4 = **52.5 m³/day** | |
| Minimum buffer (4 hours) | 4.25 × 4 = 17 m³ | |
| CIP surge capacity | 8 m³ (simultaneous CIP on both lines) | |
| **Recommended volume** | **30 m³** | Round up from 17 + surge + safety |

> Increased from 15 m³ (dry-only) to 30 m³ to handle the wet line's process water demand and more intensive CIP schedule.

**Construction details:**
- Material: PEHD (polyethylene) or fiberglass (PRFV) food-grade
- Location: Near production lines, ideally elevated (+4.00 m) for gravity feed
- Treatment upstream: Sand filter + activated carbon filter (from raw water tank)
- Level control: Level transmitter + automatic fill valve from raw water tank
- Hot water generation: Plate heat exchanger for CIP hot water (heated by steam)

### 4.4 Tank D — Softened Water Buffer

**Purpose:** Buffer between water softener output and boiler feedwater tank.

With 2 × 4 t/h boilers consuming up to 1.85 t/h of makeup water, the softener and buffer must be upgraded.

| Parameter | Value |
|---|---|
| Makeup water demand (peak) | 1.848 t/h |
| Softener configuration | **2 × 3 t/h alternating** (one online, one regenerating) |
| Regeneration cycle downtime | ~45 min per unit |
| Buffer requirement | 1.848 × 0.75 h = 1.4 m³ minimum |
| **Recommended volume** | **5 m³** |

> Upgraded from 2 m³ (dry-only) to 5 m³ to buffer the higher boiler makeup demand during softener regeneration. The dual 3 t/h alternating softener replaces the single Fang Kuai unit.

### 4.5 Tank E — Fire Water Reserve (Réserve Incendie)

> Already designed by Soufiane Incendie / INGenios — **unchanged from Rev. 1**

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

> Note: The 35 m³ appears sized for the internal RIA network + 1 PI for a reduced duration, standard for industrial sites with ONEE-backed supply. The poteaux incendie extérieurs are served directly from the ONEE network under pressure. Confirm with Soufiane Incendie.

**Critical:** The fire water reserve must be **permanently full** and **never used for process water.** Level monitoring with automatic refill from raw water tank and a low-level alarm connected to the fire alarm panel are required.

### 4.6 Tank F — Retort Cooling Water Tank (NEW — Wet Line)

**Purpose:** Dedicated buffer for the wet line batch retort cooling system with recirculating cooling tower.

| Design parameter | Value | Basis |
|---|---|---|
| Retort cooling circulation | 15–20 m³/h | During cooling phase of retort cycle |
| Number of retorts | 2–3 batch units | Typical for 2.5 TPH wet line |
| Single retort batch volume | ~5–8 m³ | Water required per cooling cycle |
| Cooling tower return | Continuous during operation | 25 °C supply, 45 °C return |
| Makeup from raw water | 0.80 t/h (evaporation + blowdown) | Section 2.5 |
| **Recommended volume** | **25 m³** | Surge capacity for 2 simultaneous retort batches |

**Construction details:**
- Material: Steel or fiberglass with corrosion-resistant lining
- Location: Adjacent to retort area and cooling tower, at grade level
- Cooling tower: Induced-draft counterflow, 200–250 kW rejection capacity
- Chemical treatment: Anti-scale + biocide dosing system (automated)
- Overflow to raw water tank (not to drain — water is reusable)
- Blowdown: Controlled discharge based on conductivity

### 4.7 Summary — Complete Tank Inventory

| Tank | Volume | Type | Status | Priority |
|---|---|---|---|---|
| **A — Raw water storage** | **250 m³** (2×125) | Béton armé enterré | **TO BUILD** | Critical |
| **B — Boiler feedwater** | **10 m³** | SS insulated (shared, 2 boilers) | **TO PROCURE** with boiler package | Critical |
| **C — Process water** | **30 m³** | PEHD/PRFV food-grade | **TO BUILD** | High |
| **D — Softened water buffer** | **5 m³** | SS or PEHD | **TO BUILD** | High |
| **E — Fire water reserve** | **35 m³** | Béton armé | Designed (INGenios) | Critical |
| **F — Retort cooling water** | **25 m³** | Steel/FRP with cooling tower | **TO BUILD** (wet line) | High |
| **TOTAL** | **355 m³** | | | |

### Comparison: Dry-only vs Dry+Wet tank requirements

| Tank | Dry Only (Rev. 1) | Dry + Wet (Rev. 2) | Change |
|---|---|---|---|
| Raw water | 120 m³ | 250 m³ | +108% |
| Boiler feedwater | 3 m³ (Fang Kuai) | 10 m³ (new) | +233% |
| Process water | 15 m³ | 30 m³ | +100% |
| Softened water buffer | 2 m³ | 5 m³ | +150% |
| Fire reserve | 35 m³ | 35 m³ | unchanged |
| Retort cooling | — | 25 m³ | **new** |
| **TOTAL** | **175 m³** | **355 m³** | **+103%** |

---

## 5. Water Treatment Chain

```
  PRIVATE WELL (forage)               ONEE Municipal Supply (DN100)
  Submersible pump                     Backup / co-primary
  8–12 m³/h                            12–18 m³/h at 2.5–3.5 bar
        │                                     │
        │    PEHD DN80–DN100                  │    DN100 + disconnecteur BA
        │                                     │    + solenoid valve (auto)
        └──────────────┬──────────────────────┘
                       │
                       ▼
             ┌──────────────────────┐
             │   RAW WATER TANK     │
             │   250 m³ (2 × 125)   │──────────────────────────────────┐
             │   Citerne d'eau brute │                                  │
             └──────────┬───────────┘                                  │
                        │                                               │
                 ┌──────┴──────┬───────────────┐                       │
                 │             │               │                       │
                 ▼             ▼               ▼                       ▼
           ┌────────┐  ┌───────────┐  ┌──────────────┐        ┌───────────────┐
           │ Sand   │  │ Softener  │  │ RETORT       │        │ FIRE RESERVE  │
           │ Filter │  │ 2×3 t/h   │  │ COOLING TANK │        │  35 m³        │
           │        │  │ alternating│  │  25 m³       │        │ Dedicated     │
           └───┬────┘  └─────┬─────┘  │ + cooling    │        └───────────────┘
               │             │        │   tower       │
               ▼             ▼        └──────┬───────┘
           ┌────────┐  ┌──────────┐          │
           │ Carbon │  │ SOFTENED  │          └──► Retort cooling
           │ Filter │  │ WATER    │                (recirculating)
           │        │  │ BUFFER   │
           └───┬────┘  │  5 m³    │
               │       └────┬─────┘
               ▼            ▼
         ┌──────────┐  ┌──────────────────┐
         │ PROCESS  │  │ BOILER FEEDWATER  │
         │ WATER    │  │ TANK 10 m³       │
         │ TANK     │  │ (+ condensate     │
         │ 30 m³    │  │  return at 85°C)  │
         └────┬─────┘  └──────┬───────────┘
              │               │
              ├──► Dry: Preconditioner (400 kg/h)
              ├──► Wet: Recipe water (1,000 kg/h)
              ├──► Wet: Can/pouch rinsing
              ├──► CIP system (both lines)
              ├──► Dry: Cooling makeup
              ├──► Sanitary (via direct line from raw tank)
              │               │
              │               └──► Feed pumps ──► 2 × 4 t/h boilers
              │
              └──► Floor washing / misc
```

---

## 6. Water Supply Sources & Fill Rates

### 6.1 Primary Source — Private Well (Forage)

| Parameter | Value |
|---|---|
| Well pump type | Submersible borehole pump (e.g. Grundfos SP or Pedrollo 4SR) |
| Required flow rate | **8–12 m³/h** (to confirm after pump test) |
| Total dynamic head | ~50–70 m (static level + friction + elevation to tanks) |
| Motor power | ~5–8 kW |
| Daily pumping hours | 10–15 h/day (to supply 118 m³/day at 8–12 m³/h) |
| Daily electricity cost | ~12–18 kWh × 1.20 MAD = **14–22 MAD/day** |
| Control | VFD recommended; auto start/stop on tank level |
| Dry-run protection | Electrode sensor or float at intake |
| Discharge pipe | PEHD DN80–DN100 to raw water tank |
| Annual pumped volume | ~28,300 m³ (80% of 35,400 m³) |
| Annual pumping cost | ~42,500 MAD |

> **Well yield concern:** The Benguerir aquifer typically yields 3–10 m³/h. At the low end, a single well **cannot** supply 118 m³/day. If the pump test shows < 8 m³/h, plan for either a second well or a higher ONEE share (30–40% instead of 20%).

### 6.2 Backup Source — ONEE Municipal Supply

| Parameter | Value |
|---|---|
| ONEE connection size | **DN100** (upgraded for combined plant demand) |
| Expected ONEE pressure at site | 2.5–3.5 bar |
| Fill rate at 3 bar, DN100 | ~12–18 m³/h |
| Activation | Automatic: solenoid valve opens when tank level < 40% |
| Disconnection device | BA (disconnecteur à zone de pression réduite) — mandatory |
| ONEE billing meter | Pulsed output, DN100 Woltman-type |
| Expected annual ONEE usage | ~20% of total = ~7,100 m³/year = **~60,350 MAD/year** |
| Time to fill 250 m³ from empty (ONEE alone) | 14–21 hours |
| Time to fill fire reserve (35 m³) | ~2–3 hours |

### 6.3 Combined Fill Capacity

| Scenario | Fill Rate | Time to Fill Raw Tank (250 m³) |
|---|---|---|
| Well only (8 m³/h) | 8 m³/h | 31 hours |
| Well only (12 m³/h) | 12 m³/h | 21 hours |
| ONEE only | 12–18 m³/h | 14–21 hours |
| Both simultaneously | 20–30 m³/h | 8–13 hours |

**Automatic switching logic:**
1. **Normal:** Well pump runs on tank level (start at 50%, stop at 90%)
2. **Low level (< 40%):** ONEE solenoid valve opens automatically, alarm raised
3. **Low-low level (< 15%):** Critical alarm, production shutdown interlock, both sources active
4. **Well failure:** ONEE sustains full plant demand indefinitely (at higher cost)
5. **ONEE failure:** Well sustains full plant demand if yield ≥ 8 m³/h; if < 8 m³/h, reduce to dry line only

**Important:** Confirm ONEE connection capacity with local ONEE office (Direction Régionale de Marrakech-Safi). Request **DN100 connection** for the combined dry+wet plant. The industrial zone main may be DN150, but individual connections must be specifically requested at DN100.

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
- **Higher extraction volume (35,000+ m³/year)** may trigger additional environmental impact study requirements

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
- CIP and washdown water requires oil/grease separator before discharge — **especially critical for wet line** (higher BOD/COD from meat processing)
- pH, COD, and BOD limits per Arrêté conjoint
- **Wet line wastewater** may require additional pre-treatment (dissolved air flotation or similar) before discharge due to high protein/fat load

### ONEE connection
- Disconnection device (clapet anti-retour + disconnecteur BA) required to prevent backflow into ONEE network
- Meter with remote reading recommended
- Declaration of industrial water use to ONEE
- ONEE may require verification that private well water cannot cross-contaminate the public network (disconnecteur BA meets this)
- **DN100 connection** requires specific application and may have higher connection fees

---

## 8. Cost Estimate

### 8.1 Well Infrastructure

| Item | Description | Estimated Cost (MAD) |
|---|---|---|
| Well drilling (forage) | 60–80 m depth, DN200 casing | 80,000–120,000 |
| Pump test (essai de pompage) | 72 h step-drawdown + constant rate | 15,000 |
| Submersible pump + motor | 8–12 m³/h, 50–70 m head, ~6 kW | 35,000–50,000 |
| VFD (variateur de fréquence) | For energy savings and soft start | 10,000 |
| Wellhead infrastructure | Concrete pad, sanitary seal, electrical panel | 18,000 |
| Discharge pipe (PEHD DN80) | Well to raw water tank, ~30–50 m | 8,000 |
| Water quality analysis (initial) | Physical + chemical + bacteriological | 3,000 |
| ABHOER authorization fees | Administrative + redevance first year | 8,000 |
| **Sub-total well** | | **177,000–232,000 MAD** |

### 8.2 Water Storage & Treatment

| Item | Description | Estimated Cost (MAD) |
|---|---|---|
| Raw water tank (2 × 125 m³ béton armé) | Including excavation, waterproofing, piping | 280,000 |
| Process water tank (30 m³ PEHD/FRP) | Including foundation, piping | 55,000 |
| Retort cooling water tank (25 m³ steel) | Including cooling tower, chemical dosing | 120,000 |
| Boiler feedwater tank (10 m³ SS insulated) | Including condensate receiver | 65,000 |
| Softened water buffer (5 m³ SS) | Including connections | 25,000 |
| Water softeners (2 × 3 t/h alternating) | Automatic regeneration, resin, brine tank | 75,000 |
| Sand filter + carbon filter | Automatic backwash, DN100 | 55,000 |
| Transfer pumping station | 2 × 8 m³/h, H=25m (raw tank to treatment) | 35,000 |
| Boiler feed pumps (4 × 8 m³/h, H=140m) | 2 running + 2 standby, for 2 boilers | 60,000 |
| Level instrumentation (6 tanks + well) | Level transmitters + alarms + PLC | 50,000 |
| Piping network (PEHD/PVC/SS) | Raw + treated + sanitary + retort loop | 85,000 |
| ONEE backup connection & meter | DN100, disconnecteur BA, solenoid valve | 40,000 |
| Wastewater pre-treatment (wet line) | Oil/grease separator + DAF unit | 80,000 |
| **Sub-total storage & treatment** | | **1,025,000 MAD** |

### 8.3 Total Water System Investment

| Category | Cost (MAD) |
|---|---|
| Well infrastructure | 177,000–232,000 |
| Water storage & treatment | 1,025,000 |
| **TOTAL (excl. fire & boilers)** | **1,202,000–1,257,000 MAD** |
| Fire water tank (35 m³) | Already in PCI budget (Soufiane Incendie) |
| 2 × 4 t/h boilers | Separate boiler procurement (not in this budget) |

### Comparison: Dry-only vs Dry+Wet investment

| Item | Dry Only (Rev. 1) | Dry + Wet (Rev. 2) | Increase |
|---|---|---|---|
| Well infrastructure | 156,000–206,000 | 177,000–232,000 | +21,000–26,000 |
| Storage & treatment | 400,000 | 1,025,000 | +625,000 |
| **Total** | **556,000–606,000** | **1,202,000–1,257,000** | **+646,000–651,000** |

> The wet line adds ~650,000 MAD to the water infrastructure, primarily from the retort cooling system (120k), larger raw water tank (120k increase), larger process water tank (20k increase), boiler feedwater system (125k), wastewater pre-treatment (80k), and larger piping/instrumentation (110k increase).

### 8.4 Annual Operating Cost Comparison

| Scenario | Water Cost | Well Maintenance | ABHOER Fee | Total Annual |
|---|---|---|---|---|
| **ONEE only (no well)** | 300,900 MAD | — | — | **300,900 MAD** |
| **Well + ONEE backup (80/20)** | 102,660 MAD | 15,000 MAD | ~7,000 MAD | **~124,700 MAD** |
| **Annual saving with well** | | | | **~176,200 MAD** |

**Payback period for well investment:** 177,000–232,000 MAD ÷ 176,200 MAD/year = **1.0–1.3 years**

> With the larger combined plant, the well pays for itself in approximately **one year** — even faster than the dry-only scenario. The higher water volume amplifies the well's cost advantage.

---

## 9. Recommendations

### Phase 1 — Well & Core Infrastructure (before production start)
1. **Drill the well (forage)** — engage a qualified drilling company; obtain ABHOER authorization first. Target yield: ≥ 8 m³/h. If yield < 8 m³/h, plan a second well or upgrade ONEE to co-primary.
2. **Conduct pump test (essai de pompage)** — minimum 72 hours; determines pump sizing and sustainable yield
3. **Confirm ONEE connection at DN100** — contact ONEE Direction Régionale Marrakech-Safi for the upgraded DN100 connection
4. **Build raw water storage (2 × 125 m³)** — critical path item for both lines
5. **Verify fire water tank (35 m³)** — confirm with Soufiane Incendie that the existing design covers the combined plant
6. **Install well pump station** — submersible pump rated for 8–12 m³/h, VFD, wellhead, electrical panel
7. **Procure boiler feedwater system** — 10 m³ SS tank, 2 × 3 t/h alternating softeners, 5 m³ buffer, feed pumps — coordinate with boiler supplier

### Phase 2 — Wet Line Water Infrastructure
8. **Build retort cooling water system** — 25 m³ tank + cooling tower + chemical dosing; coordinate with wet line equipment supplier for retort cooling specifications
9. **Build process water tank (30 m³)** — sized for combined dry+wet line demand
10. **Install wastewater pre-treatment** — oil/grease separator + DAF unit for wet line effluent (HACCP and environmental compliance)
11. **Commission water treatment chain** — sand filter + carbon filter sized for combined demand (DN100)

### Phase 3 — Optimization
12. **Install flash steam recovery vessel** — saves 9.4 m³/day peak (both lines) = ~2,820 m³/year
13. **Install water meters on each circuit** — well, ONEE, boiler × 2, preconditioner, wet line process, retort cooling, CIP (both lines), sanitary
14. **Well water quality monitoring** — online TDS/conductivity monitor; baseline quality profile
15. **Retort cooling water optimization** — monitor cooling tower performance; optimize cycles of concentration to minimize blowdown
16. **Rainwater harvesting** — 5,180 m² roof × 300 mm avg rainfall = ~1,554 m³/year for landscape and floor washing

### Phase 4 — Future Expansion
17. **Second well (forage de secours)** — if primary well yield is marginal (< 8 m³/h) or if further expansion is planned
18. **Water recycling** — CIP rinse water reuse (saves ~30% of CIP water); retort cooling water cascading to floor washing
19. **Condensate polishing** — if wet line condensate quality degrades, add polishing step before returning to feedwater tank

---

## 10. References

- FAMSUN 5T/H Pet Food Line — Equipment water specifications and Performance Guarantee Annex
- Soufiane Incendie / INGenios — Schema Synoptique Surpresseur (PCI Plan)
- BCAT — NSI ERT PET FACTORY MAROC, Dossier N° CAS-0003311-AK/23
- FAMSUN Chiller Solution V08 — Note de synthèse (6 May 2026)
- PetFactory Morocco — Condensate Return Rate Calculation
- Norme Marocaine NM 03.7.001 — Installations de production et distribution d'eau
- Décret n°2-14-499 — Règlement général de construction, sécurité incendie
- Loi 36-15 sur l'eau — Code de l'eau marocain (groundwater extraction authorization)
- ABHOER — Agence du Bassin Hydraulique de l'Oum Er-Rbia (well permit authority)
- ONEE — Conditions techniques de raccordement
