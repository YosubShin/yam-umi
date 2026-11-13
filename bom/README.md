# Bill of Materials

Parts needed for **one** YAM-UMI gripper. Prices are the effective per-unit cost
from the linked listing (pack price ÷ pack quantity) and are reference estimates
only — they move with shipping, region, and availability.

All quantities are confirmed against the assembled prototype.

The list is split in two. **Parts** are what you buy for this project and consume
building it. **[Prerequisites](#prerequisites)** are the workshop supplies and
tools the build draws on — a printer, filament, fastener kits, tape — which anyone
already 3D printing will have on hand. Only Parts are counted in the total, so the
headline figure reflects what this build actually costs you to add.

## Parts

### Motion

One rail and one carriage carry each jaw, so a single gripper needs **two rails
and two carriages** — two sets of the listing below. A bimanual setup needs two
grippers, so four sets.

This mirrors the YAM gripper's own mechanism, which also runs two MGN9 rails with
racks driven by a central pinion. Substituting a different rail size or a single
shared rail would break that correspondence, so treat MGN9 as a fixed choice
rather than a preference.

| Part | Qty | Unit price | Link | Total |
|---|---|---|---|---:|
| MGN9 100 mm linear guide rail + MGN9C carriage block | 2 sets | $9.99 / set | [Amazon](https://www.amazon.com/dp/B0D54LNVKX) | $19.98 |
| Ball bearing, 3 × 6 × 2.5 mm (shielded, MR63ZZ) | 2 (stacked as one pair) | $0.67 / pc ($13.29 / 20) | [Amazon](https://www.amazon.com/uxcell-3mmx6mmx2-5mm-Shielded-Miniature-Bearing/dp/B075CMRGY6) | $1.34 |
| Hook-and-loop straps, 6 in | 2 (one per finger) | $0.19 / pc ($13.99 / 75) | [Walmart](https://www.walmart.com/ip/NavePoint-6-Inch-Hook-and-Loop-Reusable-Strap-Cable-Cord-Wire-Ties-75-Pack-White/180238793) | $0.38 |

> The two bearings stack to give a 5 mm effective width. A single 3 × 6 × 5 mm
> bearing would do the same job in one piece; the pair was used simply because
> that is what was on hand. Either is fine.

> The pinion turns on an **M3 screw** through the stacked bearings, taken from the
> M3 kit in Prerequisites. Leave it slightly loose — see
> [assembly](../docs/assembly.md).

### Optics (optional wrist camera)

The default build is electronics-free: the glove is read by one external
camera (fixed beside the workspace, or head-worn), listed under
[Also excluded](#also-excluded) because it is shared by every glove. The wrist
fisheye below is the classic UMI view and the paper's aperture source. It
**does not fit together with the current `arc_extender`**; see
[Build configurations](../README.md#build-configurations) before buying one.

| Part | Qty | Unit price | Link | Total |
|---|---|---|---|---:|
| Arducam 1080p fisheye USB camera (IMX291, 160°, UVC, manual-focus lens, w/ mic, 1 m cable) | 1 | $56.99 | [Amazon](https://www.amazon.com/Arducam-Computer-Fisheye-Microphone-Windows/dp/B07ZS75KZR) | $56.99 |

### Gripper tips

| Part | Source |
|---|---|
| YAM gripper tips — "Linear 4310" | **No purchase needed.** Spare tips ship with the YAM follower arm, so if you own a YAM you already have them. Only if yours are lost or damaged, I2RT sells replacements as [Gripper Tips (for Linear-Gear Style Gripper)](https://i2rt.com/products/gripper-tips-for-linear-gear-style-gripper), $69 — nylon with a rubber gripping surface, frequently out of stock. |

### Total

| | |
|---|---:|
| **Per gripper, electronics-free** | **~$22** |
| Bimanual pair (2 grippers) | ~$43 |
| External camera, one per system (Arducam B0587, 4K) | ~$122 |
| Per gripper with the wrist fisheye instead (not mountable with the current arc extender) | ~$79 |

Rails, carriages, bearings and straps are the whole per-glove total. The camera
that reads the glove is bought once per system, not per glove, and is listed
under [Also excluded](#also-excluded) with the other shared items.

## Prerequisites

Not counted in the total above. These are shop supplies and tools rather than
parts of the design: if you own a 3D printer you almost certainly have most of
them already, and each covers many builds. Prices are listed so someone starting
from nothing can see the real outlay.

| Item | Used for | Indicative cost |
|---|---|---:|
| 3D printer | Printing the parts; PETG on a Bambu Lab X2D in the reference build | — |
| PETG or PLA filament | ~90 g per gripper body (127 cm³ solid volume: plate, two brackets, two adapters, two handles, pinion) plus ~65 g for the marker ball assembly (94 cm³) and ~15 g for the tails and back-marker holders, at the reference build's infill | ~$3.40 of a $19.99 / kg spool |
| Soldering iron with heat-set insert tip | Installing the threaded inserts; many insert kits bundle one | — |
| [M3 brass heat-set inserts](https://www.amazon.com/Threaded-Inserts-Assortment-Printing-Components/dp/B0DNHLGM8D), M3 × 5 mm × ⌀4 mm | M3 threads in the printed parts: 12 per gripper (plate 8, adapters 4) plus the marker-ball assembly | $12.99 / 100 pc |
| M4 brass heat-set inserts, ⌀5.6 mm seats (match `L_bracket_v5`) | Gripper-finger fastening, 2 per L bracket; replaces nuts | — |
| M2 brass heat-set inserts, ⌀3.1 mm seats, and M2 × 6 mm screws | The two gripper-back marker holders, one each, in the ends of `plate_v7` | — |
| [M3 button-head screw assortment](https://www.amazon.com/dp/B0FQJQNHF5) (840 pc, 8 lengths from 6–30 mm, hex wrench included) | General fastening, the handle screws (30 mm) and the pinion shaft screw | see listing |
| [M4 bolt and nut assortment](https://www.amazon.com/Socket-Screw-Assortment-Stainless-Thread/dp/B01F5JI6N8) | M4 screws for gripper fastening into the bracket's heat-set inserts | $16.99 / kit |
| [Scotch double-sided tape](https://www.amazon.com/dp/B0035LXTYU), 1/2 in × 250 in (3-pack) | Mounting the printed ArUco markers | see listing |
| Matte white paper or label stock | Printing the marker sheets | ~$0.10 |
| Calipers | Verifying marker sheets printed at 100% scale | — |
| Small electric screwdriver *(optional)* | Driving the many small screws | — |

Buying all of these fresh runs roughly **$45–60** depending on which kits you
pick — almost all of which carries over to later builds.

A hand driver builds this fine, but a small electric screwdriver was very
convenient — quick bit changes, bits that snap in magnetically, and USB-C
charging. The [HOTO SNAPBLOQ S-A01](https://www.amazon.com/dp/B0DK4XJ9HF) is what
was used here. No affiliation.

Two of the supplies are more particular than they look:

- **Heat-set inserts.** Insert dimensions vary between sellers at the same thread
  size. The M3 seats are drawn for **M3 × 5 mm long × 4 mm OD**. `L_bracket_v5`
  takes two M4 inserts in ⌀5.6 × 7 mm seats, and `plate_v7` takes two M2 inserts
  in ⌀3.1 × 5 mm seats for the back-marker holders; check length and outside
  diameter against the seats in the STEP file before buying or printing.
- **Double-sided tape**, specified over glue or edge tape because full-surface
  adhesion keeps the markers flat. A marker fixed only at its edges will curl, and
  a curled ArUco marker degrades pose estimates before it looks visibly wrong.

The shopping links are for **assortment kits**; use the quantities and connection
requirements in the [assembly guide](../docs/assembly.md) when selecting screws.
All M3 screws in the gripper and the marker-ball assembly must be low-profile
button-head screws. For the M4 finger screws, check thread engagement in the
bracket inserts and clearance from the opposite rack.

Screw counts per gripper, from the mated CAD of the November 2026 parts (the
lengths marked † are derived from the CAD stack-ups and still to be confirmed
on a built unit):

| Screw | Qty | Where |
|---|---:|---|
| M3 × 8 button head | 4 | rails to plate, two per rail |
| M3 × 16 button head | 8 | L bracket and adapter to the MGN9C carriage, four per side. The CAD stack is 5.1 mm of bracket under the head plus 7.5 mm of adapter, so a 16 mm screw leaves 3.4 mm for the carriage thread, which is all the MGN9C has above the rail; 14 mm grips too little and 18 mm reaches the rail |
| M3 × 30 button head † | 4 | handle through the adapter into its inserts, two per side |
| M3 × 16 button head | 1 | pinion axle through the two bearings |
| M3 × 12 button head † | 4 | arc extender to the back of the plate |
| M3 × 25 button head + M3 nut | 2 | rod mount to the arc extender |
| M3 × 10 button head | 2 | rod to the rod mount and to the ball |
| M4, two lengths | 4 | gripper fingers into the bracket inserts, see the guide |
| M2 × 6 | 2 | gripper-back marker holders into the plate ends |

## Also excluded

- The **external camera** that reads the glove: fixed and forward-facing, or
  head-worn as in [head-cam-umi](https://github.com/YosubShin/head-cam-umi). It
  is shared by every glove and every session, so it is not counted per gripper.
  The reference unit is the **Arducam B0587** (4K STARVIS2, manual focus),
  about **$122**, used both fixed and on the head strap; see
  [`pos-tracking/README.md`](../pos-tracking/README.md#the-camera-that-ended-up-winning-arducam-b0587-4k-low-light).
  Any calibrated camera with a clear view of the workspace works, but coverage
  varies a lot with field of view; the cheaper
  [Arducam B0591](https://www.amazon.com/dp/B0FX47YSJQ) (1080p30 HDR, 78° diagonal)
  measured there is an autofocus module whose focus **must be locked** via V4L2
  before use. Only the wrist-fisheye SLAM path, blocked at the moment, would do
  without an external camera.
- The YAM arm itself.

## Comparison

[HandUMI](https://github.com/murobotics-ai/handumi-hw) lists ~$110 per unit. The
figures are not directly comparable: that total amortises pack purchases down to a
per-piece cost — $0.07 of an M3 kit, $2.52 of a filament spool — where the list
above moves those to Prerequisites instead. Counted the same way, YAM-UMI comes to
roughly **$24** per glove electronics-free, plus the $122 camera shared by the
system, against HandUMI's $110; the earlier wrist-camera build came to $81.

The difference is structural rather than incidental. YAM-UMI drops the Feetech
servo ($13.89), its controller ($10.60) and power supply ($10.00) — about $34 —
and adds two rails and carriages (~$20). It also assumes you already own the YAM
gripper tips, which is reasonable for a rig that only fits a YAM, whereas HandUMI
prints its own tips and targets several arms.
