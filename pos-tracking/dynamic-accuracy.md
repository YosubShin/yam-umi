# Dynamic tracking accuracy — dodecahedral ball vs robot ground truth

*Added 2026-09-15. These measurements were made with the same dodecahedral
marker ball and detection stack as this repository, mounted on the real
YAM arm's gripper (not the handheld device), because the robot's joint
encoders provide an independent ground truth that a handheld rig cannot.
They supersede the two standing caveats in the earlier characterisation:
tracking is now certified during dynamic manipulation (not just settled
holds), and absolute pose in the robot frame is resolved.*

## Setup

- Dodeca ball: 11 visible ArUco faces (DICT_4X4_50, ids 0–10), ~12 mm
  face markers, as in [`wrist_dodecahedron_marker/`](wrist_dodecahedron_marker).
- External camera: Arducam B0587 (4K STARVIS2, 88° FOV), fixed scene mount,
  manual exposure 0.2 ms (motion frozen at any arm speed), ChArUco
  intrinsics 0.744 px RMS.
- Detection: OpenCV ArUco with `CORNER_REFINE_APRILTAG` and
  `errorCorrectionRate = 1.0`. The full 1-bit correction is safe with
  DICT_4X4_50: codes sit ≥4 bits apart, so a 1-bit-corrected read cannot
  swap ids; measured cost was 3 spurious *unknown*-id detections per 400
  frames (ignorable), measured gain ~32% recovery of marginal decodes.
- Pose: all visible faces fused into a single PnP solve against the ball's
  bundle model, warm-started frame to frame, 5 px reprojection gate.
- Ground truth: robot forward kinematics from joint encoders, linked to
  the camera frame by a hand-eye calibration (below).

## Absolute pose in the robot frame (the previously unresolved part)

The earlier "median 14% scale and 9° direction discrepancies" were
extrinsics error, as suspected — resolved by a proper hand-eye
calibration: `cv2.calibrateRobotWorldHandEye` over ~600 (camera-frame
ball pose, robot FK pose) pairs harvested from ordinary teleoperation
episodes. This solves both unknowns at once — where the camera sits in
the robot base frame and where the ball sits on the gripper flange:

| Calibration | Reconstruction residual (median) |
|---|---|
| Camera #1 (forward) | 4.8 mm / 0.85° |
| Camera #2 (side) | 4.1 mm / 0.93° |

No dedicated calibration capture is needed — any session with diverse
poses works.

## End-to-end dynamic accuracy

Measured over a full teleoperated manipulation session (30 pick-and-place
episodes, ~23,000 frames at 15 fps, normal arm speeds), fiducial pose vs
FK ground truth, evaluated at a tool point ~13 cm from the ball centre
(where errors are largest — rotation error leverages through the offset):

| Slice | Value |
|---|---|
| Frames with solved pose | 98.5% |
| Position error, median | **7.7 mm** |
| Position error, p95 | 22.7 mm |
| Rotation error, median | 1.7° |
| During grasps specifically | 7.2 mm median |

Two readings of that number:

1. **It is a *disagreement* between two systems**, each imperfect: the
   error budget is dominated by the hand-eye residual (~4.8 mm, plus
   ~2 mm from 0.85° leveraged over the 13 cm tool offset), with the
   robot's own encoders/kinematics inside the "ground truth". The
   camera-side contribution is small: the stack's *relative* precision
   is 0.7 mm RMS on rigid marker pairs (and the 0.46 mm settled-hold
   figure elsewhere in this repo remains consistent with that).
2. For imitation-learning pipelines it is exactly the relevant number:
   labels collected in the fiducial frame meet a robot that acts in its
   FK frame, and 7.7 mm median / 23 mm p95 is the boundary the policy
   experiences. In our downstream experiments, policies trained on these
   fiducial labels reached within ~11% (validation loss) of policies
   trained on robot ground truth under matched conditions — and a
   wrist-camera variant matched ground truth outright.

## Failure modes worth designing around

Across sessions, pose loss concentrated in two geometries, neither of
them decode quality:

- **Frame-edge clipping**: the ball is the highest element on the
  gripper, so high transports push it out of a fixed camera's view
  first. Frame your camera with headroom above the workspace.
- **Self-occlusion**: at some wrist orientations the arm hides the ball.
  A second camera with its own hand-eye recovers these stretches (in our
  worst episode, pose coverage went 26% → 92% by fusing a side camera's
  measurements through the two hand-eye transforms).

Detection itself was not the limiting factor: 99.97% of frames decoded
at least one face (the residual being one genuinely corrupt video frame).

## Reproducing

The measurement needs: (1) the ball on a robot with joint encoders,
(2) one recorded session with pose diversity, (3) intrinsics, (4)
`calibrateRobotWorldHandEye` over the paired poses, (5) per-frame
comparison of fused-PnP pose vs FK through the solved transforms.
Residuals of the hand-eye itself (step 4) set the floor of what step 5
can show.
