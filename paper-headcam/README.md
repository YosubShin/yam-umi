# Track 3 draft: head-camera labelling of glove demonstrations

Reader's guide for the first draft (`main.tex`, built `main.pdf`). Target: CoRL 2026 workshop
"The UMI Arena", Track 3 contributed papers, 2-4 pages excluding references, CoRL format,
single-blind, OpenReview. Due **16 Oct 2026**.

Build: `latexmk -pdf main.tex` in this directory (then `latexmk -c`).
Red text = placeholder or open question. Blue text = a number that comes from the rollout grid
still running on the robot (25 scenes per arm; 19 done at the time of writing).

## The system in five lines

1. The glove is the fiducial-tracked YAM gripper replica from the device-track paper (`../paper`).
2. The collector wears one 4K camera. It sees the fiducial ball on the glove, the jaw tags, and
   four printed AprilTag tiles taped around the workspace. Every frame gives camera pose (tiles),
   gripper pose (ball) and jaw width (tags) from that one image. No fixed camera, no IMU, no SLAM.
3. On the robot a six-joint SO-101 arm carries the same camera and keeps the gripper in view the
   way the collector's head kept the hand in view, from the robot's joint state alone. Teleop data
   and rollouts both go through it, so training and deployment share one viewpoint distribution.
4. A fixed external camera exists in the rig only as an ablation (it is how the device-track paper
   labelled the glove).
5. Policies are ACT, one recipe, joint-space actions, best checkpoint by validation loss on 6
   held-out teleoperated episodes.

## The eight policies on the robot

Every arm's teleop half carries the robot's encoder labels; only the glove half carries the
camera under test. Same 198 glove demonstrations in every mix. "val" = ACT loss on the 6
held-out teleoperated episodes, encoder targets, comparable across all rows.

| # | arm (code name) | what it is | glove labels | policy camera | training data | val |
|---|---|---|---|---|---|---|
| 1 | head_Hgt | teleop only, full budget | - | head cam | 172 teleop | 0.318 |
| 2 | mix_gHs3 | **the device** | head cam | head cam | 172 teleop + 194 glove segments | **0.263** |
| 3 | head_Hgt48 | teleop only, low budget | - | head cam | 48 teleop | 0.464 |
| 4 | mix_gHs3_48 | device, low budget | head cam | head cam | 48 teleop + 194 glove | 0.295 |
| 5 | mix_FA | conventional wrist-cam UMI | fixed cam | wrist fisheye | 168 teleop + 253 glove | 0.257 |
| 6 | head_HH | teleop labelled by the head cam, no encoders | - | head cam | 172 teleop | 0.328 |
| 7 | mix_FB | fixed camera as the whole system | fixed cam | fixed cam | 172 teleop + 255 glove | 0.256 |
| 8 | mix_gHA | head labels on the wrist view | head cam | wrist fisheye | 168 teleop + 192 glove | 0.252 |

Notes. Arms 5 and 8 have 168 teleop episodes because the wrist recording has gaps in four.
Arms 5 and 7 have more glove *segments* but 10% fewer glove *frames* (43.5k vs 48.5k): the fixed
camera loses the gripper behind the collector's body, those stretches are cut, and the episodes
fragment. Arm 6 is scored on the encoder targets too (its own-chain loss is 0.282).

## Preliminary rollout tally (19 of 25 scenes, 152 trials, 20:00 on 16 Oct)

Protocol: 25 block placements, each placed once and then re-placed to a saved reference image
(ghost alignment) for every other arm; arm order shuffled per scene; 60 s budget; outcome scored
by the operator (success / no grasp / dropped before bin / dropped at bin / timeout).

| # | arm | success | median time to success | failures |
|---|---|---|---|---|
| 1 | teleop only 172 | 16/19 | 15.8 s | 3 no-grasp |
| 2 | **device** 172 + glove | 17/19 | 17.4 s | 2 no-grasp |
| 3 | teleop only 48 | 8/19 | 16.9 s | 11 no-grasp |
| 4 | device 48 + glove | 14/19 | 17.3 s | 5 no-grasp |
| 5 | wrist-cam UMI | 11/19 | 18.5 s | 4 no-grasp, 3 dropped before bin, 1 at bin |
| 6 | head-cam teleop labels | 12/19 | 19.1 s | 7 no-grasp |
| 7 | fixed camera system | 10/19 | 17.4 s | 8 no-grasp, 1 dropped at bin |
| 8 | head labels, wrist view | 11/19 | 15.6 s | 1 no-grasp, 6 dropped before bin, 1 at bin |

