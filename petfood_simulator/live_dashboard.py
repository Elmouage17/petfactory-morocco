"""
Pet Factory — Live 1-Hour Production Simulation  (PORT 8055)
Self-contained: simulation engine + Dash dashboard.
Open: http://127.0.0.1:8055
"""
import random
import math
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State, ctx

# ─────────────────────────────────────────────────────────────────────────────
# 1.  SIMULATION ENGINE
# ─────────────────────────────────────────────────────────────────────────────
random.seed(99)


def _n(base, pct=0.03):
    return base + random.gauss(0, abs(base) * pct + 0.001)


def _drift(base, t, period=25, amp=0.05):
    return base * (1 + amp * math.sin(2 * math.pi * t / period))


def _spike(t, events, base, mult=1.2):
    for e in events:
        if e <= t < e + 3:
            return base * mult
    return base


EV_EXTRUDER  = sorted(random.sample(range(8, 52), 2))
EV_DRYER     = sorted(random.sample(range(12, 50), 2))
EV_PACK_STOP = [random.randint(28, 38)]


def build_frame(t):
    """Return dict: machine_name -> {status, kpis:{label:(val,unit)}, notes, alarms}"""
    ramp = min(1.0, t / 5.0)
    out  = {}

    # 1. Raw Materials
    silo = max(8.0, 88 - t * 0.95 + _n(0, 0.4))
    out["Raw Materials"] = {
        "status": "RUNNING" if ramp > 0 else "IDLE",
        "kpis": {
            "Silo Level":     (round(silo, 1),                       "%"),
            "Conv Rate":      (round(_n(58 * ramp, 0.04), 1),        "m³/h"),
            "Inlet Moisture": (round(_n(9.6 + 0.018 * 45, 0.03), 2), "%"),
        },
        "notes":  f"Silo {silo:.0f}% remaining",
        "alarms": ["LOW silo — refill soon"] if silo < 20 else [],
    }

    # 2. Grinding
    motor   = _spike(t, EV_EXTRUDER, _drift(168 * ramp, t, 20, 0.06), 1.18)
    g_al    = []
    if motor > 195: g_al.append(f"HIGH motor {motor:.0f} kW > 195")
    if motor < 140 and ramp > 0.5: g_al.append(f"LOW motor {motor:.0f} kW < 140")
    out["Grinding"] = {
        "status": "ALARM" if g_al else ("RUNNING" if ramp > 0 else "IDLE"),
        "kpis": {
            "Motor Load": (round(motor, 1),                "kW"),
            "Throughput": (round(_n(6.1 * ramp, 0.04), 2), "t/h"),
            "Dust ΔP":    (round(_n(0.57, 0.06), 3),       "kPa"),
        },
        "notes":  "",
        "alarms": g_al,
    }

    # 3. Dosing & Mixing
    batch = t // 3 + 1
    mixing = (t % 3) == 1
    out["Dosing & Mixing"] = {
        "status": "RUNNING" if ramp > 0 else "IDLE",
        "kpis": {
            "Batch #": (float(batch),                      ""),
            "Mass":    (round(_n(975 * ramp, 0.01), 1),    "kg"),
            "Mix CV":  (round(abs(_n(3.7, 0.15)), 2),      "%"),
        },
        "notes":  f"Batch #{batch} — {'MIXING' if mixing else 'FILLING'}",
        "alarms": [],
    }

    # 4. Preconditioner
    out["Preconditioner"] = {
        "status": "RUNNING" if ramp > 0 else "IDLE",
        "kpis": {
            "Steam":        (round(_n(345 * ramp, 0.05), 1),        "kg/h"),
            "Temp Out":     (round(_drift(88 * ramp, t, 25, 0.04), 1), "°C"),
            "Moisture Out": (round(_n(26.3, 0.03), 2),               "%"),
        },
        "notes":  "",
        "alarms": [],
    }

    # 5. Extruder
    load  = _spike(t, EV_EXTRUDER, _n(0.82 * ramp, 0.04), 0.96)
    sme   = (203 * load - 18) / max(0.1, 5.0 * ramp) if ramp > 0.1 else 0.0
    dp    = _drift(_n(30.5, 0.05), t, 18, 0.08)
    ex_al = []
    if sme > 130: ex_al.append(f"HIGH SME {sme:.0f} kWh/t")
    if dp  > 42:  ex_al.append(f"HIGH die pressure {dp:.1f} bar")
    out["Extruder"] = {
        "status": "ALARM" if ex_al else ("RUNNING" if ramp > 0 else "IDLE"),
        "kpis": {
            "Motor Load":   (round(load * 100, 1), "%"),
            "SME":          (round(sme, 1),         "kWh/t"),
            "Die Pressure": (round(dp, 1),          "bar"),
        },
        "notes":  f"Screw {round(_n(352, 0.015), 0):.0f} RPM",
        "alarms": ex_al,
    }

    # 6. Dryer
    z1   = _spike(t, EV_DRYER, _drift(_n(140, 0.03), t, 22, 0.05), 1.12)
    mout = _spike(t, EV_DRYER, _n(9.1, 0.04), 1.18)
    dr_al = []
    if z1   > 165:  dr_al.append(f"HIGH Zone-1 {z1:.0f} °C")
    if mout > 11.5: dr_al.append(f"HIGH moisture {mout:.1f}%")
    if mout < 7.0:  dr_al.append(f"LOW moisture {mout:.1f}%")
    out["Dryer"] = {
        "status": "ALARM" if dr_al else ("RUNNING" if ramp > 0 else "IDLE"),
        "kpis": {
            "Zone 1 Temp":  (round(z1, 1),                   "°C"),
            "Moisture Out": (round(mout, 2),                  "%"),
            "Steam":        (round(_n(885 * ramp, 0.04), 1),  "kg/h"),
        },
        "notes":  f"Z2:{round(_n(138,0.025),1)}°C  Z3:{round(_n(130,0.025),1)}°C",
        "alarms": dr_al,
    }

    # 7. Cooler
    exit_t = _spike(t, [30], _n(25 + 4.5, 0.04), 1.15)
    co_al  = ["HIGH exit temp — rebound risk"] if exit_t > 35 else []
    out["Cooler"] = {
        "status": "ALARM" if co_al else ("RUNNING" if ramp > 0 else "IDLE"),
        "kpis": {
            "Exit Temp": (round(exit_t, 1),               "°C"),
            "Airflow":   (round(_n(11580, 0.02), 0),       "m³/h"),
            "Rebound":   (round(max(0.0, _n(0.07, 0.3)), 3), "%"),
        },
        "notes":  f"Residence {round(_n(12.2,0.03),1)} min",
        "alarms": co_al,
    }

    # 8. Vacuum Coater
    coat_batch = t // 5
    coating    = (t % 5) < 4
    vac  = _n(102, 0.04) if coating else 0.0
    fat  = _n(58, 0.05) * ramp if coating else 0.0
    ct_al = []
    if coating and vac > 120: ct_al.append(f"HIGH vacuum {vac:.0f} mbar")
    if coating and vac < 80:  ct_al.append(f"LOW vacuum {vac:.0f} mbar")
    out["Vacuum Coater"] = {
        "status": "ALARM" if ct_al else ("RUNNING" if coating else "IDLE"),
        "kpis": {
            "Vacuum":    (round(vac, 1),            "mbar"),
            "Fat Flow":  (round(fat, 1),            "L/min"),
            "Fat Add %": (round(_n(12.1, 0.03), 2), "%"),
        },
        "notes":  f"Coat #{coat_batch} — {'COATING' if coating else 'LOADING'}",
        "alarms": ct_al,
    }

    # 9. Packaging
    stopped = t in EV_PACK_STOP
    bpm     = _n(14.2, 0.04) * ramp if not stopped else 0.0
    w_err   = _n(0.01, 5.0)
    pk_al   = []
    if stopped:        pk_al.append("LINE STOP — changeover")
    if abs(w_err) > 1: pk_al.append(f"Weight error {w_err:.2f}%")
    out["Packaging"] = {
        "status": "FAULT" if stopped else ("ALARM" if pk_al else ("RUNNING" if ramp > 0 else "IDLE")),
        "kpis": {
            "Bags/min":   (round(bpm, 1),             "/min"),
            "Room Temp":  (round(_n(20.1, 0.015), 1), "°C"),
            "Weight Err": (round(w_err, 3),            "%"),
        },
        "notes":  "Changeover" if stopped else f"Line speed {round(_n(72,0.03)*ramp,1)}%",
        "alarms": pk_al,
    }

    return out


