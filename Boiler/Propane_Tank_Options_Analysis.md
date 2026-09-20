# Analyse des Options de Citerne GPL — PetFactory Maroc
## Propane (LPG) Tank Options Analysis

**Project:** PetFactory Morocco — Sidi Bouathmane, Benguerir  
**Date:** 2026-09-20  
**Context:** A provider proposed 6 small underground tanks. This document evaluates all configurations to identify the optimal solution.

---

## 1. Factory Propane Demand Calculation

### 1.1 Steam System Requirements (from FAMSUN specs)

| Parameter | Value |
|---|---|
| Total steam consumption | 2.45 t/h at 0.8–1 MPa |
| Dryer | 1.40 t/h (indirect shell & tube) |
| Preconditioner | 0.75 t/h (30% direct + 70% jacket) |
| Liquid fat daily tanks | 0.30 t/h (indirect coil) |
| Condensate return rate | 70% (current) / 80% (with flash recovery) |

### 1.2 Propane Consumption Calculation

| Parameter | Value | Source |
|---|---|---|
| Steam enthalpy at 1 MPa (saturated) | 2,778 kJ/kg | Steam tables |
| Feed water enthalpy (70% condensate at 85°C + 30% makeup at 20°C → blended ~65°C) | 274 kJ/kg | Calculated |
| Energy per kg steam | 2,504 kJ/kg | 2,778 − 274 |
| Total thermal energy required | 6,135 MJ/h | 2,450 kg/h × 2,504 kJ/kg |
| Propane LHV | 46.35 MJ/kg | — |
| Boiler efficiency (condensing gas boiler) | 93% | Fang Kuai spec |
| **Peak propane consumption** | **142 kg/h** | 6,135 ÷ (46.35 × 0.93) |

### 1.3 Operating Profile & Storage Requirements

| Parameter | Value |
|---|---|
| Operating hours | 16 h/day (2 shifts) |
| Operating days | 25 days/month, 300 days/year |
| Average load factor | 75% of peak |
| **Average propane rate** | **107 kg/h** |
| **Daily consumption** | **1,710 kg/day (3,353 L/day)** |
| **Monthly consumption** | **42,750 kg/month (83,824 L/month)** |
| **Annual consumption** | **513,000 kg/year (~513 tonnes/year)** |
| Annual propane cost (est. 7.5 MAD/kg bulk) | **~3,850,000 MAD/year** |

> Note: Propane liquid density at 15°C = 0.51 kg/L. Tanks are filled to max 85% capacity (Moroccan & international safety norm).

### 1.4 Minimum Storage Recommendation

| Supply Security | Days of Stock | Usable Volume Needed | Gross Tank Volume (at 85% fill) |
|---|---|---|---|
| Emergency minimum | 3 days | 10,060 L | **11,835 L** |
| Minimum recommended | 7 days | 23,470 L | **27,612 L** |
| Comfortable (2 weeks) | 14 days | 46,940 L | **55,224 L** |
| Optimal (3 weeks) | 21 days | 70,410 L | **82,835 L** |

**Recommendation: 14–21 days of autonomy** for an industrial site in Morocco, considering:
- Delivery lead times (48–72h typical, longer during Ramadan/holidays)
- Supplier truck availability and routing to Benguerir
- Price negotiation leverage (larger orders = better pricing)
- Production continuity guarantee

---

## 2. Tank Options Comparison

### Common GPL Tank Sizes Available in Morocco

| Size (L) | Usable at 85% (L) | Usable (kg) | Days of supply | Type |
|---|---|---|---|---|
| 1,000 | 850 | 434 | 0.25 | Residential |
| 1,750 | 1,488 | 759 | 0.4 | Residential/Small commercial |
| 3,200 | 2,720 | 1,387 | 0.8 | Commercial |
| 5,000 | 4,250 | 2,168 | 1.3 | Commercial/Industrial |
| 10,000 | 8,500 | 4,335 | 2.5 | Industrial |
| 20,000 | 17,000 | 8,670 | 5.1 | Industrial |
| 30,000 | 25,500 | 13,005 | 7.6 | Industrial |
| 50,000 | 42,500 | 21,675 | 12.7 | Industrial bulk |

---

### OPTION A: 6 Small Underground Tanks (Provider's Proposal)

**Configuration:** 6 × 5,000 L underground = 30,000 L gross

