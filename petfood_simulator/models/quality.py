"""
Stage 8 — Quality & Water Activity Model (Layer C)
Predicts final aₓ, moisture spec compliance, and composite quality risk.
"""
import math
from .core import ProcessState, WeatherState, SKU


def _aw_surrogate(moisture_pct: float, temp_c: float,
                  fat_pct: float, starch_gel_index: float = 0.75) -> float:
    """
    Empirical aₓ surrogate:
      - moisture drives aw upward
      - high fat lowers aw (fat binds free water)
      - temperature has a small positive effect
      - starch gelatinisation (index 0–1) lowers aw slightly
    """
    base  = 0.02 * moisture_pct
    fat_c = -0.004 * fat_pct
    temp_c_effect = 0.001 * (temp_c - 20.0)
    gel   = -0.05 * starch_gel_index
    aw    = base + fat_c + temp_c_effect + gel
    return max(0.05, min(0.99, aw))


def _quality_risk_score(
    aw: float, aw_limit: float,
    moisture_pct: float, moisture_target: float,
    warehouse_temp_c: float, warehouse_rh: float,
    oxygen_exposure: float, storage_days: float,
) -> float:
    """
    Weighted composite quality risk (0 = perfect, 1 = reject).
    QR = w1·aw_risk + w2·temp_risk + w3·rh_risk + w4·O₂_risk + w5·time_risk
    """
    w = [0.35, 0.20, 0.15, 0.15, 0.15]

    aw_risk    = max(0.0, (aw - aw_limit) / (1.0 - aw_limit))
    temp_risk  = max(0.0, (warehouse_temp_c - 26.6) / 10.0)
    rh_risk    = max(0.0, (warehouse_rh - 60.0) / 40.0)
    o2_risk    = min(1.0, oxygen_exposure)
    time_risk  = min(1.0, storage_days / 180.0)

    return min(1.0, sum(w[i] * r for i, r in enumerate(
        [aw_risk, temp_risk, rh_risk, o2_risk, time_risk])))


class QualityModel:
    def __init__(
        self,
        warehouse_temp_c: float = 22.0,
        warehouse_rh_pct: float = 50.0,
        oxygen_exposure:  float = 0.05,
        storage_days:     float = 30.0,
        starch_gel_index: float = 0.75,
    ):
        self.warehouse_temp_c = warehouse_temp_c
        self.warehouse_rh_pct = warehouse_rh_pct
        self.oxygen_exposure  = oxygen_exposure
        self.storage_days     = storage_days
        self.starch_gel_index = starch_gel_index

    def predict(self, state: ProcessState,
                weather: WeatherState, sku: SKU) -> dict:
        aw = _aw_surrogate(
            state.moisture_pct, state.temperature_c,
            state.fat_pct, self.starch_gel_index)

        qr = _quality_risk_score(
            aw, sku.aw_limit,
            state.moisture_pct, sku.moisture_target_pct,
            self.warehouse_temp_c, self.warehouse_rh_pct,
            self.oxygen_exposure, self.storage_days)

        state.aw_est       = aw
        state.quality_risk = max(state.quality_risk, qr)
        state.log("8_quality")

        moisture_ok = abs(state.moisture_pct - sku.moisture_target_pct) <= 1.5
        aw_ok       = aw < sku.aw_limit

        return {
            "aw_est":         round(aw, 4),
            "quality_risk":   round(qr, 4),
            "moisture_pct":   round(state.moisture_pct, 3),
            "moisture_ok":    moisture_ok,
            "aw_ok":          aw_ok,
            "release_status": "PASS" if (moisture_ok and aw_ok and qr < 0.35) else "HOLD",
        }
