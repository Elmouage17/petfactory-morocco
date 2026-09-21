# Analyse d'Implantation — Chaudière, Réservoirs d'Eau et Citerne GPL
## Equipment Location Analysis — Boiler, Water Tanks & Propane Tank
**Project:** PetFactory Morocco — Sidi Bouathmane, Benguerir  
**Date:** 2026-09-21  
**Prepared by:** Claude AI / Sam Aribi  
**Reference drawings:**  
- Appendix E: General Layout (FAMSUN)  
- Plan PCI Usine PET FACTORY — RDC (INGenios)  
- Plan PCI Usine PET FACTORY — 1er Étage (INGenios)  
- Plan PCI — Schéma Synoptique Surpresseur (INGenios)  
- FAMSUN 0.00m Floor Plan (detailed equipment layout)

---

## 1. Site Overview

### Building Footprint & Orientation

```
                    NORTH
         B33 ─────────────────── B32
          │       10m setback      │
          │  ┌───────────────────┐ │
          │  │  Magasin    Salle │ │  Office
  B44     │  │  Produit    d'Em- │ │  By Buyer
  (W)     │  │  Fini       ball. │ │  (separate)
          │  │  (845 m²)         │ │
          │  ├──────┬──────┬─────┤ │
          │  │Unité │Chauf-│     │ │
          │  │Sec   │ferie │Unité│ │
          │  │Croq. │Maint.│Humi-│ │
          │  │(10m) │TGBT  │de   │ │
          │  │      │Huile │2000 │ │
          │  ├──────┴──────┤ m²  │ │
          │  │  Magasin     │     │ │
          │  │  Réception   │     │ │
          │  │  (1233 m²)   │     │ │
          │  └──────────────┴─────┘ │
          │    ┌──────┐ ┌──┐  ┌───┐│
          │    │Equip.│ │Si│  │Trk││
          │    │      │ │lo│  │Scl││
         B40 ──┴──────┴─┴──┴──┴───┘B39
                    SOUTH
           (── 10m setback ──)
```

**Key dimensions:**
- Building: ~43m × ~65m (estimated from FAMSUN grid + room dimensions)
- Lot: significantly larger, with 10m+ setbacks on all sides
- Building corners: B33 (NW), B32 (NE), B39 (SE), B40 (SW)
- Total building area: ~5,180 m²

### Available Open Space

| Zone | Location | Approx. Area | Current Use |
|---|---|---|---|
| **South yard** | Between building & south property line | ~600–800 m² | 200T silo, truck scale, equipment |
| **West strip** | Between building & west property line (B33–B40) | ~400–500 m² | Setback / access road |
| **East strip** | Between building & east property line (B32–B39) | ~300–400 m² | Partially used by Office building |
| **North strip** | Between building & north property line | ~300–400 m² | Setback |
| **SW corner** | South of Magasin Réception, west of silo | ~300–400 m² | Open |
| **SE corner** | South of Unité Humide, east of silo | ~200–300 m² | Truck scale, parking |

---

## 2. Boiler Room (Chaufferie) — CONFIRMED Location

### Current designation on RDC plan

The Chaufferie is **already designated** on the INGenios RDC plan, located:
- Between **Unité Sec Croquette** (west) and **Unité Humide** (east)
- Adjacent to **Maintenance** workshop and **TGBT** (main electrical panel)
- Adjacent to **Local Stockage d'Huile** (oil storage)
- Roughly at the **center of the building**, on the west side of the Unité Humide zone

The 1er Étage plan confirms **"Vide Sur Chaudière"** — the boiler room is **double-height** (ground to roof, ~8m clear), which is essential for:
- Boiler flue/stack routing through the roof
- Overhead crane or monorail for boiler maintenance
- Adequate ventilation volume for 2 × 4 t/h gas-fired boilers

### Assessment: EXCELLENT location

| Criterion | Assessment | Rating |
|---|---|---|
| **Proximity to Unité Sec (dry line)** | Direct adjacency — dryer, preconditioner, fat tanks all within 15–25m | Excellent |
| **Proximity to Unité Humide (wet line)** | Direct adjacency — retorts, cooking kettles within 20–35m | Excellent |
| **Steam pipe runs** | Central position minimizes total pipe length for both lines | Excellent |
| **Ventilation** | Double-height space, roof access for flue and fresh air | Good |
| **Maintenance access** | Adjacent to Maintenance workshop | Excellent |
| **Electrical supply** | Adjacent to TGBT (main distribution panel) | Excellent |
| **Fuel supply routing** | Propane gas line from external tank can enter through west wall | Good |
| **Condensate return** | Central position collects from both lines efficiently | Good |
| **Noise/vibration** | Interior room but away from offices (offices are north/east) | Acceptable |