Paired (same scenes) exact McNemar tests, wins / losses / two-sided p:

| comparison | wins / losses | p |
|---|---|---|
| device 48 vs teleop-only 48 (arm 4 vs 3) | 7 / 1 | 0.07 |
| device vs teleop-only, full budget (2 vs 1) | 2 / 1 | 1.0 |
| head labels vs encoders (6 vs 1) | 3 / 7 | 0.34 |
| device vs wrist-cam UMI (2 vs 5) | 6 / 0 | **0.03** |
| device vs fixed camera (2 vs 7) | 9 / 2 | 0.07 |
| device vs head labels on wrist view (2 vs 8) | 7 / 1 | 0.07 |
| label source on the wrist view (8 vs 5) | 2 / 2 | 1.0 |

Resolution: at 25 trials the binomial 95% interval is about +/-18 points; the paired tests above
are what the text should lean on, since every arm sees the same placements.

## The one-line story

The provocative version: a head camera is all a UMI needs. The defensible version: one egocentric
moving camera replaces the wrist camera *and* the pose tracker (SLAM, IMU, VR controller, fixed
base camera), and the policy is as good. What it buys: no electronics in the glove at all, since
fiducials give pose and jaw width from the head cam's view. What it costs: a moving camera at
deployment. The mitigation: a cheap servo-driven printed camera arm (SO-101 follower, about $120 in parts; glove $22, camera $122) was shown to work, and its
viewpoint model is a naive linear fit on one glove session, so the numbers here are a floor.

## The stories, in the order the paper tells them

1. **One worn camera labels the glove in the wild.** Tiles replace the fixed camera as the world
   frame; single-tile frames are chained; blind stretches are cut rather than losing the episode.
   Numbers (final): 0.7-7.4% of frames cut per session vs 8-22% for the fixed camera; tool-point
   label error vs the robot's encoders 6.5 mm median / 14.1 mm p90, 1.55 deg; a policy trained on
   head-cam labels instead of encoders pays 3% in validation loss (0.328 vs 0.318), where the
   fixed-camera glove paid 14% in the device paper.
2. **Glove data stretches a small teleop budget.** Offline: the 194 glove segments are worth
   65-100 teleop episodes (2-3 glove demos per teleop demo); 48 teleop + glove lands between 96
   and 172 teleop alone. Robot (preliminary, 19 scenes): 8/19 -> 14/19 at the 48 budget, every teleop-only
   failure a no-grasp. The gain shrinks with budget: at full budget the device and teleop-only are
   tied, which is the task ceiling (about 85%), not a failure of the glove data.
3. **The same camera on the robot closes the viewpoint gap.** Teleop and rollouts see what the
   collector saw. The positioner is driven from joint state only, identically in both.
4. **Which camera, and why.** Offline all four co-trained arms (2, 5, 7, 8) are within 0.011, so
   the loss does not separate cameras. On the robot the failure modes do: head-view arms fail only
   by never grasping; wrist-view arms drop the block during the carry, and every observed drop
   happened while the bin was outside the fisheye's view. Arm 8 vs 2 isolates the observation
   (same labels); arm 8 vs 5 isolates the label source (same observation); arm 7 asks whether a
   moving camera is needed at all.

## What we can already say safely (19 scenes)

- Glove data recovers the low-budget teleop policy (arm 4 vs 3: 14/19 vs 8/19, 7 wins to 1,
  p = 0.07 and tightening). This is the headline robot result and it matches the offline curve.
- At full budget co-training does no harm (arm 2 vs 1: 17/19 vs 16/19, tied). The task ceiling
  is about 85-90%; no-grasp is the only failure of any head-view arm.
- The camera matters more than the labels. The device beats the conventional wrist-camera recipe on
  the same placements (6 wins to 0, p = 0.03); swapping its labels onto the wrist view (arm 8) does
  not help (8 vs 5 tied, 2/2), while keeping the labels and swapping the view does (2 vs 8, 7/1).
- Failure modes split by camera: 11 drops in 38 wrist-view trials, 1 in 19 fixed-camera trials,
  0 in 95 head-view trials. Head-view policies only ever fail by not grasping.
- Head-camera labels in place of encoders cost something on the robot (arm 6 vs 1: 12/19 vs
  16/19, 3 wins to 7, not significant). Say "within noise of" rather than "as good as" until 25.

## What waits for the final count

- The budget pair and the fixed-camera comparison are at p = 0.07 with 19 scenes; two more
  discordant scenes in the same direction make both significant.
