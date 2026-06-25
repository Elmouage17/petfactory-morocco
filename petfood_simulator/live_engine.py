"""
Live simulation engine — generates minute-by-minute state for all 8 machines
over a 60-minute production run with realistic noise, drift, and random events.
"""
import random
import math
from dataclasses import dataclass, field
from typing import List, Dict


random.seed(42)


# ── Machine alarm thresholds ──────────────────────────────────────────────────
ALARMS = {
    "hammermill_motor_kw":   {"lo": 140, "hi": 195, "unit": "kW"},
    "extruder_sme":          {"lo": 60,  "hi": 130, "unit": "kWh/t"},
    "extruder_die_pressure": {"lo": 15,  "hi": 42,  "unit": "bar"},
    "dryer_moisture_out":    {"lo": 7.0, "hi": 11.5,"unit": "%"},
    "dryer_zone1_temp":      {"lo": 110, "hi": 165, "unit": "°C"},
    "cooler_exit_temp":      {"lo": 18,  "hi": 35,  "unit": "°C"},
    "coater_vacuum_mbar":    {"lo": 80,  "hi": 120, "unit": "mbar"},
    "packaging_weight_err":  {"lo": -1,  "hi": 1,   "unit": "%"},
}


def _noise(base: float, pct: float = 0.03) -> float:
    """Gaussian noise, pct of base value."""
    return base + random.gauss(0, base * pct)


def _drift(base: float, t: int, period: int = 30,
           amplitude: float = 0.04) -> float:
    """Sinusoidal drift superimposed on base value."""
    return base * (1 + amplitude * math.sin(2 * math.pi * t / period))


def _event(t: int, event_times: List[int],
           base: float, spike_mult: float = 1.25) -> float:
    """Apply a brief spike at scheduled event minutes."""
    for et in event_times:
        if et <= t < et + 3:
            return base * spike_mult
    return base


@dataclass
class MachineSnapshot:
    minute:  int
    name:    str
    status:  str          # RUNNING / ALARM / FAULT / IDLE
    kpis:    Dict[str, float] = field(default_factory=dict)
    alarms:  List[str]        = field(default_factory=list)
    notes:   str = ""


def _check_alarms(kpis: dict) -> List[str]:
    triggered = []
    for key, limits in ALARMS.items():
        if key in kpis:
            v = kpis[key]
            if v < limits["lo"]:
                triggered.append(f"LOW {key}: {v:.1f} {limits['unit']} < {limits['lo']}")
            elif v > limits["hi"]:
                triggered.append(f"HIGH {key}: {v:.1f} {limits['unit']} > {limits['hi']}")
    return triggered