### Recommendation for Boiler Room

**Keep the designated Chaufferie location. It is optimal.**

**Size the room for 2 × 4 t/h boilers:**
- Minimum floor area: ~80–100 m² (2 boilers + feedwater tank + softener + pumps + control panel)
- Clear height: 8m (as designed)
- Provide: forced ventilation louvers (east and west walls), gas detection system, emergency exit on two sides
- Boiler feedwater tank (10 m³) and softened water buffer tank (5 m³): install **inside or immediately adjacent** to the Chaufferie
- Condensate receiver tank (1–2 m³): inside the Chaufferie near the boiler feed pumps
- Water treatment (softener, RO if needed): can be in an adjacent room or covered area on the building's west exterior wall

---

## 3. Water Tanks — Recommended Locations

### 3.1 Tank Inventory (from Water System Analysis Rev 2)

| Tank | Volume | Priority | Placement Constraint |
|---|---|---|---|
| Raw water storage | 250 m³ | Critical | Near well + ONEE connection, ground level |
| Fire reserve (bâche incendie) | 35 m³ | Safety-critical | Near fire pump room, already positioned |
| Process water | 30 m³ | Important | Near both production lines |
| Retort cooling | 25 m³ | Important | Near wet line + cooling tower |
| Boiler feedwater | 10 m³ | Essential | Inside/adjacent to Chaufferie |
| Softened buffer | 5 m³ | Essential | Near treatment plant and Chaufferie |

### 3.2 Recommended Location: SOUTH-WEST YARD

**Primary water tank farm: SW corner of the site, south of Magasin Réception**

```
        ┌──────────────────────────────────────┐
        │  Magasin         │                   │
        │  Réception       │  Unité Humide     │
        │  (1233 m²)       │                   │
        └──────┬───────────┴────────┬──────────┘
               │                    │
    ┌──────────┼────────────────────┼──────────────────┐
    │          │                    │                   │
    │  ┌───────▼─────────┐  ┌──────▼──────┐            │
    │  │  RAW WATER TANK │  │  PROCESS    │            │
    │  │  250 m³         │  │  WATER 30m³ │  200T      │
    │  │  (Ø~8m × 5m H) │  │  (Ø3.5m)   │  Silo      │
    │  │  or rectangular │  ├─────────────┤            │
    │  │  10×5×5m        │  │  Retort     │            │
    │  └────────┬────────┘  │  Cooling    │   Truck    │
    │           │           │  25 m³      │   Scale    │
    │  ┌────────▼────────┐  └─────────────┘            │
    │  │ TREATMENT PLANT │       ▲                     │
    │  │ Softener, RO    │       │ short pipe to       │
    │  │ Dosing, Filters │       │ wet line retorts    │
    │  └─────────────────┘                             │
    │  ◄─── ONEE DN100 connection from street          │
    │  ◄─── Well head (drill here or nearby)           │
    │                                                  │
    └──────── Property line (south/west) ──────────────┘
```

### Rationale

| Factor | Why SW Yard |
|---|---|
| **Space availability** | Largest continuous open area (~400 m²+), flat ground |
| **ONEE connection** | Street/utility access typically from south or west side; DN100 main enters here |
| **Well location** | Drill the private well in this zone — accessible for drilling rig, away from building foundations |
| **Gravity / pumping** | Ground-level tanks with pumps to elevated building (+0.00m) — short runs |
| **Proximity to wet line** | Retort cooling tank and process water tank are close to the south wall of Unité Humide |
| **Proximity to boiler** | Treated water pipes run ~30–40m from treatment plant through building to Chaufferie |
| **Tanker access** | Water delivery tankers can access from the same south road as other trucks |
| **Expansion** | Space to add tanks if production grows |
| **No conflict with production** | Outside the building, no interference with internal operations |

### 3.3 Fire Water Reserve — KEEP EXISTING LOCATION

The RDC plan already shows:
- **Bâche à eau incendie 36 m³** with **Local Technique 3×4×4 m** (fire pump room)
- Located near the **south-west corner of the building** (near Magasin Réception / B40 area)
- Connected to the fire booster pump system (surpresseur) serving RIA and PI networks

**Recommendation:** Keep this location. It is correctly positioned near the building perimeter for fire truck access and close to the proposed water tank farm for fill supply. The fire reserve must remain a **dedicated, separate tank** — never combined with process water.

### 3.4 Retort Cooling Tower

The retort cooling system requires a **cooling tower** to reject heat from the recirculating loop (25 m³ tank → retorts → cooling tower → tank).

