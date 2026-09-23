# Analyse des Options de Citerne GPL — PetFactory Maroc
## Propane (LPG) Tank Options Analysis

**Project:** PetFactory Morocco — Sidi Bouathmane, Benguerir  
**Date:** 2026-09-20 (Rev. 2: 2026-09-23 — Corrected per Règlement Général GPL Art. 97)  
**Context:** A provider proposed 6 small underground tanks. This document evaluates all configurations to identify the optimal solution.  
**Rev. 2 Note:** Safety distances are capacity-tiered per Article 97 of the Règlement Général sur les GPL (source: AFRIQUIAGAZ Réf. 02). The Rev. 1 recommendation (Option G: 2 × 30,000 L) is invalidated — only installations ≤24,000 L (≤10 tonnes) fit the 7.5 m distances compatible with this lot.

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

**Verdict (Rev. 1): STRONG OPTION** — Best value for money, easy to maintain and expand.

> **Rev. 2 UPDATE: NON CONFORME on this lot.** Total capacity 50,000 L = ~21.7 tonnes → exceeds the 10-tonne threshold → requires 10 m+ distances (Art. 97) → property lines B39-B40 too close. Same issue as Option G and the Vetogas 50 m³ proposal.

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

**Verdict (Rev. 1): POSSIBLE but adds unnecessary complexity over Option E.**

> **Rev. 2 UPDATE: NON CONFORME on this lot.** The above-ground 30,000 L component alone exceeds 24,000 L → 10 m+ distances required → incompatible with lot dimensions.

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

**Verdict (Rev. 1): BEST OPTION — meets all requirements with room to grow.**

> **Rev. 2 UPDATE: NON CONFORME on this lot.** Total capacity 60,000 L = ~26 tonnes → exceeds the 10-tonne threshold → requires 10 m+ distances (Art. 97) → 10 m circles encroach on property boundaries B39-B40 (confirmed by PNV overlay). The Vetogas 50 m³ single-tank proposal has the same problem.

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
| **Rev. 2 Compliance** | UG rules | UG rules | UG rules | UG rules | **NON CONFORME** | **NON CONFORME** | **NON CONFORME** |

> **Rev. 2 Note:** Options E, F, G are all NON CONFORME on this lot because their above-ground capacity exceeds 24,000 L, triggering 10 m+ distances (Art. 97) that encroach on property boundaries. The revised recommendation is AFRIQUIAGAZ 22 m³ (22,000 L) — the only above-ground option in the 12,000–24,000 L tier (7.5 m distances). See Section 6.

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

### 4.2 Key Regulatory Requirements (Rev. 2 — Capacity-Tiered per Article 97)

**Safety distances are classified by total storage capacity (Article 97, Règlement Général GPL):**

| Distance requirement | ≤3,200 L (<1.4 t) | 3,200–12,000 L (1.4–5.2 t) | 12,000–24,000 L (5.2–10.4 t) | >24,000 L (>10.4 t) |
|---|---|---|---|---|
| From buildings | 3 m | 5 m | **7.5 m** | **10 m+** |
| From property line | 3 m | 5 m | **7.5 m** | **10 m+** |
| From flammable materials | 3 m | 5 m | **7.5 m** | **10 m+** |
| From delivery truck | 3 m | 3 m | 5 m | 5 m+ |
| From public establishments | — | 15 m | 40 m | 40 m+ |

> **Rev. 2 correction:** Rev. 1 used generic distances (7.5 m from buildings, 15 m from property) for all above-ground tanks. The actual regulation classifies distances by capacity. On this lot (101 × 108 m), only the 12,000–24,000 L tier (7.5 m distances) is compatible. Installations >24,000 L require 10 m+ distances that encroach on property boundaries B39-B40.

**Additional regulatory articles (source: AFRIQUIAGAZ Réf. 02):**
- **Article 99:** Truck access must allow evacuation "sans manoeuvre et en marche avant"
- **Article 101:** Electrical equipment within 7.5 m of tank openings must be safety-rated
- **Article 102:** Tank must be in open air, accessible, not under inhabited building, not enclosed, not underground
- **Article 103:** Minimum 10 kg powder fire extinguisher + water post with hose and lance (RIA)

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

## 6. Final Recommendation (Rev. 2 — Revised)

> **Rev. 2 supersedes Rev. 1.** The original recommendation (Option G: 2 × 30,000 L) is invalidated by Article 97 of the Règlement Général GPL. See Section 4.2 for the corrected capacity-tiered distances.

### Three-Way Supplier Comparison

| | Vetogas | AFRIQUIAGAZ | Option G (Rev. 1) |
|---|---|---|---|
| **Configuration** | 1 × 50 m³ | 1 × 22 m³ | 2 × 30,000 L |
| **Total capacity** | 50,000 L | 22,000 L | 60,000 L |
| **Mass at 85% fill** | ~21.7 tonnes | ~9.5 tonnes | ~26 tonnes |
| **Regulatory tier** | >10 tonnes | **5–10 tonnes** | >10 tonnes |
| **Required distance** | 10 m | **7.5 m (Art. 97)** | 10 m+ |
| **Autonomy** | 12.7 days | 5.6 days | 15.2 days |
| **Art. 103 extincteur** | 9 kg (NON) | **10 kg (OK)** | Not specified |
| **Verdict** | **NON CONFORME** | **CONFORME** | **NON CONFORME** |

