# Third-Party Notices

This project incorporates or derives from third-party material. Each item below
lists what was used and the license it was used under.

## I2RT Robotics — YAM robot models and CAD

This design is dimensioned from three sets of files published by I2RT Robotics
for YAM owners:

- the **YAM URDFs**,
- the **camera mount CAD** for the linear-gear gripper, and
- the **gripper cable retainer**.

Together these are what make the gripper geometry and the wrist camera pose match
the deployed robot.

**Scope of what is derived.** I2RT's plate CAD is supplied as a single merged
mesh, so it provides overall form but no separable components. Everything in this
repository that is not the camera mount interface or the cable retainer was drawn
from scratch — `plate_v6`, `adapter_v10`, `L_bracket_v3`, `handle_v13`, the pinion
variants, and all of `pos-tracking/` are original work, dimensioned either
independently or by measuring the physical robot. The derived content is the
mounting geometry needed to make the camera pose and jaw interface match, not the
mechanism.

**Source.** These were taken from the CAD folder I2RT distributes to customers,
linked from the [YAM product page](https://i2rt.com/products/yam-6-dof-arm) and
hosted on
[Google Drive](https://drive.google.com/drive/folders/17en5gl898ILuapsgUwBkjy4y5SOWQhB2).
That folder carries no stated licence or terms of use.

**Licence status.** I2RT publishes the same designs, in mesh form, in their
open-source [`i2rt-robotics/i2rt`](https://github.com/i2rt-robotics/i2rt)
repository under the MIT Licence — including
`i2rt/robot_models/arm/yam/v1/` (URDFs and meshes),
`i2rt/robot_models/gripper/linear_4310/assets/d405/camera_bracket_for_D405_linear_4310_.stl`
and `.../Cable_holder.stl`. That MIT grant covers the files in that repository. It
is strong evidence that I2RT intends these designs to be openly used, but it is
not itself a licence for the separately distributed CAD folder, which is where the
geometry used here came from.

The MIT Licence text as published in that repository:

```
MIT License

Copyright (c) I2RT Robotics

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

I2RT Robotics has not reviewed or endorsed this project. See the non-affiliation
notice in the [README](README.md#license-and-attribution).

## HandUMI (Murobotics)

No CAD from [`murobotics-ai/handumi-hw`](https://github.com/murobotics-ai/handumi-hw)
is used in this repository. HandUMI was the direct starting point for this work
and is credited as prior art. The design ideas adopted here are the hand-worn,
glove-style form factor, retaining the operator's fingers with hook-and-loop
straps, and keeping the two jaws mechanically synchronized — implemented
independently with a rack-and-pinion on linear rails rather than HandUMI's crank
linkage. HandUMI is licensed under Apache License 2.0.

## Universal Manipulation Interface (UMI)

No CAD from UMI is used here. UMI (Chi et al.) is the origin of the overall
approach, including fiducial-based gripper-aperture sensing, which this design
returns to. See <https://umi-gripper.github.io/>.
