# Position tracking

**This is an optional add-on.** The default way to recover wrist pose with
YAM-UMI is camera SLAM from the wrist fisheye, the same approach the original UMI
used — it needs nothing from this directory and keeps collection portable.

What is here is a **dodecahedral ArUco marker ball** on a stalk, observed by an
external forward-facing camera, for setups that can accommodate a fixed camera.
It measures sub-millimetre on settled holds (numbers below), at the cost of
confining collection to that camera's view. Markers use the **`DICT_4X4_50`**
dictionary.

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
| `wrist_stalk_adapter_v3` | 44 × 14 × 29 | Mounts the stalk to the wrist |
| `wrist_stalk_arc_adapter` | 44 × 14 × 49.8 | Arc-mount variant of the adapter |
| `arc_extender` | 43.5 × 41.5 × 57 | Extends the arc mount |
| `retainer_radial_tab` | 60.3 × 14 × 75.6 | Retains the ball on the stalk |

A dodecahedron is used so that at least one face is well-conditioned for pose
estimation from any viewing direction, which removes the orientation blind spots
a single planar marker has.

## Markers

`marker_sheet_ball_15mm_FIXED.pdf` — **15 mm markers on 19.5 mm tiles**, applied
to the twelve faces of the ball.

> **Print at 100% scale.** In the print dialog, choose *Actual size* and disable
> *Fit to page*, *Shrink oversized pages*, and any scaling. A sheet printed at
> 97% produces pose estimates that look plausible and are wrong by 3% in range —
> a failure that will not announce itself.

After printing, measure a marker with calipers against 15 mm before cutting
anything out. This takes ten seconds and is the only check that catches a
mis-scaled print.

Apply markers with double-sided tape across the **entire** face, not just the
edges, so they cannot curl or lift. A marker that bows near an edge biases the
corner detection that pose estimation depends on.

### Marker placement is not prescribed

There is deliberately **no face-to-ID mapping to follow**. Apply the twelve
markers to the twelve faces in any arrangement, then recover the layout by
running the assembled ball through a solver that estimates each marker's pose in
the ball's body frame from observations across many viewpoints.

This is worth understanding before you build: the ball's geometry is calibrated,
not assumed. It means print-and-stick tolerances are absorbed by the calibration
rather than becoming permanent error, and it means **your ball's mapping will
differ from anyone else's** — the calibration output is specific to the physical
unit you built and has to travel with it.

<!-- TODO: point at the solver. Right now a reader has the hardware and the
     marker sheet but no way to get from "ball with stickers on it" to a usable
     pose stream. Either link the tool you used, name the off-the-shelf
     equivalent, or write down the procedure and the output format. This is the
     single biggest gap for anyone trying to reproduce the tracking. -->

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

The Arducam numbers were measured before any mount or field-of-view tuning for that
camera. The 15 mm faces give it comfortable pixels at this range, so the gap to
the Sony is a field-of-view and mounting difference rather than a sensor limit —
treat 68% as a floor, not a verdict on cheaper webcams.

#### Locking focus on the external camera

**Lock the external camera's focus before collecting anything.** The Arducam is
an autofocus module, and autofocus is actively harmful here: refocusing changes
the effective focal length, which shifts the pose solution under a camera the
calibration assumes is fixed. The result is drift that looks like tracking noise
and is not.

There is no hardware switch — set it through V4L2 on Linux. Control names differ
across kernel and driver versions, so list them first:

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

1. **Settled holds only.** Tracking during dynamic motion has not been certified;
   that measurement is still outstanding. Do not quote 0.46 mm as accuracy for a
   moving arm — which is, of course, the case that matters for data collection.
2. **Relative, not absolute.** Precision and relative motion are trustworthy.
   Absolute pose in the robot's frame is not. A camera-versus-forward-kinematics
   comparison showed median 14% scale and 9° direction discrepancies. The
   suspicion is forward-kinematics, lever-arm, or extrinsics error rather than the
   camera itself, but it has not been run down, so no absolute world-frame claim
   is being made here.

<!-- TODO: publish the calibration procedure itself — how the bundle solve is run
     and what it outputs — so someone else can reproduce these numbers rather than
     just read them. -->

## Aperture markers

Gripper aperture is read from ArUco markers on the gripper tips, seen by the
wrist fisheye camera.

`markers/tip_markers_9mm_ID13_14.pdf` — **9 mm markers, IDs 13 and 14**, one per
tip. The 9 mm size is chosen to stay resolvable in the fisheye view, where the
tips sit well off-axis and the effective resolution is much lower than the
sensor's nominal figure suggests.

The same 100% scale rule and full-face taping apply as for the ball markers
above.

Each marker sits **25 mm from the gripper base** — as far from the fisheye camera
as the tip's flat area allows. The camera looks down at an angle, so distance from
it moves the marker toward the centre of the frame and away from the distorted
edge; the limit is mechanical, not optical, since the tip narrows and eventually
offers no flat patch wide enough to seat a marker. See
[assembly](../docs/assembly.md#4-aperture-markers).

An earlier variant detected aperture from the external forward-facing camera
instead, using 12 mm markers on printed tails that carried them behind the jaws.
That approach and its parts live in a separate repository, since they belong to
the external-camera setup rather than to this one.