| Criterion | Assessment |
|---|---|
| **Total gross capacity** | 30,000 L |
| **Usable capacity (85%)** | 25,500 L = 13,005 kg |
| **Days of autonomy** | **7.6 days** |
| **Safety distance (underground, Moroccan norms)** | 1.5 m from buildings, 3 m between tanks |
| **Total footprint** | ~120 m² (6 tanks spaced 3 m apart + access) |
| **Installation cost (est.)** | 450,000–600,000 MAD |
| **Civil works** | 6 separate excavations, 6 concrete cradles, 6 cathodic protection systems |
| **Piping** | Complex manifold connecting 6 tanks to vaporizer |
| **Maintenance** | 6× inspection/testing schedules, 6× cathodic protection checks |
| **Refill logistics** | Tanker must fill 6 tanks sequentially (slow) |
| **Permits** | Single ICPE-type permit for total volume, but 6 inspection reports |
| **Redundancy** | Good — can isolate any tank for maintenance |

**Advantages:**
- Good redundancy — can isolate individual tanks
- Smaller individual excavations
- Standard sizes readily available from all Moroccan suppliers
- Lower individual tank cost

**Disadvantages:**
- Only 7.6 days of supply — tight for industrial operations
- Highest total installation cost (6× civil works, 6× cathodic protection)
- Most complex piping (6-branch manifold)
- Highest ongoing maintenance burden (6× periodic inspections)
- Slowest refill process
- Largest total footprint
- Most leak detection points to monitor

**Verdict: NOT RECOMMENDED** — High cost, high complexity, marginal autonomy.

---

### OPTION B: 3 Medium Underground Tanks

**Configuration:** 3 × 10,000 L underground = 30,000 L gross

| Criterion | Assessment |
|---|---|
| **Total gross capacity** | 30,000 L |
| **Usable capacity (85%)** | 25,500 L = 13,005 kg |
| **Days of autonomy** | **7.6 days** |
| **Safety distance** | 1.5 m from buildings, 3 m between tanks |
| **Total footprint** | ~80 m² |
| **Installation cost (est.)** | 350,000–480,000 MAD |
| **Civil works** | 3 excavations, 3 concrete cradles, 3 cathodic protection systems |
| **Piping** | 3-branch manifold |
| **Maintenance** | 3× inspection schedules |
| **Refill logistics** | Tanker fills 3 tanks (moderate) |

**Advantages:**
- Good redundancy (can isolate 1 of 3)
- Lower installation and maintenance cost than Option A
- Simpler piping

**Disadvantages:**
- Same 7.6-day autonomy as Option A
- Still 3× civil works and 3× cathodic protection
- Still underground = no visual inspection possible

**Verdict: MARGINAL** — Better than A, but same inadequate autonomy.

---

### OPTION C: 2 Large Underground Tanks

**Configuration:** 2 × 20,000 L underground = 40,000 L gross

| Criterion | Assessment |
|---|---|
| **Total gross capacity** | 40,000 L |
| **Usable capacity (85%)** | 34,000 L = 17,340 kg |
| **Days of autonomy** | **10.1 days** |
| **Safety distance** | 1.5 m from buildings, 3 m between tanks |
| **Total footprint** | ~60 m² |
| **Installation cost (est.)** | 380,000–500,000 MAD |
| **Civil works** | 2 excavations, 2 concrete cradles, 2 cathodic protection systems |
| **Piping** | Simple dual-feed manifold |
| **Maintenance** | 2× inspection schedules |
| **Refill logistics** | Fast — 2 tanks only |

**Advantages:**
- Reasonable 10-day autonomy
- Redundancy (lead/lag operation)
- Moderate installation cost
- Simpler piping and maintenance vs. A & B
- Underground = no visual impact, no wind/sun exposure

**Disadvantages:**
- 20,000 L tanks are larger equipment to transport/crane into position
- Underground = expensive cathodic protection + leak detection
- Cannot visually inspect for corrosion
- 10 days autonomy still below the 14-day recommendation

**Verdict: ACCEPTABLE** — A reasonable middle ground, but above-ground may be better value.

---

### OPTION D: 1 Single Large Underground Tank

**Configuration:** 1 × 50,000 L underground

| Criterion | Assessment |
|---|---|
| **Total gross capacity** | 50,000 L |
| **Usable capacity (85%)** | 42,500 L = 21,675 kg |
| **Days of autonomy** | **12.7 days** |
| **Safety distance** | 1.5 m from buildings |
| **Total footprint** | ~45 m² |
| **Installation cost (est.)** | 400,000–550,000 MAD |
| **Civil works** | 1 large excavation, 1 concrete cradle, 1 cathodic protection system |
| **Piping** | Simplest — single feed line |
| **Maintenance** | 1× inspection schedule |
| **Refill logistics** | Fastest — single fill point |

