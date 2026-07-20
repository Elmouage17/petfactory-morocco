# Note de Calcul — Taux de Retour des Condensats
## Condensate Return Rate Calculation
**Project:** PetFactory Morocco — Sidi Bouathmane  
**Supplier:** FAMSUN (5T/H Pet Food Line)  
**Reference drawings:** 蒸汽图纸（摩洛哥Pet Factory）_t3.dwg, PLAN VAPEUR PDF FAMSUN.pdf  
**Date:** 2026-07-20  
**Prepared by:** Claude AI / Sam Aribi  

---

## 1. Steam Distribution (from FAMSUN Steam Cylinder Drawing)

| Equipment | Pipe Size | Steam Flow | Heating Type |
|---|---|---|---|
| Dryer (烘干机) | DN100 | 1.40 t/h | Indirect (shell & tube) |
| Preconditioner (预调化机) | DN60 | 0.75 t/h | Mixed: 30% direct injection + 70% jacket |
| Liquid fat daily tanks | DN32 | 0.30 t/h | Indirect coil |
| **Total** | **DN100 main** | **2.45 t/h** | |

> Source: FAMSUN steam cylinder drawing — max steam consumption 2.45 t/h at 0.8–1 MPa

---

## 2. Condensate Generation per Equipment

| Equipment | Steam In | Recovery Rate | Basis | Condensate |
|---|---|---|---|---|
| Dryer | 1.40 t/h | 92% | All indirect heat exchange | 1.288 t/h |
| Preconditioner | 0.75 t/h | 63% | 30% direct (lost to product) + 70% jacket @ 90% | 0.473 t/h |
| Liquid fat tanks | 0.30 t/h | 85% | Closed coil, indirect | 0.255 t/h |
| **Subtotal** | **2.45 t/h** | | | **2.016 t/h** |

---

## 3. Flash Steam Losses at Steam Traps

Condensate discharged from **1 MPa → 0.1 MPa** at steam traps:

| Parameter | Value |
|---|---|
| Enthalpy of saturated liquid at 1 MPa (hf) | 762.8 kJ/kg |
| Enthalpy of saturated liquid at 0.1 MPa (hf) | 417.4 kJ/kg |
| Latent heat at 0.1 MPa (hfg) | 2,258 kJ/kg |
| **Flash fraction** | **(762.8 − 417.4) / 2,258 = 15.3%** |

**Flash steam lost = 2.016 × 0.153 = 0.308 t/h**

---

## 4. Condensate Return Rate — Results

| Scenario | Condensate Returned | Return Rate |
|---|---|---|
| Current system (no flash vessel) | 2.016 − 0.308 = **1.708 t/h** | **69.7%** |
| With flash steam recovery vessel | 1.708 + (0.308 × 0.847) = **1.969 t/h** | **80.4%** |

**Industry benchmark for pet food plants: 75–85%**

---

## 5. Analysis & Recommendations

### Current situation (~70%)
The system is slightly below industry benchmark. The primary condensate loss sources are:

1. **Direct steam injection in preconditioner** (~30% of preconditioner steam, ~0.225 t/h) — steam enters the product and cannot be recovered. This is inherent to the process.
2. **Flash steam venting at traps** (~0.308 t/h) — currently lost to atmosphere.

### Recommendation: Add Flash Steam Recovery Vessel
Installing a flash vessel on the condensate header would:
- Recover ~0.261 t/h of condensate equivalent
- Improve return rate from **70% → 80%**
- Reduce boiler makeup water by ~260 kg/h
- Reduce chemical treatment costs proportionally
- Estimated annual water saving: ~2,280 t/year

### Makeup water required
| Scenario | Makeup water needed |
|---|---|
| Current | 2.45 − 1.708 = **0.742 t/h** |
| With flash recovery | 2.45 − 1.969 = **0.481 t/h** |

---

---

## 6. P&ID Analysis — Condensate Return Lines (Extracted from DWG file via LibreDWG)

> Source: Direct text extraction from 蒸汽图纸（摩洛哥Pet Factory）_t3.dwg using LibreDWG 0.13.3

### Condensate pipe inventory — as labelled in DWG

**From Extruder body (MYGL165 machine piping — 机身管路):**

| Qty | Size | Label in DWG | Description |
|---|---|---|---|
| 3 | DN15 | 高压冷凝水 / high pressure condensed | Extrusion barrel condensate — 3 barrel sections |
| 3 | DN15 | 中压冷凝水 / medium pressure condensed | Jacket condensate — 3 sections |
| 1 | DN20 | 高压冷凝水 / high pressure condensed | HP collection pipe (collects 3×DN15 HP) |
| 1 | DN20 | 中压冷凝水 / medium pressure condensed | MP collection pipe (collects 3×DN15 MP) |
| 1 | DN25 | 中压冷凝水 / low pressure condensed | Main condensate from extruder (collects DN20 HP + DN20 MP) |

**From Dryer (烘干机) — 4 heat exchanger zones:**

