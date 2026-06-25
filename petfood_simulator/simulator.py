"""
Pet Factory Digital Twin — Main Simulation Pipeline
Benguerir, Morocco · Famsun 5 TPH line

Usage:
    python simulator.py                        # default run
    python simulator.py --moisture 8.5         # override dryer target
    python simulator.py --rh 75 --temp 38      # hot humid day scenario
"""
import argparse
import json
from models import (
    PlantContext, WeatherState, SKU, ProcessState,
    RawMaterials, Preconditioner, Extruder, Dryer,
    Cooler, Coater, Packaging, QualityModel,
)


def run_simulation(
    weather: WeatherState | None = None,
    sku:     SKU | None          = None,
    verbose: bool                = True,
) -> dict:
    context = PlantContext()
    weather = weather or WeatherState()
    sku     = sku     or SKU()
    weather.update_dew_point()

    # ── Unit operations ─────────────────────────────────────────────────────
    raw_materials  = RawMaterials()
    preconditioner = Preconditioner(steam_flow_kgph=350, water_flow_kgph=400)
    extruder       = Extruder(motor_load_frac=0.82, barrel_temp_c=145)
    dryer          = Dryer(inlet_air_temp_c=140, belt_speed_frac=0.5)
    cooler         = Cooler(residence_min=12)
    coater         = Coater(fat_addition_pct=12, palatant_addition_pct=2)
    packaging      = Packaging(room_temp_c=20, room_rh_pct=45)
    quality_model  = QualityModel(warehouse_temp_c=22, storage_days=30)

    # ── Pipeline execution ──────────────────────────────────────────────────
    state = ProcessState(mass_flow_kgph=sku.design_throughput_kgph)

    state = raw_materials.run(state, context, weather, sku)
    state = preconditioner.run(state, context, weather)
    state = extruder.run(state, context, weather)
    state = dryer.run(state, context, weather)
    state = cooler.run(state, context, weather)
    state = coater.run(state, context, weather)
    state = packaging.run(state, context, weather)
    quality = quality_model.predict(state, weather, sku)

    # ── KPI summary ─────────────────────────────────────────────────────────
    result = {
        "site":            context.site_name,
        "sku":             sku.name,
        "weather": {
            "dry_bulb_c":        weather.dry_bulb_c,
            "relative_humidity": weather.relative_humidity,
            "dew_point_c":       round(weather.dew_point_c, 2),
        },
        "throughput_kgph": round(state.mass_flow_kgph, 1),
        "throughput_tph":  round(state.mass_flow_kgph / 1000, 3),
        "final_moisture_pct": quality["moisture_pct"],
        "final_aw":           quality["aw_est"],
        "sme_kwh_t":          round(state.sme_kwh_t, 2),
        "quality_risk":       quality["quality_risk"],
        "release_status":     quality["release_status"],
        "moisture_ok":        quality["moisture_ok"],
        "aw_ok":              quality["aw_ok"],
        "stage_log":          state.stage_log,
    }

    if verbose:
        _print_report(result)
    return result


def _print_report(r: dict):
    sep = "─" * 60
    print(f"\n{'═'*60}")
    print(f"  PET FACTORY DIGITAL TWIN — Simulation Report")
    print(f"  {r['site']}  ·  SKU: {r['sku']}")
    print(f"{'═'*60}")
    print(f"  Weather   : {r['weather']['dry_bulb_c']} °C  |  "
          f"RH {r['weather']['relative_humidity']} %  |  "
          f"Dew pt {r['weather']['dew_point_c']} °C")
    print(sep)
    print(f"  Throughput       : {r['throughput_tph']:.3f} t/h")
    print(f"  Final Moisture   : {r['final_moisture_pct']:.2f} %")
    print(f"  Water Activity   : {r['final_aw']:.4f}  (limit 0.60)")
    print(f"  SME              : {r['sme_kwh_t']:.1f} kWh/t")
    print(f"  Quality Risk     : {r['quality_risk']:.4f}  (0=best, 1=reject)")
    print(sep)
    status_sym = "✅ PASS" if r['release_status'] == "PASS" else "⛔ HOLD"
    print(f"  Release Status   : {status_sym}")
    print(f"  Moisture OK      : {'✅' if r['moisture_ok'] else '❌'}")
    print(f"  aₓ OK            : {'✅' if r['aw_ok'] else '❌'}")
    print(f"{'═'*60}\n")
    print("  Stage-by-stage log:")
    for stage, vals in r["stage_log"].items():
        if isinstance(vals, dict) and "moisture_pct" in vals:
            print(f"    {stage:<25} moisture={vals['moisture_pct']:.2f}%  "
                  f"T={vals['temperature_c']:.1f}°C  "
                  f"flow={vals['mass_flow_kgph']:.0f} kg/h")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pet Factory Digital Twin")
    parser.add_argument("--temp", type=float, default=25.0,  help="Ambient dry-bulb °C")
    parser.add_argument("--rh",   type=float, default=45.0,  help="Ambient RH %%")
    parser.add_argument("--sku",  type=str,   default="Standard Dry Kibble")
    parser.add_argument("--json", action="store_true",        help="Output raw JSON")
    args = parser.parse_args()

    weather = WeatherState(dry_bulb_c=args.temp, relative_humidity=args.rh)
    sku     = SKU(name=args.sku)

    result = run_simulation(weather=weather, sku=sku, verbose=not args.json)
    if args.json:
        print(json.dumps(result, indent=2))
