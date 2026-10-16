"""Budget curve: robot val loss vs teleop episodes, teleop-only vs teleop + 194 glove segments.
Head-label chain (24/48/96/172, round 2 strict v3) and the encoder chain (48/172, final design)."""
import csv, collections
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
rows = collections.defaultdict(list)
for r in csv.DictReader(open("../../../pilot/e8/head_val_curves.csv")):
    if r["val_loss"] != "NA": rows[r["run"]].append(float(r["val_loss"]))
m = {k: min(v) for k, v in rows.items()}
n = [24, 48, 96, 172]
tele_h = [m[f"head_HHc{k}_act50@robotval"] if k != 172 else m["head_HHc_act50@robotval"] for k in [24, 48, 96]] + [m["head_HHc_act50@robotval"]]
mix_h = [m[f"mix_HHs3c{k}_act50@robotval"] for k in [24, 48, 96]] + [m["mix_HHs3c_act50@robotval"]]
tele_e = {48: m["head_Hgt48_act50@robotval"], 172: m["head_Hgt_act50@robotval"]}
mix_e = {48: m["mix_gHs3_48_act50@robotval"], 172: m["mix_gHs3_act50@robotval"]}
fig, ax = plt.subplots(figsize=(4.6, 3.0))
ax.plot(n, tele_h, "o-", color="#444", label="teleop only (head-cam labels)")
ax.plot(n, mix_h, "s-", color="#c0392b", label="+194 glove segments")
ax.plot(list(tele_e), list(tele_e.values()), "o--", color="#444", mfc="white", label="teleop only (encoder labels)")
ax.plot(list(mix_e), list(mix_e.values()), "s--", color="#c0392b", mfc="white", label="+194 glove (encoder labels)")
ax.set_xscale("log"); ax.set_xticks(n); ax.set_xticklabels(n); ax.minorticks_off()
ax.set_xlabel("teleoperated episodes in the training set"); ax.set_ylabel("robot val loss (6 held-out eps)")
ax.grid(alpha=.3); ax.legend(fontsize=7, frameon=False); fig.tight_layout(); fig.savefig("budget.pdf"); fig.savefig("budget.png", dpi=160)
print({"tele_h": tele_h, "mix_h": mix_h, "tele_e": tele_e, "mix_e": mix_e})