**Recommended location:** On the **roof of Unité Humide** or on a **steel platform** immediately outside the east or south wall of Unité Humide.

| Option | Pros | Cons |
|---|---|---|
| **Roof-mounted** (preferred) | Short pipe runs to retorts below, uses no ground space, natural air circulation | Structural load (~3–5 tonnes wet), maintenance access needed |
| **Ground-level, south yard** | Easy maintenance access, no structural load | Longer pipe runs, uses ground space near water tanks |

### 3.5 Boiler Feedwater Tank & Softened Buffer

These small tanks (10 m³ + 5 m³) must be **inside or immediately adjacent to the Chaufferie:**
- Boiler feed tank receives treated softened water + returned condensate
- Must be at atmospheric pressure with deaerator vent
- Feedwater pumps draw from this tank directly to boilers
- Maximum distance boiler feedwater tank → boiler: **5m** (to prevent NPSH issues)

---

## 4. Propane Tank (Citerne GPL) — Recommended Location

### 4.1 Configuration (from Propane Tank Options Analysis)

**Recommended Option G:** 2 × 30,000 L above-ground tanks = 60,000 L gross (15.2 days autonomy)

### 4.2 Safety Distances (Moroccan Norms — NM 03.4.072)

| Requirement | Distance |
|---|---|
| Tank to building | **7.5 m minimum** |
| Tank to property line | **15 m minimum** |
| Between tanks | **3 m minimum** |
| Tank to flame source / electrical installation | **15 m minimum** |
| Tank to boiler flue | **15 m minimum** |
| Fenced perimeter required | Yes, with locked gate |
| Retention basin | Required (110% of largest tank volume) |

### 4.3 Footprint Required

| Element | Dimensions |
|---|---|
| Each 30,000 L tank | ~2.4m Ø × 7.5m L (horizontal cylindrical) |
| 2 tanks + 3m gap | ~8m × 8m concrete pad |
| Retention basin | ~10m × 10m × 0.5m deep |
| Safety zone (7.5m all sides) | ~25m × 25m = **~625 m² total exclusion zone** |
| Fenced area | ~15m × 15m |
| Vaporizer + regulator station | ~4m × 3m, adjacent to tanks |

### 4.4 Recommended Location: SOUTH-EAST YARD

**Place the propane tank farm in the SE corner of the lot, south of the 200T silo / east of the truck scale area.**

```
                                    Building south wall
                                          │
    ────────────────┬─────────────────────┤
                    │                     │
       200T Silo    │    7.5m min         │
                    │    ◄────►           │
    ────────────────┤         ┌───────────┴──────────┐
                    │         │  PROPANE TANK FARM    │
       Truck        │         │                      │
       Scale        │         │  ┌───────┐  ┌──────┐ │
                    │         │  │30,000L│  │30,00L│ │
       Tanker ──────┼────►    │  │ Tank 1│3m│Tank 2│ │
       Access Road  │         │  └───────┘  └──────┘ │
                    │         │                      │
                    │         │  Vaporizer + Regs    │
                    │         │  Retention Basin     │
                    │         │  ───Fenced Area───   │
                    │         └──────────────────────┘
                    │              15m min
    ────────────────┴─────────────────────────────────
                    Property line (south / SE)
```

### Rationale

| Factor | Why SE Yard |
|---|---|
| **Safety distance from buildings** | 7.5m+ clearance from south wall of building — open yard provides this naturally |
| **Safety distance from property line** | SE corner of the lot appears to have 15m+ from the property boundary based on the General Layout |
| **Separation from water tanks** | Propane SE, water tanks SW — **opposite sides of the south yard** — eliminates cross-contamination risk and simplifies emergency zoning |
| **Tanker access** | The truck scale and delivery road are already in the SE area — propane tankers use the same access |
| **Gas pipe routing** | ~40–50m underground gas line from vaporizer to Chaufferie, entering through the building's south or east wall |
| **Distance from offices** | Offices are on the NE side (Office By Buyer) — propane is on the SE, maximum separation |
| **Distance from silo** | The 200T grain silo is nearby but propane above-ground tanks + fencing + retention basin provide adequate protection. Maintain 15m from silo if it generates dust (ATEX classification) |
| **No conflict with fire system** | Fire pump room and bâche incendie are on the SW side — propane is SE, separate emergency zones |
| **Wind direction** | Benguerir prevailing winds are NE to SW (Atlantic influence). Propane in SE means any leak disperses away from the building, toward open ground |
| **Expansion** | Space to add a 3rd tank pad later without reconfiguring |

### 4.5 Alternative Location: WEST YARD (Backup Option)

If the SE yard has insufficient clearance from the property line:

| Criterion | West Yard Option |
|---|---|
| Location | West side of building, between B33–B40 line and west property boundary |
| Advantage | Long straight run for tanker access, away from all other utilities |
| Disadvantage | May conflict with the 10m setback, farther from truck access road |
| Gas pipe run | ~50–60m to Chaufferie through west wall |

**This is a backup only.** The SE yard is preferred.

---

## 5. Integrated Site Layout — Summary

```
                         NORTH
              ┌─── Property Line ────────────────────┐
              │                                      │
              │  B33 ──────────────────────── B32     │
              │   │  ┌──────────────────────┐  │     │ Office
              │   │  │Mag.Produit │Emballage│  │     │ By Buyer
              │   │  │Fini (845m²)│         │  │     │
              │   │  ├─────┬──────┼─────────┤  │     │
              │   │  │Unité│CHAUF-│  Unité  │  │     │
              │   │  │Sec  │FERIE │  Humide │  │     │
     WEST     │   │  │Croq.│+Maint│  (2000  │  │     │    EAST
              │   │  │     │+Feed │   m²)   │  │     │
              │   │  │     │water │         │  │     │
              │   │  ├─────┴──────┤         │  │     │
              │   │  │Mag.Récep.  │         │  │     │
              │   │  │(1233 m²)   │         │  │     │
              │   │  └────────────┴─────────┘  │     │
              │   │                             │     │
              │  ┌┴───────────┐    ┌────────────┴──┐  │
              │  │ WATER TANK │    │  PROPANE TANK │  │
              │  │ FARM (SW)  │    │  FARM (SE)    │  │
              │  │            │    │               │  │
              │  │• Raw 250m³ │    │• 2×30,000L AG │  │
              │  │• Process   │    │• Vaporizer    │  │
              │  │  30m³      │    │• Retention    │  │
              │  │• Treatment │    │• Fenced       │  │
              │  │• Well head │    │               │  │
              │  │• ONEE conn.│    │  200T  Truck  │  │
              │  │            │    │  Silo  Scale  │  │
              │  └────────────┘    └───────────────┘  │
              │  B40 ──────────────────────── B39     │
              │                                      │
              └─── Property Line ────────────────────┘
                         SOUTH
                     (Tanker access road)
```

### Zoning Logic

| Zone | Contents | Why Grouped Here |
|---|---|---|
| **Center (Chaufferie)** | 2 × 4 t/h boilers, feedwater tank (10 m³), softened buffer (5 m³), condensate receiver, water treatment | Central to both production lines, minimizes steam + water piping, adjacent to TGBT |
| **SW Yard** | Raw water tank (250 m³), process water (30 m³), retort cooling (25 m³), treatment plant, well, ONEE | Groups all water infrastructure, near street for ONEE, accessible for drilling, feeds Chaufferie through short run |
| **SW Building corner** | Fire reserve (35 m³), fire pump room (already positioned) | Already designed by INGenios, near building perimeter, fed from water tank farm |
| **SE Yard** | 2 × 30,000 L propane tanks, vaporizer, gas regulator | Separated from water and fire systems, near truck access, prevailing wind carries leaks away from building |
| **Roof / East wall (Unité Humide)** | Cooling tower for retort loop | Short pipe runs to retorts, uses no ground space |

---

## 6. Pipe Routing Summary

| Service | From → To | Approx. Run | Size | Route |
|---|---|---|---|---|
| **Raw water** | Well / ONEE → Raw tank (SW) | 10–20m | DN100 | Underground, south yard |
| **Treated water** | Treatment (SW) → Chaufferie | 30–40m | DN50 | Underground through building south wall |
| **Process water** | Process tank (SW) → Production | 25–35m | DN65 | Underground through south wall, manifold inside |
| **Retort cooling** | Cooling tank (SW) → Retorts → Cooling tower | 30–40m (loop) | DN80 | Through south wall of Unité Humide |
| **Fire main** | Fire tank (SW corner) → RIA/PI network | Per INGenios design | DN80/100 | Already designed |
| **Propane gas** | Vaporizer (SE) → Chaufferie | 40–50m | DN50 gas | Underground (PE or steel), enters east/south wall |
| **Steam (dry line)** | Chaufferie → Dryer, preconditioner, fat tanks | 15–25m | DN100/60/32 | Overhead in production area (per FAMSUN) |
| **Steam (wet line)** | Chaufferie → Retorts, cooking kettles | 20–35m | DN100/80 | Overhead through wall to Unité Humide |
| **Condensate return** | All equipment → Chaufferie | Various | DN25/50 | Gravity return, overhead then down to feed tank |

---