# Pre-build all 60 frames at startup
FRAMES = [build_frame(t) for t in range(60)]

# ─────────────────────────────────────────────────────────────────────────────
# 2.  CONSTANTS & HELPERS
# ─────────────────────────────────────────────────────────────────────────────
BG   = "#0D1B2A"
CARD = "#112233"
ACC  = "#F0A500"
GRN  = "#2ECC71"
RED  = "#E74C3C"
ORG  = "#E67E22"
BLU  = "#2E6DA4"
TXT  = "#FFFFFF"
MUT  = "#88AACC"

STATUS_COLOR = {"RUNNING": GRN, "ALARM": ORG, "FAULT": RED, "IDLE": MUT}

MACH_ORDER = [
    "Raw Materials", "Grinding", "Dosing & Mixing",
    "Preconditioner", "Extruder", "Dryer",
    "Cooler", "Vacuum Coater", "Packaging",
]
ICONS = {
    "Raw Materials":  "🏭",
    "Grinding":       "⚙️",
    "Dosing & Mixing": "⚖️",
    "Preconditioner": "♨️",
    "Extruder":       "🔩",
    "Dryer":          "🌡️",
    "Cooler":         "❄️",
    "Vacuum Coater":  "💧",
    "Packaging":      "📦",
}

SPARK_KEY = {
    "Raw Materials":   "Silo Level",
    "Grinding":        "Motor Load",
    "Dosing & Mixing": "Mix CV",
    "Preconditioner":  "Moisture Out",
    "Extruder":        "SME",
    "Dryer":           "Moisture Out",
    "Cooler":          "Exit Temp",
    "Vacuum Coater":   "Vacuum",
    "Packaging":       "Bags/min",
}


