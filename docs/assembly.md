# Assembly

> **This document is a skeleton.** The build order below is inferred from the
> geometry, not transcribed from a real build. Correct it against the assembled
> prototype before publishing, and add a photo per step.

## Before you start

- Print everything in [`hardware/STL/`](../hardware/STL/). See
  [Printing](../README.md#printing).
- **Install the M3 heat-set inserts first**, while the parts are still bare and
  reachable with a soldering iron. Doing this after assembly is much harder, and a
  misaligned insert usually means reprinting the part.

  Threads are brass **M3 × 5 mm × ⌀4 mm** inserts melted in with a soldering iron
  insert tip — not tapped plastic, not captive nuts. Insert dimensions vary
  between sellers at the same thread size, so check yours against the seat
  diameter in the STEP file before printing a full set.
- Print the marker sheets at 100% scale. See
  [`pos-tracking/README.md`](../pos-tracking/README.md).
- Have the spare YAM gripper tips on hand.

## 1. Rails and carriages

Mount **two** MGN9 100 mm rails to `plate_v6`, one per jaw, and slide a MGN9C
carriage onto each. This is the same rail arrangement the YAM gripper uses
internally, which is what makes the jaw travel match the robot's.

Check that both carriages travel freely over the full stroke before anything else
goes on. Rail parallelism is set here, and a bind introduced at this step is
felt by the operator as friction on every pinch — which is exactly what the
servo-free design exists to avoid.

**Keep the rubber end caps, and trim them.** The rails ship with rubber caps at
each end. Left as they are, they foul the jaw adapter riding above the carriage;
removed entirely, nothing stops a carriage running off the end of the rail and
shedding its ball bearings. Cut a few millimetres off the top of each cap
instead: the adapter then passes over freely, while the remaining stub still
catches the carriage before it derails.

## 2. Pinion

Stack the two 3 × 6 × 2.5 mm bearings, then mount the pinion on an **M3 screw**
through them so it meshes with the racks on both moving jaws.

**Do not tighten the screw down.** Run it in only far enough to locate the pinion,
leaving it free to spin. Torquing it clamps the screw head against the top face of
the pinion, and that contact adds exactly the kind of friction the servo-free
design exists to eliminate. Snug, not tight: the pinion should spin under a
fingertip once the screw is set. The pinion is what makes the two jaws move
symmetrically from a single-handed pinch.

**The pinion's heat-set inserts must go in perpendicular to the face.** This is
the one insert on the build where a degree or two of tilt is not cosmetic: it
cants the pinion off its rotation axis, so the gear meshes deeper into one rack
than the other. The result is an asymmetric aperture and friction that varies
through the stroke — the exact defect this mechanism exists to avoid. Seat these
inserts with the iron held square to the face, and check the pinion spins true
before going further.

**Choosing a pinion.** Four variants are provided (`v0`–`v3`), differing only in
outside diameter in 0.1 mm steps. Print all four, then fit each in turn: place the
pinion between the two racks and slide the racks into their final assembly
position. Keep whichever runs smoothest. `v3` was the best fit in the reference
build, but the right one depends on your printer and filament, so choose it by
feel rather than by trusting this number.

<!-- TODO: where do the racks live — integral to the adapters, integral to the
     plate, or separate parts? -->

## 3. Jaw adapters and gripper tips

Bolt `adapter_v10` to each carriage. Install the YAM "Linear 4310" gripper tips
into the adapters.

Screws are not called out by size anywhere in this build. Work from an M3/M4
assortment kit and pick the shortest screw that fully engages its insert — the
printed parts are drawn for M3 × 5 mm inserts, so an over-long screw bottoms out
against the insert rather than clamping the joint.

<!-- TODO: if a size chart would help, record what you actually used per joint. -->

## 4. Aperture markers

Apply the 9 mm tip markers (`pos-tracking/markers/tip_markers_9mm_ID13_14.pdf`,
IDs 13 and 14 — one per tip) to the gripper tips, one on each jaw.

**Position each marker 25 mm from the gripper base** — as far from the fisheye
camera as the tip's flat area allows.

Two unrelated constraints bound this, and only one of them is optical. The camera
sits above the gripper looking down at an angle, so moving a marker *away* from it
carries the marker up toward the centre of the frame. Farther is therefore
optically better, all the way:

- **Too close to the camera** and the marker falls toward the edge of the
  fisheye's field of view, where distortion is worst and corner detection
  degrades — closer still and it leaves the frame altogether.
- **Too far** and you run out of somewhere to put it. The tip narrows toward its
  end, so past a point there is no flat patch wide enough to hold the marker
  without it bending or folding over an edge — and a marker that is not flat will
  not solve cleanly.

25 mm is where the flat area runs out on these tips, not an optical compromise. On
different tips, find the farthest point that still seats the marker flat.

Use double-sided tape across the whole face, not just at the edges, so they cannot
curl.

Check marker visibility across the full open-to-closed range before committing to
a build. Markers visible when open but clipped when closed lose exactly the frames
where grasp detail matters most.

<!-- TODO: note which ID you put on which jaw. Width estimation only needs the
     separation, but a consistent left/right convention keeps downstream code from
     having to guess handedness. -->

## 5. Camera mount

Attach `L_bracket_v3` and `YAM_linear_gripper_fisheye_camera_mount` to the plate,
then mount the Arducam module.

**Set the focus, then leave it alone.** The wrist fisheye focuses mechanically —
you turn the lens barrel by hand; there is no autofocus and nothing to set in
software. Focus it at the working distance where the gripper tips and the
manipulated object sit, checking that the 9 mm tip markers resolve cleanly at both
open and closed aperture, then lock the lens with its retaining ring so handling
cannot shift it.

Do this **before** calibrating the camera intrinsics. Turning the barrel changes
the effective focal length, so a focus adjustment made after calibration
invalidates it — and a stale intrinsic quietly corrupts both the aperture
estimate and any SLAM pose derived from this camera.

**Verify the extrinsic.** This is the claim the whole design rests on. With the
camera mounted, confirm the camera-to-tip transform matches the one on the
deployed YAM arm — ideally by capturing the same scene from both and comparing,
not just by trusting the mount geometry.

## 6. Handle and straps

Attach `handle_v13`, then thread **one hook-and-loop strap per finger — two per
gripper**, one for the thumb and one for the index/middle finger.

Each finger position has two strap holes, but a single strap through one pair was
enough to retain the finger in the reference build. The second hole is there if
you want to shift the strap's position for a different hand size, or run two
straps per finger for a firmer hold.

## 7. Wrist tracker (optional)

If using marker-based pose tracking rather than SLAM, assemble the dodecahedral
tracker: `stalk_rod_80mm` into `wrist_stalk_adapter_v3`, `dodeca_marker_ball_v2`
on the stalk, retained by `retainer_radial_tab`.

Apply the 15 mm markers to the twelve faces **in any arrangement**. The
face-to-ID mapping is recovered by calibration afterwards rather than prescribed,
so there is no layout to match — but the calibration output is specific to the
ball you built and has to be kept with it. See
[`pos-tracking/README.md`](../pos-tracking/README.md).