**Advantages:**
- Near-adequate autonomy (12.7 days)
- Simplest piping and maintenance
- Lowest ongoing inspection cost
- Single fill point = fastest refueling
- Underground = no visual impact

**Disadvantages:**
- **Zero redundancy** — if the tank needs maintenance, the factory stops
- Large 50,000 L tank requires heavy crane and major excavation
- Cathodic protection for a single large tank is expensive
- Leak detection system more critical (all eggs in one basket)
- 12.7 days still below 14-day target

**Verdict: NOT RECOMMENDED** — No redundancy is unacceptable for production continuity.

---

### OPTION E: 2 Above-Ground Bulk Tanks (RECOMMENDED)

**Configuration:** 2 × 25,000 L above-ground = 50,000 L gross

| Criterion | Assessment |
|---|---|
| **Total gross capacity** | 50,000 L |
| **Usable capacity (85%)** | 42,500 L = 21,675 kg |
| **Days of autonomy** | **12.7 days** |
| **Safety distance (above-ground, Morocco)** | 7.5 m from buildings, 3 m between tanks, 15 m from property line |
| **Total footprint (incl. safety zone)** | ~250 m² (but only concrete pad ~30 m²) |
| **Installation cost (est.)** | 280,000–380,000 MAD |
| **Civil works** | 2 concrete pads with retention basin, fencing |
| **Piping** | Simple dual-feed manifold, accessible for maintenance |
| **Maintenance** | Visual inspection possible, no cathodic protection needed |
| **Refill logistics** | Fast — 2 fill points, easy tanker access |

**Advantages:**
- **Lowest installation cost** — no excavation, no cathodic protection
- **Easy maintenance** — visual inspection, accessible piping, easy painting
- Good redundancy (lead/lag operation)
- ~13 days autonomy
- Simple civil works (concrete pad + retention basin)
- Easy to add a 3rd tank later if consumption grows
- Faster installation timeline (2–3 weeks vs. 6–8 weeks underground)

**Disadvantages:**
- Larger safety distances required (7.5 m from buildings)
- Requires dedicated fenced area on site
- Sun/wind exposure requires sunshade or painting for thermal control
- Visible — may need architectural screening
- Higher safety distances from property line (15 m)

**Verdict: STRONG OPTION** — Best value for money, easy to maintain and expand.

---

### OPTION F: 1 Above-Ground Bulk + 1 Underground (Hybrid)

**Configuration:** 1 × 30,000 L above-ground + 1 × 20,000 L underground = 50,000 L gross

| Criterion | Assessment |
|---|---|
| **Total gross capacity** | 50,000 L |
| **Usable capacity (85%)** | 42,500 L = 21,675 kg |
| **Days of autonomy** | **12.7 days** |
| **Installation cost (est.)** | 350,000–480,000 MAD |

**Advantages:**
- Redundancy across two different failure modes
- Underground tank handles daily supply; above-ground is reserve
- Reduces above-ground footprint

**Disadvantages:**
- Two different maintenance regimes (cathodic protection + visual)
- More complex than a single-type installation
- Marginal benefit over all above-ground

**Verdict: POSSIBLE but adds unnecessary complexity over Option E.**

---

### OPTION G: 2 Above-Ground + Future Expansion (BEST OPTION)

**Configuration:** 2 × 30,000 L above-ground = 60,000 L gross, with space allocated for a 3rd tank

| Criterion | Assessment |
|---|---|
| **Total gross capacity** | 60,000 L |
| **Usable capacity (85%)** | 51,000 L = 26,010 kg |
| **Days of autonomy** | **15.2 days** |
| **Safety distance** | 7.5 m from buildings, 3 m between tanks, 15 m from property line |
| **Total footprint (incl. safety zone)** | ~300 m² |
| **Installation cost (est.)** | 320,000–420,000 MAD |
| **Civil works** | 2 concrete pads (pour 3rd pad later), retention basin, fencing |
| **Piping** | Dual-feed manifold with capped 3rd connection |

**Advantages:**
- **15+ days of autonomy** — exceeds the 14-day recommendation
- Best price negotiation position (larger deliveries)
- Redundancy (lead/lag operation)
- Pre-planned expansion path for production growth
- Low installation cost (no excavation)
- Easy maintenance (visual, accessible)
- Fast installation (3–4 weeks)

**Disadvantages:**
- Larger safety zone needed (~300 m²)
- Must be located away from buildings and property line
- Needs fencing and possibly architectural screening

