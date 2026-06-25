"""
Stage 6 — Double-Shaft Vacuum Coater (C0112 · 2000 L · 800 kg/batch)
Fat/palatant application, vacuum infusion model, oxidation risk.
"""
from .core import ProcessState, PlantContext, WeatherState


class Coater:
    """
    Vacuum: 100 mbar · Batch cycle: 300 s · Fat addition: 6–36 %
    Oil tank: 1000 L heated · Palatant tank: 1000 L
    """
    def __init__(
        self,
        fat_addition_pct:      float = 12.0,   # % of kibble mass
        palatant_addition_pct: float = 2.0,
        vacuum_mbar:           float = 100.0,
        coating_temp_c:        float = 65.0,
        batch_time_s:          float = 300.0,
        coating_uniformity:    float = 0.95,   # 0–1
    ):
        self.fat_addition_pct      = fat_addition_pct
        self.palatant_addition_pct = palatant_addition_pct
        self.vacuum_mbar           = vacuum_mbar
        self.coating_temp_c        = coating_temp_c
        self.batch_time_s          = batch_time_s
        self.coating_uniformity    = coating_uniformity

    def _oxidation_risk(self, temp_c: float, fat_pct: float,
                        moisture_pct: float) -> float:
        """
        Lipid oxidation is accelerated by high temperature, high fat, and low moisture.
        Arrhenius-inspired proxy (0–1 scale).
        """
        temp_factor = max(0.0, (temp_c - 40.0) / 60.0)
        fat_factor  = fat_pct / 36.0
        aw_factor   = max(0.0, 1.0 - moisture_pct / 12.0)
        return min(1.0, temp_factor * fat_factor * aw_factor * 0.4)

    def run(self, state: ProcessState,
            _context: PlantContext, _weather: WeatherState) -> ProcessState:
        total_addition = self.fat_addition_pct + self.palatant_addition_pct
        added_mass     = state.mass_flow_kgph * (total_addition / 100.0)
        state.mass_flow_kgph += added_mass

        # Fat dilutes bulk moisture percentage
        state.moisture_pct = state.moisture_pct * (1 - total_addition / 100.0)

        # Fat content update
        state.fat_pct += self.fat_addition_pct * (
            state.mass_flow_kgph / (state.mass_flow_kgph + added_mass))

        ox_risk = self._oxidation_risk(
            self.coating_temp_c, state.fat_pct, state.moisture_pct)
        state.quality_risk = max(state.quality_risk, ox_risk)

        state.log("6_coater")
        return state
