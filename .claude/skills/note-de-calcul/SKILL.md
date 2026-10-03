---
name: note-de-calcul
description: Rédige une Note de Calcul (NDC) d'ingénierie pour le projet PetFactory Maroc — vapeur, condensats, tuyauterie, air comprimé, eau, chiller, incendie. Use when the user asks for a calculation note, sizing, "note de calcul", "NDC", pipe/tank/compressor/boiler sizing, or to check a FAMSUN or supplier figure.
---

# Note de Calcul — PetFactory Maroc

Produces a traceable, verifiable engineering calculation note in the project's house format.
Default language: **French**, with English sub-headings (the project's documents are bilingual FR/EN, sources often Chinese).

## 1. Before calculating — gather inputs

1. Find the source data in the repo first (do not invent inputs):
   - `Boiler/` — steam drawing (`蒸汽图纸…dwg` + `.png`), RFP, boiler quotes, existing NDCs
   - `Compressor/` — `NDC de réseau d'air comprimé.xlsx`, supplier offers
   - `General/` — FAMSUN contract: CPS, CCTP, Scope of Work (Appendix C), guaranteed performance annex, layout (Appendix E)
   - `Mike’s documents/` — line layouts per level (0.00 / +4.00 / +8.50 / +13.50 m), chiller solution
   - `Water System/`, `Soufiane Incendie/`, `Silo/`
   - `petfood_simulator/` — process model, can supply flows/scenarios
2. For every input, record **value, unit, source file, and page/table/label**. Translate Chinese labels and keep the original in brackets, e.g. `Sécheur (烘干机)`.
3. If an input is missing, state the assumption explicitly in an **Hypothèses** table and add it to the "À demander à FAMSUN / fournisseur" list. Never hide an assumption inside a calculation.
4. Ask the user only for inputs that cannot be found or reasonably assumed.

## 2. Pitfalls to check every time

- **Pression relative vs absolue.** Supplier figures ("0.8–1 MPa", "8 bar") are usually **gauge (barg)**. Steam tables use **absolute**. State which one, and convert (+0.101 MPa) before reading tables.
- **Units.** t/h vs kg/h vs kg/s; Nm³/min vs m³/min (FAD) for air; DN vs actual internal diameter (use schedule, e.g. DN50 Sch40 → Di = 52.5 mm).
- **Direct steam injection** (préconditionneur, extrudeuse) is consumed by the product — not returned as condensate.
- **Flash steam** is a loss of condensate *mass*; recovering it in a flash vessel yields low-pressure steam for reuse, not more returned condensate. Do not double-count.
- **Design margin.** Show the bare result first, then apply margin separately and say why (e.g. +10 % future capacity, +15 % leaks for compressed air).
- **Altitude / ambient** for compressors and chillers: site is near Benguerir/Marrakech (≈ 450 m, summer ambient up to 45 °C).

## 3. Reference data

Saturated steam (absolute pressure) — verify against a full steam table for final issue:

| P abs (MPa) | Tsat (°C) | hf (kJ/kg) | hfg (kJ/kg) | hg (kJ/kg) |
|---|---|---|---|---|
| 0.101 | 100.0 | 419.1 | 2256.4 | 2675.6 |
| 0.2 | 120.2 | 504.7 | 2201.6 | 2706.3 |
| 0.3 | 133.5 | 561.4 | 2163.5 | 2724.9 |
| 0.4 | 143.6 | 604.7 | 2133.4 | 2738.1 |
| 0.5 | 151.8 | 640.1 | 2108.0 | 2748.1 |
| 0.6 | 158.8 | 670.4 | 2085.8 | 2756.2 |
| 0.7 | 164.9 | 697.0 | 2065.8 | 2762.8 |
| 0.8 | 170.4 | 720.9 | 2047.5 | 2768.3 |
| 0.9 | 175.4 | 742.6 | 2030.5 | 2773.0 |
| 1.0 | 179.9 | 762.5 | 2014.6 | 2777.1 |
| 1.1 | 184.1 | 781.1 | 1999.6 | 2780.7 |
| 1.2 | 188.0 | 798.3 | 1985.4 | 2783.7 |

Typical design velocities for pipe sizing:

| Fluid | Velocity |
|---|---|
| Saturated steam, mains | 20–35 m/s |
| Saturated steam, branches | 15–25 m/s |
| Condensate (liquid, gravity/pumped) | 1–2 m/s |
| Condensate with flash (two-phase) | ≤ 15 m/s on flash-steam volume |
| Compressed air, main header | 6–8 m/s (Δp ≤ 0.1 bar total) |
| Cold/chilled water | 1–2.5 m/s |
| Boiler feedwater (pump suction) | 0.5–1 m/s |

Run the arithmetic in Python (not mentally) and keep the script if the note is non-trivial, so it can be re-run when FAMSUN data changes.

## 4. Document structure

```
# Note de Calcul — <Sujet>
## <English title>
**Projet :** PetFactory Maroc — 5 T/h Pet Food Line (FAMSUN)
**Lot :** <Chaudière | Air comprimé | Eau | Froid | Incendie | Process>
**Référence :** NDC-<LOT>-<NNN>  **Révision :** A  **Date :** <YYYY-MM-DD>
**Documents de référence :** <files>
**Préparé par :** Claude AI / <user>   **Vérifié par :** ______

1. Objet / Purpose — one paragraph: what is calculated and why
2. Données d'entrée / Inputs — table: paramètre | valeur | unité | source
3. Hypothèses / Assumptions — numbered, each with justification
4. Méthode / Method — formulas with symbols defined
5. Calculs / Calculations — step by step, one table per step, show substitution
6. Résultats / Results — summary table, the key number in bold
7. Comparaison — vs FAMSUN/supplier figure, contract guarantee, or benchmark; écart in %
8. Conclusions & Recommandations — numbered, actionable
9. Points à clarifier / À demander à FAMSUN — numbered list
10. Références
```

## 5. Output

- Save as Markdown in the relevant lot folder: `<Lot>/NDC_<Sujet>.md` (e.g. `Boiler/NDC_Dimensionnement_Ligne_Vapeur.md`).
- If the user wants a deliverable for FAMSUN, management or the BET, also produce a `.docx` using the **docx** skill (same structure, tables as real Word tables).
- If a Python script was used, save it next to the note as `<Lot>/ndc_<sujet>.py`.

## 6. Self-check before handing over

- [ ] Every input has a source or is listed as an assumption
- [ ] Gauge/absolute stated for every pressure
- [ ] Units consistent through every step; final result has units
- [ ] Mass balance closes (in = out + losses)
- [ ] Result compared with the FAMSUN/supplier figure and the gap explained
- [ ] Margin applied separately and justified
- [ ] "Vérifié par" left blank — a human engineer must sign it off