def simulate_hour(
    ambient_temp_c: float = 25.0,
    ambient_rh:     float = 45.0,
    throughput_kgph: float = 5000.0,
) -> List[List[MachineSnapshot]]:
    """
    Return a list of 60 frames, each containing one snapshot per machine.
    """
    frames: List[List[MachineSnapshot]] = []

    # Pre-schedule random events
    extruder_spikes = random.sample(range(10, 55), 2)
    dryer_events    = random.sample(range(15, 50), 2)
    cooler_event    = [random.randint(20, 45)]
    pack_stoppages  = [random.randint(30, 40)]

    # Cumulative counters
    cum_tons      = 0.0
    cum_steam_kg  = 0.0
    cum_power_kwh = 0.0
    cum_bags      = 0

    # Warm-up: first 5 minutes machines ramp up
    RAMP_MINS = 5

    for t in range(60):
        ramp = min(1.0, t / RAMP_MINS)
        frame: List[MachineSnapshot] = []

        # ── 1. Raw Material Reception ─────────────────────────────────────
        silo_level  = max(10, 85 - t * 0.9 + _noise(0, 0.5))
        conv_rate   = _noise(throughput_kgph * 0.011, 0.03) * ramp   # m³/h chain conv
        rm_kpis = {
            "silo_level_pct":    round(silo_level, 1),
            "conveyor_rate_m3h": round(conv_rate, 1),
            "inlet_moisture_pct": round(_drift(9.5 + ambient_rh * 0.015, t), 2),
            "magnet_status":      1.0,
        }
        frame.append(MachineSnapshot(t, "Raw Materials",
                                     "RUNNING" if ramp > 0 else "IDLE", rm_kpis))

        # ── 2. Grinding ───────────────────────────────────────────────────
        mill_load = _event(t, extruder_spikes,
                           _drift(168 * ramp, t, period=20, amplitude=0.06), 1.18)
        grind_kpis = {
            "hammermill_motor_kw": round(mill_load, 1),
            "throughput_th":       round(_noise(6.2 * ramp, 0.04), 2),
            "screen_diff_pressure_pa": round(_noise(320, 0.08), 0),
            "dust_collector_dp_kpa":   round(_noise(0.58, 0.05), 3),
        }
        grind_alarms = _check_alarms(grind_kpis)
        frame.append(MachineSnapshot(t, "Grinding",
                                     "ALARM" if grind_alarms else "RUNNING",
                                     grind_kpis, grind_alarms))

        # ── 3. Dosing & Mixing ────────────────────────────────────────────
        batch_num = t // 3 + 1   # new batch every ~3 min
        in_mix    = (t % 3) == 1
        mix_kpis = {
            "batch_number":     float(batch_num),
            "batch_mass_kg":    round(_noise(980 * ramp, 0.01), 1),
            "mix_cv_pct":       round(abs(_noise(3.8, 0.15)), 2),
            "scale_accuracy_pct": round(_noise(0.18, 0.2), 3),
            "mixer_status":     1.0 if in_mix else 0.0,
        }
        frame.append(MachineSnapshot(t, "Dosing & Mixing",
                                     "RUNNING" if ramp > 0 else "IDLE", mix_kpis,
                                     notes=f"Batch #{batch_num} {'MIXING' if in_mix else 'FILLING'}"))

        # ── 4. Preconditioner ─────────────────────────────────────────────
        steam_flow  = _noise(340 * ramp, 0.05)
        cond_temp   = _drift(88 * ramp, t, period=25, amplitude=0.04)
        cond_moist  = _noise(26.5, 0.03)
        pc_kpis = {
            "steam_flow_kgph":      round(steam_flow, 1),
            "water_added_kgph":     round(_noise(390 * ramp, 0.04), 1),
            "discharge_temp_c":     round(cond_temp, 1),
            "discharge_moisture_pct": round(cond_moist, 2),
            "residence_time_min":   round(_noise(3.1, 0.03), 2),
        }
        cum_steam_kg += steam_flow / 60
        frame.append(MachineSnapshot(t, "Preconditioner", "RUNNING" if ramp > 0 else "IDLE", pc_kpis))

        # ── 5. Extruder ───────────────────────────────────────────────────
        motor_load  = _event(t, extruder_spikes, _noise(0.83 * ramp, 0.04), 0.97)
        motor_kw    = 203 * motor_load
        sme         = (motor_kw - 18) / (throughput_kgph / 1000) if ramp > 0.2 else 0
        die_press   = _drift(_noise(31, 0.05), t, period=18, amplitude=0.08)
        barrel_temp = _noise(145, 0.02)
        ex_kpis = {
            "motor_load_pct":      round(motor_load * 100, 1),
            "motor_kw":            round(motor_kw, 1),
            "sme_kwh_t":           round(sme, 1),
            "barrel_temp_c":       round(barrel_temp, 1),
            "extruder_die_pressure": round(die_press, 1),
            "screw_speed_rpm":     round(_noise(352, 0.015), 0),
            "knife_rpm":           round(_noise(1200, 0.02), 0),
        }
        ex_alarms = _check_alarms(ex_kpis)
        cum_power_kwh += motor_kw / 60
        frame.append(MachineSnapshot(t, "Extruder",
                                     "ALARM" if ex_alarms else "RUNNING",
                                     ex_kpis, ex_alarms))

        # ── 6. Dryer ──────────────────────────────────────────────────────
        z1 = _event(t, dryer_events, _drift(_noise(140, 0.03), t, 22, 0.05), 1.12)
        z2 = _noise(138, 0.025)
        z3 = _noise(130, 0.025)
        z4 = _noise(118, 0.025)
        dryer_moist = _event(t, dryer_events, _noise(9.1, 0.04), 1.18)
        dr_kpis = {
            "dryer_zone1_temp": round(z1, 1),
            "zone2_temp_c":     round(z2, 1),
            "zone3_temp_c":     round(z3, 1),
            "zone4_temp_c":     round(z4, 1),
            "dryer_moisture_out": round(dryer_moist, 2),
            "exhaust_rh_pct":   round(_noise(65, 0.06), 1),
            "belt_speed_pct":   round(_noise(50, 0.02), 1),
            "steam_kgph":       round(_noise(890 * ramp, 0.04), 1),
        }
        dr_alarms = _check_alarms(dr_kpis)
        cum_steam_kg += dr_kpis["steam_kgph"] / 60
        cum_power_kwh += 62.26 / 60
        frame.append(MachineSnapshot(t, "Dryer",
                                     "ALARM" if dr_alarms else "RUNNING",
                                     dr_kpis, dr_alarms))

        # ── 7. Cooler ─────────────────────────────────────────────────────
        exit_t = _event(t, cooler_event,
                        _noise(ambient_temp_c + 4.5, 0.04), 1.15)
        co_kpis = {
            "cooler_exit_temp":   round(exit_t, 1),
            "airflow_m3h":        round(_noise(11580, 0.02), 0),
            "residence_time_min": round(_noise(12.2, 0.03), 1),
            "fan_kw":             round(_noise(20.8, 0.03), 1),
            "moisture_rebound_pct": round(max(0, _noise(0.08, 0.3)), 3),
        }
        co_alarms = _check_alarms(co_kpis)
        frame.append(MachineSnapshot(t, "Cooler",
                                     "ALARM" if co_alarms else "RUNNING",
                                     co_kpis, co_alarms))

        # ── 8. Vacuum Coater ──────────────────────────────────────────────
        batch_coat = t // 5
        in_coat    = (t % 5) < 4
        vacuum_v   = _noise(102, 0.04) if in_coat else 0
        fat_flow   = _noise(58, 0.05) * ramp if in_coat else 0
        ct_kpis = {
            "coater_batch":      float(batch_coat),
            "coater_vacuum_mbar": round(vacuum_v, 1),
            "fat_flow_lpm":      round(fat_flow, 1),
            "fat_addition_pct":  round(_noise(12.1, 0.03), 2),
            "coating_temp_c":    round(_noise(64, 0.025), 1),
            "cycle_time_s":      round(_noise(298, 0.02), 0),
        }
        ct_alarms = _check_alarms(ct_kpis)
        frame.append(MachineSnapshot(t, "Vacuum Coater",
                                     "ALARM" if ct_alarms else
                                     ("RUNNING" if in_coat else "IDLE"),
                                     ct_kpis, ct_alarms,
                                     notes=f"Coat #{batch_coat} {'COATING' if in_coat else 'FILLING'}"))

        # ── 9. Packaging ─────────────────────────────────────────────────
        stopped     = t in pack_stoppages
        bags_per_min = _noise(14.2, 0.04) * ramp if not stopped else 0
        cum_bags    += int(bags_per_min)
        w_err        = _noise(0.02, 5.0)
        pk_kpis = {
            "bags_per_min":      round(bags_per_min, 1),
            "bags_total":        float(cum_bags),
            "avg_bag_kg":        round(_noise(10.1, 0.005), 3),
            "packaging_weight_err": round(w_err, 3),
            "room_temp_c":       round(_noise(20.2, 0.015), 1),
            "room_rh_pct":       round(_noise(44.5, 0.02), 1),
            "line_speed_pct":    round(_noise(72, 0.03) * ramp if not stopped else 0, 1),
        }
        pk_alarms = _check_alarms(pk_kpis)
        if stopped:
            pk_alarms.append("LINE STOP: scheduled changeover")

        frame.append(MachineSnapshot(t, "Packaging",
                                     "FAULT" if stopped else
                                     ("ALARM" if pk_alarms else "RUNNING"),
                                     pk_kpis, pk_alarms))

        # ── Plant-level KPIs ─────────────────────────────────────────────
        cum_tons += throughput_kgph * ramp / 60000   # tonnes this minute
        avail     = 1.0 - (1 if stopped else 0) * (1/60)
        perf      = min(1.0, (bags_per_min / 14.2) if bags_per_min > 0 else 0)
        quality   = 1.0 - (0.02 if any(f.status in ("ALARM","FAULT")
                                       for f in frame) else 0)
        oee       = avail * perf * quality

        plant_kpis = {
            "oee_pct":          round(oee * 100, 1),
            "cum_tonnes":       round(cum_tons, 3),
            "cum_steam_kg":     round(cum_steam_kg, 1),
            "cum_power_kwh":    round(cum_power_kwh, 1),
            "cum_bags":         float(cum_bags),
            "active_alarms":    float(sum(len(f.alarms) for f in frame)),
        }
        frame.append(MachineSnapshot(t, "Plant Summary", "RUNNING", plant_kpis))

        frames.append(frame)

    return frames
