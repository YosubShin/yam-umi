"""Tally and paired tests for the 2026-10-16 rollout grid. python fig/grid_stats.py [trials.jsonl]"""
import json, sys, itertools
from collections import Counter, defaultdict
from math import comb
from pathlib import Path
G = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "co/pilot/rollout_logs/grid_20261016/trials.jsonl"
ARMS = ["head_Hgt", "mix_gHs3", "head_Hgt48", "mix_gHs3_48", "mix_FA", "head_HH", "mix_FB", "mix_gHA"]
rows = [json.loads(l) for l in open(G) if l.strip()]
res = {a: {} for a in ARMS}
for r in rows: res[r["policy"]][r["scene"]] = r
scenes = sorted({r["scene"] for r in rows})
def succ(a): return {s: res[a][s]["outcome"] == "success" for s in scenes}
code = {"no_grasp": "n", "dropped_before_bin": "d", "dropped_at_bin": "b", "timeout": "t"}
print(f"{len(scenes)} scenes")
for i, a in enumerate(ARMS, 1):
    c = Counter(res[a][s]["outcome"] for s in scenes)
    k = c.pop("success", 0)
    fails = " ".join(f"{code.get(o, o)}{n}" for o, n in sorted(c.items()))
    tts = sorted(res[a][s]["elapsed_s"] for s in scenes if res[a][s]["outcome"] == "success")
    med = tts[len(tts)//2] if tts else float("nan")
    print(f"{i} {a:12s} {k:2d}/{len(scenes)}  tts med {med:.1f}  fails {fails}")
def mcnemar(a, b):
    sa, sb = succ(a), succ(b)
    x = sum(sa[s] and not sb[s] for s in scenes); y = sum(sb[s] and not sa[s] for s in scenes)
    n = x + y; p = min(1.0, 2 * sum(comb(n, i) for i in range(min(x, y) + 1)) / 2**n) if n else 1.0
    return x, y, p
print("\npair: a-only / b-only  exact two-sided p")
for i, j in [(2,1),(4,3),(2,5),(2,7),(2,8),(8,5),(6,1),(2,4),(1,3),(5,7),(5,8),(4,1)]:
    a, b = ARMS[i-1], ARMS[j-1]; x, y, p = mcnemar(a, b)
    print(f"  {i} vs {j} ({a} vs {b}): {x}/{y}  p={p:.3f}")
drops = lambda arms: sum(res[a][s]["outcome"] in ("dropped_before_bin", "dropped_at_bin") for a in arms for s in scenes)
fails = lambda arms: sum(res[a][s]["outcome"] != "success" for a in arms for s in scenes)
print(f"\nd+b wrist arms (5,8): {drops(['mix_FA','mix_gHA'])} of {fails(['mix_FA','mix_gHA'])} failures")
print(f"d+b head arms (1-4,6): {drops(['head_Hgt','mix_gHs3','head_Hgt48','mix_gHs3_48','head_HH'])} of {fails(['head_Hgt','mix_gHs3','head_Hgt48','mix_gHs3_48','head_HH'])}")
print(f"d+b fixed (7): {drops(['mix_FB'])} of {fails(['mix_FB'])}")
print("\nper-scene (arm order 1..8, . = success, letter = fail)")
for s in scenes: print(f"  S{s:2d} " + " ".join("." if res[a][s]["outcome"]=="success" else code.get(res[a][s]["outcome"],"?") for a in ARMS))