def _hex_rgba(hex_col, alpha=0.13):
    """Convert #RRGGBB to rgba(r,g,b,alpha) for Plotly fillcolor."""
    h = hex_col.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


def make_spark(vals, col):
    """Tiny sparkline figure."""
    fig = go.Figure(go.Scatter(
        y=vals if vals else [0],
        mode="lines",
        line=dict(color=col, width=1.8),
        fill="tozeroy",
        fillcolor=_hex_rgba(col),
    ))
    fig.update_layout(
        margin=dict(l=0, r=0, t=2, b=2),
        height=48,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        showlegend=False,
    )
    return fig


def build_cards(t):
    """Build all 9 machine cards for frame t."""
    frame = FRAMES[t]

    # Build sparkline history (last 25 points)
    spark_hist = {m: [] for m in MACH_ORDER}
    for i in range(max(0, t - 24), t + 1):
        f = FRAMES[i]
        for m in MACH_ORDER:
            key = SPARK_KEY[m]
            v   = f[m]["kpis"].get(key, (0.0, ""))
            spark_hist[m].append(v[0])

    cards = []
    for mname in MACH_ORDER:
        snap = frame[mname]
        col  = STATUS_COLOR.get(snap["status"], MUT)

        kpi_rows = []
        for lbl, (val, unit) in snap["kpis"].items():
            kpi_rows.append(
                html.Div([
                    html.Span(lbl,
                              style={"color": MUT, "fontSize": "10px"}),
                    html.Span(f"{val:.1f} {unit}".strip(),
                              style={"color": TXT, "fontSize": "11px",
                                     "fontWeight": "bold",
                                     "fontFamily": "monospace"}),
                ], style={"display": "flex",
                           "justifyContent": "space-between",
                           "marginBottom": "3px"})
            )

        alarm_pills = [
            html.Span(a[:45],
                      style={"background": RED, "color": BG,
                             "fontSize": "9px", "padding": "1px 6px",
                             "borderRadius": "8px", "marginRight": "3px",
                             "display": "inline-block", "marginBottom": "2px"})
            for a in snap["alarms"][:2]
        ]

        card = html.Div([
            # Machine name + status badge
            html.Div([
                html.Span(f"{ICONS.get(mname, '')} {mname}",
                          style={"fontWeight": "bold", "fontSize": "12px"}),
                html.Span(snap["status"],
                          style={"fontSize": "10px", "color": col,
                                 "background": _hex_rgba(col, 0.15),
                                 "padding": "2px 8px",
                                 "borderRadius": "10px",
                                 "fontWeight": "bold"}),
            ], style={"display": "flex",
                       "justifyContent": "space-between",
                       "marginBottom": "8px"}),

            # KPI rows
            html.Div(kpi_rows),

            # Notes
            html.P(snap["notes"],
                   style={"color": MUT, "fontSize": "10px",
                           "margin": "4px 0 2px",
                           "fontStyle": "italic"}) if snap["notes"] else html.Span(),

            # Alarm pills
            html.Div(alarm_pills) if alarm_pills else html.Span(),

            # Sparkline
            dcc.Graph(
                figure=make_spark(spark_hist[mname], col),
                config={"displayModeBar": False},
                style={"marginTop": "6px"},
            ),
        ], style={
            "background": BG,
            "borderRadius": "8px",
            "padding": "12px",
            "border": f"2px solid {col}",
        })
        cards.append(card)

    return cards