**Verdict: BEST OPTION — meets all requirements with room to grow.**

---

## 3. Comparison Matrix

| Criterion | A: 6×5k UG | B: 3×10k UG | C: 2×20k UG | D: 1×50k UG | E: 2×25k AG | F: Hybrid | **G: 2×30k AG** |
|---|---|---|---|---|---|---|---|
| **Gross capacity (L)** | 30,000 | 30,000 | 40,000 | 50,000 | 50,000 | 50,000 | **60,000** |
| **Days of autonomy** | 7.6 | 7.6 | 10.1 | 12.7 | 12.7 | 12.7 | **15.2** |
| **Redundancy** | High | Good | Good | None | Good | Good | **Good** |
| **Install cost (MAD)** | 450–600k | 350–480k | 380–500k | 400–550k | 280–380k | 350–480k | **320–420k** |
| **Annual maint. cost** | High | Medium | Medium | Low | Low | Medium | **Low** |
| **Civil works complexity** | Very high | High | Medium | Medium | Low | Medium | **Low** |
| **Piping complexity** | Very high | Medium | Low | Lowest | Low | Medium | **Low** |
| **Refill speed** | Slow | Medium | Fast | Fastest | Fast | Fast | **Fast** |
| **Inspectability** | None (UG) | None (UG) | None (UG) | None (UG) | Full | Partial | **Full** |
| **Expandability** | Difficult | Possible | Difficult | None | **Easy** | Possible | **Easy** |
| **Footprint (total)** | 120 m² | 80 m² | 60 m² | 45 m² | 250 m² | 200 m² | **300 m²** |
| **Permit complexity** | High | Medium | Medium | Medium | Medium | High | **Medium** |
| **OVERALL SCORE** | 3/10 | 5/10 | 6/10 | 4/10 | 8/10 | 6/10 | **9/10** |

---

## 4. Moroccan Regulatory Framework

### 4.1 Applicable Regulations

| Regulation | Scope |
|---|---|
| **Dahir du 25 août 1914** (as amended) | Base law on classified installations (établissements classés) |
| **Décret n° 2-09-286** (2010) | Classification of dangerous installations |
| **Arrêté viziriel du 13 octobre 1933** | Storage of flammable liquids and gases |
| **Norme Marocaine NM 03.4.072** | LPG storage installations — design and safety |
| **Norme Marocaine NM 03.4.073** | LPG underground storage — specific requirements |
| **ONEE/Ministère de l'Énergie** guidelines | Energy infrastructure standards |
| **Règlement de construction parasismique (RPS 2011)** | Seismic design for tank foundations (Zone II for Benguerir) |

### 4.2 Key Regulatory Requirements

**Safety distances (above-ground tanks > 3,200 L):**
- 7.5 m minimum from any building
- 15 m from property boundary
- 3 m between tanks
- 15 m from any flame source or electrical installation
- Fenced perimeter with locked gate

**Safety distances (underground tanks):**
- 1.5 m from buildings (reduced because of burial protection)
- 3 m between tanks
- 0.60 m minimum soil cover
- Cathodic protection mandatory

