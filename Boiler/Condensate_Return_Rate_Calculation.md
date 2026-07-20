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

## 6. P&ID Analysis — Condensate Return Line (from FAMSUN PLAN VAPEUR)

### Condensate return schematic (as-drawn)

```
[Dryer DN100] ── steam trap (ST-01) ──┐
[Preconditioner DN60] ── steam trap (ST-02) ──┤──► DN25 condensate header ──► Boiler feedwater
[Fat tanks DN32] ── steam trap (ST-03) ──┘
         ↑
   φ219×1800 sub-steam cylinder
   (bottom drain: DN25, position ④)
```

### Instrumentation confirmed in drawings

| Tag | Type | Location |
|---|---|---|
| ST-01 to ST-03 | Steam traps (疏水阀) | At each equipment condensate outlet |
| ④ | Drain/isolation valve | Bottom of steam distribution cylinder |
| ⑤ ⑥ ⑦ | Condensate isolation valves | Condensate header |
| DN25 | Condensate return pipe | Main header back to boiler |

### P&ID gaps — items missing from FAMSUN drawings

| Missing element | Risk if not added |
|---|---|
| **Condensate receiver tank** (1–2 m³) | No buffer vessel shown — risk of water hammer at boiler inlet |
| **Flow transmitter (FT)** on condensate return | Cannot measure actual return rate in operation |
| **Temperature sensor (TT)** on condensate header | Cannot verify sub-cooling at traps or detect trap failure |
| **Check valve** on return line before boiler | Risk of backflow contaminating condensate |
| **Level control** on boiler feedwater tank | Not shown in these drawings |
| **Flash steam recovery vessel** | 0.308 t/h of flash steam currently vented to atmosphere |

### Action required — Items to request from FAMSUN

1. Condensate receiver tank with level gauge, overflow, and condensate pump
2. Flow transmitter (FT) + temperature transmitter (TT) on condensate return header
3. Check valve (non-return valve) before boiler feedwater inlet
4. Revised P&ID showing complete condensate loop with all instrumentation

---

## 7. References
- FAMSUN Drawing: 蒸汽图纸（摩洛哥Pet Factory）_t3.dwg (Drawing No. A3-SH-01, dated 2024-09-19)
- FAMSUN PLAN VAPEUR PDF — Steam cylinder diagram, MYGL165 piping system, Floor plans ±0.00M and +8.50M
- Steam tables: saturated steam properties at 1 MPa and 0.1 MPa
