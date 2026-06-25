"""
Pet Factory Digital Twin — Scenario Comparison CLI

Usage:
    python compare.py                          # all scenarios
    python compare.py --group "Seasonal Weather"
    python compare.py --group "SKU Comparison"
    python compare.py --png                    # save chart to PNG
"""
import argparse, sys, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from simulator import run_simulation
from scenarios import SCENARIOS, SCENARIO_GROUPS

BG      = "#0D1B2A"
CARD    = "#1B3A5C"
ACCENT  = "#F0A500"
TEXT    = "#FFFFFF"
SUBTEXT = "#A8C8E8"
GREEN   = "#2ECC71"
RED     = "#E74C3C"


def run_all(group: str | None = None) -> dict[str, dict]:
    keys = SCENARIO_GROUPS.get(group, list(SCENARIOS)) if group else list(SCENARIOS)
    results = {}
    for key in keys:
        sc = SCENARIOS[key]
        sc["weather"].update_dew_point()
        r = run_simulation(weather=sc["weather"], sku=sc["sku"], verbose=False)
        r["_label"] = sc["label"]
        r["_color"] = sc["color"]
        results[key] = r
    return results


def print_table(results: dict):
    SEP = "─" * 95
    print(f"\n{'═'*95}")
    print(f"  {'SCENARIO':<28} {'Throughput':>10} {'Moisture':>10} {'aₓ':>8} "
          f"{'SME':>9} {'Risk':>8} {'Status':>8}")
    print(SEP)
    for key, r in results.items():
        status_sym = "✅ PASS" if r["release_status"] == "PASS" else "⛔ HOLD"
        print(f"  {r['_label']:<28} {r['throughput_tph']:>9.3f}t "
              f"{r['final_moisture_pct']:>9.2f}%  "
              f"{r['final_aw']:>7.4f}  "
              f"{r['sme_kwh_t']:>7.1f}  "
              f"{r['quality_risk']:>7.4f}  {status_sym}")
    print(f"{'═'*95}\n")


def plot_comparison(results: dict, save_path: str | None = None):
    scenarios = list(results.values())
    labels    = [s["_label"] for s in scenarios]
    colors    = [s["_color"] for s in scenarios]
    n         = len(scenarios)
    x         = np.arange(n)
    bar_w     = 0.55

    fig, axes = plt.subplots(2, 3, figsize=(20, 11))
    fig.patch.set_facecolor(BG)
    fig.suptitle("Pet Factory Digital Twin — Scenario Comparison",
                 fontsize=15, fontweight="bold", color=ACCENT, y=0.98)

    panels = [
        (axes[0,0], "Throughput (t/h)",     [s["throughput_tph"]      for s in scenarios], None,     None),
        (axes[0,1], "Final Moisture (%)",    [s["final_moisture_pct"]  for s in scenarios], (7.5,10.5),"#F0A500"),
        (axes[0,2], "Water Activity aₓ",    [s["final_aw"]            for s in scenarios], (0,0.60), "#E74C3C"),
        (axes[1,0], "SME (kWh/t)",          [s["sme_kwh_t"]           for s in scenarios], (80,120), "#9B59B6"),
        (axes[1,1], "Quality Risk Score",   [s["quality_risk"]        for s in scenarios], (0,0.35), "#E74C3C"),
        (axes[1,2], "Release Status",       [1 if s["release_status"]=="PASS" else 0
                                             for s in scenarios],       None,     None),
    ]

    for ax, title, vals, spec_range, spec_color in panels:
        ax.set_facecolor(CARD)
        ax.spines[:].set_color(SUBTEXT)
        ax.tick_params(colors=TEXT, labelsize=8)
        ax.set_title(title, color=ACCENT, fontsize=10, fontweight="bold", pad=8)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=22, ha="right", fontsize=7.5, color=TEXT)
        ax.yaxis.label.set_color(TEXT)

        if title == "Release Status":
            bar_colors = [GREEN if v == 1 else RED for v in vals]
            ax.bar(x, vals, width=bar_w, color=bar_colors, edgecolor=BG, linewidth=0.5)
            ax.set_yticks([0, 1])
            ax.set_yticklabels(["HOLD", "PASS"], color=TEXT)
            for i, v in enumerate(vals):
                ax.text(i, v + 0.03, "PASS" if v else "HOLD",
                        ha="center", va="bottom", fontsize=8,
                        color=GREEN if v else RED, fontweight="bold")
        else:
            bars = ax.bar(x, vals, width=bar_w, color=colors,
                          edgecolor=BG, linewidth=0.5, alpha=0.9)
            # Value labels on bars
            for bar, val in zip(bars, vals):
                ax.text(bar.get_x() + bar.get_width()/2,
                        bar.get_height() + max(vals)*0.01,
                        f"{val:.2f}", ha="center", va="bottom",
                        fontsize=7.5, color=TEXT, fontweight="bold")

        # Spec band
        if spec_range:
            ax.axhspan(spec_range[0], spec_range[1],
                       alpha=0.12, color=spec_color, zorder=0)
            ax.axhline(spec_range[0], color=spec_color, lw=1, ls="--", alpha=0.6)
            ax.axhline(spec_range[1], color=spec_color, lw=1, ls="--", alpha=0.6)

        ax.grid(axis="y", color="#1a2a3a", lw=0.5, zorder=0)

    # Legend — spec bands
    legend_items = [mpatches.Patch(color="#F0A500", alpha=0.3, label="Moisture spec band"),
                    mpatches.Patch(color="#E74C3C", alpha=0.3, label="aₓ / Risk limit"),
                    mpatches.Patch(color="#9B59B6", alpha=0.3, label="Target SME range")]
    fig.legend(handles=legend_items, loc="lower center", ncol=3,
               framealpha=0.3, facecolor=BG, edgecolor=SUBTEXT,
               labelcolor=TEXT, fontsize=8, bbox_to_anchor=(0.5, 0.01))

    plt.tight_layout(rect=[0, 0.05, 1, 0.97])

    out = save_path or "/Users/samaribi/Documents/Pet factory /scenario_comparison.png"
    plt.savefig(out, dpi=160, bbox_inches="tight", facecolor=BG)
    print(f"  Chart saved → {out}")
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pet Factory Scenario Comparison")
    parser.add_argument("--group", type=str, default=None,
                        help=f"Scenario group: {list(SCENARIO_GROUPS)}")
    parser.add_argument("--png",   action="store_true", help="Save PNG chart")
    parser.add_argument("--list",  action="store_true", help="List available scenarios")
    args = parser.parse_args()

    if args.list:
        for g, keys in SCENARIO_GROUPS.items():
            print(f"\n  {g}:")
            for k in keys:
                print(f"    {k:<22} — {SCENARIOS[k]['label']}")
        sys.exit(0)

    group = args.group
    print(f"\n  Running {'all' if not group else repr(group)} scenarios…")
    results = run_all(group)
    print_table(results)

    if args.png or True:   # always generate chart
        plot_comparison(results)
