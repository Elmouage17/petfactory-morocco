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

## 6. References
- FAMSUN Drawing: 蒸汽图纸（摩洛哥Pet Factory）_t3.dwg (Drawing No. A3-SH-01, dated 2024-09-19)
- FAMSUN PLAN VAPEUR PDF — Floor plans ±0.00M and +8.50M
- Steam tables: saturated steam properties at 1 MPa and 0.1 MPa
