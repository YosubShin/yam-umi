# YAM-UMI

An open-source, hand-worn [UMI](https://umi-gripper.github.io/)-style data
collection device for the **[I2RT YAM](https://i2rt.com/products/yam-6-dof-arm)
arm's linear gripper**.

YAM-UMI is deliberately built for one arm.
It mirrors the YAM linear gripper's jaw geometry, reuses the YAM wrist camera
mount, and reproduces the gripper's own rail-and-pinion mechanism, so **the
camera pose relative to the gripper tips, and the way those tips move, are the
same during data collection as on the deployed robot**. Aperture is recovered
from ArUco fiducials rather than a servo encoder, so there is no motor to
backdrive and no loaded plastic linkage to fail.

<p align="center">
  <img src="media/umi-vs-yam-gripper.jpg" alt="The YAM arm's linear gripper beside the YAM-UMI handheld device, showing matched jaw geometry and the same wrist camera mount" width="620">
</p>
<p align="center"><em>Left: the YAM arm's gripper. Right: YAM-UMI. Same jaw geometry,
same camera mount, same tips — so the wrist camera sees the same thing in both.</em></p>

<p align="center">
  <img src="media/demo-pick-place.gif" alt="Operator performing a pick-and-place with the YAM-UMI gripper, dodecahedral tracker visible above the wrist" width="480">
</p>
<p align="center"><em>Pick-and-place demonstration, with the dodecahedral wrist tracker
attached. Full quality: <a href="media/demo-pick-place.mp4">demo-pick-place.mp4</a>.</em></p>

> **Status: hardware released, pipeline in progress.** The mechanical design is
> printed and assembled, and the optional wrist tracker is characterised for
> settled holds (0.46 mm RMS). End-to-end data collection and policy training with
> this device have not been run yet, and the parity claims below are by
> construction rather than measured — see
> [Status and limitations](#status-and-limitations).

## Why another UMI variant

The point of a UMI-style rig is to collect demonstrations without a robot in the
loop, then train a policy that consumes wrist-camera images. That only works if
what the camera sees at collection time resembles what it sees at deployment
time.

That principle is UMI's own, not this project's. The
[UMI paper](https://arxiv.org/abs/2402.10329) states it directly — *"When
deploying UMI on a robot, we place GoPro cameras with the same location with
respect to the same 3D-printed fingers as on the hand-held gripper"* — and reports
wrist-camera video that is "almost indistinguishable" between demonstration and
deployment.

What differs between designs is the **direction** in which the match is made. UMI
adapts the robot to the interface: mount UMI's fingers and a GoPro on any arm with
a parallel jaw stroke over 85 mm, and the match follows. YAM-UMI adapts the
interface to the robot: the arm keeps its stock gripper tips and stock camera
mount, and the handheld device changes to match. That direction suits a fleet
already standardized on one arm, or a deployment configuration you would rather
not modify — at the cost of fitting nothing else.

This design began as an attempt to use
[HandUMI](https://github.com/murobotics-ai/handumi-hw) on a YAM. HandUMI is one
of the few open hand-worn UMI designs whose linkage keeps the two jaws
**synchronized**, moving together the way a parallel gripper does rather than
independently following the operator's two fingers. For anyone targeting a linear
gripper that property is the hard part, and it made HandUMI the natural starting
point here. Two things kept it from working on a YAM.

### 1. The camera extrinsic could not be matched

HandUMI takes a third position: rather than adapting either side, it keeps one
shared body across arms and swaps only the gripper tips, leaving the rest to
software retargeting. That is what lets a single rig serve an AgileX Piper, an ARX
X5, a Trossen WidowX and others — but it means the wrist camera sits where the
shared body allows, and its mount does not readily adjust to reproduce the YAM
camera's angle relative to the gripper tips. The resulting viewpoint shift is a
domain gap the policy has to absorb.

YAM-UMI instead reuses the YAM gripper's own fisheye camera mount on a body that
reproduces the YAM jaw geometry, so the camera-to-tip transform is matched by
construction rather than corrected in software. Because the device also accepts
the **actual gripper tips that ship with the YAM arm**, the jaws occlude the same
part of the frame, the aperture-to-pixel mapping is the same, and the contact
patch on the object is the same.

The cost is generality: this rig targets the YAM linear gripper and nothing else.
That is a deliberate trade, not an oversight.

### 2. The servo and the lever linkage

HandUMI measures aperture with a Feetech servo encoder, which gives a clean
per-frame width signal. The operator pays for it by backdriving the servo through
its gear train on every pinch, adding friction to the one motion the device
exists to record faithfully.

The linkage was the more immediate problem. In hand, its printed lever parts
popped out of the mechanism under normal use — the load path runs through
printed plastic links, and that is where it failed.

YAM-UMI carries the motion on two MGN9 linear rails instead, with a single pinion
between two racks — one rack per jaw — to keep the jaws synchronized.

**This is the mechanism the YAM gripper itself uses.** Two MGN9 rails, two racks,
and a pinion is not an arbitrary alternative to the crank linkage; it is what is
inside the robot's own linear gripper. So the parity here is not only optical and
geometric but *kinematic*: the jaws travel the way the robot's jaws travel, the
aperture is symmetric about the same centerline, and the relationship between the
operator's pinch and the resulting width is the one the robot can actually
execute. There is no mechanism-level retargeting between collection and
deployment, because there is no mechanism difference to retarget.

Aperture is read from ArUco markers, the approach the original UMI used.
Consequences:

- **No backdrive friction.** The pinch is governed by the rails and the
  rack-and-pinion coupling only.
- **No servo, controller, or power supply** in the bill of materials, and no
  cable routing for them.
- **No loaded lever linkage.** The printed parts are brackets and mounts, not
  structural links carrying the pinch load.

<p align="center">
  <img src="media/rack-and-pinion.jpg" alt="View from the gripper tip side: a central pinion meshing with a rack on each jaw, keeping the two jaws synchronized" width="480">
</p>
<p align="center"><em>Viewed from the tip side: one pinion between two racks, one rack
per jaw, riding two MGN9 rails — the same arrangement as inside the YAM arm's own
linear gripper. A single-handed pinch drives both jaws symmetrically, with no
servo in the loop and no linkage carrying the load.</em></p>

## What it records

| Signal | Source |
|---|---|
| Wrist pose, SE(3) | Camera SLAM from the wrist fisheye — the original UMI approach, and the default here. Optionally, a dodecahedral ArUco marker ball observed by an external camera |
| Gripper aperture | 9 mm ArUco markers on the gripper tips, seen by the wrist fisheye camera |
| Wrist-view video | Fisheye USB camera on the YAM camera mount |

SLAM is the default because it keeps collection portable, which is the whole
point of a UMI-style rig. Nothing in this repository is required for it — the
wrist camera and mount are all it needs.

### Optional: dodecahedral wrist tracker

If your setup can accommodate a fixed external camera, this repository also
includes a dodecahedral marker ball and the mounts that attach it to the gripper.
It buys precision at the cost of confining collection to the camera's view.

Measured with the ball at roughly 94 cm standoff, **on settled holds**:

| Metric | Result |
|---|---|
| Within-hold precision | 0.46 mm RMS (median), p90 0.68 mm |
| Revisit repeatability | 0.08–0.17 mm SD per axis (lateral 0.12, depth 0.17) |

Coverage — the fraction of frames with enough faces visible to solve a bundle
pose — depends strongly on the external camera:

| Camera | ≥1 face | ≥2 faces | ≥3 faces |
|---|---|---|---|
| Sony (4K 30p, H.264) | 100% | 90.8% | 77.5% |
| Arducam B0591 (1080p, focus locked via v4l2) | 79.6% | 68.3% | 59.1% |

Two caveats travel with these numbers, and they are not small:

1. **Settled holds only.** Tracking during dynamic motion has not been certified.
   Do not read 0.46 mm as moving-arm accuracy.
2. **Relative, not absolute.** Precision and relative motion are trustworthy;
   absolute pose in the robot's frame is not yet resolved. A camera-vs-forward-
   kinematics comparison showed median 14% scale and 9° direction discrepancies,
   suspected to be forward-kinematics, lever-arm, or extrinsics error rather than
   the camera, but not yet run down.

The Arducam coverage was measured before any mount or field-of-view tuning for that
camera, so it is a floor rather than a verdict on cheaper webcams.

See [`pos-tracking/README.md`](pos-tracking/README.md) for the build and
calibration procedure.

A VR-controller mount is not provided but would be straightforward to add —
contributions welcome.

## Parts

### Gripper body — [`hardware/`](hardware/)

Printed parts are provided as STEP and STL. The STEP files are the source of
truth; the STLs were tessellated from them at 0.05 mm chordal tolerance and are
watertight, so re-export from STEP if you want a different resolution.

| Part | Size (mm) | Role |
|---|---|---|
| `plate_v6` | 102 × 65 × 10.4 | Main plate; carries both linear rails, the camera arm, and the pinion axle |
| `adapter_v10` | 50 × 25.9 × 10.6 | Carriage-to-jaw adapter; presents the YAM gripper tip interface |
| `pinion_z18_deep_v0`–`v3` | ⌀20.0–19.7 × 10.6 | Module 1, z=18 spur pinion coupling the two jaw racks for symmetric motion, as in the YAM gripper. Four fit variants — see [Printing](#printing) |
| `handle_v13` | 32 × 17 × 55 | Operator handle |
| `L_bracket_v3` | — | Camera arm bracket |
| `YAM_linear_gripper_fisheye_camera_mount` | — | Fisheye camera mount, matching the YAM wrist camera pose |

<!-- TODO: confirm the Role column. The pinion/rack coupling is confirmed by the
     tip-side photo, but the plate, adapter, handle and bracket roles are still
     inferred from geometry rather than from your notes. -->

**Gripper tips are not printed.** Use the "Linear 4310" tips that ship with the
YAM arm — that is what makes the contact geometry identical to deployment. If you
do not have spares, I2RT sells them as
[Gripper Tips (for Linear-Gear Style Gripper)](https://i2rt.com/products/gripper-tips-for-linear-gear-style-gripper)
($69), though they are frequently out of stock.

### Position tracking — [`pos-tracking/`](pos-tracking/)

See [`pos-tracking/README.md`](pos-tracking/README.md) for marker specifications
and printing instructions.

- `wrist_dodecahedron_marker/` — the dodecahedral marker ball (51 mm across),
  its stalk, wrist adapter, arc adapter, extender, and retainer, plus the 15 mm
  marker sheet.
- `markers/` — the 9 mm tip-marker sheet (IDs 13, 14) used for aperture sensing
  from the wrist fisheye camera.

Marker placement on the ball is not prescribed: stick the twelve markers on in
any arrangement and recover the face-to-ID mapping by calibration. That absorbs
print-and-stick tolerances instead of baking them in as permanent error, but it
also means each ball's calibration is specific to the unit it was measured on.

## Build

- [Bill of materials](bom/README.md) — ~$79 per gripper in parts, plus shop supplies (filament, fastener kits, tape) if you are starting from nothing.
- [Assembly](docs/assembly.md) — build order and fastener placement.

### Printing

Everything was printed in **PETG** on a Bambu Lab X2D with the stock PETG profile
and *Support for PLA/PETG* enabled. No part needed tuning beyond support
settings. PLA should work too — nothing here runs warm and it is an indoor,
hand-held device — PETG is simply what these were printed in.

**The pinion comes in four variants.** `pinion_z18_deep_v0`–`v3` are the same
18-tooth, module-1 pinion at descending outside diameter — 20.0, 19.9, 19.8 and
19.7 mm — a 0.1 mm clearance ladder against the racks. **Print all four on one
plate and pick the one that runs smoothest** in your assembly. Printer, filament
and insert alignment all shift the effective fit, so the right variant is
empirical rather than predictable; `v3` was the best fit in the reference build,
which is why the rest of the docs name it.

## Status and limitations

- **No end-to-end result yet.** The device has not been used to collect a dataset
  and train a policy. The camera-extrinsic parity claim is by construction and
  has not been validated against recorded imagery.
- **Wrist tracker precision is characterised for settled holds only**
  (0.46 mm RMS at ~94 cm). Dynamic-motion tracking is not yet certified, and
  absolute pose in the robot frame is unresolved — see
  [`pos-tracking/README.md`](pos-tracking/README.md).
- **The tracker's calibration procedure is not published**, so the numbers above
  can be read but not yet reproduced.
- **Aperture accuracy is unmeasured.** A comparison of fiducial-derived width
  against the YAM encoder, or against calipers over a swept aperture, would be
  the most valuable single addition to this repo.
- **Fiducial occlusion** is an inherent failure mode; there is no fallback width
  estimate when markers are lost.
- **Single-arm scope.** No support for other grippers is planned.

## Related work

- **[UMI](https://umi-gripper.github.io/)** (Chi et al.,
  [arXiv:2402.10329](https://arxiv.org/abs/2402.10329)) — the original handheld
  gripper, the source of both the fiducial-based aperture sensing this design
  returns to and the principle of minimizing the observation embodiment gap.
  UMI achieves that match by mounting its own fingers and camera on the robot;
  YAM-UMI reverses the direction.
- **[HandUMI](https://github.com/murobotics-ai/handumi-hw)** (Murobotics) — the
  direct starting point for this work, and one of the few open hand-worn UMI
  designs with a synchronized parallel-jaw mechanism. YAM-UMI takes the
  glove-style form factor and the hook-and-loop finger retention from it, and
  diverges on camera placement, jaw mechanism, and aperture sensing for the
  reasons above. If you want a robot-agnostic rig rather than a YAM-specific one,
  or a direct encoder reading of aperture, HandUMI is the better fit. No HandUMI
  CAD is used here.
- **[Generalist](https://generalistai.com/)** — the wearable data-collection
  approach HandUMI credits as its own motivation.

### The robot this targets

- **[YAM 6-DOF arm](https://i2rt.com/products/yam-6-dof-arm)** (I2RT Robotics) —
  the arm YAM-UMI is built for. 6 DOF, 2 kg payload, 95 mm gripper throw.
- **[YAM documentation](https://doc.i2rt.com/products/yam)** — specifications and
  setup for the arm and its linear gripper.
- **[`i2rt-robotics/i2rt`](https://github.com/i2rt-robotics/i2rt)** — the Python
  client library, URDF, and robot meshes. The meshes there are what this design's
  gripper geometry and camera mount are dimensioned from; see
  [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## License and attribution

This project is released under the [MIT License](LICENSE).

Geometry in this repository is dimensioned from mesh files published by I2RT
Robotics under the MIT License. See
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the full attribution.

**This project is not affiliated with, endorsed by, or sponsored by I2RT
Robotics.** "YAM" is used only to identify the robot arm this hardware is
designed for.