| Zone | Label in DWG | Steam trap |
|---|---|---|
| 干燥一区 (Zone 1) | 冷凝水 | Float trap FT43-10 DN25 |
| 干燥二区Ⅰ (Zone 2-I) | 冷凝水 | Float trap (DN25) |
| 干燥二区Ⅱ (Zone 2-II) | 冷凝水 | Float trap (DN25) |
| 干燥三区 (Zone 3) | 冷凝水 | Float trap FT14-10 DN25 |

> Technical requirement in DWG: "每台干燥机有其独立的疏水管道" — each dryer has its own independent condensate pipe.

**From main steam distribution (分气缸 / steam header):**

| Qty | Label in DWG | Purpose |
|---|---|---|
| 2 | 疏水 Condensate | Drainage/steam trap points on the main steam supply line |

### Total condensate return pipe count

| Return stream | Size | Notes |
|---|---|---|
| Extruder DN25 main | DN25 | Collects all extruder body condensate |
| Dryer Zone 1 | DN25 (trap outlet) | Via float trap FT43-10 |
| Dryer Zone 2-I | DN25 (trap outlet) | Via float trap |
| Dryer Zone 2-II | DN25 (trap outlet) | Via float trap |
| Dryer Zone 3 | DN25 (trap outlet) | Via float trap FT14-10 |
| Steam line drain 1 | DN15 | Main supply pipe trap |
| Steam line drain 2 | DN15 | Main supply pipe trap |
| **Main return header** | **DN50** | **Single line back to boiler, with check valve (止回阀)** |

**Total confirmed condensate return connections: 7 individual pipes → 1 main DN50 return header**

### Condensate return schematic (from DWG data)

```
EXTRUDER (MYGL165):
  Barrel section 1 ──DN15 HP──┐
  Barrel section 2 ──DN15 HP──┤──► DN20 HP ──┐
  Barrel section 3 ──DN15 HP──┘              │
  Jacket section 1 ──DN15 MP──┐              ├──► DN25 main ──┐
  Jacket section 2 ──DN15 MP──┤──► DN20 MP ──┘               │
  Jacket section 3 ──DN15 MP──┘                               │
                                                               ├──► DN50 check valve ──► Boiler feedwater
DRYER:                                                         │
  Zone 1 (DN25 FT43-10) ──────────────────────────────────────┤
  Zone 2-I (DN25 trap) ───────────────────────────────────────┤
  Zone 2-II (DN25 trap) ──────────────────────────────────────┤
  Zone 3 (DN25 FT14-10) ──────────────────────────────────────┤
                                                               │
STEAM LINE DRAINS (×2, DN15) ───────────────────────────────►─┘
```

### Confirmed instrumentation (from DWG BOM — 表1)

| Item | Size | Description | Qty |
|---|---|---|---|
| Float steam trap 浮球疏水阀 FT43-10 | DN25 | Dryer condensate trap | 1 |
| Float steam trap 浮球疏水阀 FT14-10 | DN25 | Dryer condensate trap | 1 |
| Check valve 止回阀 | DN50 | Main condensate return (BOM item 8) | 1 |
| Globe valve 波纹管密封截止阀 | DN25 | Condensate isolation valves (BOM item 4) | 4 |
| Y-filter 过滤器 Y型 | DN25 | Condensate strainer | 1 |

### P&ID gaps — items missing from FAMSUN drawings

| Missing element | Risk if not added |
|---|---|
| **Condensate receiver tank** (1–2 m³) | No buffer vessel shown — risk of water hammer at boiler inlet |
| **Flow transmitter (FT)** on DN50 return | Cannot measure actual return rate in operation |
| **Temperature transmitter (TT)** on condensate header | Cannot verify sub-cooling at traps or detect trap failure |
| **Level control** on boiler feedwater tank | Not shown in these drawings |
| **Flash steam recovery vessel** | 0.308 t/h of flash steam currently vented to atmosphere |
| **Steam traps for Zone 2-I and 2-II** | Only FT43-10 and FT14-10 labelled — 2 intermediate dryer traps unnamed |

### Action required — Items to request from FAMSUN

1. Confirm steam trap model/rating for dryer zones 2-I and 2-II (not labelled in DWG)
2. Condensate receiver tank with level gauge, overflow, and condensate pump
3. Flow transmitter (FT) on DN50 main condensate return header
4. Temperature transmitter (TT) on condensate header upstream of check valve
5. Revised P&ID showing complete condensate loop with all 7 return branches and instrumentation

---

## 7. References
- FAMSUN Drawing: 蒸汽图纸（摩洛哥Pet Factory）_t3.dwg (Drawing No. A3-SH-01, dated 2024-09-19)
- FAMSUN PLAN VAPEUR PDF — Steam cylinder diagram, MYGL165 piping system, Floor plans ±0.00M and +8.50M
- Steam tables: saturated steam properties at 1 MPa and 0.1 MPa
