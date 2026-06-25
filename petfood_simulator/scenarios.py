"""
Preset scenarios for the Pet Factory digital twin.
Each scenario bundles a WeatherState + SKU + label + description.
"""
from models import WeatherState, SKU

SCENARIOS = {
    "summer_peak": {
        "label":       "Summer Peak (Aug)",
        "description": "Hottest month · Benguerir · High humidity risk",
        "weather":     WeatherState(dry_bulb_c=38, wet_bulb_c=26, relative_humidity=35),
        "sku":         SKU(name="Standard Dry Kibble"),
        "color":       "#E74C3C",
    },
    "winter_cold": {
        "label":       "Winter Cold (Jan)",
        "description": "Cold dry conditions · lower moisture absorption",
        "weather":     WeatherState(dry_bulb_c=8,  wet_bulb_c=6,  relative_humidity=72),
        "sku":         SKU(name="Standard Dry Kibble"),
        "color":       "#2E6DA4",
    },
    "spring_mild": {
        "label":       "Spring Mild (Apr)",
        "description": "Optimal baseline conditions",
        "weather":     WeatherState(dry_bulb_c=22, wet_bulb_c=15, relative_humidity=48),
        "sku":         SKU(name="Standard Dry Kibble"),
        "color":       "#2ECC71",
    },
    "humid_storm": {
        "label":       "Humid Storm Event",
        "description": "Worst-case RH spike · moisture rebound risk",
        "weather":     WeatherState(dry_bulb_c=28, wet_bulb_c=26, relative_humidity=90),
        "sku":         SKU(name="Standard Dry Kibble"),
        "color":       "#9B59B6",
    },
    "sku_standard": {
        "label":       "SKU: Standard Kibble",
        "description": "9 % moisture target · 8 % fat",
        "weather":     WeatherState(dry_bulb_c=25, relative_humidity=45),
        "sku":         SKU(name="Standard Dry Kibble",
                           moisture_target_pct=9.0,
                           recipe={"chicken_meal":0.30,"corn":0.25,"wheat":0.20,
                                   "rice":0.10,"fat":0.08,"vitamins_minerals":0.07}),
        "color":       "#F0A500",
    },
    "sku_high_protein": {
        "label":       "SKU: High-Protein",
        "description": "8.5 % moisture · higher chicken meal · lower starch",
        "weather":     WeatherState(dry_bulb_c=25, relative_humidity=45),
        "sku":         SKU(name="High-Protein Kibble",
                           moisture_target_pct=8.5,
                           recipe={"chicken_meal":0.45,"corn":0.15,"wheat":0.10,
                                   "rice":0.08,"fat":0.14,"vitamins_minerals":0.08}),
        "color":       "#E74C3C",
    },
    "sku_senior": {
        "label":       "SKU: Senior Formula",
        "description": "9.5 % moisture · lower fat · high fibre",
        "weather":     WeatherState(dry_bulb_c=25, relative_humidity=45),
        "sku":         SKU(name="Senior Formula",
                           moisture_target_pct=9.5,
                           recipe={"chicken_meal":0.22,"corn":0.20,"wheat":0.25,
                                   "rice":0.18,"fat":0.05,"vitamins_minerals":0.10}),
        "color":       "#2ECC71",
    },
}

SCENARIO_GROUPS = {
    "Seasonal Weather":  ["summer_peak", "winter_cold", "spring_mild", "humid_storm"],
    "SKU Comparison":    ["sku_standard", "sku_high_protein", "sku_senior"],
}
