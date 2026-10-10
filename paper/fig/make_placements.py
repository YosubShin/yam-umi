#!/usr/bin/env python3
"""Fig. 4: the rollout placements over the forward camera's view.

Each disc is one placement: the number inside is successes over all policies
and repeats (n/10), the colour encodes the same count (red 0 .. green 10), and
the arrow points to that scene's bin.

  python fig/make_placements.py    # writes fig/placements.png
"""
import json
from pathlib import Path

import cv2
import numpy as np

G = Path.home() / "co/pilot/rollout_logs/grid_final"
OUT = Path(__file__).resolve().parent / "placements.png"

rs = [json.loads(l) for l in open(G / "trials.jsonl")]
names = list(dict.fromkeys(r["policy"] for r in rs))
geo = {int(k): v for k, v in json.load(open(G / "scene_geometry.json")).items()}

x0, y0, x1, y1 = 380, 40, 1700, 1080                 # table region of the 1920x1080 frame
im = cv2.imread(str(G / "scene2_ref.png"))[y0:y1, x0:x1].copy()
im = cv2.addWeighted(im, 0.45, np.full_like(im, 255), 0.55, 0)   # washed-out background


def col(k):  # k successes of 10 -> red .. green (BGR)
    t = k / 10
    return (int(40 + 40 * (1 - t)), int(60 + 180 * t), int(230 * (1 - t) + 30 * t))


for s, g in sorted(geo.items()):
    b = np.array(g["block"]) - [x0, y0]; c = np.array(g["bin"]) - [x0, y0]
    cv2.arrowedLine(im, tuple(b.astype(int)), tuple(c.astype(int)), (120, 120, 120), 2, cv2.LINE_AA, tipLength=0.04)
for s, g in sorted(geo.items()):
    b = np.array(g["block"]) - [x0, y0]
    n_ok = sum(r["outcome"] == "success" for r in rs if r["scene"] == s)
    k = n_ok
    n_all = sum(1 for r in rs if r["scene"] == s)
    cv2.circle(im, tuple(b.astype(int)), 34, col(k), -1, cv2.LINE_AA)
    cv2.circle(im, tuple(b.astype(int)), 34, (255, 255, 255), 2, cv2.LINE_AA)
    txt = f"{n_ok}/{n_all}"
    (tw, th), _ = cv2.getTextSize(txt, cv2.FONT_HERSHEY_SIMPLEX, 0.62, 2)
    cv2.putText(im, txt, (int(b[0]) - tw // 2, int(b[1]) + th // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.62, (255, 255, 255), 2, cv2.LINE_AA)

# legend
for i, k in enumerate(range(0, 11, 2)):
    cv2.circle(im, (40 + i * 46, 36), 16, col(k), -1); cv2.putText(im, str(k), (30 + i * 46, 42), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(im, "successes of 10 at the placement (all policies, both repeats);  arrow: block -> bin",
            (330, 42), cv2.FONT_HERSHEY_SIMPLEX, 0.52, (30, 30, 30), 1, cv2.LINE_AA)
cv2.putText(im, "robot base", (20, 1020), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (30, 30, 30), 2, cv2.LINE_AA)
cv2.imwrite(str(OUT), im)
print(OUT, im.shape)


# ---- Fig. 4 right half: the alignment "ghost" view the harness shows before every trial ----
# A live forward frame captured by the viewer during an alignment prompt (saved Rerun recording),
# blended 50/50 with that scene's reference, and the per-pixel misalignment image.
import sys
RRD = Path("/mnt/nvme/data.rrd"); T_PICK, SCENE_PICK = 1791587338, 15   # scene 15, block being slid onto the ghost
if RRD.exists():
    from rerun.experimental import RrdReader
    live = None
    for ch in RrdReader(str(RRD)).stream().filter(content="/live/forward"):
        rb = ch.to_record_batch()
        for t, b in zip(rb.column("log_time").to_pylist(), rb.column("EncodedImage:blob")):
            if int(t.timestamp()) == T_PICK and live is None:
                live = cv2.imdecode(np.asarray(b.as_py()[0], np.uint8), cv2.IMREAD_COLOR)
    if live is not None:
        ref = cv2.resize(cv2.imread(str(G / f"scene{SCENE_PICK}_ref.png")), (live.shape[1], live.shape[0]))
        blend = cv2.addWeighted(live, 0.5, ref, 0.5, 0)
        diff = cv2.cvtColor(cv2.absdiff(live, ref).max(axis=2), cv2.COLOR_GRAY2BGR)
        for img, txt in ((blend, "live + reference (50/50)"), (diff, "misalignment")):
            cv2.putText(img, txt, (14, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 4, cv2.LINE_AA)
            cv2.putText(img, txt, (14, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA)
        right = np.vstack([blend, np.full((8, blend.shape[1], 3), 255, np.uint8), diff])
        H = im.shape[0]; right = cv2.resize(right, (int(right.shape[1] * H / right.shape[0]), H), interpolation=cv2.INTER_AREA)
        both = np.hstack([im, np.full((H, 14, 3), 255, np.uint8), right])
        cv2.imwrite(str(OUT.with_name("rollout_protocol.png")), both)
        print(OUT.with_name("rollout_protocol.png"), both.shape)
    else:
        print("ghost frame not found in the recording", file=sys.stderr)
