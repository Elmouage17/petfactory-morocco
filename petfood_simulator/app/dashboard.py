"""
Pet Factory Digital Twin — Plotly/Dash Operator Dashboard
Run: python app/dashboard.py
Then open: http://127.0.0.1:8050
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import dash
from dash import dcc, html, Input, Output, callback
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json

from simulator import run_simulation
from optimization.optimizer import grid_search_optimize
from models import WeatherState, SKU
from scenarios import SCENARIOS, SCENARIO_GROUPS

# ── Colour palette (matches PFD diagram) ────────────────────────────────────
BG       = "#0D1B2A"
CARD_BG  = "#1B3A5C"
ACCENT   = "#F0A500"
GREEN    = "#2ECC71"
RED      = "#E74C3C"
BLUE     = "#2E6DA4"
TEXT     = "#FFFFFF"
SUBTEXT  = "#A8C8E8"

CARD_STYLE = {
    "background": CARD_BG, "borderRadius": "10px",
    "padding": "16px", "marginBottom": "16px",
    "border": f"1px solid {BLUE}",
}

KPI_STYLE = {
    **CARD_STYLE,
    "textAlign": "center", "minWidth": "150px", "flex": "1",
}

# ── Stage names for log display ──────────────────────────────────────────────
STAGE_ORDER = [
    "1_raw_materials", "2_preconditioner", "3_extruder",
    "4_dryer", "5_cooler", "6_coater", "7_packaging", "8_quality",
]
STAGE_LABELS = {
    "1_raw_materials":  "Raw Materials",
    "2_preconditioner": "Preconditioner",
    "3_extruder":       "Extruder",
    "4_dryer":          "Dryer",
    "5_cooler":         "Cooler",
    "6_coater":         "Coater",
    "7_packaging":      "Packaging",
    "8_quality":        "Quality Check",
}

app = dash.Dash(__name__, title="Pet Factory Digital Twin")
app.layout = html.Div(style={"background": BG, "minHeight": "100vh",
                              "fontFamily": "Inter, sans-serif", "color": TEXT,
                              "padding": "24px"}, children=[

    # ── Header ───────────────────────────────────────────────────────────────
    html.Div([
        html.H1("PET FACTORY — DIGITAL TWIN",
                style={"color": ACCENT, "margin": 0, "fontSize": "24px",
                       "fontWeight": "bold", "letterSpacing": "2px"}),
        html.P("Famsun 5 TPH · Benguerir, Morocco · Real-time Simulator",
               style={"color": SUBTEXT, "margin": "4px 0 0 0", "fontSize": "13px"}),
    ], style={**CARD_STYLE, "marginBottom": "24px"}),

    # ── Tabs ─────────────────────────────────────────────────────────────────
    dcc.Tabs(id="main-tabs", value="tab-sim",
             colors={"border": BLUE, "primary": ACCENT, "background": CARD_BG},
             style={"marginBottom": "16px"},
             children=[
        dcc.Tab(label="▶  Simulation",          value="tab-sim",
                style={"color": SUBTEXT, "background": BG},
                selected_style={"color": ACCENT, "background": CARD_BG,
                                "fontWeight": "bold"}),
        dcc.Tab(label="📊  Scenario Comparison", value="tab-compare",
                style={"color": SUBTEXT, "background": BG},
                selected_style={"color": ACCENT, "background": CARD_BG,
                                "fontWeight": "bold"}),
    ]),

    # ── Simulation tab content (rendered by callback) ────────────────────────
    html.Div(id="tab-content"),

    # ── Hidden elements always in DOM (needed by callbacks) ──────────────────
    html.Div([
        # Simulation tab controls
        html.Div(id="sim-tab-controls", children=[
            html.Div([
                html.H3("Environment & SKU", style={"color": ACCENT, "marginTop": 0}),
                html.Div([
                    html.Div([
                        html.Label("Ambient Temp (°C)", style={"color": SUBTEXT}),
                        dcc.Slider(id="temp-slider", min=5, max=45, step=1, value=25,
                                   marks={5:"5",15:"15",25:"25",35:"35",45:"45"},
                                   tooltip={"always_visible": True}),
                    ], style={"flex": "1", "marginRight": "24px"}),
                    html.Div([
                        html.Label("Relative Humidity (%)", style={"color": SUBTEXT}),
                        dcc.Slider(id="rh-slider", min=10, max=95, step=5, value=45,
                                   marks={10:"10",30:"30",50:"50",70:"70",90:"90"},
                                   tooltip={"always_visible": True}),
                    ], style={"flex": "1", "marginRight": "24px"}),
                    html.Div([
                        html.Label("SKU", style={"color": SUBTEXT}),
                        dcc.Dropdown(id="sku-dropdown",
                            options=[
                                {"label": "Standard Dry Kibble",  "value": "Standard Dry Kibble"},
                                {"label": "High-Protein Kibble",  "value": "High-Protein Kibble"},
                                {"label": "Senior Formula",       "value": "Senior Formula"},
                            ],
                            value="Standard Dry Kibble",
                            style={"background": CARD_BG, "color": TEXT,
                                   "border": f"1px solid {BLUE}"},
                        ),
                    ], style={"flex": "1"}),
                ], style={"display": "flex", "gap": "16px"}),
                html.Div([
                    html.Button("▶  Run Simulation", id="run-btn", n_clicks=0,
                                style={"background": BLUE, "color": TEXT, "border": "none",
                                       "padding": "10px 24px", "borderRadius": "6px",
                                       "fontSize": "14px", "fontWeight": "bold",
                                       "cursor": "pointer", "marginTop": "16px",
                                       "marginRight": "12px"}),
                    html.Button("⚙  Optimize Setpoints", id="opt-btn", n_clicks=0,
                                style={"background": ACCENT, "color": BG, "border": "none",
                                       "padding": "10px 24px", "borderRadius": "6px",
                                       "fontSize": "14px", "fontWeight": "bold",
                                       "cursor": "pointer", "marginTop": "16px"}),
                    html.Span(id="status-msg",
                              style={"color": SUBTEXT, "marginLeft": "16px",
                                     "fontSize": "13px", "verticalAlign": "middle"}),
                ]),
            ], style=CARD_STYLE),
            html.Div(id="kpi-row", style={"display": "flex", "gap": "12px",
                                           "flexWrap": "wrap", "marginBottom": "16px"}),
            html.Div([
                html.Div([dcc.Graph(id="stage-chart")], style={**CARD_STYLE, "flex": "2"}),
                html.Div([dcc.Graph(id="gauge-chart")], style={**CARD_STYLE, "flex": "1"}),
            ], style={"display": "flex", "gap": "16px"}),
            html.Div([dcc.Graph(id="temp-moisture-chart")], style=CARD_STYLE),
            html.Div(id="opt-result-div", style={**CARD_STYLE, "display": "none"}),
        ]),

        # Scenario comparison tab controls
        html.Div(id="compare-tab-controls", children=[
            html.Div([
                html.H3("Scenario Comparison", style={"color": ACCENT, "marginTop": 0}),
                html.Div([
                    html.Div([
                        html.Label("Scenario Group", style={"color": SUBTEXT}),
                        dcc.Dropdown(id="group-dropdown",
                            options=[{"label": g, "value": g}
                                     for g in SCENARIO_GROUPS],
                            value="Seasonal Weather",
                            style={"background": CARD_BG, "color": TEXT,
                                   "border": f"1px solid {BLUE}"},
                        ),
                    ], style={"flex": "1", "marginRight": "24px"}),
                    html.Div([
                        html.Label("Individual Scenarios", style={"color": SUBTEXT}),
                        dcc.Checklist(id="scenario-checklist",
                            options=[{"label": f"  {v['label']}", "value": k}
                                     for k, v in SCENARIOS.items()],
                            value=list(SCENARIO_GROUPS["Seasonal Weather"]),
                            labelStyle={"display": "block", "color": TEXT,
                                        "fontSize": "12px", "marginBottom": "4px"},
                        ),
                    ], style={"flex": "1"}),
                ], style={"display": "flex", "gap": "24px"}),
                html.Button("📊  Compare Scenarios", id="compare-btn", n_clicks=0,
                            style={"background": BLUE, "color": TEXT, "border": "none",
                                   "padding": "10px 24px", "borderRadius": "6px",
                                   "fontSize": "14px", "fontWeight": "bold",
                                   "cursor": "pointer", "marginTop": "16px"}),
                html.Span(id="compare-status",
                          style={"color": SUBTEXT, "marginLeft": "16px",
                                 "fontSize": "13px", "verticalAlign": "middle"}),
            ], style=CARD_STYLE),

            # Comparison charts
            html.Div([
                html.Div([dcc.Graph(id="cmp-moisture-chart")],
                         style={**CARD_STYLE, "flex": "1"}),
                html.Div([dcc.Graph(id="cmp-aw-chart")],
                         style={**CARD_STYLE, "flex": "1"}),
            ], style={"display": "flex", "gap": "16px"}),
            html.Div([
                html.Div([dcc.Graph(id="cmp-risk-chart")],
                         style={**CARD_STYLE, "flex": "1"}),
                html.Div([dcc.Graph(id="cmp-throughput-chart")],
                         style={**CARD_STYLE, "flex": "1"}),
            ], style={"display": "flex", "gap": "16px"}),
            html.Div([dcc.Graph(id="cmp-radar-chart")], style=CARD_STYLE),
        ]),

        dcc.Store(id="sim-store"),
        dcc.Store(id="opt-store"),
        dcc.Store(id="compare-store"),
    ], style={"display": "none"}),   # hidden wrapper — real content in tab-content
])


# ── Helpers ──────────────────────────────────────────────────────────────────
def make_kpi_card(label, value, unit="", ok=None):
    colour = (GREEN if ok is True else RED if ok is False else ACCENT)
    return html.Div([
        html.P(label, style={"color": SUBTEXT, "margin": 0, "fontSize": "11px"}),
        html.H2(f"{value}", style={"color": colour, "margin": "4px 0 0 0",
                                    "fontSize": "28px", "fontWeight": "bold"}),
        html.P(unit, style={"color": SUBTEXT, "margin": 0, "fontSize": "11px"}),
    ], style=KPI_STYLE)


# ── Callbacks ─────────────────────────────────────────────────────────────────
@callback(
    Output("sim-store", "data"),
    Output("status-msg", "children"),
    Input("run-btn", "n_clicks"),
    Input("temp-slider", "value"),
    Input("rh-slider", "value"),
    Input("sku-dropdown", "value"),
    prevent_initial_call=False,
)
def run_sim(n, temp, rh, sku_name):
    weather = WeatherState(dry_bulb_c=temp, relative_humidity=rh)
    sku     = SKU(name=sku_name)
    result  = run_simulation(weather=weather, sku=sku, verbose=False)
    return result, f"Simulation complete · {result['throughput_tph']:.2f} t/h"


@callback(
    Output("opt-store", "data"),
    Output("opt-result-div", "children"),
    Output("opt-result-div", "style"),
    Input("opt-btn", "n_clicks"),
    Input("temp-slider", "value"),
    Input("rh-slider", "value"),
    prevent_initial_call=True,
)
def run_opt(n, temp, rh):
    if not n:
        return {}, [], {"display": "none"}
    weather = WeatherState(dry_bulb_c=temp, relative_humidity=rh)
    result  = grid_search_optimize(weather=weather, verbose=False)
    if not result:
        return {}, html.P("No feasible solution found.", style={"color": RED}), CARD_STYLE

    sp = result["setpoints"]
    kp = result["kpis"]
    children = [
        html.H3("⚙ Optimal Setpoints", style={"color": ACCENT, "marginTop": 0}),
        html.Div([
            html.Div([
                html.P(f"Steam flow: {sp['steam_flow_kgph']} kg/h",   style={"color": TEXT}),
                html.P(f"Water flow: {sp['water_flow_kgph']} kg/h",   style={"color": TEXT}),
                html.P(f"Motor load: {sp['motor_load_frac']*100:.0f}%", style={"color": TEXT}),
            ], style={"flex": "1"}),
            html.Div([
                html.P(f"Dryer air: {sp['inlet_air_temp_c']} °C",      style={"color": TEXT}),
                html.P(f"Belt speed: {sp['belt_speed_frac']*100:.0f}%", style={"color": TEXT}),
                html.P(f"Fat addition: {sp['fat_addition_pct']}%",      style={"color": TEXT}),
            ], style={"flex": "1"}),
            html.Div([
                html.P(f"Profit: {kp['profit_mad_h']:.0f} MAD/h",       style={"color": GREEN}),
                html.P(f"Moisture: {kp['moisture_pct']:.2f}%",           style={"color": TEXT}),
                html.P(f"Status: {'✅ PASS' if kp['release_status']=='PASS' else '⛔ HOLD'}",
                       style={"color": GREEN if kp['release_status']=='PASS' else RED}),
            ], style={"flex": "1"}),
        ], style={"display": "flex", "gap": "24px"}),
    ]
    return result, children, CARD_STYLE


@callback(
    Output("kpi-row", "children"),
    Output("stage-chart", "figure"),
    Output("gauge-chart", "figure"),
    Output("temp-moisture-chart", "figure"),
    Input("sim-store", "data"),
)
def update_charts(data):
    if not data:
        empty = go.Figure()
        empty.update_layout(paper_bgcolor=BG, plot_bgcolor=BG)
        return [], empty, empty, empty

    # KPI cards
    kpis = [
        make_kpi_card("Throughput", f"{data['throughput_tph']:.2f}", "t/h"),
        make_kpi_card("Final Moisture", f"{data['final_moisture_pct']:.2f}", "%",
                      ok=data["moisture_ok"]),
        make_kpi_card("Water Activity aₓ", f"{data['final_aw']:.4f}", "limit 0.60",
                      ok=data["aw_ok"]),
        make_kpi_card("SME", f"{data['sme_kwh_t']:.1f}", "kWh/t"),
        make_kpi_card("Quality Risk", f"{data['quality_risk']:.3f}", "0=best",
                      ok=data["quality_risk"] < 0.35),
        make_kpi_card("Release", data["release_status"], "",
                      ok=data["release_status"] == "PASS"),
    ]

    # Stage chart — moisture & temperature by stage
    log = data.get("stage_log", {})
    stages, moistures, temps, flows = [], [], [], []
    for key in STAGE_ORDER:
        if key in log and isinstance(log[key], dict) and "moisture_pct" in log[key]:
            stages.append(STAGE_LABELS[key])
            moistures.append(log[key]["moisture_pct"])
            temps.append(log[key]["temperature_c"])
            flows.append(log[key]["mass_flow_kgph"])

    fig_stage = make_subplots(specs=[[{"secondary_y": True}]])
    fig_stage.add_trace(go.Bar(
        x=stages, y=moistures, name="Moisture (%)",
        marker_color=BLUE, opacity=0.85), secondary_y=False)
    fig_stage.add_trace(go.Scatter(
        x=stages, y=temps, name="Temperature (°C)",
        mode="lines+markers", line=dict(color=ACCENT, width=2),
        marker=dict(size=8)), secondary_y=True)
    fig_stage.update_layout(
        title="Moisture & Temperature Through Production Stages",
        paper_bgcolor=BG, plot_bgcolor=BG,
        font=dict(color=TEXT), legend=dict(bgcolor=CARD_BG),
        xaxis=dict(gridcolor="#1a2a3a"), yaxis=dict(gridcolor="#1a2a3a"),
    )
    fig_stage.update_yaxes(title_text="Moisture (%)", secondary_y=False, color=BLUE)
    fig_stage.update_yaxes(title_text="Temperature (°C)", secondary_y=True, color=ACCENT)

    # Gauge chart — quality risk
    qr = data["quality_risk"]
    gauge_color = GREEN if qr < 0.25 else ACCENT if qr < 0.5 else RED
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=round(qr, 4),
        title={"text": "Quality Risk Score", "font": {"color": TEXT}},
        delta={"reference": 0.35, "decreasing": {"color": GREEN}},
        gauge={
            "axis": {"range": [0, 1], "tickcolor": TEXT,
                     "tickfont": {"color": TEXT}},
            "bar":  {"color": gauge_color},
            "bgcolor": CARD_BG,
            "steps": [
                {"range": [0, 0.25],   "color": "#0a2a0a"},
                {"range": [0.25, 0.5], "color": "#2a2a0a"},
                {"range": [0.5, 1.0],  "color": "#2a0a0a"},
            ],
            "threshold": {
                "line": {"color": RED, "width": 3},
                "thickness": 0.75, "value": 0.35,
            },
        },
        number={"font": {"color": gauge_color, "size": 36}},
    ))
    fig_gauge.update_layout(
        paper_bgcolor=BG, font=dict(color=TEXT), height=300)

    # Flow chart — mass flow through stages
    fig_flow = go.Figure()
    fig_flow.add_trace(go.Scatter(
        x=stages, y=flows, name="Mass Flow (kg/h)",
        mode="lines+markers+text",
        line=dict(color=GREEN, width=2),
        marker=dict(size=10, color=GREEN),
        text=[f"{f:.0f}" for f in flows],
        textposition="top center",
        textfont=dict(color=GREEN, size=10),
    ))
    fig_flow.update_layout(
        title="Mass Flow Rate Through Production Stages (kg/h)",
        paper_bgcolor=BG, plot_bgcolor=BG,
        font=dict(color=TEXT), showlegend=False,
        xaxis=dict(gridcolor="#1a2a3a"),
        yaxis=dict(gridcolor="#1a2a3a", title="kg/h"),
    )

    return kpis, fig_stage, fig_gauge, fig_flow


# ── Tab router ───────────────────────────────────────────────────────────────
@callback(Output("tab-content", "children"), Input("main-tabs", "value"))
def render_tab(tab):
    if tab == "tab-sim":
        return html.Div([
            html.Div([
                html.H3("Environment & SKU", style={"color": ACCENT, "marginTop": 0}),
                html.Div([
                    html.Div([
                        html.Label("Ambient Temp (°C)", style={"color": SUBTEXT}),
                        dcc.Slider(id="temp-slider", min=5, max=45, step=1, value=25,
                                   marks={5:"5",15:"15",25:"25",35:"35",45:"45"},
                                   tooltip={"always_visible": True}),
                    ], style={"flex":"1","marginRight":"24px"}),
                    html.Div([
                        html.Label("Relative Humidity (%)", style={"color": SUBTEXT}),
                        dcc.Slider(id="rh-slider", min=10, max=95, step=5, value=45,
                                   marks={10:"10",30:"30",50:"50",70:"70",90:"90"},
                                   tooltip={"always_visible": True}),
                    ], style={"flex":"1","marginRight":"24px"}),
                    html.Div([
                        html.Label("SKU", style={"color": SUBTEXT}),
                        dcc.Dropdown(id="sku-dropdown",
                            options=[
                                {"label":"Standard Dry Kibble","value":"Standard Dry Kibble"},
                                {"label":"High-Protein Kibble","value":"High-Protein Kibble"},
                                {"label":"Senior Formula",     "value":"Senior Formula"},
                            ],
                            value="Standard Dry Kibble",
                            style={"background":CARD_BG,"color":TEXT,
                                   "border":f"1px solid {BLUE}"},
                        ),
                    ], style={"flex":"1"}),
                ], style={"display":"flex","gap":"16px"}),
                html.Div([
                    html.Button("▶  Run Simulation", id="run-btn", n_clicks=0,
                                style={"background":BLUE,"color":TEXT,"border":"none",
                                       "padding":"10px 24px","borderRadius":"6px",
                                       "fontSize":"14px","fontWeight":"bold",
                                       "cursor":"pointer","marginTop":"16px",
                                       "marginRight":"12px"}),
                    html.Button("⚙  Optimize Setpoints", id="opt-btn", n_clicks=0,
                                style={"background":ACCENT,"color":BG,"border":"none",
                                       "padding":"10px 24px","borderRadius":"6px",
                                       "fontSize":"14px","fontWeight":"bold",
                                       "cursor":"pointer","marginTop":"16px"}),
                    html.Span(id="status-msg",
                              style={"color":SUBTEXT,"marginLeft":"16px",
                                     "fontSize":"13px","verticalAlign":"middle"}),
                ]),
            ], style=CARD_STYLE),
            html.Div(id="kpi-row",
                     style={"display":"flex","gap":"12px","flexWrap":"wrap","marginBottom":"16px"}),
            html.Div([
                html.Div([dcc.Graph(id="stage-chart")], style={**CARD_STYLE,"flex":"2"}),
                html.Div([dcc.Graph(id="gauge-chart")], style={**CARD_STYLE,"flex":"1"}),
            ], style={"display":"flex","gap":"16px"}),
            html.Div([dcc.Graph(id="temp-moisture-chart")], style=CARD_STYLE),
            html.Div(id="opt-result-div", style={**CARD_STYLE,"display":"none"}),
        ])
    else:
        return html.Div([
            html.Div([
                html.H3("Scenario Comparison", style={"color": ACCENT, "marginTop": 0}),
                html.Div([
                    html.Div([
                        html.Label("Scenario Group", style={"color": SUBTEXT}),
                        dcc.Dropdown(id="group-dropdown",
                            options=[{"label":g,"value":g} for g in SCENARIO_GROUPS],
                            value="Seasonal Weather",
                            style={"background":CARD_BG,"color":TEXT,
                                   "border":f"1px solid {BLUE}"},
                        ),
                    ], style={"flex":"1","marginRight":"24px"}),
                    html.Div([
                        html.Label("Select Scenarios to Compare",
                                   style={"color": SUBTEXT, "marginBottom": "8px",
                                          "display": "block"}),
                        dcc.Checklist(id="scenario-checklist",
                            options=[{"label": f"  {v['label']}", "value": k}
                                     for k, v in SCENARIOS.items()],
                            value=list(SCENARIO_GROUPS["Seasonal Weather"]),
                            labelStyle={"display":"block","color":TEXT,
                                        "fontSize":"12px","marginBottom":"4px"},
                        ),
                    ], style={"flex":"1"}),
                ], style={"display":"flex","gap":"24px"}),
                html.Button("📊  Compare Scenarios", id="compare-btn", n_clicks=0,
                            style={"background":BLUE,"color":TEXT,"border":"none",
                                   "padding":"10px 24px","borderRadius":"6px",
                                   "fontSize":"14px","fontWeight":"bold",
                                   "cursor":"pointer","marginTop":"16px"}),
                html.Span(id="compare-status",
                          style={"color":SUBTEXT,"marginLeft":"16px",
                                 "fontSize":"13px","verticalAlign":"middle"}),
            ], style=CARD_STYLE),
            html.Div([
                html.Div([dcc.Graph(id="cmp-moisture-chart")],
                         style={**CARD_STYLE,"flex":"1"}),
                html.Div([dcc.Graph(id="cmp-aw-chart")],
                         style={**CARD_STYLE,"flex":"1"}),
            ], style={"display":"flex","gap":"16px"}),
            html.Div([
                html.Div([dcc.Graph(id="cmp-risk-chart")],
                         style={**CARD_STYLE,"flex":"1"}),
                html.Div([dcc.Graph(id="cmp-throughput-chart")],
                         style={**CARD_STYLE,"flex":"1"}),
            ], style={"display":"flex","gap":"16px"}),
            html.Div([dcc.Graph(id="cmp-radar-chart")], style=CARD_STYLE),
        ])


# ── Scenario comparison callback ──────────────────────────────────────────────
@callback(
    Output("compare-status",         "children"),
    Output("cmp-moisture-chart",     "figure"),
    Output("cmp-aw-chart",           "figure"),
    Output("cmp-risk-chart",         "figure"),
    Output("cmp-throughput-chart",   "figure"),
    Output("cmp-radar-chart",        "figure"),
    Input("compare-btn",             "n_clicks"),
    Input("scenario-checklist",      "value"),
    prevent_initial_call=False,
)
def compare_scenarios(n, selected_keys):
    selected_keys = selected_keys or list(SCENARIO_GROUPS["Seasonal Weather"])

    results = []
    for key in selected_keys:
        sc = SCENARIOS[key]
        sc["weather"].update_dew_point()
        r  = run_simulation(weather=sc["weather"], sku=sc["sku"], verbose=False)
        r["_label"] = sc["label"]
        r["_color"] = sc["color"]
        r["_key"]   = key
        results.append(r)

    labels  = [r["_label"] for r in results]
    colors  = [r["_color"] for r in results]

    def bar_fig(title, vals, spec_line=None, yaxis=""):
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=labels, y=vals, marker_color=colors,
            text=[f"{v:.2f}" for v in vals],
            textposition="outside", textfont=dict(color=TEXT, size=10),
        ))
        if spec_line is not None:
            fig.add_hline(y=spec_line, line_dash="dash",
                          line_color=RED, opacity=0.7,
                          annotation_text=f"Limit {spec_line}",
                          annotation_font_color=RED)
        fig.update_layout(
            title=title, paper_bgcolor=BG, plot_bgcolor=BG,
            font=dict(color=TEXT), showlegend=False,
            xaxis=dict(gridcolor="#1a2a3a", tickangle=-20),
            yaxis=dict(gridcolor="#1a2a3a", title=yaxis),
        )
        return fig

    fig_moist = bar_fig("Final Moisture (%)",
                        [r["final_moisture_pct"] for r in results],
                        spec_line=10.5, yaxis="%")
    # Add spec band
    fig_moist.add_hrect(y0=7.5, y1=10.5, fillcolor=ACCENT,
                        opacity=0.08, line_width=0, annotation_text="Spec band")

    fig_aw = bar_fig("Water Activity (aₓ)",
                     [r["final_aw"] for r in results],
                     spec_line=0.60, yaxis="aₓ")

    fig_risk = bar_fig("Quality Risk Score (0=best, 1=reject)",
                       [r["quality_risk"] for r in results],
                       spec_line=0.35, yaxis="Risk")

    fig_thru = bar_fig("Throughput (t/h)",
                       [r["throughput_tph"] for r in results],
                       yaxis="t/h")

    # Radar chart — multi-KPI profile per scenario
    kpi_names = ["Throughput", "Moisture\nSpec", "aₓ Safety",
                 "Low Risk", "SME\nEfficiency"]

    def normalise(vals, lo, hi, invert=False):
        out = [(v - lo) / (hi - lo + 1e-9) for v in vals]
        return [1 - v if invert else v for v in out]

    throughputs = normalise([r["throughput_tph"] for r in results], 3, 5.5)
    moist_score = [1 - abs(r["final_moisture_pct"] - 9.0) / 3.0 for r in results]
    aw_safety   = normalise([r["final_aw"] for r in results], 0, 0.6, invert=True)
    low_risk    = normalise([r["quality_risk"] for r in results], 0, 1, invert=True)
    sme_eff     = normalise([r["sme_kwh_t"] for r in results], 20, 130, invert=True)

    fig_radar = go.Figure()
    for i, r in enumerate(results):
        vals = [throughputs[i], moist_score[i], aw_safety[i],
                low_risk[i], sme_eff[i]]
        vals += [vals[0]]   # close polygon
        cats  = kpi_names + [kpi_names[0]]
        fig_radar.add_trace(go.Scatterpolar(
            r=vals, theta=cats, name=r["_label"],
            fill="toself", opacity=0.55,
            line=dict(color=r["_color"], width=2),
        ))
    fig_radar.update_layout(
        title="Multi-KPI Scenario Profile (normalised 0–1, higher=better)",
        polar=dict(
            bgcolor=CARD_BG,
            radialaxis=dict(visible=True, range=[0,1], color=SUBTEXT,
                            gridcolor="#2a3a4a"),
            angularaxis=dict(color=TEXT, gridcolor="#2a3a4a"),
        ),
        paper_bgcolor=BG, font=dict(color=TEXT),
        legend=dict(bgcolor=CARD_BG, bordercolor=BLUE),
    )

    status = f"Compared {len(results)} scenarios"
    return status, fig_moist, fig_aw, fig_risk, fig_thru, fig_radar


if __name__ == "__main__":
    print("\n  Pet Factory Digital Twin Dashboard")
    print("  Open: http://127.0.0.1:8050\n")
    app.run(debug=False, port=8050)