## 7. Critical Design Notes

### 7.1 Propane-Specific

1. **ATEX zoning** around propane tanks: Zone 1 within 3m, Zone 2 within 7.5m — no electrical equipment in these zones without Ex-rated certification
2. **Gas detection** required at vaporizer station, along gas pipe route into building, and inside Chaufferie
3. **Emergency shutoff valve** on the gas line at the building entry point — operable from outside
4. **Ventilation** of gas pipe trench (if not direct-buried PE) to prevent gas accumulation
5. The **15m distance from the boiler flue** is critical — route the gas pipe to enter the Chaufferie away from the flue exit

### 7.2 Water-Specific

1. The **250 m³ raw water tank** is a major structure (~10m × 5m × 5m if rectangular, or ~8m Ø × 5m H if cylindrical). Confirm soil bearing capacity for the SW yard.
2. **Well drilling:** Engage a hydrogeological survey before drilling. The SW yard location allows drilling rig access without disrupting the building.
3. **Retention basin** around fuel oil / chemical storage near the water tanks to prevent contamination.
4. **Backflow prevention** on the ONEE connection (required by ONEE regulations).

### 7.3 Boiler-Specific

1. **Flue routing:** Stack exits through the roof above the Chaufferie. The double-height void (Vide Sur Chaudière) confirms this is planned.
2. **Combustion air:** 2 × 4 t/h boilers require ~8,000 m³/h of combustion air. Provide louvers on at least 2 walls.
3. **Blowdown tank:** Install outside the Chaufferie (south wall) with drain to industrial sewer.
4. **Chemical storage** for water treatment (salt for softener, chemicals for RO): covered area adjacent to treatment plant in SW yard.

---

## 8. Distances Verification Checklist

| Check | Required | Estimated on Plan | Status |
|---|---|---|---|
| Propane tank → building wall | ≥ 7.5 m | ~10–12 m (SE yard) | OK |
| Propane tank → property line | ≥ 15 m | ~15–20 m (to verify with surveyor) | Verify |
| Propane tank → 200T silo | ≥ 15 m (dust source) | ~15 m | Verify |
| Propane tank → fire water tank | N/A (different zone) | ~40 m (SW vs SE) | OK |
| Propane tank → boiler flue | ≥ 15 m | ~50 m | OK |
| Propane tank → offices | ≥ 15 m | ~60 m+ | OK |
| Propane tank → truck scale | Accessible | ~10 m | OK |
| Water tanks → well head | Short run | ~10–15 m | OK |
| Water tanks → Chaufferie | Reasonable | ~35 m | OK |
| Fire tank → fire pump room | Short run | ~5 m (already designed) | OK |

---

## 9. Action Items

| # | Action | Responsible | Priority |
|---|---|---|---|
| 1 | Confirm lot dimensions and exact setback distances with surveyor/cadastral plan | Owner/Architect | High |
| 2 | Verify SE yard has ≥15m from property line for propane tanks | Owner/Architect | High |
| 3 | Commission hydrogeological survey for well location in SW yard | Owner | High |
| 4 | Confirm Chaufferie dimensions can accommodate 2 × 4 t/h boilers (request FAMSUN updated layout) | FAMSUN/Owner | High |
| 5 | Request INGenios to update fire plan for propane tank ATEX zones | INGenios | Medium |
| 6 | Obtain soil bearing test for 250 m³ tank pad in SW yard | Structural eng. | Medium |
| 7 | Size the propane gas pipe (DN50 estimated) for 40–50m run from vaporizer to Chaufferie | MEP engineer | Medium |
| 8 | Confirm prevailing wind direction at Benguerir site (NE → SW assumed) | Met. data | Low |
| 9 | Design water treatment plant layout for SW yard (softener, filters, dosing, RO) | Water eng. | Medium |
| 10 | Plan tanker access road to serve both SE (propane) and SW (water delivery) areas | Civil eng. | Medium |

---

## 10. References

- Plan PCI Usine PET FACTORY — RDC, INGenios (Indice A)
- Plan PCI Usine PET FACTORY — 1er Étage, INGenios (Indice A)
- Plan PCI — Schéma Synoptique Surpresseur, INGenios
- Appendix E: General Layout, FAMSUN (GY-01)
- FAMSUN 0.00m Floor Plan (detailed equipment layout, grid A–D × 3–16)
- Propane Tank Options Analysis (PetFactory Morocco, 2026-09-20)
- Water Tank Sizing Analysis Rev 2 (PetFactory Morocco, 2026-09-21)
- Norme Marocaine NM 03.4.072 — LPG storage installations
- Règle APSAD R5 — Fire protection (RIA sizing)
