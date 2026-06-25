"""
Stage 4 — Circulating Belt Dryer (E0124 · GZDH2200×2-8 · 62.26 kW)
Energy balance, evaporation kinetics, multi-zone moisture convergence.
"""
import math
from .core import ProcessState, PlantContext, WeatherState

CP_AIR        = 1.006     # kJ/(kg·°C)
RHO_AIR       = 1.18      # kg/m³ at ~30 °C
LATENT_HEAT   = 2450.0    # kJ/kg water evaporated (at drying temps)
MASS_TRANSFER = 0.00018   # empirical k (kg/(m²·s·kPa)) — calibrated to 8–10 % exit
BELT_AREA_M2  = 44.0      # 2200 mm × 2-layer × 4 zones ≈ 44 m²
PRODUCT_SURFACE_FACTOR = 0.45  # product surface temp ≈ 45 % of air temp (heat-transfer limited)


def _saturation_pressure_kpa(temp_c: float) -> float:
    """Antoine equation (kPa)."""
    return 0.6105 * math.exp(17.27 * temp_c / (temp_c + 237.3))


class Dryer:
    """
    2-layer belt · 4 drying zones · Steam-heated air · VFD belt speed.
    """
    def __init__(
        self,
        inlet_air_temp_c:  float = 140.0,
        air_flow_m3ph:     float = 21_168.0,   # 5884 m³/h × 3.6 for unit consistency
        belt_speed_frac:   float = 0.5,         # 0–1 fraction of max belt speed
        steam_kgph:        float = 900.0,       # steam to heat exchanger
        thermal_eff:       float = 0.85,
    ):
        self.inlet_air_temp_c = inlet_air_temp_c
        self.air_flow_m3ph    = air_flow_m3ph
        self.belt_speed_frac  = belt_speed_frac
        self.steam_kgph       = steam_kgph
        self.thermal_eff      = thermal_eff

    def _residence_time_h(self) -> float:
        """Slower belt → longer residence → more drying."""
        max_time_h = 0.75     # ~45 min at slowest
        min_time_h = 0.20
        return max_time_h - (max_time_h - min_time_h) * self.belt_speed_frac

    def run(self, state: ProcessState,
            _context: PlantContext, weather: WeatherState) -> ProcessState:
        t_res_h = self._residence_time_h()
        t_res_s = t_res_h * 3600

        # Air-side capacity
        air_mass_kgph = self.air_flow_m3ph * RHO_AIR
        Q_air = air_mass_kgph * CP_AIR * (self.inlet_air_temp_c - state.temperature_c)  # kJ/h

        # Evaporation kinetics — driving force uses product surface temp, not air temp
        surface_temp_c = self.inlet_air_temp_c * PRODUCT_SURFACE_FACTOR
        P_sat  = _saturation_pressure_kpa(surface_temp_c)
        P_air  = _saturation_pressure_kpa(weather.dew_point_c)
        evap_rate_kgs = MASS_TRANSFER * BELT_AREA_M2 * max(0, P_sat - P_air)  # kg/s
        evap_kgh      = evap_rate_kgs * 3600 * t_res_h     # scale by residence fraction

        dry_mass  = state.mass_flow_kgph * (1 - state.moisture_pct / 100)
        water_in  = state.mass_flow_kgph * (state.moisture_pct / 100)
        water_out = max(water_in - evap_kgh, dry_mass * 0.06)  # floor at 6 % moisture

        state.mass_flow_kgph = dry_mass + water_out
        state.moisture_pct   = water_out / state.mass_flow_kgph * 100

        # Product exits dryer hot
        state.temperature_c = self.inlet_air_temp_c * 0.55    # empirical ≈ 55 % of inlet air T

        # Steam cost tracking (attach to state for optimizer)
        state.stage_log["4_dryer_steam_kgph"] = {"steam_kgph": self.steam_kgph}  # type: ignore[assignment]
        state.log("4_dryer")
        return state