def build_kpi_strip(t, oee, cum_tons, cum_steam, cum_power, cum_bags, total_alarms):
    """Build the top KPI strip."""
    def pill(label, val, unit, col=ACC):
        return html.Div([
            html.P(label, style={"color": MUT, "margin": 0, "fontSize": "10px"}),
            html.H3(str(val), style={"color": col, "margin": "2px 0 0",
                                      "fontSize": "18px", "fontWeight": "bold"}),
            html.P(unit,     style={"color": MUT, "margin": 0, "fontSize": "10px"}),
        ], style={
            "textAlign": "center", "background": CARD, "borderRadius": "8px",
            "padding": "8px 14px", "border": f"1px solid {BLU}",
            "flex": "1", "minWidth": "80px",
        })

    return [
        pill("⏱ Minute",  f"00:{t:02d}", "",     ACC),
        pill("OEE",        f"{oee:.1f}",  "%",    GRN if oee >= 80 else ORG),
        pill("Produced",   f"{cum_tons}", "t",    ACC),
        pill("Steam",      f"{cum_steam}","kg",   ACC),
        pill("Power",      f"{cum_power}","kWh",  ACC),
        pill("Bags",       f"{cum_bags}", "",     ACC),
        pill("Alarms",     f"{total_alarms}", "active",
             RED if total_alarms > 0 else GRN),
    ]


