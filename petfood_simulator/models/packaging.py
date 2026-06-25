"""
Stage 7 — Packaging & Finished Goods
Room climate control, seal quality, throughput bottleneck.
"""
from .core import ProcessState, PlantContext, WeatherState

STAGE_CAPACITIES_KGPH = {
    "extruder":   5_000,
    "dryer":      5_500,
    "cooler":     6_500,
    "coater":     4_800,
    "packer":     4_200,
}


class Packaging:
    """
    4 × finished bins 40 m³ · 14-head weigher
    Packs: 400 g pouches to 25 kg bulk bags
    Room: 18–22 °C · 40–50 % RH · positive pressure
    """
    def __init__(
        self,
        room_temp_c:   float = 20.0,
        room_rh_pct:   float = 45.0,
        seal_quality:  float = 0.98,    # 0–1, affects shelf-life risk
    ):
        self.room_temp_c  = room_temp_c
        self.room_rh_pct  = room_rh_pct
        self.seal_quality = seal_quality

    def _room_moisture_absorption(self, state: ProcessState) -> float:
        """
        Product absorbs moisture if room RH is high and product is cool.
        Simplified linear model.
        """
        if self.room_rh_pct > 50:
            return (self.room_rh_pct - 50.0) * 0.005
        return 0.0

    def run(self, state: ProcessState,
            _context: PlantContext, _weather: WeatherState) -> ProcessState:
        # Line throughput is the tightest stage
        line_tph = min(STAGE_CAPACITIES_KGPH.values())
        state.mass_flow_kgph = min(state.mass_flow_kgph, line_tph)

        # Room moisture pick-up
        state.moisture_pct += self._room_moisture_absorption(state)

        # Poor seal quality raises quality risk
        seal_risk = (1.0 - self.seal_quality) * 0.5
        state.quality_risk = min(1.0, state.quality_risk + seal_risk)

        state.temperature_c = self.room_temp_c
        state.log("7_packaging")
        return state
