"""
Core data classes shared across all unit operation modules.
"""
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class PlantContext:
    site_name: str = "Benguerir, Morocco"
    latitude: float = 32.25
    longitude: float = -7.95
    elevation_m: float = 460.0
    utility_prices: Dict[str, float] = field(default_factory=lambda: {
        "steam_mad_per_kg": 0.18,     # MAD per kg steam
        "electricity_mad_per_kwh": 1.20,
        "water_mad_per_m3": 8.50,
    })
    warehouse_limits: Dict[str, float] = field(default_factory=lambda: {
        "max_temp_c": 26.6,
        "max_rh_pct": 60.0,
        "max_days": 180,
    })


@dataclass
class WeatherState:
    dry_bulb_c: float = 25.0
    wet_bulb_c: float = 18.0
    relative_humidity: float = 45.0   # %
    dew_point_c: float = 12.5

    def update_dew_point(self):
        """Magnus formula approximation."""
        a, b = 17.27, 237.7
        alpha = (a * self.dry_bulb_c) / (b + self.dry_bulb_c) + \
                __import__("math").log(self.relative_humidity / 100.0)
        self.dew_point_c = (b * alpha) / (a - alpha)


@dataclass
class SKU:
    name: str = "Standard Dry Kibble"
    recipe: Dict[str, float] = field(default_factory=lambda: {
        "chicken_meal": 0.30,
        "corn": 0.25,
        "wheat": 0.20,
        "rice": 0.10,
        "fat": 0.08,
        "vitamins_minerals": 0.07,
    })
    moisture_target_pct: float = 9.0
    aw_limit: float = 0.60
    density_target: float = 380.0      # g/L bulk density
    design_throughput_kgph: float = 5000.0


@dataclass
class ProcessState:
    mass_flow_kgph: float = 5000.0
    moisture_pct: float = 10.0
    temperature_c: float = 25.0
    aw_est: float = 0.55
    density: float = 380.0             # g/L
    quality_risk: float = 0.0          # 0–1 score
    sme_kwh_t: float = 0.0
    fat_pct: float = 8.0
    stage_log: Dict[str, dict] = field(default_factory=dict)

    def log(self, stage: str):
        self.stage_log[stage] = {
            "mass_flow_kgph": round(self.mass_flow_kgph, 2),
            "moisture_pct":   round(self.moisture_pct, 3),
            "temperature_c":  round(self.temperature_c, 2),
            "aw_est":         round(self.aw_est, 4),
            "density":        round(self.density, 1),
            "quality_risk":   round(self.quality_risk, 4),
        }