def build_oee_chart(oee_hist):
    fig = go.Figure()
    xs  = list(range(len(oee_hist)))
    fig.add_trace(go.Scatter(
        x=xs, y=oee_hist,
        mode="lines", fill="tozeroy",
        line=dict(color=GRN, width=2),
        fillcolor="rgba(46,204,113,0.15)",
    ))
    fig.add_hline(y=85, line_dash="dash", line_color=ACC,
                  annotation_text="85% target",
                  annotation_font_color=ACC)
    fig.update_layout(
        title=dict(text="OEE %", font=dict(color=ACC, size=12)),
        paper_bgcolor=BG, plot_bgcolor=BG,
        font=dict(color=TXT, size=10),
        margin=dict(l=35, r=8, t=28, b=28),
        showlegend=False,
        xaxis=dict(gridcolor="#1a2a3a", title="min", range=[0, 60]),
        yaxis=dict(gridcolor="#1a2a3a", range=[0, 105]),
    )
    return fig


def build_trends_chart(hst):
    xs  = list(range(len(hst["oee"])))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xs, y=hst["sme"],  mode="lines",
                             name="SME kWh/t", line=dict(color=ACC, width=1.8)))
    fig.add_trace(go.Scatter(x=xs, y=hst["mout"], mode="lines",
                             name="Moisture %", line=dict(color=BLU, width=1.8)))
    fig.add_trace(go.Scatter(x=xs, y=hst["bpm"],  mode="lines",
                             name="Bags/min", line=dict(color=GRN, width=1.8)))
    fig.update_layout(
        title=dict(text="Key Process Trends", font=dict(color=ACC, size=12)),
        paper_bgcolor=BG, plot_bgcolor=BG,
        font=dict(color=TXT, size=10),
        margin=dict(l=35, r=8, t=28, b=28),
        xaxis=dict(gridcolor="#1a2a3a", title="min", range=[0, 60]),
        yaxis=dict(gridcolor="#1a2a3a"),
        legend=dict(bgcolor=CARD, bordercolor=BLU, font=dict(size=10)),
    )
    return fig


def build_alarm_log(t):
    items = []
    for i in range(t, -1, -1):
        f = FRAMES[i]
        for mname, snap in f.items():
            for a in snap["alarms"]:
                col = RED if ("HIGH" in a or "STOP" in a or "FAULT" in a) else ORG
                items.append(
                    html.P(f"[{i:02d}m] {mname}: {a}",
                           style={"margin": "1px 0", "color": col})
                )
        if len(items) >= 20:
            break
    if not items:
        items = [html.P("No alarms.", style={"color": GRN, "margin": 0})]
    return items


# ─────────────────────────────────────────────────────────────────────────────
# 3.  APP LAYOUT
# ─────────────────────────────────────────────────────────────────────────────
def cs(extra=None):
    s = {"background": CARD, "borderRadius": "10px", "padding": "14px",
         "border": f"1px solid {BLU}", "marginBottom": "10px"}
    if extra:
        s.update(extra)
    return s


def btn(label, bid, bg=BLU, fg=TXT):
    return html.Button(label, id=bid, n_clicks=0, style={
        "background": bg, "color": fg, "border": "none",
        "padding": "8px 20px", "borderRadius": "6px",
        "fontWeight": "bold", "fontSize": "13px",
        "cursor": "pointer", "marginRight": "8px",
    })


app = Dash(__name__, title="Pet Factory Live")
app.config.suppress_callback_exceptions = True

