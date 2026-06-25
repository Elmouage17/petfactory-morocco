"""
Stage 5 — Counterflow Cooler (C0122 · 6–7 t/h · 22 kW fan)
Cooling curve, dew-point exposure check, moisture rebound risk.
"""
from .core import ProcessState, PlantContext, WeatherState

H_TRANSFER   = 45.0    # W/(m²·°C) — typical forced-air counterflow cooler
COOLER_AREA  = 12.0    # m² effective heat transfer area
CP_PRODUCT   = 1.8     # kJ/(kg·°C)


class Cooler:
    """
    Counterflow cooler · Fan 22 kW · Air 11 580 m³/h
    Residence: 10–15 min · Discharge: T_ambient + 3–5 °C
    """
    def __init__(
        self,
        residence_min:  float = 12.0,
        airflow_m3ph:   float = 11_580.0,
        target_delta_c: float = 4.0,     # desired (T_out - T_ambient)
    ):
        self.residence_min  = residence_min
        self.airflow_m3ph   = airflow_m3ph
        self.target_delta_c = target_delta_c

    def run(self, state: ProcessState,
            _context: PlantContext, weather: WeatherState) -> ProcessState:
        T_amb  = weather.dry_bulb_c
        T_in   = state.temperature_c
        T_tgt  = T_amb + self.target_delta_c

        # Newton's law of cooling over residence time
        t_sec  = self.residence_min * 60
        m_kgs  = state.mass_flow_kgph / 3600
        UA     = H_TRANSFER * COOLER_AREA / 1000   # kW/°C
        T_out  = T_tgt + (T_in - T_tgt) * \
                 __import__("math").exp(-UA * t_sec / (m_kgs * CP_PRODUCT))

        state.temperature_c = max(T_out, T_tgt)

        # Moisture rebound risk (product surface hits dew point)
        dew_pt           = weather.dew_point_c
        surface_temp     = state.temperature_c
        exposure_factor  = min(1.0, self.residence_min / 15.0)
        rebound_risk     = max(0.0, (dew_pt - surface_temp) * exposure_factor * 0.01)
        state.moisture_pct += rebound_risk * 0.5   # small rebound addition

        state.quality_risk = max(state.quality_risk, rebound_risk)
        state.log("5_cooler")
        return state
