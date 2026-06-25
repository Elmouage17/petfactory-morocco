"""
Pet Factory — 5 TPH Production Line
PFD/P&ID-style Block Diagram (Digital Twin)
Benguerir, Morocco
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import matplotlib.patheffects as pe

# ── Colour palette ──────────────────────────────────────────────────────────
CLR = {
    "block":    "#1B3A5C",   # dark navy — unit operation boxes
    "block_hl": "#2E6DA4",   # highlighted block
    "txt":      "#FFFFFF",
    "arrow":    "#F0A500",   # material flow
    "steam":    "#E74C3C",   # steam / heat
    "air":      "#2ECC71",   # air streams
    "elec":     "#9B59B6",   # electrical / control
    "bg":       "#0D1B2A",
    "title":    "#F0A500",
    "sub":      "#A8C8E8",
    "border":   "#2E6DA4",
}

# ── Stage definitions ────────────────────────────────────────────────────────
STAGES = [
    {
        "id": 1, "label": "1 · RAW MATERIAL\nRECEPTION & STORAGE",
        "detail": "Drum Precleaner 40 t/h\nPermanent Magnet ≥0.3T\n200T Steel Silo · 14 Surge Bins\nLevel & Temp Monitoring",
        "inputs":  ["Bulk grains\nProteins · Meals"],
        "outputs": ["Cleaned &\nStaged Materials"],
        "x": 0.05, "y": 0.72,
    },
    {
        "id": 2, "label": "2 · GRINDING",
        "detail": "Hammermill 200 kW · 3000 RPM\n6–7 t/h · VFD feed control\nPlan Sifter · Dust Collector\nΔP trigger: 0.5–0.7 MPa",
        "inputs":  [],
        "outputs": ["Ground Meal\n(uniform powder)"],
        "x": 0.05, "y": 0.45,
    },
    {
        "id": 3, "label": "3 · DOSING & MIXING",
        "detail": "Batch Scale 1000 kg · 500 kg\nLoad cells ≤±0.3% accuracy\nPaddle Mixer CV ≤5%\nMix time: 45–60 s/batch",
        "inputs":  ["Micro-ingredients\n(vitamins/minerals)"],
        "outputs": ["Homogeneous\nDry Mix"],
        "x": 0.05, "y": 0.18,
    },
    {
        "id": 4, "label": "4 · PRECONDITIONING\n& EXTRUSION",
        "detail": "Twin-Screw Extruder SJPS165 · 203 kW\nConditioner 22 kW · 2–4 min residence\nSteam: 0.1–0.4 MPa · Water: 1600 kg/h\nBarrel 130–160°C · 20–40 bar · SME 80–120 kWh/t",
        "inputs":  ["Steam 16 bar\n700 kg/h", "Water\n1600 kg/h", "Meat Slurry\n3–33 L/min"],
        "outputs": ["Hot Wet Kibble\n25–30% moisture"],
        "x": 0.38, "y": 0.18,
    },
    {
        "id": 5, "label": "5 · DRYING",
        "detail": "Belt Dryer GZDH2200×2-8 · 62 kW\n2-layer belt · 4 drying zones\nAir temp 120–160°C\nTarget moisture 8–10% (aᵥᵥ < 0.6)",
        "inputs":  ["Steam\n180–220 kg/t"],
        "outputs": ["Dried Kibble\n8–10% moisture"],
        "x": 0.38, "y": 0.45,
    },
    {
        "id": 6, "label": "6 · COOLING",
        "detail": "Counterflow Cooler · 6–7 t/h\nCooling fan 22 kW · 11,580 m³/h\nTime: 10–15 min\nDischarge: T_ambient + 3–5°C",
        "inputs":  ["Ambient Air"],
        "outputs": ["Stabilised Kibble"],
        "x": 0.38, "y": 0.72,
    },
    {
        "id": 7, "label": "7 · VACUUM COATING",
        "detail": "Double-Shaft Vacuum Coater 2000L\nVacuum: 100 mbar\nFats/Oils: 6–36% addition\nBatch cycle: 300 s",
        "inputs":  ["Heated Fats/Oils\n160 L/min", "Palatants\n& Pigments"],
        "outputs": ["Coated Kibble"],
        "x": 0.70, "y": 0.72,
    },
    {
        "id": 8, "label": "8 · PACKAGING\n& FINISHED GOODS",
        "detail": "4 × Finished Bins 40 m³ each\n14-head weigher · Linear Screen\nBagging: 400g–25kg\nRoom: 18–22°C · 40–50% RH",
        "inputs":  [],
        "outputs": ["Sealed Retail\nBags"],
        "x": 0.70, "y": 0.45,
    },
]

# ── Main flow connections (from_id → to_id) ──────────────────────────────────
MAIN_FLOW = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]

# ── Box dimensions ────────────────────────────────────────────────────────────
BW, BH = 0.23, 0.22   # box width / height (figure-fraction units)

fig, ax = plt.subplots(figsize=(22, 14))
fig.patch.set_facecolor(CLR["bg"])
ax.set_facecolor(CLR["bg"])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")


def box_center(stage):
    return stage["x"] + BW / 2, stage["y"] + BH / 2


def draw_block(ax, stage, highlight=False):
    x, y = stage["x"], stage["y"]
    fc = CLR["block_hl"] if highlight else CLR["block"]

    # Outer glow
    glow = FancyBboxPatch((x - 0.003, y - 0.003), BW + 0.006, BH + 0.006,
                           boxstyle="round,pad=0.01", linewidth=0,
                           facecolor=CLR["border"], alpha=0.5, zorder=2)
    ax.add_patch(glow)

    # Main box
    box = FancyBboxPatch((x, y), BW, BH,
                          boxstyle="round,pad=0.01", linewidth=1.5,
                          edgecolor=CLR["border"], facecolor=fc, zorder=3)
    ax.add_patch(box)

    cx, cy = x + BW / 2, y + BH / 2

    # Stage label
    ax.text(cx, cy + 0.04, stage["label"], ha="center", va="center",
            fontsize=8.5, fontweight="bold", color=CLR["txt"],
            zorder=4, linespacing=1.4)

    # Detail text
    ax.text(cx, cy - 0.055, stage["detail"], ha="center", va="center",
            fontsize=6.2, color=CLR["sub"], zorder=4, linespacing=1.4)

    # Stage number badge
    badge = plt.Circle((x + 0.018, y + BH - 0.018), 0.016,
                        color=CLR["title"], zorder=5)
    ax.add_patch(badge)
    ax.text(x + 0.018, y + BH - 0.018, str(stage["id"]),
            ha="center", va="center", fontsize=7, fontweight="bold",
            color=CLR["bg"], zorder=6)


def arrow(ax, x0, y0, x1, y1, color=CLR["arrow"], lw=2, label="", style="->"):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                 arrowprops=dict(arrowstyle=style, color=color,
                                 lw=lw, connectionstyle="arc3,rad=0.0"),
                 zorder=7)
    if label:
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        ax.text(mx, my + 0.012, label, ha="center", va="bottom",
                fontsize=6, color=color, zorder=8,
                bbox=dict(boxstyle="round,pad=0.15", fc=CLR["bg"],
                           ec=color, alpha=0.85, lw=0.8))


# ── Draw all blocks ──────────────────────────────────────────────────────────
stage_map = {s["id"]: s for s in STAGES}
for s in STAGES:
    draw_block(ax, s)

# ── Main material flow arrows ─────────────────────────────────────────────────
flow_labels = {
    (1, 2): "Chain Conv.\n55–90 m³/h",
    (2, 3): "Screw Conv.\n30 m³/h",
    (3, 4): "Dry Mix Feed",
    (4, 5): "Wet Kibble\n25–30% H₂O",
    (5, 6): "Dried Kibble\n8–10% H₂O",
    (6, 7): "Cooled Kibble\nT_amb+3–5°C",
    (7, 8): "Coated Kibble",
}

for (fid, tid) in MAIN_FLOW:
    fs, ts = stage_map[fid], stage_map[tid]
    fx, fy = box_center(fs)
    tx, ty = box_center(ts)

    # Vertical flows (same column)
    if abs(fs["x"] - ts["x"]) < 0.05:
        if fy > ty:  # downward
            arrow(ax, fx, fs["y"], tx, ts["y"] + BH + 0.005,
                  label=flow_labels.get((fid, tid), ""))
        else:        # upward
            arrow(ax, fx, fs["y"] + BH, tx, ts["y"] - 0.005,
                  label=flow_labels.get((fid, tid), ""))
    else:
        # Horizontal: right column feed from stage 3 → 4
        arrow(ax, fs["x"] + BW + 0.005, fy, ts["x"] - 0.005, ty,
              label=flow_labels.get((fid, tid), ""))

# ── Special connector: Stage 6 (top-left area) → Stage 7 (top-right) ─────────
# Stage 6 is at x=0.38, y=0.72 and Stage 7 is at x=0.70, y=0.72 — same row
s6, s7 = stage_map[6], stage_map[7]
arrow(ax, s6["x"] + BW + 0.005, s6["y"] + BH / 2,
      s7["x"] - 0.005, s7["y"] + BH / 2,
      label=flow_labels.get((6, 7), ""))

# ── Stage 7 → 8 (downward in right column) ────────────────────────────────────
s8 = stage_map[8]
arrow(ax, s7["x"] + BW / 2, s7["y"],
      s8["x"] + BW / 2, s8["y"] + BH + 0.005,
      label=flow_labels.get((7, 8), ""))

# ── Utility streams ───────────────────────────────────────────────────────────
# Steam to Extruder (stage 4)
s4 = stage_map[4]
arrow(ax, s4["x"] - 0.06, s4["y"] + BH / 2 + 0.05,
      s4["x"] - 0.005, s4["y"] + BH / 2 + 0.05,
      color=CLR["steam"], lw=1.5, label="Steam 16 bar")
ax.text(s4["x"] - 0.115, s4["y"] + BH / 2 + 0.05, "BOILER",
        ha="center", va="center", fontsize=6.5, color=CLR["steam"],
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.2", fc=CLR["bg"],
                   ec=CLR["steam"], lw=1))

# Steam to Dryer (stage 5)
s5 = stage_map[5]
arrow(ax, s5["x"] - 0.06, s5["y"] + BH / 2,
      s5["x"] - 0.005, s5["y"] + BH / 2,
      color=CLR["steam"], lw=1.5, label="Steam\n180–220 kg/t")

# Air to Cooler (stage 6)
s6 = stage_map[6]
arrow(ax, s6["x"] - 0.06, s6["y"] + BH / 2,
      s6["x"] - 0.005, s6["y"] + BH / 2,
      color=CLR["air"], lw=1.5, label="Ambient Air\n11,580 m³/h")

# Exhaust air from dryer
arrow(ax, s5["x"] + BW / 2, s5["y"] + BH + 0.005,
      s5["x"] + BW / 2, s5["y"] + BH + 0.055,
      color=CLR["air"], lw=1.2, label="Exhaust\nAir + Moisture")

# ── SCADA/MYCOS overlay bar ───────────────────────────────────────────────────
scada_box = FancyBboxPatch((0.02, 0.005), 0.96, 0.06,
                             boxstyle="round,pad=0.01", linewidth=1,
                             edgecolor=CLR["elec"], facecolor="#0D1B2A",
                             alpha=0.9, zorder=2)
ax.add_patch(scada_box)
ax.text(0.5, 0.035, "MYCOS / FIMCOS  ·  MES/SCADA Automation Layer  ·  "
        "PLCs · VFDs · Steam Proportional Valves · Thermal Sensors · "
        "PostgreSQL Historian  →  Python Digital Twin Engine  →  Plotly/Dash Dashboard",
        ha="center", va="center", fontsize=6.8, color=CLR["elec"],
        fontweight="bold", zorder=3)

# ── Legend ────────────────────────────────────────────────────────────────────
legend_items = [
    mpatches.Patch(color=CLR["arrow"], label="Material Flow"),
    mpatches.Patch(color=CLR["steam"], label="Steam / Heat"),
    mpatches.Patch(color=CLR["air"],   label="Air Stream"),
    mpatches.Patch(color=CLR["elec"],  label="Control / SCADA"),
]
ax.legend(handles=legend_items, loc="lower right",
          bbox_to_anchor=(0.98, 0.09), fontsize=7.5,
          framealpha=0.3, facecolor=CLR["bg"],
          edgecolor=CLR["border"], labelcolor=CLR["txt"])

# ── Title ─────────────────────────────────────────────────────────────────────
ax.text(0.5, 0.965,
        "PET FACTORY — 5 TPH PRODUCTION LINE  |  PFD / P&ID Block Diagram",
        ha="center", va="center", fontsize=14, fontweight="bold",
        color=CLR["title"], zorder=10)
ax.text(0.5, 0.945,
        "Famsun · Benguerir, Morocco  |  Digital Twin v1.0",
        ha="center", va="center", fontsize=9, color=CLR["sub"], zorder=10)

plt.tight_layout(pad=0.5)
plt.savefig("/Users/samaribi/Documents/Pet factory /digital_twin_pfd.png",
            dpi=180, bbox_inches="tight", facecolor=CLR["bg"])
plt.show()
print("PFD saved to: /Users/samaribi/Documents/Pet factory /digital_twin_pfd.png")
