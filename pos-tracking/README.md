# Position tracking

**This is an optional add-on.** The default way to recover wrist pose with
YAM-UMI is camera SLAM from the wrist fisheye, the same approach the original UMI
used, with visual-inertial SLAM. It needs no marker-ball hardware and keeps
collection portable. The wrist-camera aperture markers described below are
still needed to measure jaw opening.

What is here is a **dodecahedral ArUco marker ball** on a stalk, observed by an
external forward-facing camera, for setups that can accommodate a fixed camera.
It measures sub-millimetre on settled holds (numbers below), at the cost of
confining collection to that camera's view. Ball markers use the
**`DICT_4X4_100`** dictionary, IDs 25–35; IDs 36–49 are for the
forward-camera extension described below. IDs 0–24 are reserved for the
robot-mounted ball used to validate tracking against forward kinematics (see
[forward-cam-umi](https://github.com/YosubShin/forward-cam-umi)).

<p align="center">
  <img src="../media/assembly-with-tracker.jpg" alt="The assembled YAM-UMI gripper with the dodecahedral ArUco marker ball mounted on its wrist stalk" width="560">
</p>
<p align="center"><em>The assembled gripper with the dodecahedral tracker on its
stalk, held clear of the hand and of the fisheye camera's view.</em></p>

## Parts

| Part | Size (mm) | Notes |
|---|---|---|
| `dodeca_marker_ball_v2` | 51.05 across | Regular dodecahedron; carries the 15 mm markers |
| `stalk_rod_80mm` | 8 × 8 × 80 | Rod holding the ball clear of the hand |
| `wrist_stalk_arc_adapter` | 44 × 14 × 49.8 | Mounts the stalk to the wrist |
| `arc_extender` | 43.5 × 41.5 × 57 | Extends the arc mount |

A dodecahedron is used so that at least one face is well-conditioned for pose
estimation from any viewing direction, which removes the orientation blind spots
a single planar marker has.

## Markers

`glove_markers_v4.pdf`, group *dodecahedron ball*: **nominal 15 mm black
squares on 19.5 mm tiles, IDs 25–35**, applied to eleven faces of the ball.
Use measured black-square sizes for calibration.

The basic wrist-camera-and-ball assembly uses the sheet's left column:
the *dodecahedron ball* group and the *tips WRIST* group
([below](#aperture-markers)).

### Optional forward-camera extensions

The right-hand column contains the *tails* (BACK, TOP, FORWARD, OUTSIDE,
BOTTOM) and *base* (BACK, TOP) groups, IDs 36–49. They belong to the
[forward-cam-umi extensions](https://github.com/YosubShin/forward-cam-umi):
extra markers and printed parts provide an occlusion backup for the ball
and let the external camera measure aperture. They are not required for
the basic wrist-camera-and-ball assembly. Follow the companion repository
if using those extensions; both projects share this sheet so the marker
IDs do not collide.

### Measure and prepare the markers

Print at **100% / Actual size** on matte paper or label stock, disabling
all automatic scaling. Before cutting, check the 100 mm bar and take
**six black-square measurements per group**, across different markers and
alternating width and height. Average and record each group separately;
the white border is the cutting boundary, not the measurement boundary.
Enter the measured sizes in the unit's marker map and use the measured
ball size in its calibration. See the assembly guide's
[measurement procedure](../docs/assembly.md#measure-before-you-cut--every-marker-group).

Apply thin double-sided tape across the **entire back of the uncut marker
region**, then cut through paper and tape together, preserving the white
border. Bond every edge flat. Do not use glue, glossy paper, or tape over
the printed face: curled edges and reflections interfere with corner
detection. The same preparation applies to ball, finger, and extension
markers.

### Marker placement is not prescribed

There is deliberately **no face-to-ID mapping to follow**. Apply the eleven
markers to the faces in any arrangement, then recover the layout by
running the assembled ball through a solver that estimates each marker's pose in
the ball's body frame from observations across many viewpoints.

This is worth understanding before you build: the ball's geometry is calibrated,
not assumed. It means print-and-stick tolerances are absorbed by the calibration
rather than becoming permanent error, and it means **your ball's mapping will
differ from anyone else's** — the calibration output is specific to the physical
unit you built and has to travel with it.

Follow [forward-cam-umi steps 2–6](https://github.com/YosubShin/forward-cam-umi/blob/main/scripts/README.md)
for camera setup, intrinsics, a rotation take, detection, and ball geometry
solving. Use the measured marker size and keep the solved geometry with
that physical ball. Moving, re-sticking, or swapping a marker requires
recalibrating it. The assembly guide summarizes the
[camera and calibration sequence](../docs/assembly.md#the-forward-camera-mount-focus-calibrate-solve-the-ball).

### Measured performance

All figures below were taken with the ball at roughly 94 cm standoff from the
external camera, **on settled holds**.

**Precision**

| Metric | Result |
|---|---|
| Within-hold | 0.46 mm RMS (median), p90 0.68 mm |
| Revisit repeatability | 0.08–0.17 mm SD per axis (lateral 0.12, depth 0.17) |

**Coverage** — the fraction of frames with enough faces visible to solve a bundle
pose. This is where the choice of external camera shows up:

| Camera | ≥1 face | ≥2 faces | ≥3 faces |
|---|---|---|---|
| Sony (4K 30p, H.264) | 100% | 90.8% | 77.5% |
| Arducam B0591 (1080p, focus locked via v4l2) | 79.6% | 68.3% | 59.1% |

The B0591 numbers were measured before any mount or field-of-view tuning for
that camera. The 15 mm faces give it comfortable pixels at this range, so the
gap to the Sony is a field-of-view and mounting difference rather than a
sensor limit — treat 68% as a floor, not a verdict on cheaper webcams.

#### The camera that ended up winning: Arducam B0587 (4K low-light)

After the table above we moved to the **Arducam B0587** (4K STARVIS2 sensor,
~88° FOV, UVC/MJPEG) and it became the workhorse — it is the camera behind
every number in [`dynamic-accuracy.md`](dynamic-accuracy.md):

| Metric | Result |
|---|---|
| ChArUco intrinsics | 0.744 px RMS at 4K |
| Rigid marker-pair RMS (best pairs) | 0.7 mm |
| Detection vs arm speed | flat to 3 m/s — no measured ceiling |
| Per-frame ≥1-face detection, full teleop session | 99.97% |

**Why it works — the motion-blur unlock.** Fiducial tracking during motion
dies by corner smear, not by frame rate: at 25 fps a marker moving 1 m/s
travels 40 mm between frames, but what kills the *decode* is how far it moves
during the *exposure*. The recipe is a very fast shutter on a sensor that can
afford it:

- **Exposure 0.2 ms** (`exposure_time_absolute=2`, manual mode, gain 0,
  sharpness 0). At 0.2 ms, even 3 m/s of motion smears only 0.6 mm —
  sub-pixel at ~1 m standoff — so the corner detector simply never sees
  blur, and the speed ceiling disappears.
- **A low-light sensor makes that exposure usable.** 0.2 ms under ordinary
  indoor lighting starves a typical webcam sensor; the STARVIS2's
  sensitivity yields clean, zero-gain images at that shutter in a bright
  lab. This pairing — fast shutter *enabled by* low-light silicon — is the
  whole trick, and it is worth selecting cameras for explicitly. (In dim,
  ceiling-light-only conditions the same camera certified at 1 ms +
  gain 20 with equivalent tracking quality.)

Hard-won caveats that travel with this camera class:

1. **Control readback lies.** UVC exposure writes are accepted and read
   back correctly *whether or not the imaging pipeline latched them* — and
   on some modules they only latch after streaming has started. Apply the
   settings mid-stream and verify **behaviourally**: wave a hand in front
   of the lens; at 0.2 ms it must be frozen, not smeared. We lost a full
   session to trusting readback before learning this.
2. **Image brightness is not an exposure probe** on HDR/tone-mapping ISPs —
   some modules normalise brightness toward a target regardless of the real
   exposure. Streaks and blur are the probe; brightness is not.
3. **Some modules' `focus_absolute` is accepted but inert** (the B0587
   focuses by physically rotating the barrel only). Verify focus with a
   live sharpness meter, then mechanically lock the barrel with a witness
   mark — and recalibrate intrinsics after *any* barrel movement.
4. **Flickering LED lighting strobes at sub-millisecond shutters.** Room
   light that looks steady to the eye can beat against a 0.2 ms exposure;
   use DC or high-frequency-driven lighting for the capture volume.

#### Locking focus on the external camera

**Lock the external camera's focus before calibration and collection.**
Refocusing changes the imaging parameters used by the pose solver.

The **B0587** focuses mechanically: rotate the lens barrel while viewing the
live meter in [focus_tune.py](https://github.com/YosubShin/forward-cam-umi/blob/main/scripts/focus_tune.py),
then mark the barrel and leave it fixed. Its `focus_absolute` control can be
accepted without changing focus; do not rely on that control for this module.

For an **autofocus module such as the B0591** used in the earlier coverage
measurement, disable autofocus and lock a fixed setting through V4L2 on Linux.
Control names differ across kernel and driver versions, so list them first:

```
v4l2-ctl -d /dev/video0 --list-ctrls
```

Then disable autofocus and pin a focus value, using whichever names appeared
(`focus_automatic_continuous` on newer uvcvideo, `focus_auto` on older):

```
v4l2-ctl -d /dev/video0 --set-ctrl=focus_automatic_continuous=0
v4l2-ctl -d /dev/video0 --set-ctrl=focus_absolute=<value>
```

Pick the value by focusing on the ball at your working standoff, reading back
`focus_absolute`, then setting it explicitly. These controls reset when the device
is replugged, so reapply them at the start of every session — or with a udev rule
— and re-run the camera calibration if the focus value ever changes.

#### What these numbers do and do not support

1. **Settled holds only** — *resolved 2026-09*: dynamic tracking has since
   been certified on the real arm at full manipulation speed; see
   [`dynamic-accuracy.md`](dynamic-accuracy.md). The 0.46 mm figure remains
   the settled-hold precision, consistent with the 0.7 mm rigid-pair RMS
   measured there.
2. **Relative, not absolute** — *resolved 2026-09*: the 14% scale / 9°
   direction discrepancies were extrinsics error, fixed by a proper
   robot-world hand-eye calibration; absolute robot-frame pose now agrees
   with forward kinematics to 7.7 mm median / 22.7 mm p95, with the
   hand-eye residual (4.8 mm) as the floor. Details and method in
   [`dynamic-accuracy.md`](dynamic-accuracy.md).

## Aperture markers

Gripper aperture is read from AprilTag markers on the gripper tips, seen by the
wrist fisheye camera. Both tip markers must decode to obtain a metric
aperture measurement for a frame; verify detection throughout opening and
closing before recording. These markers are also needed when wrist pose
comes from SLAM instead of the marker ball.

`glove_markers_v4.pdf`, group *tips WRIST*: **AprilTag 16h5 markers with
nominal 6 mm black squares on 8 mm tiles, IDs 2 (A) and 3 (B)**, one per tip.
They use a separate AprilTag family so they don't take IDs from the ArUco range. The markers have to stay
resolvable in the fisheye view, where the tips sit well off-axis and the
effective resolution is much lower than the sensor's nominal figure suggests.

Measure and prepare the finger group separately using the procedure above.
In the reference build, each marker sits on the **top of the finger,
30 mm from its root**, facing the wrist camera. Keep the entire tile flat
and both markers visible throughout the full opening. Check detection
with [tag_contrast.py](https://github.com/YosubShin/forward-cam-umi/blob/main/scripts/tag_contrast.py).
If repositioning a marker after calibration, repeat the affected geometry
and aperture calibration. See the
[assembly instructions](../docs/assembly.md#apply-the-gripper-tip-markers).