- Arm 7's placement in the ranking, with its caveat (below).
- Whether arm 6 closes the gap to arm 1.

## Caveats to keep in the text

- The fixed camera was mounted low because the positioner occupied the high vantage point; its
  occlusion rate (8-22%) is an upper bound for a fixed camera in this workspace. Arm 8 is the
  control that does not depend on the mount height.
- Tile layout was refit from one session by median single-tile poses, not bundle-adjusted.
- Positioner lag about 0.4 s; joint limits on the largest sweeps.
- Appearance gap: the head cam sees the collector's arm and the glove's fingers; glove-only
  policies do not transfer (val 0.52 vs 0.26 co-trained), as in the device paper.
- 25 trials per arm; one seed per policy.

## Anecdotes (operator notes, `~/co/pilot/rollout_logs/grid_20261016/anecdotes.md`)

- Scene 5, low budget: teleop-only could not close in on the block; the mix missed its first
  grasp, backed off, re-grasped and succeeded.
- Scene 5, arm 8: opened the gripper mid-carry with the block out of the wrist camera's view.
- Wrist-view arms drop when the wrist view is looking away from the bin; the converse was never
  seen.

## Feedback received so far

**Yuan (16 Oct, after reading the draft and setting up collection on a Mac).**

1. *Jaw-width accuracy deserves its own check.* Their fixed-camera width estimator read a
   59.1 mm opening with 0.29 mm p95 error in one view but 2.3 and 5.1 mm in two turned poses.
   Done: a width sentence in the label-accuracy paragraph, from the 112 teleoperated episodes
   where encoders are the reference (3.5% of stroke median, 7.9% p90, 2.3% when closed, no lag,
   100% coverage in 9 of 10 episodes, a 4-6% under-read at full opening). Also binned by workspace quartile, distance, camera elevation and
   line-of-sight angle to the jaws (forward kinematics on the encoder joints): every bin 2.8-4.8%
   median, 6.8-8.5% p90, worst looking across the jaws. The fixed camera of the device paper read
   the same gripper at 4.4% median, 94% coverage. What this does not cover: openings never seen in
   calibration (the teleop estimators are fit on alternate frames of the same session; the glove's
   are fit on spacer holds in one session and applied to the other three, unmeasured).
2. *Tile placement and visibility.* Clips where the head cam tracked the glove but got no world
   pose; a tag PDF open on a laptop confused localisation. Done: two practical rules in the
   collection paragraph (tiles where the gaze lands at the grasp, two in view from the natural head
   pose, none under the bin or in the arm's sweep; no other tag in the scene).

**Yosub.** The tail was not explained; it is now (collection paragraph). It is the part that makes
an electronics-free glove possible: fingertip tags face the wrist camera and are invisible from
behind the hand (0 of 13.7k frames in the first test, Aug 2026), so each jaw carries a wedge with
tags on five faces, read against a fixed tag on the gripper back. The original feasibility
numbers (robot gripper, fixed camera, Aug-Sep 2026): single-tail fallback 5-7 mm RMS over the
95 mm swing; later wedges with more faces, 94% coverage and 4.4% of stroke median error.

## Confound to keep in mind (not in the paper)

Between last week's rollouts and this grid the glove width map changed (closed-on-object anchor
0.246 -> 0.225, the squeeze level). Last week's mid-air drops, including the wrist and fixed-cam
arms, cannot be attributed to the camera because of that; this grid is clean (all eight arms use
the new map), and within it the head-view arms have not dropped once. Grasp tuning is necessary
regardless of camera.

## Where help is wanted (Igor)

- Citations and one or two background sentences in Section 1: SLAM/IMU tracking in UMI-style
  devices vs fiducial or marker-based localisation; prior work that moves a robot-side camera to
  match a human viewpoint (active perception, head-mounted or arm-mounted cameras); the
  egocentric viewpoint gap literature. No related-work section is planned; clauses in place.
- Tone of the limitations paragraph and the "what is next" sentence.
- Anything in the system section that is unclear to a reader who has not seen the rig.
- The red `\todo` items: how the camera is worn (mount, weight), teaser figure, placements figure.

Repository layout: `main.tex` (preamble, title, teaser figure, bibliography) pulls in one file per
section from `sections/` (`abstract`, `idea`, `system`, `experiments`, `limitations`), so edit the
text there. `resources/venue.md` records the venue rules and dates. `refs.bib` (shared with the
device paper), `fig/make_budget.py`
regenerates `fig/budget.pdf` from `~/co/pilot/e8/head_val_curves.csv`. The device-track paper is
in `../paper` and is the reference for style and length.
