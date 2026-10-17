#!/usr/bin/env python3
"""Rollout figure: one scene, the four camera arms (2, 5, 7, 8), four moments each, from the fixed
workspace camera (recorded by eval_grid since scene 15) with the policy's own view inset.

  python fig/make_rollouts.py [scene]      # writes fig/rollouts.jpg (default scene 16)
"""
import glob, json, sys
from pathlib import Path
import cv2, numpy as np

G = Path.home() / "co/pilot/rollout_logs/grid_20261016"
OUT = Path(__file__).resolve().parent / "rollouts.jpg"
SC = int(sys.argv[1]) if len(sys.argv) > 1 else 16
ARMS = [("mix_gHs3", "2  device (head camera)"), ("mix_FA", "5  wrist-camera UMI"), ("mix_FB", "7  fixed camera"), ("mix_gHA", "8  head labels, wrist view")]
TIMES = [2, 6, 10, 14]
NICE = {"success": "success", "no_grasp": "no grasp", "dropped_before_bin": "dropped during the carry", "dropped_at_bin": "dropped at the bin", "timeout": "timeout"}
R = {(r["policy"], r["scene"]): r for r in map(json.loads, open(G / "trials.jsonl"))}

def frame_at(path, t, fps):
    cap = cv2.VideoCapture(path); n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); cap.set(cv2.CAP_PROP_POS_FRAMES, min(int(t * fps), n - 1)); ok, im = cap.read(); return im

def label(im, text, org, scale, thick=2):
    cv2.putText(im, text, org, cv2.FONT_HERSHEY_DUPLEX, scale, (255, 255, 255), thick + 3, cv2.LINE_AA)
    cv2.putText(im, text, org, cv2.FONT_HERSHEY_DUPLEX, scale, (20, 20, 20), thick, cv2.LINE_AA)

rows = []
for n, name in ARMS:
    w = glob.glob(str(G / f"{n}_S{SC}r0_*_world.mp4"))[0]; p = [x for x in glob.glob(str(G / f"{n}_S{SC}r0_*.mp4")) if "world" not in x][0]
    row = []
    for t in TIMES:
        W = frame_at(w, t, 10); P = frame_at(p, t, 15)
        W = (W if W is not None else np.zeros((540, 960, 3), np.uint8))[40:500, 120:900].copy()
        if P is not None:
            ph = 150; pw = int(ph * P.shape[1] / P.shape[0]); P = cv2.resize(P, (pw, ph), interpolation=cv2.INTER_AREA)
            cv2.rectangle(P, (0, 0), (pw - 1, ph - 1), (255, 255, 255), 3); W[-ph:, -pw:] = P
        label(W, f"{t} s", (12, 34), 0.9)
        row.append(W)
    strip = np.hstack(row); label(strip, f"{name}: {NICE[R[(n, SC)]['outcome']]}", (12, strip.shape[0] - 14), 1.0)
    rows.append(strip)
out = np.vstack(rows)
cv2.imwrite(str(OUT), out, [cv2.IMWRITE_JPEG_QUALITY, 88]); print(OUT, out.shape)