**Permit process for industrial GPL storage > 6,000 L total:**
1. Dossier d'autorisation submitted to Prefecture/Province
2. Environmental impact assessment (if > 50,000 L)
3. Fire safety study (étude de sécurité incendie) — already commissioned (NSI ERT document)
4. Inspection by Protection Civile
5. Operating permit (autorisation d'exploiter) from Governor

### 4.3 Required Safety Equipment (all options)

- Emergency shutoff valve (vanne d'arrêt d'urgence)
- Pressure relief valve on each tank
- Level gauge with high-level alarm
- Excess flow valve on liquid line
- Fire extinguishers (powder type, 50 kg minimum)
- Earthing/grounding system
- Lightning protection
- Leak detection system (underground) or retention basin (above-ground)
- Safety signage (ATEX zone marking)

---

## 5. GPL Suppliers in Morocco

| Supplier | Coverage | Notes |
|---|---|---|
| **Afriquia Gaz** (AKWA Group) | National | Largest Moroccan GPL distributor, strong in Marrakech-Safi region |
| **Vivo Energy Maroc** (Shell brand) | National | International standards, reliable logistics |
| **Ziz Energies** | Central/South | Good presence in Benguerir area |
| **National Gaz** | National | Competitive pricing for bulk industrial |
| **Maghreb Oxygène** | National | Also supplies industrial gases |
| **Total Energies Maroc** | National | International standards |

**Recommendation:** Request quotes from Afriquia Gaz, Vivo Energy, and National Gaz for:
- Tank supply and installation (rental vs. purchase)
- Bulk GPL delivery contract (prix vrac)
- Maintenance and inspection services

> Many Moroccan GPL suppliers offer **tank rental programs** where the tanks are free (or low rental) in exchange for a multi-year supply contract. This can eliminate the capital cost entirely.

---

## 6. Final Recommendation

### Primary: Option G — 2 × 30,000 L Above-Ground Tanks

**Why this is the best choice:**

1. **Adequate autonomy:** 15.2 days exceeds the 14-day recommendation, ensuring uninterrupted production during holidays, supply disruptions, or price negotiations.

2. **Lowest total cost of ownership:** No excavation, no cathodic protection, no underground leak detection. Simple concrete pads and retention basin. Estimated saving of 100,000–200,000 MAD vs. underground options.

3. **Easy maintenance:** Visual inspection catches corrosion, leaks, or damage immediately. Accessible piping for repairs. Simple repainting every 5–7 years.

4. **Redundancy:** Lead/lag operation means one tank can be taken offline for maintenance or inspection while the other sustains production.

5. **Expandability:** Pre-pour a 3rd concrete pad. When production grows (new line, longer shifts), adding a 3rd tank is a 2-week project, not a major construction.

6. **Fast installation:** 3–4 weeks from order to operation, vs. 6–8 weeks for underground.

7. **Better supplier terms:** Larger storage = fewer, larger deliveries = lower per-kg price. At 513 tonnes/year, even 0.25 MAD/kg savings = 128,000 MAD/year.

### Why NOT the provider's suggestion (6 small underground tanks)

The provider's proposal of 6 small underground tanks is the **worst option** evaluated:

| Issue | Impact |
|---|---|
| Only 7.6 days of supply | Production at risk during any delivery delay |
| 6× civil works (excavation + concrete cradle) | Highest installation cost |
| 6× cathodic protection systems | Highest ongoing maintenance cost |
| Complex 6-branch piping manifold | Most failure points |
| 6× periodic inspections | Most administrative burden |
| Cannot visually inspect underground tanks | Corrosion may go undetected |
| Slow refueling (6 sequential fills) | Longer tanker time on site |

**The provider may have suggested this configuration because:**
- They stock 5,000 L tanks and want to sell existing inventory
- Underground tanks have higher installation margins
- They are accustomed to smaller commercial clients, not industrial
- They did not calculate the factory's actual daily consumption

### Site Layout Requirement

The 2 × 30,000 L above-ground installation requires a dedicated zone:
- Tank pad: ~15 m × 5 m (2 tanks side by side, 3 m apart)
- Safety perimeter: 7.5 m from nearest building wall
- Fenced area: ~25 m × 12 m (~300 m²)
- Located near the boiler room for short piping run
- Tanker access road capable of 25-tonne vehicle
- Retention basin (bac de rétention) under both tanks

### Action Items

1. **Request quotes** from Afriquia Gaz, Vivo Energy, and National Gaz for 2 × 30,000 L above-ground GPL storage with supply contract
2. **Ask about tank rental programs** — supplier-owned tanks in exchange for multi-year supply agreement
3. **Confirm site layout** — identify a 300 m² zone near the boiler room that meets safety distances
4. **Commission fire safety update** — the existing NSI ERT study (Soufiane Incendie) may need revision to include GPL storage
5. **Submit permit application** — dossier d'autorisation to the Prefecture de Benguerir with GPL storage plan

---

## 7. Cost Summary (Estimated, MAD)

| Cost Element | Option A (6×5k UG) | **Option G (2×30k AG)** | Savings |
|---|---|---|---|
| Tank supply | 180,000 | 200,000 | (20,000) |
| Excavation & civil works | 200,000 | 60,000 | **140,000** |
| Cathodic protection | 90,000 | 0 | **90,000** |
| Piping & manifold | 80,000 | 35,000 | **45,000** |
| Safety equipment | 50,000 | 40,000 | **10,000** |
| Fencing & retention | 0 | 25,000 | (25,000) |
| **Total installation** | **600,000** | **360,000** | **240,000** |
| Annual maintenance | 45,000 | 15,000 | **30,000/yr** |
| Annual inspections | 36,000 | 12,000 | **24,000/yr** |
| **5-year total cost** | **1,005,000** | **495,000** | **510,000** |

> These are estimates for comparison purposes. Actual costs will depend on supplier quotes and site conditions. Tank rental programs may eliminate the tank supply cost entirely.
