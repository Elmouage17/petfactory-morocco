"""
Stage 3 — Twin-Screw Extruder (E0104 · SJPS165 · 203 kW)
SME calculation, barrel temperature model, density/expansion proxy.
"""
from .core import ProcessState, PlantContext, WeatherState

MOTOR_RATED_KW  = 203.0
MOTOR_IDLE_KW   = 18.0     # baseline mechanical loss at no load
SME_TARGET_LOW  = 80.0     # kWh/t minimum for standard kibble
SME_TARGET_HIGH = 120.0    # kWh/t maximum


class Extruder:
    """
    Twin-screw SJPS165 · 203 kW · Barrel 130–160 °C · 20–40 bar die pressure
    Knife cutter 300–3000 RPM determines kibble length.
    """
    def __init__(
        self,
        screw_speed_rpm:  float = 350.0,
        motor_load_frac:  float = 0.82,    # fraction of rated power
        barrel_temp_c:    float = 145.0,
        die_pressure_bar: float = 30.0,
        knife_rpm:        float = 1200.0,
    ):
        self.screw_speed_rpm  = screw_speed_rpm
        self.motor_load_frac  = motor_load_frac
        self.barrel_temp_c    = barrel_temp_c
        self.die_pressure_bar = die_pressure_bar
        self.knife_rpm        = knife_rpm

    def _sme(self, mass_flow_kgph: float) -> float:
        """Operational SME = actual motor power / throughput."""
        P_actual = MOTOR_RATED_KW * self.motor_load_frac
        return (P_actual - MOTOR_IDLE_KW) / (mass_flow_kgph / 1000.0)

    def _density(self, sme: float, moisture_pct: float) -> float:
        """
        Empirical proxy: higher SME → more expansion → lower bulk density.
        Wetter feed → better lubrication → slightly lower density.
        Reference: 380 g/L at SME=100, moisture=27 %.
        """
        d = 380.0
        d -= (sme - 100.0) * 1.2
        d += (moisture_pct - 27.0) * 2.5
        return max(280.0, min(480.0, d))

    def run(self, state: ProcessState,
            _context: PlantContext, _weather: WeatherState) -> ProcessState:
        sme = self._sme(state.mass_flow_kgph)
        state.sme_kwh_t     = sme
        state.temperature_c = self.barrel_temp_c
        state.density       = self._density(sme, state.moisture_pct)

        # SME adds mechanical heat → small additional moisture evaporation
        mech_heat_kj_h = (MOTOR_RATED_KW * self.motor_load_frac) * 3600 * 0.3
        evap_from_heat = mech_heat_kj_h / 2257.0          # kg/h water evaporated
        dry_mass = state.mass_flow_kgph * (1 - state.moisture_pct / 100)
        water    = state.mass_flow_kgph * (state.moisture_pct / 100) - evap_from_heat
        state.mass_flow_kgph = dry_mass + max(water, 0)
        state.moisture_pct   = max(water, 0) / state.mass_flow_kgph * 100

        state.log("3_extruder")
        return state
