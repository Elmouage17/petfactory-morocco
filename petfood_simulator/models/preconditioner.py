"""
Stage 2 — Single-Layer Preconditioner (E0103, 22 kW)
Moisture balance and temperature update before extrusion.
"""
from .core import ProcessState, PlantContext, WeatherState

# Physical constants
LATENT_HEAT_STEAM = 2257.0   # kJ/kg at 100 °C
CP_PRODUCT        = 1.8      # kJ/(kg·°C) dry pet-food mix
EVAP_FRACTION     = 0.05     # fraction of added water that flash-evaporates


class Preconditioner:
    """
    Steam: 0.1–0.4 MPa regulated · Water: up to 1 600 kg/h
    Residence time: 2–4 min · Target moisture out: 25–30 %
    """
    def __init__(
        self,
        steam_flow_kgph: float = 350.0,    # kg/h steam added
        water_flow_kgph: float = 400.0,    # kg/h liquid water added
        residence_min:   float = 3.0,
        steam_pressure_mpa: float = 0.25,
        thermal_loss_frac:  float = 0.05,
    ):
        self.steam_flow_kgph    = steam_flow_kgph
        self.water_flow_kgph    = water_flow_kgph
        self.residence_min      = residence_min
        self.steam_pressure_mpa = steam_pressure_mpa
        self.thermal_loss_frac  = thermal_loss_frac

    def run(self, state: ProcessState,
            _context: PlantContext, _weather: WeatherState) -> ProcessState:
        m   = state.mass_flow_kgph          # kg/h dry basis feed
        M_i = state.moisture_pct / 100.0

        # --- Moisture balance -------------------------------------------
        # mass of dry solids
        dry_kgph = m * (1 - M_i)
        water_in = m * M_i

        steam_condensed = self.steam_flow_kgph * 0.92   # ~8 % passes through
        water_added     = self.water_flow_kgph
        evaporation     = (steam_condensed + water_added) * EVAP_FRACTION

        water_out    = water_in + steam_condensed + water_added - evaporation
        total_out    = dry_kgph + water_out
        M_out        = water_out / total_out

        state.moisture_pct   = M_out * 100
        state.mass_flow_kgph = total_out

        # --- Temperature update -----------------------------------------
        heat_steam = steam_condensed * LATENT_HEAT_STEAM          # kJ/h
        heat_water = water_added * 4.18 * (60 - state.temperature_c)  # pre-heated water ≈60°C
        evap_cooling = evaporation * LATENT_HEAT_STEAM
        thermal_loss = heat_steam * self.thermal_loss_frac

        delta_T = ((heat_steam + heat_water - evap_cooling - thermal_loss)
                   / (total_out * CP_PRODUCT))
        state.temperature_c = state.temperature_c + delta_T

        state.log("2_preconditioner")
        return state
