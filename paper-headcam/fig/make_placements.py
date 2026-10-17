#!/usr/bin/env python3
"""Rollout placements over the fixed camera's view (as in the device paper). Each disc is one
placement: successes over the eight arms (n/8), colour red 0 .. green 8; the arrow points to that
scene's bin (detected by colour in the scene reference image).

  python fig/make_placements.py      # writes fig/placements.png
"""
import json
from pathlib import Path
import cv2, numpy as np

G = Path.home() / "co/pilot/rollout_logs/grid_20261016"
OUT = Path(__file__).resolve().parent / "placements.png"
rs = [json.loads(l) for l in open(G / "trials.jsonl")]
pl = {int(k): np.array(v) for k, v in json.load(open(G / "placements.json")).items()}
N_ARMS = len({r["policy"] for r in rs})

def bin_centre(sc):
    im = cv2.imread(str(G / f"scene{sc}_ref.png")); hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    m = cv2.morphologyEx(cv2.inRange(hsv, (85, 25, 40), (115, 140, 200)), cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    c = max(cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0], key=cv2.contourArea); M = cv2.moments(c)
    return np.array([M["m10"] / M["m00"], M["m01"] / M["m00"]])

x0, y0, x1, y1 = 300, 20, 1800, 1080
im = cv2.imread(str(G / "scene1_ref.png"))[y0:y1, x0:x1].copy()
im = cv2.addWeighted(im, 0.45, np.full_like(im, 255), 0.55, 0)

def col(k, n):
    t = k / n; return (int(40 + 40 * (1 - t)), int(60 + 180 * t), int(230 * (1 - t) + 30 * t))

scenes = sorted(s for s in pl if any(r["scene"] == s for r in rs))
for s in scenes:
    b = pl[s] - [x0, y0]; c = bin_centre(s) - [x0, y0]
    cv2.arrowedLine(im, tuple(b.astype(int)), tuple(c.astype(int)), (120, 120, 120), 2, cv2.LINE_AA, tipLength=0.04)
for s in scenes:
    b = pl[s] - [x0, y0]; k = sum(r["outcome"] == "success" for r in rs if r["scene"] == s); n = sum(1 for r in rs if r["scene"] == s)
    cv2.circle(im, tuple(b.astype(int)), 34, col(k, n), -1, cv2.LINE_AA); cv2.circle(im, tuple(b.astype(int)), 34, (255, 255, 255), 3, cv2.LINE_AA)
    txt = f"{k}/{n}"; (tw, th), _ = cv2.getTextSize(txt, cv2.FONT_HERSHEY_DUPLEX, 0.8, 2)
    cv2.putText(im, txt, (int(b[0] - tw / 2), int(b[1] + th / 2)), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(im, f"successes of {N_ARMS} arms at each placement; arrow: block -> bin", (20, 40), cv2.FONT_HERSHEY_DUPLEX, 0.9, (40, 40, 40), 2, cv2.LINE_AA)
cv2.putText(im, "robot base", (20, im.shape[0] - 20), cv2.FONT_HERSHEY_DUPLEX, 0.9, (40, 40, 40), 2, cv2.LINE_AA)
cv2.imwrite(str(OUT), im); print(OUT, len(scenes), "scenes")