### Primary: AFRIQUIAGAZ — 1 × 22,000 L Above-Ground Tank

**Why this is the only compliant choice on this lot:**

1. **Regulatory compliance:** 22,000 L falls within the 12,000–24,000 L tier of Article 97. Required safety distance is 7.5 m. The SE corner of the lot provides >15 m in all directions — more than double the requirement. Confirmed by AFRIQUIAGAZ implantation plan Réf. 01 (dated 05-02-2026, CONFORME).

2. **Complete safety equipment:** Per Article 103 — extincteur 10 kg poudre, RIA (Robinet d'Incendie Armé), clôture grillagée Ø6mm hauteur 2 m, alimentation en eau 1"½ - 2 bars.

3. **Lowest installation cost:** Single tank, no excavation, 1 concrete pad, 1 retention basin. Estimated ~240,000 MAD total installation.

4. **Fast installation:** 2–3 weeks from order to operation.

5. **Local supplier:** AFRIQUIAGAZ (Groupe AKWA) — 139, Bd Moulay Ismail, Roches Noires, Casablanca. Largest Moroccan GPL distributor. Strong presence in Marrakech-Safi region.

### The Trade-off: Reduced Autonomy

| | AFRIQUIAGAZ 22 m³ | Old Option G |
|---|---|---|
| Autonomy | **5.6 days** | 15.2 days |
| Deliveries needed | ~5×/month | 2×/month |
| Regulatory compliance | **CONFORME** | NON CONFORME |

**Mitigation strategies:**
1. **Regular deliveries every 4 days** — AFRIQUIAGAZ based in Casablanca (~250 km from Benguerir)
2. **Automatic reorder threshold at 40%** (8,800 L usable) = 2.6 days of margin before stockout
3. **Future 2nd tank (to validate):** Consult AFRIQUIAGAZ on whether 2 × 22,000 L as separate installations each remain in the 5–10 t category, or if the 44,000 L total is classified as >10 t

### Why NOT the other proposals

**Vetogas (50 m³) — NON CONFORME for 3 reasons:**
1. ~21.7 tonnes → exceeds 10-tonne threshold → 10 m distances required
2. 10 m circles encroach on property lines B39-B40 (confirmed by PNV overlay)
3. Fire extinguisher specified at 9 kg — below the 10 kg minimum of Article 103

**Option G (2 × 30,000 L) — NON CONFORME:**
- 60,000 L total = ~26 tonnes → same >10-tonne tier as Vetogas
- Same 10 m+ distance problem on this lot
- Rev. 1 analysis used generic distances without capacity classification

**Original provider (6 × 5,000 L underground) — NOT RECOMMENDED:**
- Highest cost (1,005,000 MAD over 5 years), most complex, marginal autonomy (7.6 days)

### Site Layout Requirement (Revised)

The AFRIQUIAGAZ 22 m³ above-ground installation requires:
- Tank pad: single horizontal tank (~6.2 m × 2.2 m)
- Safety perimeter: 7.5 m from nearest building wall (Art. 97)
- Fenced enclosure with locked gate (clôture grillagée Ø6mm, H 2m)
- Located at SE corner near the chaufferie for short piping run
- Tanker access for delivery truck (Art. 99: marche avant, sans manoeuvre)
- Retention basin (bac de rétention) under tank
- RIA + extincteur 10 kg (Art. 103)

### Action Items (Revised)

1. **Confirm order with AFRIQUIAGAZ** — 1 × 22 m³ aérienne. Negotiate tank rental program (citerne gratuite vs contrat pluriannuel).
2. **Clarify 2nd tank regulation** — Ask AFRIQUIAGAZ if 2 × 22 m³ (separate installations) stay in the 5–10 t category each, or if total 44,000 L triggers >10 t classification.
3. **Establish delivery contract** — GPL vrac, frequency every 4 days, automatic reorder threshold at 40%.
4. **Update fire safety study** — Revise NSI ERT (Soufiane Incendie) to include GPL 22 m³ storage and Art. 103 equipment.
5. **Submit permit application** — dossier d'autorisation to the Prefecture de Benguerir with AFRIQUIAGAZ plan Réf. 01.

---

## 7. Cost Summary (Estimated, MAD) — Rev. 2

| Cost Element | Option A (6×5k UG) | **AFRIQUIAGAZ 22 m³ (Rev. 2)** | Savings |
|---|---|---|---|
| Tank supply | 180,000 | ~120,000 | **60,000** |
| Excavation & civil works | 200,000 | 40,000 | **160,000** |
| Cathodic protection | 90,000 | 0 | **90,000** |
| Piping & manifold | 80,000 | 25,000 | **55,000** |
| Safety equipment | 50,000 | 35,000 | **15,000** |
| Fencing & retention | 0 | 20,000 | (20,000) |
| **Total installation** | **600,000** | **240,000** | **360,000** |
| Maintenance (5 years) | 225,000 | 60,000 | **165,000** |
| Inspections (5 years) | 180,000 | 50,000 | **130,000** |
| **5-year total cost** | **1,005,000** | **350,000** | **655,000** |

> These are estimates for comparison purposes. Actual costs will depend on supplier quotes and site conditions. Tank rental programs may eliminate the tank supply cost entirely. More frequent delivery costs (~5×/month vs 2×/month) are offset by the lower installation cost.
