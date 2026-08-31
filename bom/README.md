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

### Optics

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
| **Per gripper** | **~$79** |
| Bimanual pair (2 grippers) | ~$157 |

The wrist camera is roughly 72% of that. Everything else — rails, carriages,
bearings, straps — comes to about $22.

## Prerequisites

Not counted in the total above. These are shop supplies and tools rather than
parts of the design: if you own a 3D printer you almost certainly have most of
them already, and each covers many builds. Prices are listed so someone starting
from nothing can see the real outlay.

| Item | Used for | Indicative cost |
|---|---|---:|
| 3D printer | Printing the parts; PETG on a Bambu Lab X2D in the reference build | — |
| PETG or PLA filament | ~65 g per gripper (90.6 cm³ solid volume) | ~$1.30 of a $19.99 / kg spool |
| Soldering iron with heat-set insert tip | Installing the threaded inserts; many insert kits bundle one | — |
| [M3 brass heat-set inserts](https://www.amazon.com/Threaded-Inserts-Assortment-Printing-Components/dp/B0DNHLGM8D), M3 × 5 mm × ⌀4 mm | All threads in the printed parts | $12.99 / 100 pc |
| [M3 button-head screw assortment](https://www.amazon.com/dp/B0FQJQNHF5) (840 pc, 8 lengths from 6–30 mm, hex wrench included) | General fastening, plus the pinion shaft screw | see listing |
| [M4 bolt and nut assortment](https://www.amazon.com/Socket-Screw-Assortment-Stainless-Thread/dp/B01F5JI6N8) | General fastening | $16.99 / kit |
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
  size. These parts are drawn for **M3 × 5 mm long × 4 mm OD** — check the seat
  diameter in the STEP files against whatever you buy before printing a full set.
- **Double-sided tape**, specified over glue or edge tape because full-surface
  adhesion keeps the markers flat. A marker fixed only at its edges will curl, and
  a curled ArUco marker degrades pose estimates before it looks visibly wrong.

Fasteners are deliberately given as **assortment kits rather than exact counts**.
The build uses a handful of M3 and M4 screws in a few lengths; pick what fits as
you go rather than working to a parts list.

## Also excluded

- The **external forward-facing camera** used to observe the dodecahedral wrist
  tracker. This is a different camera from the wrist fisheye above, and it is
  needed only for marker-based pose tracking — the SLAM path uses the wrist camera
  alone. Any calibrated camera with a clear view of the workspace works, but
  coverage varies a lot with field of view; see the measured comparison in
  [`pos-tracking/README.md`](../pos-tracking/README.md). The cheaper of the two
  cameras measured there is the
  [Arducam B0591](https://www.amazon.com/dp/B0FX47YSJQ) (1080p30 HDR, 78° diagonal).
  It is an autofocus module, and its focus **must be locked** via V4L2 before use —
  see [`pos-tracking/README.md`](../pos-tracking/README.md).
- The YAM arm itself.

## Comparison

[HandUMI](https://github.com/murobotics-ai/handumi-hw) lists ~$110 per unit. The
figures are not directly comparable: that total amortises pack purchases down to a
per-piece cost — $0.07 of an M3 kit, $2.52 of a filament spool — where the list
above moves those to Prerequisites instead. Counted the same way, YAM-UMI comes to
roughly **$81** against HandUMI's $110.

The difference is structural rather than incidental. YAM-UMI drops the Feetech
servo ($13.89), its controller ($10.60) and power supply ($10.00) — about $34 —
and adds two rails and carriages (~$20). It also assumes you already own the YAM
gripper tips, which is reasonable for a rig that only fits a YAM, whereas HandUMI
prints its own tips and targets several arms.
