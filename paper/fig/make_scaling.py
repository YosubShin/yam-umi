#!/usr/bin/env python3
"""Fig. 3: validation loss on the robot's held-out episodes vs training-set size,
both observation arms. Reads the pilot's val-curve CSVs (best checkpoint per
run) so the figure tracks the data. Run from anywhere:

  python fig/make_scaling.py          # writes fig/scaling.pdf and .png
"""
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

E8 = Path.home() / "co/pilot/e8"
OUT = Path(__file__).resolve().parent


def best(csv_paths, run):
    """Minimum val_loss over checkpoints for `run` across the given CSVs, or None."""
    m = None
    for p in csv_paths:
        if not p.exists():
            continue
        for r in csv.DictReader(open(p)):
            if r["run"] == run and r["val_loss"] not in ("", "NA"):
                v = float(r["val_loss"]); m = v if m is None else min(m, v)
    return m


R7, SC, GV = E8 / "round7_val_curves.csv", E8 / "scaling_curves.csv", E8 / "glove_val_curves.csv"
ALL = [R7, SC, GV]

# series: label -> [(episodes, run)]; values resolved from the CSVs
ARMS = {
    "forward + fovea observations": {
        "teleop, ground-truth labels": [(50, "scale50_Cf"), (100, "scale100_Cf"), (185, "all7_Cf_act50")],
        "teleop, fiducial labels": [(50, "scale50_Bj"), (100, "scale100_Bj"), (185, "all7_Bj_act50")],
        "glove, native pace": [(50, "glove50_Bj_act50@robotval"), (100, "glove100_Bj_act50@robotval"), (165, "glove_Bj_act50@robotval")],
        "glove, paced": [(165, "glove_Bj_s_act50@robotval")],
        "teleop 185 + glove 165 (paced)": [(350, "mix_Bj_s_act50@robotval")],
        "teleop 92 + glove 93 (native)": [(185, "budget185_mix_Bj_act50@robotval")],
    },
    "wrist fisheye observations": {
        "teleop, ground-truth labels": [(185, "all7_Cw_act50")],
        "teleop, fiducial labels": [(50, "scale50_Aj"), (100, "scale100_Aj"), (185, "all7_Aj_act50")],
        "glove, native pace": [(50, "glove50_Aj_act50@robotval"), (100, "glove100_Aj_act50@robotval"), (165, "glove_Aj_act50@robotval")],
        "glove, paced": [(165, "glove_Aj_s_act50@robotval")],
        "teleop 185 + glove 165 (paced)": [(350, "mix_Aj_s_act50@robotval")],
        "teleop 92 + glove 93 (paced)": [(185, "dilute92_Aj_s_act50@robotval")],
        "teleop 46 + glove 139 (paced)": [(185, "dilute46_Aj_s_act50@robotval")],
    },
}
STYLE = {  # label -> (marker, colour, linestyle, filled)
    "teleop, ground-truth labels": ("o", "tab:blue", "-", True),
    "teleop, fiducial labels": ("s", "tab:orange", "-", True),
    "glove, native pace": ("^", "tab:green", "--", False),
    "glove, paced": ("^", "tab:green", "", True),
    "teleop 185 + glove 165 (paced)": ("D", "black", "", True),
    "teleop 92 + glove 93 (paced)": ("D", "black", "", False),
    "teleop 92 + glove 93 (native)": ("D", "grey", "", False),
    "teleop 46 + glove 139 (paced)": ("v", "black", "", False),
}

plt.rcParams.update({"font.size": 7, "axes.titlesize": 7.5, "legend.fontsize": 6.2, "xtick.labelsize": 6.5, "ytick.labelsize": 6.5})
fig, axes = plt.subplots(1, 2, figsize=(5.6, 2.25), sharey=True)
handles = {}
for ax, (title, series) in zip(axes, ARMS.items()):
    for label, pts in series.items():
        xy = [(n, best(ALL, run)) for n, run in pts]
        xy = [(n, v) for n, v in xy if v is not None]
        if not xy:
            continue
        mk, col, ls, filled = STYLE[label]
        xs, ys = zip(*xy)
        h, = ax.plot(xs, ys, marker=mk, color=col, linestyle=ls or "none", markersize=5, linewidth=1.2,
                     markerfacecolor=col if filled else "white", markeredgecolor=col, label=label)
        handles.setdefault(label, h)
    ax.set_title(title); ax.set_xlabel("training episodes"); ax.set_xticks([50, 100, 185, 350])
    ax.grid(alpha=0.3)
axes[0].set_ylabel("val loss on robot episodes")
order = ["teleop, ground-truth labels", "teleop, fiducial labels", "glove, native pace", "glove, paced",
         "teleop 185 + glove 165 (paced)", "teleop 92 + glove 93 (paced)", "teleop 92 + glove 93 (native)", "teleop 46 + glove 139 (paced)"]
fig.legend([handles[k] for k in order if k in handles], [k for k in order if k in handles],
           loc="upper center", bbox_to_anchor=(0.5, 0.0), ncol=4, frameon=False, handletextpad=0.4, columnspacing=1.0)
fig.tight_layout()
fig.savefig(OUT / "scaling.pdf", bbox_inches="tight"); fig.savefig(OUT / "scaling.png", dpi=200, bbox_inches="tight")
for title, series in ARMS.items():
    print(title)
    for label, pts in series.items():
        print(f"  {label:34s}", [(n, round(best(ALL, run), 3) if best(ALL, run) is not None else None) for n, run in pts])