app.layout = html.Div(
    style={"background": BG, "minHeight": "100vh",
           "fontFamily": "Inter,sans-serif", "color": TXT, "padding": "14px"},
    children=[

        # Header
        html.Div([
            html.H1("🏭  PET FACTORY — LIVE SIMULATION",
                    style={"color": ACC, "margin": 0, "fontSize": "19px",
                           "fontWeight": "bold"}),
            html.P("Famsun 5 TPH · Benguerir · 1-Hour Production Run",
                   style={"color": MUT, "margin": "3px 0 0", "fontSize": "11px"}),
        ], style=cs({"marginBottom": "10px"})),

        # Controls
        html.Div([
            btn("▶  START", "b-start", GRN, BG),
            btn("⏸  PAUSE", "b-pause", ORG, BG),
            btn("↺  RESET", "b-reset", BLU, TXT),
            html.Span("Speed:", style={"color": MUT, "fontSize": "12px",
                                        "marginLeft": "16px", "marginRight": "8px"}),
            html.Div(
                dcc.Slider(id="spd", min=1, max=10, step=1, value=1,
                           marks={1: "1×", 2: "2×", 5: "5×", 10: "10×"},
                           tooltip={"always_visible": False}),
                style={"width": "200px", "display": "inline-block",
                       "verticalAlign": "middle"},
            ),
            html.Span(id="banner",
                      style={"marginLeft": "20px", "fontSize": "12px",
                             "fontWeight": "bold", "color": GRN},
                      children="✅  Ready — press ▶ START"),
        ], style=cs({"display": "flex", "alignItems": "center",
                      "flexWrap": "wrap", "padding": "10px 14px"})),

        # KPI strip (pre-populated at t=0)
        html.Div(
            id="kpi-strip",
            children=build_kpi_strip(0, 0.0, 0.0, 0.0, 0.0, 0, 0),
            style={"display": "flex", "gap": "8px",
                   "flexWrap": "wrap", "marginBottom": "10px"},
        ),

        # 3×3 machine grid (pre-populated at t=0)
        html.Div(
            id="mgrid",
            children=build_cards(0),
            style={"display": "grid",
                   "gridTemplateColumns": "repeat(3, 1fr)",
                   "gap": "10px", "marginBottom": "10px"},
        ),

        # Charts row
        html.Div([
            html.Div(
                dcc.Graph(id="g-oee",
                          figure=build_oee_chart([]),
                          config={"displayModeBar": False},
                          style={"height": "230px"}),
                style=cs({"flex": "1", "marginBottom": 0}),
            ),
            html.Div(
                dcc.Graph(id="g-trends",
                          figure=build_trends_chart({"oee":[],"sme":[],"mout":[],"bpm":[]}),
                          config={"displayModeBar": False},
                          style={"height": "230px"}),
                style=cs({"flex": "2", "marginBottom": 0}),
            ),
        ], style={"display": "flex", "gap": "10px", "marginBottom": "10px"}),

        # Alarm log
        html.Div([
            html.B("⚠ Alarm Log", style={"color": ACC, "fontSize": "12px"}),
            html.Div(
                id="alog",
                children=build_alarm_log(0),
                style={"fontFamily": "monospace", "fontSize": "11px",
                       "maxHeight": "100px", "overflowY": "auto",
                       "marginTop": "6px"},
            ),
        ], style=cs({"marginBottom": 0})),

        # State stores
        dcc.Store(id="ctl", data={"run": False, "rev": 0}),
        dcc.Store(id="tst", data={"t": 0, "rev": 0}),
        dcc.Store(id="hst", data={"oee": [], "sme": [], "mout": [], "bpm": []}),
        dcc.Interval(id="iv", interval=1000, n_intervals=0),
    ],
)


# ─────────────────────────────────────────────────────────────────────────────
# 4.  CALLBACKS
# ─────────────────────────────────────────────────────────────────────────────

@app.callback(
    Output("ctl", "data"),
    Input("b-start", "n_clicks"),
    Input("b-pause", "n_clicks"),
    Input("b-reset", "n_clicks"),
    State("ctl", "data"),
    prevent_initial_call=True,
)
def on_button(_s, _p, _r, ctl):
    tid = ctx.triggered_id
    if   tid == "b-start": ctl["run"] = True
    elif tid == "b-pause": ctl["run"] = False
    elif tid == "b-reset": ctl = {"run": False, "rev": ctl["rev"] + 1}
    return ctl


