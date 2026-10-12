# Squeeze-force channel for the glove: ideas and to-dos

Status: parked (2026-10-12) while the head-camera work runs. Nothing here is built yet.

## Why

In the placement-grid rollouts (15 placements × 2, 30 trials per policy) the policies trained
with glove data grasped the block as often as the teleop-only reference (28/30 vs 26/30 for the
co-trained wrist policy) but dropped it more: 43 % of grasps converted to the bin against 62 %,
falling with glove fraction. The cause is what the two corpora record for the gripper.
Teleoperation stores the *commanded* width (0.246 on a block, past contact, so the fingers
squeeze); the glove can only store the *measured* width (0.335 on the same block), and a policy
that reproduces it as a command merely touches. The width map we use (measured → commanded,
`calib/width_to_cmd_glove.json`) is a single static curve and cannot tell a light hold from a firm one.

## The idea

Put a spring in the operator's load path so that squeezing past contact produces a measurable
displacement, and record it as an extra channel. On the robot the same quantity comes for free:
the YAM gripper motor runs in MIT mode (position target + kp), so force = kp × position error,
and the driver reports torque every frame. Match the robot's kp to the glove spring's rate
(through the gripper's stroke ratio) and the two corpora share a force channel in newtons.
No hardware change on the robot.

## Mechanism (chosen)

Two carriages on the handle-side rail; the other rail is unchanged.

- **Inner carriage**: today's assembly minus the handle — rack adapter (teeth to the pinion),
  the stock YAM finger. The pinion still couples the two jaws rigidly, so parallel closing and
  the width reading are untouched.
- **Outer carriage** (handle side only): L-bracket and handle move onto it. Between the two
  carriages, along the rail: one die spring on one M3 shoulder screw (4 mm shoulder).
- Load path: finger → handle → outer carriage → bracket face → spring → boss on the inner
  adapter → finger. The spring sees **2F** (the hand supplies the force for both fingers through
  the pinion). The screw head on the far side of the bracket is the extension stop (and what the
  bracket pulls on when opening); a standoff on the boss, 2 mm shorter than the installed spring,
  is the compression stop, so the spring never goes solid and the operator feels a definite end.
- Assembly order along the screw: head | bracket | spring | boss — the spring goes on from the
  thread end (its 4 mm hole does not pass the 7 mm head). Leave the bracket removable.
- Adds nothing to glove height; the rails/plate need ~30 mm more length on the handle side
  (two 29 mm MGN9C carriages + travel). The pinion, adapter, L-bracket, handle, finger are the existing parts.
- Operator motion: 2 mm of travel at the handle, below what is felt as travel.

Drawings: [`spring_mechanism.png`](spring_mechanism.png) (section at rest / squeezed) and
[`double_carriage.png`](double_carriage.png) (top view with the real adapter_v10 / L_bracket_v4 /
handle_v14 / plate_v6 outlines; the side view in it is schematic).

Rejected alternatives and why:
- Spring fingertip inside/behind the finger (per-finger springs): costs ~9 mm of jaw opening
  per finger on the robot (86 → ~68 mm) if also built on the robot; unnecessary once the robot's
  software spring is used.
- Hinged handle with a spring: fewest parts, but the displacement happens inside the hand where
  no camera sees it (would need a stalk marker).
- A spring on both rails: nothing to measure — the pinion makes the two finger forces equal,
  and two springs fight the pinion.
- Leaf spring / wave spring / disc stack: viable low-profile options if the die spring does not fit;
  not needed with the along-the-rail layout.

## Measurement (chosen: binary flag; continuous later)

Per-frame precision of a 3D marker-to-marker distance from the label cameras, measured on glove5
with the jaw cubes, is **3–4 mm** (adjacent faces of one cube) — far too coarse for 2 mm of travel.
So:
- **Binary flag (first version)**: a thin cover on the boss over the spring with a 2 mm window;
  a red tab on an arm from the bracket sits under the solid cover at rest and appears in the
  window at the 2 mm stop. Any camera reads it as a colour blob. One extra channel (0/1) in the
  dataset; the robot's bit is the gripper torque / position error crossing the matched threshold.
  Also makes the operator's squeeze consistent (squeeze to the stop), which is itself half the fix.
- **Continuous (upgrade)**: two coplanar flat tags (moving tab + fixed reference) read as an
  in-image offset normalised by tag size (depth drops out): ~0.1–0.2 mm per frame, i.e. ~10
  force levels over 2 mm. Or a 5:1 printed lever carrying the tag. No extra cube needed.
- Camera: the fixed forward cam and the head cam see the rail area (where the ball and cubes
  are); the wrist fisheye probably does not. TODO confirm the top faces near the rail stay
  visible during a grasp.

## Parts

- 1 × MGN9C carriage (plus rails lengthened to ~150 mm; the plate is printed).
- Die spring 8 × 4 × 20 mm, light class (TL/blue ≈ 6–10 N/mm; Misumi SWF8-20 = 7.8 N/mm;
  SWF6-20 = 5.9 N/mm fits a thinner adapter). The 50-pc "TF/TL/TM/TH/TB 8×20" kit gives all five
  rates for tuning. Round-wire 8 × 20 × 1.2 mm-wire springs (~7 N/mm) from an assortment also work
  for the flag version.
- 1 × M3 shoulder screw, 4 mm shoulder × 25 mm (or M4×30 partially threaded SHCS + M4 insert).
- Optional: 4.3 × 9 mm steel washers under the spring and the head; red tape for the flag.
- Existing M3 heat-set inserts.

Spring sizing: threshold ≈ 1 mm, stop at 2 mm. With TL at ~8 N/mm: 8 N at 1 mm / 16 N at 2 mm
on the spring = 4 / 8 N at the fingers. Pick the class from the measured squeeze force
(TODO: kitchen-scale readings of a normal hold with the glove); calibrate the installed spring
with a hung weight.

## Software to-dos

- [ ] `yam_zmq_host.py`: publish gripper torque / position error per frame (`effort.gripper`),
      client passes it through; `build_dataset.py` records it for teleop episodes.
- [ ] Glove builds: detect the flag (colour blob in the window) per frame → `squeeze` channel;
      later the coplanar-tag offset → force in N.
- [ ] Set the YAM gripper kp so that kp × (stroke ratio) = glove spring rate; verify with a scale
      between the fingers at a known position error.
- [ ] Replace the static width map by the spring law: command = contact width − F / k.
- [ ] Policy: add the channel to `observation.state` (and as an action to predict), retrain the
      paced glove-only and co-trained arms, re-run the placement grid; the metric is grasp
      conversion (bin / grasped), which was 43 % vs 62 %.

## Open questions

- Squeeze force of a normal hold on the glove (sets the spring class).
- Whether the window faces up or sideways (which camera sees the rail area during a grasp).
- Whether the YAM gripper's lead-screw friction leaves a dead band large enough to matter at the
  flag threshold (expected 1–2 N; measure once the host publishes torque).
