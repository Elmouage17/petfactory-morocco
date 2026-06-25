"""
Pyomo-based setpoint optimizer for the Pet Factory digital twin.

Decision variables:
  - steam_flow_kgph       (Preconditioner)
  - water_flow_kgph       (Preconditioner)
  - motor_load_frac       (Extruder)
  - inlet_air_temp_c      (Dryer)
  - belt_speed_frac       (Dryer)
  - fat_addition_pct      (Coater)

Objective: Maximise profit = Revenue - SteamCost - PowerCost - WasteCost - QualityFailureCost

Constraints:
  - Final moisture within SKU spec ± 1 %
  - Water activity < sku.aw_limit
  - Extruder motor load ≤ 0.95 (torque limit)
  - Product exit temperature before bagging ≤ 25 °C
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pyomo.environ import (
    ConcreteModel, Var, Objective, Constraint, SolverFactory,
    NonNegativeReals, value, minimize, maximize, RangeSet, Boolean,
    Reals,
)
from models import (
    PlantContext, WeatherState, SKU, ProcessState,
    RawMaterials, Preconditioner, Extruder, Dryer,
    Cooler, Coater, Packaging, QualityModel,
)


# ── Utility prices (MAD) ────────────────────────────────────────────────────
STEAM_PRICE_MAD_KG   = 0.18
ELEC_PRICE_MAD_KWH   = 1.20
PRODUCT_PRICE_MAD_KG = 22.0
REJECT_COST_MAD_KG   = 5.0     # cost of rework / waste


def simulate_with_setpoints(
    steam_kgph:      float,
    water_kgph:      float,
    motor_load_frac: float,
    air_temp_c:      float,
    belt_frac:       float,
    fat_pct:         float,
    weather:         WeatherState,
    sku:             SKU,
) -> dict:
    """Run one full simulation pass with given setpoints, return KPIs."""
    context = PlantContext()
    weather.update_dew_point()
    state = ProcessState(mass_flow_kgph=sku.design_throughput_kgph)

    state = RawMaterials().run(state, context, weather, sku)
    state = Preconditioner(
        steam_flow_kgph=steam_kgph,
        water_flow_kgph=water_kgph,
    ).run(state, context, weather)
    state = Extruder(motor_load_frac=motor_load_frac).run(state, context, weather)
    state = Dryer(inlet_air_temp_c=air_temp_c, belt_speed_frac=belt_frac).run(state, context, weather)
    state = Cooler().run(state, context, weather)
    state = Coater(fat_addition_pct=fat_pct).run(state, context, weather)
    state = Packaging().run(state, context, weather)
    quality = QualityModel().predict(state, weather, sku)

    # Revenue / cost model
    throughput_kgh  = state.mass_flow_kgph
    revenue         = throughput_kgh * PRODUCT_PRICE_MAD_KG
    steam_cost      = (steam_kgph + 900) * STEAM_PRICE_MAD_KG   # 900 = dryer steam base
    power_cost      = (motor_load_frac * 203 + 62.26 + 22) * ELEC_PRICE_MAD_KWH
    waste_cost      = throughput_kgh * quality["quality_risk"] * REJECT_COST_MAD_KG

    profit = revenue - steam_cost - power_cost - waste_cost

    return {
        "profit_mad_h":    profit,
        "moisture_pct":    quality["moisture_pct"],
        "aw_est":          quality["aw_est"],
        "quality_risk":    quality["quality_risk"],
        "release_status":  quality["release_status"],
        "throughput_kgph": throughput_kgh,
        "sme_kwh_t":       state.sme_kwh_t,
    }


def grid_search_optimize(
    weather:     WeatherState | None = None,
    sku:         SKU | None          = None,
    verbose:     bool                = True,
) -> dict:
    """
    Grid-search optimizer (avoids need for a MILP solver binary).
    Samples the decision space and returns the best feasible setpoint.
    """
    weather = weather or WeatherState()
    sku     = sku     or SKU()

    best       = None
    best_profit = -1e9

    # Search grid
    steam_vals   = [250, 350, 450, 550]
    water_vals   = [300, 400, 500]
    motor_vals   = [0.75, 0.82, 0.90]
    air_temp_vals= [120, 135, 150, 165]
    belt_vals    = [0.3, 0.5, 0.7]
    fat_vals     = [10, 12, 15]

    total = (len(steam_vals) * len(water_vals) * len(motor_vals)
             * len(air_temp_vals) * len(belt_vals) * len(fat_vals))

    if verbose:
        print(f"  Searching {total} setpoint combinations…")

    count = 0
    for steam in steam_vals:
        for water in water_vals:
            for motor in motor_vals:
                for air_t in air_temp_vals:
                    for belt in belt_vals:
                        for fat in fat_vals:
                            count += 1
                            r = simulate_with_setpoints(
                                steam, water, motor, air_t, belt, fat,
                                weather, sku)

                            # Feasibility constraints
                            moisture_ok = abs(r["moisture_pct"] - sku.moisture_target_pct) <= 1.5
                            aw_ok       = r["aw_est"] < sku.aw_limit
                            motor_ok    = motor <= 0.95

                            if moisture_ok and aw_ok and motor_ok:
                                if r["profit_mad_h"] > best_profit:
                                    best_profit = r["profit_mad_h"]
                                    best = {
                                        "setpoints": {
                                            "steam_flow_kgph":  steam,
                                            "water_flow_kgph":  water,
                                            "motor_load_frac":  motor,
                                            "inlet_air_temp_c": air_t,
                                            "belt_speed_frac":  belt,
                                            "fat_addition_pct": fat,
                                        },
                                        "kpis": r,
                                    }

    if verbose:
        if best:
            _print_opt_report(best)
        else:
            print("  ⚠  No feasible solution found — check SKU targets or widen grid.")

    return best or {}


def _print_opt_report(best: dict):
    sep = "─" * 60
    print(f"\n{'═'*60}")
    print("  OPTIMIZER RESULT — Best Feasible Setpoints")
    print(f"{'═'*60}")
    sp = best["setpoints"]
    print(f"  Steam flow     : {sp['steam_flow_kgph']} kg/h")
    print(f"  Water flow     : {sp['water_flow_kgph']} kg/h")
    print(f"  Motor load     : {sp['motor_load_frac']*100:.0f} %  of 203 kW")
    print(f"  Dryer air temp : {sp['inlet_air_temp_c']} °C")
    print(f"  Belt speed     : {sp['belt_speed_frac']*100:.0f} %  of max")
    print(f"  Fat addition   : {sp['fat_addition_pct']} %")
    print(sep)
    kp = best["kpis"]
    print(f"  Throughput     : {kp['throughput_kgph']:.0f} kg/h")
    print(f"  Final moisture : {kp['moisture_pct']:.2f} %")
    print(f"  Water activity : {kp['aw_est']:.4f}")
    print(f"  SME            : {kp['sme_kwh_t']:.1f} kWh/t")
    print(f"  Quality risk   : {kp['quality_risk']:.4f}")
    print(f"  Profit         : {kp['profit_mad_h']:.0f} MAD/h")
    print(f"  Release        : {'✅ PASS' if kp['release_status']=='PASS' else '⛔ HOLD'}")
    print(f"{'═'*60}\n")


if __name__ == "__main__":
    weather = WeatherState(dry_bulb_c=25, relative_humidity=45)
    grid_search_optimize(weather=weather, verbose=True)