@app.callback(
    Output("tst",       "data"),
    Output("hst",       "data"),
    Output("banner",    "children"),
    Output("banner",    "style"),
    Output("kpi-strip", "children"),
    Output("mgrid",     "children"),
    Output("g-oee",     "figure"),
    Output("g-trends",  "figure"),
    Output("alog",      "children"),
    Input("iv",  "n_intervals"),
    Input("spd", "value"),
    Input("ctl", "data"),
    State("tst", "data"),
    State("hst", "data"),
    prevent_initial_call=True,
)
def tick(_, spd, ctl, tst, hst):
    # Reset when rev bumped
    if ctl["rev"] != tst.get("rev", 0):
        tst = {"t": 0, "rev": ctl["rev"]}
        hst = {"oee": [], "sme": [], "mout": [], "bpm": []}

    t = tst["t"]
    if ctl["run"] and t < 59:
        t = min(t + max(1, int(spd)), 59)
    tst["t"] = t

    frame = FRAMES[t]
    ramp  = min(1.0, t / 5.0)

    # Cumulative plant KPIs
    cum_bags  = int(sum(FRAMES[i]["Packaging"]["kpis"]["Bags/min"][0] for i in range(t + 1)))
    cum_steam = round(sum(FRAMES[i]["Dryer"]["kpis"]["Steam"][0] / 60 for i in range(t + 1)), 1)
    cum_power = round(t * (203 * 0.82 + 62 + 22) / 60, 1)
    cum_tons  = round(t * 5.0 * ramp / 60, 3)

    total_alarms = sum(len(v["alarms"]) for v in frame.values())
    statuses     = [v["status"] for v in frame.values()]
    has_fault    = "FAULT" in statuses
    has_alarm    = "ALARM" in statuses

    avail = 0.0 if has_fault else 1.0
    bpm   = frame["Packaging"]["kpis"]["Bags/min"][0]
    perf  = bpm / 14.2 if bpm > 0 else 0.0
    qual  = max(0.0, 1.0 - 0.03 * total_alarms)
    oee   = max(0.0, min(100.0, avail * perf * qual * 100))

    hst["oee"].append(oee)
    hst["sme"].append(frame["Extruder"]["kpis"]["SME"][0])
    hst["mout"].append(frame["Dryer"]["kpis"]["Moisture Out"][0])
    hst["bpm"].append(bpm)

    # Banner
    if has_fault:
        ban_txt  = "🔴  FAULT ACTIVE"
        ban_styl = {"color": RED,  "fontSize": "12px", "fontWeight": "bold", "marginLeft": "20px"}
    elif has_alarm:
        ban_txt  = f"⚠  {total_alarms} ALARM(S)"
        ban_styl = {"color": ORG,  "fontSize": "12px", "fontWeight": "bold", "marginLeft": "20px"}
    elif not ctl["run"] and t == 0:
        ban_txt  = "✅  Ready — press ▶ START"
        ban_styl = {"color": GRN,  "fontSize": "12px", "fontWeight": "bold", "marginLeft": "20px"}
    elif not ctl["run"]:
        ban_txt  = f"⏸  Paused at {t:02d}m"
        ban_styl = {"color": MUT,  "fontSize": "12px", "fontWeight": "bold", "marginLeft": "20px"}
    else:
        ban_txt  = "✅  All Systems Normal"
        ban_styl = {"color": GRN,  "fontSize": "12px", "fontWeight": "bold", "marginLeft": "20px"}

    strip  = build_kpi_strip(t, oee, cum_tons, cum_steam, cum_power, cum_bags, total_alarms)
    cards  = build_cards(t)
    fig_oee = build_oee_chart(hst["oee"])
    fig_tr  = build_trends_chart(hst)
    alog    = build_alarm_log(t)

    return tst, hst, ban_txt, ban_styl, strip, cards, fig_oee, fig_tr, alog


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("  Pet Factory Live Simulation")
    print("  → Open: http://127.0.0.1:8055")
    print("  → Press ▶ START to begin the 1-hour run")
    print("=" * 55 + "\n")
    app.run(debug=False, port=8055, host="127.0.0.1")
