"""
Stage 1 — Raw Material Reception & Storage
Initialises ProcessState from ambient conditions and SKU recipe.
"""
import math
from .core import ProcessState, PlantContext, WeatherState, SKU


def _ingredient_moisture(recipe: dict, weather: WeatherState) -> float:
    """
    Estimate blended inlet moisture from recipe and ambient RH.
    Hygroscopic grains absorb ~0.05 % moisture per % RH above 50 %.
    """
    base = sum({
        "chicken_meal": 8.0,
        "corn": 12.0,
        "wheat": 13.0,
        "rice": 11.5,
        "fat": 0.1,
        "vitamins_minerals": 5.0,
    }.get(k, 10.0) * v for k, v in recipe.items())
    rh_correction = max(0.0, (weather.relative_humidity - 50.0) * 0.05)
    return base + rh_correction


class RawMaterials:
    """
    Drum Precleaner 40 t/h · Permanent Magnet ≥0.3T
    200T Steel Silo · 14 Surge Bins
    """
    throughput_limit_kgph: float = 40_000   # 40 t/h cleaner capacity

    def run(self, state: ProcessState,
            context: PlantContext, weather: WeatherState,
            sku: SKU) -> ProcessState:
        state.moisture_pct   = _ingredient_moisture(sku.recipe, weather)
        state.temperature_c  = weather.dry_bulb_c   # stored at ambient
        state.fat_pct        = sku.recipe.get("fat", 0.08) * 100
        state.mass_flow_kgph = min(sku.design_throughput_kgph,
                                   self.throughput_limit_kgph)
        state.log("1_raw_materials")
        return state
