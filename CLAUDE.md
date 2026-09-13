# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PetFactory Morocco — engineering, business, and digital twin repository for a 5 TPH (tonnes per hour) pet food factory in Benguerir, Morocco, built on a Famsun production line. The repo mixes:

- **Digital twin simulator** (`petfood_simulator/`) — Python models of the 8-stage production line
- **Engineering documents** — P&IDs, boiler specs, compressor sizing, fire safety plans, water treatment (stored as PDFs, DOCX, XLSX, DWG in `Boiler/`, `Compressor/`, `Silo/`, `Water System/`, `Soufiane Incendie/`, `General/`)
- **Business documents** — buyer briefs, pitch sheets, playbooks, executive summaries (repo root, bilingual EN/FR)
- **Automation scripts** — email dispatch (`scripts/send_report_email.py`)

Currency throughout is MAD (Moroccan Dirham). Site coordinates: 32.25°N, 7.95°W, elevation 460 m.

## Running the Digital Twin

All simulator commands run from the `petfood_simulator/` directory.

```bash
cd petfood_simulator

# Single simulation (default: 25°C, 45% RH, Standard Dry Kibble)
python simulator.py

# Override weather / SKU
python simulator.py --temp 38 --rh 75 --sku "High-Protein Kibble"

# JSON output (for piping)
python simulator.py --temp 30 --rh 60 --json

# Scenario comparison (table + PNG chart)
python compare.py                          # all scenarios
python compare.py --group "Seasonal Weather"
python compare.py --group "SKU Comparison"

# Setpoint optimizer (grid search over 6 decision variables)
python optimization/optimizer.py

# Dash dashboard (interactive, port 8050)
python app/dashboard.py                    # then open http://127.0.0.1:8050

# Live 1-hour production dashboard (port 8055)
python live_dashboard.py                   # then open http://127.0.0.1:8055
```

Dependencies: `matplotlib`, `numpy`, `dash`, `plotly`, `pyomo`. No requirements.txt exists yet — install manually.

## Simulator Architecture

The simulator models 8 sequential unit operations as a pipeline. Each stage is a class in `petfood_simulator/models/` with a `.run(state, context, weather, ...)` method that mutates and returns a `ProcessState` dataclass.

**Pipeline order** (matches physical line):
1. `RawMaterials` — reception, silo storage, magnet cleaning
2. `Preconditioner` — steam + water conditioning (2–4 min residence)
3. `Extruder` — twin-screw SJPS165, 203 kW; computes SME (kWh/t)
4. `Dryer` — 4-zone belt dryer, targets 8–10% moisture
5. `Cooler` — counterflow, discharge at T_ambient + 3–5°C
6. `Coater` — vacuum coating with fats/oils and palatants
7. `Packaging` — bagging at 18–22°C, 40–50% RH
8. `QualityModel` — predicts moisture, water activity (a_w), quality risk score, release status (PASS/HOLD)

**Core dataclasses** (`models/core.py`):
- `PlantContext` — site metadata, utility prices (MAD), warehouse limits
- `WeatherState` — dry bulb, wet bulb, RH, dew point (Magnus formula)
- `SKU` — recipe dict, moisture target, a_w limit, throughput
- `ProcessState` — mutable state flowing through the pipeline (mass flow, moisture, temperature, a_w, density, quality risk, stage log)

**Key subsystems:**
- `scenarios.py` — preset weather/SKU bundles grouped as "Seasonal Weather" and "SKU Comparison"
- `optimization/optimizer.py` — grid-search over 6 setpoints (steam, water, motor load, dryer air temp, belt speed, fat%) maximizing profit while respecting moisture/a_w/torque constraints
- `live_engine.py` — minute-by-minute simulation with noise, drift, and random events for 60-minute production runs; generates alarm states
- `live_dashboard.py` — self-contained Dash app (port 8055) with embedded simulation engine for real-time operator view
- `app/dashboard.py` — main Dash dashboard (port 8050) with simulation tab + scenario comparison tab

## Integrations

- **Gmail MCP** (`.mcp.json`) — configured for sending weekly executive summary PDFs via `scripts/send_report_email.py`
- **Stop hook** (`.claude/settings.json`) — triggers on files matching `Resume_Executif`, prints a reminder about email dispatch

## Conventions

- Bilingual project: documents exist in both French and English variants
- The PFD diagram script (`digital_twin_pfd.py`) has a hardcoded macOS save path — update the output path when running elsewhere
- `compare.py` also has a hardcoded macOS fallback path for chart output; pass `--png` or modify the default
- SKU names used across the codebase: "Standard Dry Kibble", "High-Protein Kibble", "Senior Formula"
