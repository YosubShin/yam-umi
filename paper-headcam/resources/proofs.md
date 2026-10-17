# Citation proofs

One entry per cited statement in `paper-headcam/sections/`. Each source was downloaded into `resources/library/<bibkey>/` (kept local, git-ignored) and read by one agent; the quotes below were then checked against an independent text extraction of the saved file.

Quote check: **verified** = found verbatim in the source text (ignoring punctuation, line breaks and the letters that PDF ligatures scramble); **verified by hand** = found by hand where the PDF text extracts garbled; **unconfirmed** = not found, treat as a paraphrase until checked.

Generated 2026-10-16 from workflow run wf_1436e346-5a0 (one Haiku agent per statement); fixes in the commit "paper-headcam: fix nine cited claims to match their sources".

| # | § | Citations | Verdict | Resolution |
|---|---|---|---|---|
| S01 | §1 | campos2021orbslam3, chi2024umi | partial | Fixed |
| S02 | §1 | fastumi2024 | partial | Fixed |
| S03 | §1 | tinyumi2026, yubi2026 | partial | Fixed |
| S04 | §1 | quest2rehab2022, vrtracking2024 | supported | Supported |
| S05 | §1 | yamumi2026 | partial | Fixed |
| S06 | §1 | hsu2022hands | supported | Supported as written. |
| S07 | §1 | umiarena2026 | supported | Supported as written. |
| S08 | §1 | land2001eye | supported | Supported (PDF supplied by hand) |
| S09 | §1 | olson2011apriltag, wang2016apriltag2 | partial | Fixed |
| S10 | §1 | kareer2025egomimic | supported | Supported as written. |
| S11 | §1 | cheng2024opentelevision, chuang2025avaloha | supported | Supported as written. |
| S12 | §2 | i2rtyam | partial | No change |
| S13 | §2 | yamumi2026 | partial | No change |
| S14 | §2 | garrido2014aruco | supported | Supported (PDF supplied by hand) |
| S15 | §2 | wu2017dodecapen | supported | Supported as written. |
| S16 | §2 | shah2013robotworld | partial | Fixed |
| S17 | §2 | so101 | partial | Fixed |
| S18 | §2 | zhao2023act | supported | Supported as written. |
| S19 | §2 | lerobot2024 | supported | Supported as written. |
| S20 | §2 | yamumi2026 | supported | Supported as written. |
| S21 | §3 | chi2024umi | partial | No change needed |
| S22 | §3 | fu2024mobilealoha, kareer2025egomimic | partial | Fixed |
| S23 | §3 | mandlekar2021robomimic | supported | Supported as written. |
| S24 | §4 | triggs2000bundle | supported | Supported as written. |
| S25 | §4 | forwardcamumi2026, yamumi2026 | partial | Fixed |

## S01 (§1)

**Claim the citation must support:** UMI tracks with SLAM on the wrist camera, which needs a mapping pass and texture; tracking can be lost.

**Current text** (`sections/idea.tex`):

> SLAM over the wrist camera \citep{chi2024umi,campos2021orbslam3} needs a mapping pass for every new scene and enough texture in it, and loses track under occlusion and fast motion;

**Verdict:** partial

**Resolution:** Fixed: "an episode is lost when tracking is" was unsupported; now "needs a mapping pass for every new scene and enough texture in it, and loses track under occlusion and fast motion".

**Sources:**

- `chi2024umi`: `library/chi2024umi/paper.pdf`; https://arxiv.org/pdf/2402.10329 — arXiv 2402.10329 PDF (the arXiv version of the UMI paper, RSS 2024). Text extracted with gs to /home/x1/github/yam-umi/paper-headcam/resources/library/chi2024umi/text.txt and per page in pages/. Ligatures corrected by hand.
- `campos2021orbslam3`: `library/campos2021orbslam3/paper.pdf`; https://arxiv.org/pdf/2007.11898 — arXiv 2007.11898 v2 PDF, an accepted-manuscript version of the IEEE T-RO 2021 paper (the IEEE header says accepted for publication). Text extracted with gs to /home/x1/github/yam-umi/paper-headcam/resources/library/campos2021orbslam3/text.txt and per page in pages/.

**Quotes:**

- `chi2024umi`, Sec. HD4 (IMU-aware tracking), p. 3 left column — supports: UMI tracks the gripper with ORB-SLAM3 on the wrist camera; tracking can fail (motion blur, lack of visual features), but only briefly tolerated — *verified*

  > maintains tracking for a short period of time even if visual tracking fails due to motion blur or a lack of visual features

- `chi2024umi`, Sec. HD4 (map-then-localize data collection), p. 6 — supports: SLAM requires a mapping pass for each new scene — *verified by hand*

  > For each new scene, we first collect a video that builds a map for the scene.

- `chi2024umi`, Sec. III (Mapping bullet, data collection), p. 15 — supports: SLAM requires a mapping pass; map quality matters for tracking robustness — *verified*

  > obtaining a high-quality map is critical for precise and robust SLAM tracking, especially for rapid motions during demonstrations.

- `chi2024umi`, Sec. VIII (Limitations), p. 11 — supports: SLAM needs a textured scene — *verified by hand*

  > visual SLAM’s requirement for sufficient texture in the environment

- `chi2024umi`, Sec. D (SLAM System Details, Map as Initialization), p. 17 — supports: closest statement about wasted data, but it refers to ORB-SLAM3 initialization periods where no camera pose can be estimated, not to demonstrations being discarded when tracking is lost — *verified*

  > resulting in a large proportion of wasted data

- `campos2021orbslam3`, Sec. II-D (Robustness to tracking loss), p. 8 — supports: visual SLAM tracking can be lost under occlusion and fast motion — *verified*

  > occlusion and fast motions result in losing track of visual elements, getting the system lost.

- `campos2021orbslam3`, Abstract / Introduction, p. 2 — supports: after tracking is lost, the system starts a new map — *verified*

  > when it gets lost, it starts a new map that will be seamlessly merged with previous maps when revisiting mapped areas.

- `campos2021orbslam3`, Sec. II-D (Robustness to tracking loss), p. 9 — supports: a lost SLAM run discards the map (not the demonstration episode) — *verified*

  > If the system gets lost within 15 seconds after IMU initialization, the map is discarded.

**Agent's note:** Supported: (a) UMI needs a mapping pass per scene and says sufficient texture is required for visual SLAM; (b) ORB-SLAM3 tracking can be lost under occlusion or fast motion, and it then starts a new map. Not supported: the claim that an episode (demonstration) is lost when tracking is lost. Neither paper says that demonstrations with SLAM tracking failures are discarded. UMI only says tracking survives brief failures, and it discards data during ORB-SLAM3 initialization ("wasted data") and filters trajectories kinematically (HD6), which is not tracking-based. Minimal rewording the quotes support: "SLAM over the wrist camera \citep{chi2024umi,campos2021orbslam3} needs a mapping pass and a textured scene, and when visual tracking is lost the SLAM system starts a new map \citep{campos2021orbslam3}." If the episode-loss point is kept, it needs a source from the authors (for example, the UMI data pipeline code) or a statement in the paper's own text.

## S02 (§1)

**Claim the citation must support:** FastUMI adds an off-the-shelf visual-inertial tracker (T265) to the handheld device.

**Current text** (`sections/idea.tex`):

> an off-the-shelf visual-inertial tracker adds a second device, a RealSense T265, to the handheld gripper \citep{fastumi2024};

**Verdict:** partial

**Resolution:** Fixed: FastUMI puts the T265 on the handheld device, not the wrist; now "adds a second device, a RealSense T265, to the handheld gripper".

**Sources:**

- `fastumi2024`: `library/fastumi2024/paper.pdf`; https://arxiv.org/pdf/2409.19499 — arXiv 2409.19499v2 (1 Feb 2025), the arXiv preprint; text extracted to /home/x1/github/yam-umi/paper-headcam/resources/library/fastumi2024/text.txt with gs (ligatures such as fi appear mangled in that file, so quotes below are copied as they read in the PDF).

**Quotes:**

- `fastumi2024`, Abstract, p.1 ("replacing complex Visual-Inertial Odometry (VIO) implementations with an off-the-shelf tracking module"; the hyphen is a line-break artifact) — supports: off-the-shelf visual-inertial tracker (the paper calls it an off-the-shelf tracking module, implemented with a RealSense T265 that has an integrated IMU) — *verified*

  > with an off-the-shelf tracking module

- `fastumi2024`, Fig. 1 caption, p.2 — supports: T265 tracker is mounted on the handheld device, in addition to the GoPro camera (the second device) — *verified*

  > The handheld device, used to collect demonstration data from human operators, includes a GoPro② for visual feedback, a RealSense T265① for end-effector pose tracking

- `fastumi2024`, Section III.B Pose Tracking Module, p.3 — supports: the tracker is visual-inertial (integrated IMU) and replaces the UMI VIO solution — *verified*

  > The T265, featuring a high-performance integrated IMU, replaces UMI’s visual odometry solution

- `fastumi2024`, Section III.B, p.3 (two-column text; the sentence continues with "crucial for environmental context capture") — supports: the T265 is the pose tracker and the GoPro is a separate camera — *verified*

  > the T265 provides accurate pose tracking even under partial occlusions, while the GoPro delivers an expansive view

- `fastumi2024`, Section V (related-work discussion), p.9 or nearby — supports: the only wrist-mounted device the paper names is the GoPro camera, not the T265; this is the source of the mismatch with the wrist claim — *verified*

  > Additionally, its wrist-mounted gopro camera records high-resolution visual data

**Agent's note:** The source supports the tracker part: FastUMI uses an off-the-shelf tracking module (RealSense T265 with integrated IMU, a visual-inertial sensor) on the handheld device, alongside a separate GoPro camera. It does not support \"to the wrist\": the paper places the T265 on the handheld device and calls the GoPro the wrist-mounted camera. The wrist claim in the statement is not backed by this source. Minimal rewording the quotes do support: \"an off-the-shelf visual-inertial tracker \\citep{fastumi2024} adds a second device to the handheld device, next to the camera\" (or simply: \"FastUMI pairs its camera with an off-the-shelf tracking module (a RealSense T265) on the handheld device \\citep{fastumi2024}\"). If the paper's point is about the wrist, a different citation or wording for the wrist-mounted camera is needed. Note that the task's own description, \"a second device on the wrist\", conflicts with what the source says about where the T265 sits, so the task framing should be checked against the paper's intent."}

## S03 (§1)

**Claim the citation must support:** YUBI and tinyumi put a VR controller in or on the gripper, tracked by the VR system; it adds weight.

**Current text** (`sections/idea.tex`):

> a VR controller in or on the gripper \citep{yubi2026,tinyumi2026} adds weight to the hand (\SI{119}{g} of YUBI's \SI{319}{g}) and brings a tracking system of its own, whose accuracy has to be measured separately \citep{vrtracking2024,quest2rehab2022};

**Verdict:** partial

**Resolution:** Fixed: "VR tracker" became "VR controller"; the weight claim now uses YUBI's own figure (119 g of 319 g). tinyumi supports only the mount.

**Sources:**

- `yubi2026`: `library/yubi2026/paper.pdf`; https://arxiv.org/pdf/2606.10244 — arXiv PDF (June 2026 technical report), read via rendered pages 2-5 of the PDF; text.txt and text_squeezed.txt in the same folder are gs extractions with scrambled ligatures, so quotes were checked against the rendered pages. Ran with a 'VR controller' rather than 'VR tracker' wording: the device is a Meta Quest 3S controller.
- `tinyumi2026`: `library/tinyumi2026/README.md`; https://raw.githubusercontent.com/vovw/tinyumi/main/README.md — Default branch (main) README.md. Also saved pos-tracking/quest_mount/handumi_v1/README.md as /home/x1/github/yam-umi/paper-headcam/resources/library/tinyumi2026/quest_mount_README.md (from raw.githubusercontent.com/vovw/tinyumi/main/pos-tracking/quest_mount/handumi_v1/README.md). Neither file mentions the weight of the mount or the controller.

**Quotes:**

- `yubi2026`, Section 1 (Introduction), p. 3 — supports: YUBI puts VR tracking hardware in each gripper — *verified by hand*

  > Combined with the gripper redesign, the YUBI system integrates high-frequency VR sensors directly into each gripper

- `yubi2026`, Section 1 (Introduction), p. 3 — supports: The VR tracking system (Quest 3S) is a separate component on top of the gripper, i.e. a tracking system of its own — *verified by hand*

  > Each YUBI gripper can be fabricated for under $200 USD with 3D printed parts (excluding the Quest 3S tracking system)

- `yubi2026`, Section 3.1 (YUBI Design), p. 5 — supports: Weight added to the hand: the VR controller adds 119 g to the handheld mass in YUBI — *verified by hand*

  > reducing the handheld mass to approximately 319 g (200 g gripper + 119 g VR controller)

- `tinyumi2026`, README.md, 'Print and assemble' step 2 — supports: tinyumi offers a Quest controller mount for the gripper — *verified*

  > Print **one** suitable [left or right Quest support](pos-tracking/quest_mount/handumi_v1/README.md) separately if using a controller. It is not included in either full project.

- `tinyumi2026`, README.md, 'Print and assemble' step 4 — supports: The Quest controller is used as a pose source on the gripper — *verified*

  > then calibrate the chosen camera and pose source.

- `tinyumi2026`, README.md, intro paragraph — supports: Caveat: tracking performance of the Quest mount is not established; no weight claim is made — *verified*

  > physical fit, strength, full hand/cable clearance and tracking performance are not yet established.

**Agent's note:** YUBI supports the claim: its gripper carries a Quest 3S controller for 6-DoF tracking (the Quest tracking system is excluded from the build cost, so it is a separate system), and the handheld mass is 319 g including the 119 g VR controller. tinyumi supports only the mount part: it offers a Quest controller support on the gripper used as a pose source. Nothing in the tinyumi README or the Quest mount README says the mount adds weight to the hand or describes the Quest's own tracking system, so the 'adds weight' and 'tracking system of its own' parts are not backed for tinyumi. Minimal rewording the quotes do support: "a VR controller in or on the gripper \citep{yubi2026,tinyumi2026} is tracked by its own VR system, and in YUBI's build the controller adds 119\,g to the hand \citep{yubi2026}." Also note the citation is for a Quest controller (not a VR tracker), and the 780-900 g numbers on page 4 are prior-work figures (Zeng et al.; Xu et al.), so they should not be attributed to YUBI.

## S04 (§1)

**Claim the citation must support:** Consumer VR tracking accuracy has to be measured against a reference.

**Current text** (`sections/idea.tex`):

> a VR controller in or on the gripper \citep{yubi2026,tinyumi2026} adds weight to the hand (\SI{119}{g} of YUBI's \SI{319}{g}) and brings a tracking system of its own, whose accuracy has to be measured separately \citep{vrtracking2024,quest2rehab2022};

**Verdict:** supported

**Resolution:** Supported: both sources measure consumer VR tracking against a reference. quest2rehab2022 was downloaded by hand (the agent was blocked by MDPI) and checked in the main loop.

**Sources:**

- `vrtracking2024`: `library/vrtracking2024/paper.pdf`; https://arxiv.org/pdf/2412.06116 — arXiv 2412.06116v1 preprint (Banaszczyk et al., 'How Accurate is the Positioning in VR? Using Motion Capture and Robotics to Compare Positioning Capabilities of Popular VR Headsets'). Text extracted with gs to /home/x1/github/yam-umi/paper-headcam/resources/library/vrtracking2024/text.txt.
- `quest2rehab2022`: `library/quest2rehab2022/paper.pdf`; https://www.mdpi.com/1424-8220/22/15/5511 — publisher PDF (open access, CC BY), downloaded by hand by Igor on 2026-10-16

**Quotes:**

- `vrtracking2024`, Section 7 (Headsets positioning and accuracy), p. 6 of arXiv v1 (two-column layout; 'max errors' is split across a line break in the PDF text layer) — supports: Consumer Meta Quest headsets (Quest 2 and Quest Pro) show non-trivial positional errors, reported as RMSE of about 3 mm and maxima of about 10 to 12 mm, measured against the motion-capture reference. — *verified*

  > In the case of the HMDs accuracy, we obtained 3.17[mm] and 3.23[mm] of RMSE for Quest 2 and Quest Pro, respectively, with max errors of 10.48[mm] and 11.97[mm]

- `vrtracking2024`, Section 1 (Introduction), p. 1-2 of arXiv v1 — supports: The accuracy of consumer VR headset tracking is measured against a reference (motion capture, with a cooperative robot reproducing the trajectories). — *verified*

  > The trajectories, captured using a state-of-the-art motion capture system, serve as the objective ground truth for our measurements

- `vrtracking2024`, Section 7, p. 6 of arXiv v1 — supports: Alternative shorter quote for the 'measured errors' part of the claim, if the sentence is trimmed. — *verified*

  > we obtained 3.17[mm] and 3.23[mm] of RMSE for Quest 2 and Quest Pro, respectively

- `quest2rehab2022`, Section 1 Introduction — supports: VR tracking accuracy has to be evaluated, not assumed — *verified*

  > The performance evaluation of a VR motion tracking device is crucial to evaluate their appropriateness for research and clinical applications.

- `quest2rehab2022`, Abstract — supports: measured against a motion-capture reference — *verified*

  > The controller measures were compared with those of a Qualisys optical capture system.

- `quest2rehab2022`, Abstract — supports: non-trivial errors (about a centimetre) — *verified by hand*

  > The results showed a mean absolute error of 13.52 ± 6.57 mm at a distance of 500 mm from the head-mounted display along the x-direction.

**Agent's note:** vrtracking2024 (Banaszczyk et al., arXiv 2412.06116) supports the claim as worded: it measures Meta Quest 2 and Quest Pro positioning against a motion-capture ground truth and reports non-trivial errors (RMSE about 3.2 mm, max about 10 to 12 mm). It also states that the 'accuracy' is judged against the manufacturer's specification, which is a weak claim that the paper treats as acceptable, so the paper does not show consumer tracking is unmeasured by default. The quest2rehab2022 source (Carnevale et al., Sensors 2022, DOI 10.3390/s22155511) could not be obtained from any legitimate open copy in this run (MDPI returns Access Denied; PMC and Europe PMC did not serve a PDF), so the second half of the citation, the claim that 'these papers' both perform such measurements, is unverified. Minimal rewording that the quotes support: 'brings a tracking system of its own, whose accuracy has to be measured separately \\citep{vrtracking2024}' (drop quest2rehab2022 until its PDF is checked, or re-run this check later when the MDPI copy is reachable). The paper also should not say the headset tracking is 'not given' by the manufacturer, since vrtracking2024 cites a manufacturer accuracy specification; a safer phrase would be 'whose accuracy has to be measured separately against a reference'."}] UPDATE (main loop, after the PDF was supplied by hand): quest2rehab2022 obtained and checked; it measures the Quest 2 controller against a Qualisys optical motion-capture reference and reports a 13.52 ± 6.57 mm mean absolute error at 500 mm, so both citations support the clause as written.

## S05 (§1)

**Claim the citation must support:** Our earlier glove used a fixed 4K camera over the workspace that gives absolute labels.

**Current text** (`sections/idea.tex`):

> a fixed 4K camera over the workspace, the choice of our earlier glove \citep{yamumi2026}, gives absolute labels but ties collection to the camera's mount, and the collector's own body hides the hand from it, \SI{8}{}--\SI{22}{\percent} of frames per session in the data below (\S\ref{sec:labels}).

**Verdict:** partial

**Resolution:** Fixed: the device paper never mentions a tripod or body occlusion; now "ties collection to the camera's mount", and body occlusion rests on this paper's own 8-22% (§2).

**Sources:**

- `yamumi2026`: `library/yamumi2026/main.tex`; https://github.com/YosubShin/yam-umi (paper/main.tex, copied from local checkout /home/x1/github/yam-umi/paper/main.tex) — Local copy of the device paper source (paper/main.tex) from the yam-umi checkout. Also copied README.md to the same directory at /home/x1/github/yam-umi/paper-headcam/resources/library/yamumi2026/README.md (from /home/x1/github/yam-umi/README.md) and quoted from it for the occlusion and view-constraint wording. Not a preprint; it is the project's own source.

**Quotes:**

- `yamumi2026`, main.tex, Abstract/intro paragraph (line 34) — supports: Earlier glove was labelled by a fixed 4K camera over the workspace — *verified*

  > seen by one fixed 4K camera over the workspace, gives the pose

- `yamumi2026`, main.tex, line 34 — supports: Labels are absolute (no drift) — *verified*

  > No IMU and no SLAM, so no drift: every label is an absolute per-frame measurement with a known error

- `yamumi2026`, main.tex, Section 'The idea' / device description (line 59) — supports: The workspace must stay in the fixed camera's view — *verified*

  > The trade-off is that the workspace must be in the fixed camera's view

- `yamumi2026`, main.tex, line 59 — supports: The hand hides the tracker (occlusion) from the fixed camera view — *verified*

  > marker cubes on the jaws and four back markers keep the fixed camera tracking when the hand hides the ball at grasp

- `yamumi2026`, main.tex, Discussion/limitations paragraph (line 127) — supports: Occlusion of the tracker by the hand from the fixed view — *verified*

  > from one fixed viewpoint the hand hides the ball at grasp

- `yamumi2026`, README.md, section 'Dodecahedral wrist tracker' — supports: Fixed external camera is the tracker's view (README corroboration) — *verified*

  > The external camera tracks the marker ball and the gripper-back markers.

- `yamumi2026`, README.md, section 'Dodecahedral wrist tracker' — supports: Workspace/collection must stay in camera view (README corroboration) — *verified*

  > Collection must remain within the cameras' view.

**Agent's note:** Supported: the fixed 4K camera over the workspace gives absolute labels with no drift, the workspace must stay in the fixed camera's view, and the hand hides the ball (tracker) at grasp from that fixed view. Not supported: "ties collection to a tripod" (the source never mentions a tripod; it describes a fixed camera on a printed mount, and a fixed camera over the workspace) and "loses the hand behind the collector's own body" (the source says the hand hides the ball at grasp from one fixed viewpoint, not that the collector's body occludes the hand). Minimal rewording the quotes support: "a fixed 4K camera over the workspace, the choice of our earlier glove \citep{yamumi2026}, gives absolute labels but requires the workspace to stay in the camera's view, and the hand hides the tracking ball at grasp from that fixed viewpoint," (drop "tripod" and "behind the collector's own body").

## S06 (§1)

**Claim the citation must support:** A hand-centric view reduces scene observability but improves generalisation.

**Current text** (`sections/idea.tex`):

> And it frames the jaws and little else, so the goal of a carry, here the bin, can leave the policy's view while the task still depends on it: a hand-centric view trades observability of the scene for generalisation \citep{hsu2022hands}.

**Verdict:** supported

**Sources:**

- `hsu2022hands`: `library/hsu2022hands/paper.pdf`; https://arxiv.org/pdf/2203.12677 — arXiv 2203.12677 PDF (Hsu, Kim, Rafailov, Wu, Finn; ICLR 2022 paper). Text extracted with gs to text.txt in the same directory. Quotes copied from the extracted text; ligatures (ﬁ) corrected to plain letters.

**Quotes:**

- `hsu2022hands`, Abstract, p. 1 — supports: Hand-centric view reduces observability relative to third-person view, while improving training efficiency and generalisation (both halves of the claim). — *verified*

  > Compared with the more commonly used global third-person perspective, a hand-centric (eye-in-hand) perspective affords reduced observability, but we find that it consistently improves training efficiency and out-of-distribution generalization.

- `hsu2022hands`, Abstract, p. 1 — supports: Caveat: the generalisation/efficiency benefit holds only when hand-centric observability is sufficient. Supports qualifying the paper's sentence. — *verified*

  > However, this is only the case when hand-centric observability is sufficient; otherwise, including a third-person perspective is necessary for learning, but also harms out-of-distribution generalization.

**Agent's note:** The abstract directly states both halves of the claim: a hand-centric (eye-in-hand) view affords reduced observability compared with a third-person view, and it consistently improves training efficiency and out-of-distribution generalization. The paper's sentence "trades observability of the scene for generalisation" matches this framing. One caveat from the same abstract: the benefit holds only when hand-centric observability is sufficient; otherwise a third-person view is needed and harms generalization. The paper's sentence does not state this condition, but it is not contradicted by it. Optional tightening if desired: "...a hand-centric view trades observability of the scene for generalisation and training efficiency \\citep{hsu2022hands}, though this holds when the hand-centric view remains sufficiently observable." The claim as worded is supported.

## S07 (§1)

**Claim the citation must support:** The workshop names tracking beyond SLAM and the egocentric viewpoint gap as open problems.

**Current text** (`sections/idea.tex`):

> wo of the open problems this workshop names \citep{umiarena2026} are in-the-wild tracking that does not rest on SLAM, and the viewpoint gap between what a handheld device records and what the robot sees.

**Verdict:** supported

**Sources:**

- `umiarena2026`: `library/umiarena2026/page.html`; https://umi-arena.airoa.io/ — Live workshop web page fetched with curl -L on 2026-10-16 (saved as page.html; extracted text in text.txt alongside). Not a preprint. The page is static HTML and the relevant text is present in the raw HTML.

**Quotes:**

- `umiarena2026`, Track 3 · Contributed Papers section — supports: The page presents these as open problems of UMI-style manipulation, the setting in which the workshop names its open problems. — *verified*

  > We invite 4-page, non-archival papers on the open problems of UMI-style manipulation.

- `umiarena2026`, Topics of interest list, under Track 3 · Contributed Papers — supports: (a) In-the-wild tracking beyond SLAM, the first open problem named in the paper sentence. — *verified*

  > Robust in-the-wild tracking and localization beyond fragile SLAM

- `umiarena2026`, Topics of interest list, under Track 3 · Contributed Papers — supports: (b) The viewpoint gap between handheld data collection and robot deployment, the second open problem named in the paper sentence. — *verified*

  > The egocentric viewpoint gap between handheld collection and robot deployment

**Agent's note:** Both parts are backed. The page lists "Robust in-the-wild tracking and localization beyond fragile SLAM" and "The egocentric viewpoint gap between handheld collection and robot deployment" as topics of interest, and Track 3 calls the topic list open problems ("the open problems of UMI-style manipulation"). The paper's "tracking that does not rest on SLAM" is a slightly stronger paraphrase of "beyond fragile SLAM", but it is a fair reading. If you want the closest wording, use "in-the-wild tracking and localization beyond fragile SLAM". The page itself says the topics are "not limited to", so "names among its open problems" is accurate and "names two of its open problems" is not a claim the page makes. The page is a live web page, so the wording may change after this snapshot.

## S08 (§1)

**Claim the citation must support:** Gaze leads the hand in everyday manipulation.

**Current text** (`sections/idea.tex`):

> The collector's head tracks the hand by habit, since gaze goes to each object just before the hand acts on it \citep{land2001eye};

**Verdict:** supported

**Resolution:** Supported (PDF supplied by hand): Land & Hayhoe show gaze leads each manipulative action by about half a second. Reworded: "the head follows the hand ... since gaze leads the hand" read as a contradiction; now "the head tracks the hand by habit, since gaze goes to each object just before the hand acts on it".

**Sources:**

- `land2001eye`: `library/land2001eye/paper.pdf`; https://doi.org/10.1016/S0042-6989(01)00102-X — publisher PDF, downloaded by hand by Igor via library access on 2026-10-16

**Quotes:**

- `land2001eye`, Abstract — supports: gaze leads the hand — *verified*

  > indicating that eye movements are planned into the motor pattern and lead each action

- `land2001eye`, Section 1 Introduction — supports: gaze precedes the action by a fraction of a second — *verified*

  > the relevant eye movements usually precede the motor acts they mediate by a fraction of a second

- `land2001eye`, Fig. 2 caption (tea-making, 137 object-related actions) — supports: measured lead of fixation over manipulation — *verified*

  > Movements of the whole body (A) precede the first fixation (B) by an average of 0.61 s (a), and these precede the first signs of manipulation (C) by 0.56 s (b).

- `land2001eye`, Section 2 — supports: everyday tasks (tea-making, sandwich-making), head free to move — *verified*

  > In both cases the location of foveal gaze was monitored continuously using a head-mounted eye tracker with an accuracy of about 1°, and the head was free to move.

**Agent's note:** Checked in the main loop after Igor supplied the PDF (the agent found no legal open copy). Supports "gaze leads the hand in everyday manipulation" (tea- and sandwich-making, head-mounted eye tracker, head free). It is about gaze (eyes, with the head free), not head pose; "the head follows the hand" is our own observation. Wording note: "the head follows the hand ... since gaze leads the hand" reads as a contradiction. Suggested: "The collector's head tracks the hand by habit, since gaze goes to each object just before the hand acts on it \citep{land2001eye};"

## S09 (§1)

**Claim the citation must support:** AprilTags are printed fiducials that give a 6-DoF pose from one image.

**Current text** (`sections/idea.tex`):

> From its view the fiducial ball gives the pose, the jaw tags give the width, and printed AprilTag \citep{olson2011apriltag} tiles taped on the table give the world frame, so the glove itself carries no electronics at all, and the scene around the gripper, bin included, stays in frame.

**Verdict:** partial

**Resolution:** Fixed: Wang & Olson 2016 does not state 6-DoF pose for AprilTags; dropped from this sentence. Olson 2011 covers it. (Code: OpenCV aruco with AprilTag dictionaries and CORNER_REFINE_APRILTAG.)

**Sources:**

- `olson2011apriltag`: `library/olson2011apriltag/paper.pdf`; https://april.eecs.umich.edu/media/pdfs/olson2011tags.pdf — Author's open copy of the ICRA 2011 paper from the APRIL lab site. Text extracted with gs to text.txt in the same directory. The PDF uses the fi ligature, so 'fiducial' is spelled out in the quotes below.
- `wang2016apriltag2`: `library/wang2016apriltag2/paper.pdf`; https://april.eecs.umich.edu/media/pdfs/wang2016iros.pdf — Author's open copy of the IROS 2016 paper from the APRIL lab site. Text extracted with gs to text.txt in the same directory. The PDF uses the fi ligature, so 'fiducial' is spelled out in the quotes below.

**Quotes:**

- `olson2011apriltag`, Abstract — supports: AprilTag detections give the full 6-DoF pose of the tag relative to the camera — *verified*

  > allowing full 6 DOF localization of features from a single image.

- `olson2011apriltag`, Section I, Introduction, left column — supports: Detections give the tag pose relative to the camera (position and orientation) — *verified*

  > visual fiducial systems provide camera-relative position and orientation of a tag.

- `olson2011apriltag`, Section I, Introduction, right column — supports: AprilTag is a printed visual fiducial system — *verified*

  > the targets can be cheaply printed on a standard printer

- `wang2016apriltag2`, Abstract — supports: AprilTag 2 is an improved detector — *verified*

  > This work describes AprilTag 2, a completely redesigned tag detector that improves robustness and efficiency compared to the original AprilTag system.

- `wang2016apriltag2`, Section III, Tag Detector (quad edge refinement) — supports: AprilTag 2 detections are used for pose estimation (only partial support for 6-DoF) — *verified*

  > the edge refinement step improves localization accuracy when tags are used for pose estimation.

**Agent's note:** Olson 2011 supports the claim as worded: its abstract says the tag system allows full 6-DOF localization from a single image, and its introduction says the targets are printed on a standard printer and give camera-relative position and orientation. Wang & Olson 2016 supports only the "improved detector" part explicitly and says tags are used for pose estimation. It does not state that AprilTag 2 gives a full 6-DoF pose. Its only "full 6-DOF pose" sentence describes ARToolKit markers, not AprilTags, so it must not be cited for that. Suggested minimal rewording: "printed AprilTag \citep{olson2011apriltag} tiles taped on the table give the world frame, since detections give the full 6-DoF tag pose relative to the camera \citep{olson2011apriltag}; AprilTag 2 \citep{wang2016apriltag2} is an improved detector for such pose estimation." Source files are in the library directories listed above, with text.txt beside each PDF.

## S10 (§1)

**Claim the citation must support:** EgoMimic co-trains on robot data and egocentric human data from head-worn glasses, with tracked hand pose.

**Current text** (`sections/idea.tex`):

> EgoMimic \citep{kareer2025egomimic} co-trains one policy on robot data and egocentric human video from head-worn glasses, with the hand's pose tracked from the video;

**Verdict:** supported

**Sources:**

- `kareer2025egomimic`: `library/kareer2025egomimic/paper.pdf`; https://arxiv.org/pdf/2410.24221 — arXiv:2410.24221v1 preprint (Kareer et al., EgoMimic), not the ICRA 2025 proceedings version. Text extracted with gs to /home/x1/github/yam-umi/paper-headcam/resources/library/kareer2025egomimic/text.txt. Ligature-broken words were checked against the text and the quotes below avoid them.

**Quotes:**

- `kareer2025egomimic`, Section I (Introduction), contributions paragraph, right column, p. 1-2 — supports: EgoMimic co-trains a single policy on robot data and egocentric human data. — *verified*

  > unify and treat human and robot data as equals and co-train from both data sources with a single end-to-end policy.

- `kareer2025egomimic`, Figure 1 caption, p. 1 — supports: The human data is recorded with head-worn Project Aria glasses (egocentric), not a held device. — *verified*

  > wearing a pair of Project Aria glasses while performing manipulation tasks with our own hands.

- `kareer2025egomimic`, Section III-A (Data Collection Systems and Hardware Design), p. 3 — supports: Aria glasses are head-worn egocentric capture devices. — *verified*

  > Aria glasses are head-worn devices for capturing multimodal egocentric data.

- `kareer2025egomimic`, Section III-A, p. 3 — supports: Hand tracking is performed from the glasses' egocentric camera data. — *verified*

  > two mono-color scene cameras for device pose and hand tracking

- `kareer2025egomimic`, Section III-B (Aria Machine Perception Services), p. 4 — supports: The hand pose is estimated from the glasses' recordings by the MPS hand-tracking service, not from a gripper measurement. — *verified*

  > estimates device pose via SLAM, a semi-dense pointcloud of the environment, hand tracking relative to the device frame, and even eye gaze.

**Agent's note:** The claim is supported as worded. The source states that EgoMimic co-trains human egocentric data and robot data with a single end-to-end policy, that the human data is captured with head-worn Project Aria glasses, and that the hand pose comes from hand tracking on the glasses' egocentric data via MPS. The source does not describe a held device with measured gripper width for the human data; the held grippers it mentions are other prior works (ref. [4]). The sources are an arXiv v1 preprint, so the ICRA 2025 version was not checked for wording differences.

## S11 (§1)

**Claim the citation must support:** AV-ALOHA and Open-TeleVision move a robot camera with the operator's head through a VR headset.

**Current text** (`sections/idea.tex`):

> Active-vision teleoperation \citep{chuang2025avaloha,cheng2024opentelevision} moves a robot camera with the operator's head through a VR headset;

**Verdict:** supported

**Sources:**

- `chuang2025avaloha`: `library/chuang2025avaloha/paper.pdf`; https://arxiv.org/pdf/2409.17435 — arXiv preprint, latest version fetched by curl (the text footer reads arXiv:2409.17435v2, 8 Mar 2025). Text extracted to /home/x1/github/yam-umi/paper-headcam/resources/library/chuang2025avaloha/text.txt with gs. The two-column layout interleaves text, so quotes were checked against the extracted lines and ligatures were corrected by hand.
- `cheng2024opentelevision`: `library/cheng2024opentelevision/paper.pdf`; https://arxiv.org/pdf/2407.01512 — arXiv preprint of the CoRL 2024 paper, as fetched by curl. Text extracted to /home/x1/github/yam-umi/paper-headcam/resources/library/cheng2024opentelevision/text.txt with gs. Ligatures were corrected by hand in the quotes.

**Quotes:**

- `chuang2025avaloha`, Section II (Related Work / system description, left column, around the AV-ALOHA description paragraph; text file lines 82-90) — supports: AV-ALOHA: a camera on a robot arm is moved by the teleoperator's head (and body) motion, tracked via a VR headset, during teleoperation/demonstration — *verified*

  > During demonstration, the AV arm is controlled by the user’s head and body movements to dynamically adjust the camera perspective. The user wears a VR headset that streams a live feed from the camera attached to the AV arm

- `chuang2025avaloha`, Section III, AV-ALOHA: Description of the Robot System (left column, text file lines 153-158) — supports: AV-ALOHA: the camera-carrying arm (AV arm, a ZED mini stereo camera) follows the operator's head movement, tracked by a VR headset — *verified*

  > whose movements are controlled by the operator’s head movement via a Meta Quest 2 or 3 VR headset [51]

- `chuang2025avaloha`, Figure 1 caption (text file lines 29-30) — supports: AV-ALOHA: the VR headset movement controls the robot camera arm during teleoperation — *verified*

  > In this system, a VR headset provides a live feed from the AV camera to the user. The movement of the VR headset controls the AV arm.

- `cheng2024opentelevision`, Section 1 Introduction, paragraph on perception (text file lines 75-79) — supports: Open-TeleVision: an actuated camera on the robot head is moved to follow the teleoperator's head during teleoperation, with the VR device as the tracking/display device — *verified*

  > We use a single active stereo RGB camera on the robot head equipped with 2 or 3 DoFs actuation, mimicking human head movement to observe a large workspace. During teleoperation, the camera moves along with the operator’s head, streaming real-time, ego-centric 3D observations to the VR device.

- `cheng2024opentelevision`, Section 2 TeleVision System (text file lines 106-108) — supports: Open-TeleVision: the VR headset tracks the operator's head pose, which is used to drive the robot's head/camera — *verified*

  > The VR devices stream the operator’s hand, head and wrist poses in SE(3) to the server, which handles the human-to-robot motion retargeting.

**Agent's note:** Fully supported as worded. Both papers describe a robot camera that follows the operator's head through a VR headset during teleoperation. Open-TeleVision uses an actuated robot head (2 or 3 DoF). AV-ALOHA uses a dedicated 7-DoF arm carrying a stereo camera. One nuance: in AV-ALOHA the arm is driven by head and body (neck) movement together, not by head motion alone, so "follow the teleoperator's head motion" is a slight simplification. The paper sentence "moves a robot camera with the operator's head through a VR headset" is accurate as written. Optionally "with the operator's head (and body) movements" would be more exact for AV-ALOHA. No rewording is required.

## S12 (§2)

**Claim the citation must support:** The YAM is an I2RT arm with a gripper.

**Current text** (`sections/system.tex`):

> he glove is the fiducial-tracked replica of the YAM's gripper \citep{i2rtyam} from \citet{yamumi2026}: the robot's own fingers on a rack-and-pinion linear mechanism, an 11-face \SI{15}{mm} ArUco \citep{garrido2014aruco} dodecahedron on the back of the hand in the manner of DodecaPen \citep{wu2017dodecapen} and, on each jaw, a printed \emph{tail}: a wedge behind the finger carrying \SI{12}{mm} AprilTags on five faces, beside a fixed tag on the gripper back.

**Verdict:** partial

**Resolution:** No change: the sentence only says "the YAM's gripper"; the agent flagged "linear/parallel-jaw", which this sentence does not claim.

**Sources:**

- `i2rtyam`: `library/i2rtyam/page.html`; https://i2rt.com/products/yam-6-dof-arm — Live I2RT product page for the YAM 6-DoF arm, saved as page.html on the date of the run; plain-text extract at /home/x1/github/yam-umi/paper-headcam/resources/library/i2rtyam/text.txt. I2RT's GitHub org (github.com/i2rt-robotics) was checked via the public API only: the i2rt repo has no description, and the org's yam-abc-reproduce repo describes YAM as off-the-shelf i2rt hardware, but neither states the gripper type. No I2RT docs page was found.

**Quotes:**

- `i2rtyam`, Product page, spec block under the 'YAM' heading (text.txt line 177) — supports: The YAM has a gripper (the 95 mm stroke is the only gripper spec given) — *verified*

  > Gripper Throw: 95 mm

- `i2rtyam`, Product page, 'Precision Meets Power in a Compact Form' section (text.txt line 182) — supports: The YAM has a gripper; the page gives no finger or jaw geometry — *verified*

  > Our patent-pending gripper delivers an impressive 95 mm throw while maintaining a compact footprint

- `i2rtyam`, Product page header/brand line (text.txt line 3) — supports: The arm is made by I2RT Robotics — *verified*

  > – I2RT Robotics

**Agent's note:** The page supports that the YAM is a robot arm by I2RT Robotics and that it has a gripper with a 95 mm throw. It does not support the qualifiers "linear" or "parallel-jaw": the page never uses those words, and the grep of the saved HTML found no jaw or finger description. Suggested minimal rewording of the sentence, which the quotes support: "The glove is the fiducial-tracked replica of the YAM's gripper \citep{i2rtyam} from \citet{yamumi2026}" can stay as is, provided the paper does not claim the gripper is linear or parallel-jaw. If the paper needs that claim, it needs a different source, such as I2RT's gripper documentation or CAD, which I did not find. Also consider adding the 95 mm throw as the cited fact if the glove's geometry depends on it.

## S13 (§2)

**Claim the citation must support:** The YAM-UMI glove: robot fingers, rack-and-pinion linear mechanism, 11-face 15 mm ArUco ball on the back of the hand, jaw tags.

**Current text** (`sections/system.tex`):

> he glove is the fiducial-tracked replica of the YAM's gripper \citep{i2rtyam} from \citet{yamumi2026}: the robot's own fingers on a rack-and-pinion linear mechanism, an 11-face \SI{15}{mm} ArUco \citep{garrido2014aruco} dodecahedron on the back of the hand in the manner of DodecaPen \citep{wu2017dodecapen} and, on each jaw, a printed \emph{tail}: a wedge behind the finger carrying \SI{12}{mm} AprilTags on five faces, beside a fixed tag on the gripper back.

**Verdict:** partial

**Resolution:** No change: "on the back of the hand" is in the device paper (manual quote below). Note Yosub has since replaced "two AprilTags in the jaws" with the tail design, which these quotes do not cover.

**Sources:**

- `yamumi2026`: `library/yamumi2026/README.md`; https://github.com/YosubShin/yam-umi (checked out at /home/x1/github/yam-umi) — Project's own repository files, not a preprint. Copies in the library dir: README.md (byte-identical to repo README.md, already present), pos-tracking_README.md (copy of pos-tracking/README.md), assembly.md (copy of docs/assembly.md). Quotes below are from these copies. paper/main.tex was not used as the source for the claim.

**Quotes:**

- `yamumi2026`, README.md, Overview, paragraph after the summary table (line 35-36) — supports: The glove reuses the YAM's own rail-and-pinion linear mechanism — *verified*

  > reproduces the gripper's own rail-and-pinion mechanism

- `yamumi2026`, README.md, Design section (line 54) — supports: The glove uses the robot's own gripper fingers — *verified*

  > YAM-UMI keeps the robot's stock gripper fingers and camera mount

- `yamumi2026`, README.md, mechanism section (lines 83-84) — supports: Linear rail mechanism with rack-and-pinion coupling of the jaws — *verified*

  > YAM-UMI carries the motion on two MGN9 linear rails instead, with a single pinion between two racks — one rack per jaw — to keep the jaws synchronized.

- `yamumi2026`, pos-tracking_README.md, section Markers (lines 39-40) — supports: The ball carries 15 mm ArUco markers on eleven faces (dodecahedral ball) — *verified*

  > nominal 15 mm black squares on 19.5 mm tiles, IDs 25–35, applied to eleven faces of the ball.

- `yamumi2026`, pos-tracking_README.md, intro (line 9) — supports: The dodecahedral ArUco ball is mounted on a stalk — *verified*

  > a dodecahedral ArUco marker ball on a stalk

- `yamumi2026`, pos-tracking_README.md, figure alt text (line 19) — supports: Placement of the ball on the wrist stalk, not explicitly on the back of the hand — *verified*

  > with the dodecahedral ArUco marker ball mounted on its wrist stalk

- `yamumi2026`, assembly.md, section Apply the gripper-tip markers (line 296; bold markup removed) — supports: Two AprilTags in the jaws — *verified*

  > Two 6 mm AprilTag 16h5 markers, IDs 2 and 3, go on the top of the gripper fingers, one per jaw

- `yamumi2026`, README.md, Signal/source table (line 104) — supports: AprilTag markers on the gripper tips (jaws) — *verified*

  > 6 mm AprilTag (16h5) markers on the gripper tips

- `yamumi2026`, device paper paper/main.tex, §1 The device, Principle (added by hand; the agent missed it) — supports: ball on the back of the hand — *verified*

  > A dodecahedral ball with eleven \SI{15}{mm} ArUco faces on the back of the hand gives the pose

**Agent's note:** The rail-and-pinion mechanism, the reuse of the YAM's own fingers, the 11-face 15 mm ArUco dodecahedral ball and the two AprilTags in the jaws are all backed by the quotes. The one unsupported detail is "on the back of the hand": the sources place the ball on a wrist stalk (the figure alt text says "mounted on its wrist stalk") and say the hand can hide it, but never say "back of the hand". Minimal rewording that the quotes support: "...and an 11-face 15 mm ArUco dodecahedral ball mounted on a wrist stalk, two AprilTags in the jaws." Also note that the "two AprilTags" detail comes from docs/assembly.md, not README.md (README.md only says "AprilTag markers on the gripper tips").

## S14 (§2)

**Claim the citation must support:** ArUco is a square binary fiducial system whose markers give the camera pose.

**Current text** (`sections/system.tex`):

> he glove is the fiducial-tracked replica of the YAM's gripper \citep{i2rtyam} from \citet{yamumi2026}: the robot's own fingers on a rack-and-pinion linear mechanism, an 11-face \SI{15}{mm} ArUco \citep{garrido2014aruco} dodecahedron on the back of the hand in the manner of DodecaPen \citep{wu2017dodecapen} and, on each jaw, a printed \emph{tail}: a wedge behind the finger carrying \SI{12}{mm} AprilTags on five faces, beside a fixed tag on the gripper back.

**Verdict:** supported

**Resolution:** Supported (PDF supplied by hand): ArUco is a square binary fiducial system designed for camera pose estimation.

**Sources:**

- `garrido2014aruco`: `library/garrido2014aruco/paper.pdf`; https://doi.org/10.1016/j.patcog.2014.01.005 — publisher PDF, downloaded by hand by Igor via library access on 2026-10-16

**Quotes:**

- `garrido2014aruco`, Abstract — supports: fiducial system for camera pose — *verified by hand*

  > This paper presents a fiducial marker system specially appropriated for camera pose estimation in applications such as augmented reality and robot localization.

- `garrido2014aruco`, Abstract — supports: square binary markers; dictionary generation and detection — *verified by hand*

  > we derive the maximum theoretical inter-marker distance that dictionaries of square binary markers can have. Second, a method for automatically detecting the markers and correcting possible errors is proposed.

- `garrido2014aruco`, Section 1 Introduction — supports: square markers give the camera pose from their corners — *verified*

  > The reason why is that they allow us to extract the camera pose from their four corners, given that the camera is properly calibrated.

**Agent's note:** Checked in the main loop after Igor supplied the PDF (the agent found no legal open copy). Supports the claim as worded: ArUco is a square binary fiducial marker system (dictionary generation, detection with error correction) designed for camera pose estimation. The dodecahedron and 15 mm size in the sentence are ours, not this paper's.

## S15 (§2)

**Claim the citation must support:** DodecaPen tracks 6-DoF pose with one camera and a marker-covered dodecahedron.

**Current text** (`sections/system.tex`):

> he glove is the fiducial-tracked replica of the YAM's gripper \citep{i2rtyam} from \citet{yamumi2026}: the robot's own fingers on a rack-and-pinion linear mechanism, an 11-face \SI{15}{mm} ArUco \citep{garrido2014aruco} dodecahedron on the back of the hand in the manner of DodecaPen \citep{wu2017dodecapen} and, on each jaw, a printed \emph{tail}: a wedge behind the finger carrying \SI{12}{mm} AprilTags on five faces, beside a fixed tag on the gripper back.

**Verdict:** supported

**Sources:**

- `wu2017dodecapen`: `library/wu2017dodecapen/paper.pdf`; https://research.facebook.com/file/565262174921432/uist2017_pen.pdf — Author/publisher open copy of the UIST 2017 paper (Wu et al., 'DodecaPen: Accurate 6DoF Tracking of a Passive Stylus'), downloaded from the Facebook Research link. Plain-text extraction saved as text.txt alongside; quotes were checked against the rendered PDF pages.

**Quotes:**

- `wu2017dodecapen`, Figure 1 caption, p. 1 — supports: DodecaPen tracks the 6-DoF pose of an object with a single camera — *verified*

  > Our proposed system can track the 6DoF pose of (a) a calibrated pen (the DodecaPen) from (b) a single camera with submillimeter accuracy.

- `wu2017dodecapen`, Introduction, paragraph 1, p. 1 — supports: tracked object is a dodecahedron covered in square binary fiducial markers, tracked with one camera — *verified*

  > Our system is particularly easy to implement, requiring only a monocular camera, a 3D printed dodecahedron, and hand-glued binary square markers.

- `wu2017dodecapen`, Section 'Dodecahedron Design' (continuation), p. 3 (text in column 1 after Figure 2) — supports: the markers are glued onto the dodecahedron's surface; also gives the source's own dimensions — *verified*

  > Each edge of the resulting dodecahedron is 12.9 mm in length, while the markers glued on its surface have edges of length 10.8 mm and are printed with a laser printer.

- `wu2017dodecapen`, Section 'Dodecahedron Design', p. 2 — supports: the dodecahedron is used in place of single markers to track the object's pose — *verified*

  > Although binary square fiducial markers are commonly attached to cubes [9, 14], pose recovery can fail when only a single marker is visible due to an ambiguity in the PnP problem [32]. By substituting a dodecahedron as the tracked object, we ensure that at least two planes are visible in most cases, eliminating the ambiguity.

**Agent's note:** The claim as worded is supported: DodecaPen uses a single monocular camera to track the 6-DoF pose of a calibrated pen-mounted dodecahedron whose faces carry hand-glued binary square (ArUco-style) fiducial markers. The paper's sentence says the 15 mm, 11-face ArUco dodecahedron is built "in the manner of DodecaPen". That phrasing is fine, but the source's own dodecahedron has a 12.9 mm edge, not 15 mm. If the sentence is meant to describe DodecaPen's dimensions, it should not state 15 mm and should cite the 12.9 mm figure; if it only describes the construction method, no change is needed. The source gives the marker count as no face count, so "11-face" is not checked by this citation and is not verified here.

## S16 (§2)

**Claim the citation must support:** The tile-to-base link is a robot-world/hand-eye calibration (Shah 2013).

**Current text** (`sections/system.tex`):

> (i) and (ii) compose to the gripper's pose in the tile frame, and a tile-to-robot-base link from a one-time hand-eye calibration on the robot \todo{Yosub: which solver? cite it (Shah 2013 if it is OpenCV's calibrateRobotWorldHandEye);

**Verdict:** partial

**Resolution:** Fixed: forward-cam-umi contains no robot-world solver (its docs say the hand-eye is robot-side and unreleased); Shah citation removed, \todo asks Yosub for the solver actually used.

**Sources:**

- `shah2013robotworld`: `library/shah2013robotworld/paper.pdf`; https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=910225 — NIST-hosted copy of Shah, 'Solving the Robot-World/Hand-Eye Calibration Problem Using the Kronecker Product', J. Mechanisms and Robotics 5(3), 2013 (DOI 10.1115/1.4024473). Unpaywall reports no open-access location for this DOI, so this is the NIST repository copy, not the publisher PDF. Its first page carries the [DOI: 10.1115/1.4024473] line and the published-online date, so it is likely the published version, but this was not verified against the publisher. Extracted text at /home/x1/github/yam-umi/paper-headcam/resources/library/shah2013robotworld/text.txt.

**Quotes:**

- `shah2013robotworld`, Abstract (first page), and the same wording at Section 1 Introduction. The PDF renders the equals sign as a glyph that extracts as '¼'; read as AX=YB. — supports: Shah 2013 solves the robot-world/hand-eye problem AX=YB. — *verified by hand*

  > This paper constructs a separable closed-form solution to the robot-world/hand-eye calibration problem AX=YB.

- `shah2013robotworld`, Section 1 Introduction, setup of Fig. 1 — supports: Y is the unknown fixed transform between the robot-mounted camera and robot-mounted target (the hand-eye part, end effector to sensor/target). — *verified*

  > Both the camera for the computer vision system and the target for the sensor system are rigidly attached to a moving robot arm with a fixed unknown transformation Y between them.

- `shah2013robotworld`, Section 1 Introduction, setup of Fig. 1 — supports: X is the unknown fixed transform between the stationary sensor and the stationary object, i.e. the robot-world link. The paper does not name the robot base. — *verified by hand*

  > There is a fixed unknown transformation X between the stationary sensor and object.

**Agent's note:** Partially supported. The source supports the core of the claim: Shah 2013 gives a closed-form solution to the robot-world/hand-eye problem AX=YB, with X the fixed transform between the stationary sensor and object and Y the fixed transform between the robot-mounted camera and robot-mounted target. It does not support three parts of the sentence as written. (1) It never mentions a robot base or a tile/world frame; X is the sensor-to-object link, and mapping it to tile-to-robot-base is the paper's interpretation, not Shah's wording. (2) It says nothing about a session in which the robot carried the ball, or about fitting the link once from such a session. (3) It describes the problem in terms of poses, not a calibration target on tiles. Minimal rewording the quotes support: "a tile-to-robot-base link, fitted once from a session in which the robot carried the ball by solving the robot-world/hand-eye problem $AX{=}YB$ \citep{shah2013robotworld}," with the robot-to-tile role described by the authors themselves rather than attributed to Shah. Code check, forward-cam-umi at commit 65fded2 (2026-10-11), shallow clone in the scratchpad: no call to cv2.calibrateRobotWorldHandEye, cv2.calibrateHandEye or any hand-eye solver exists in the repo (grep for calibrateRobotWorldHandEye, CALIB_ROBOT_WORLD, calibrateHandEye, robotworld and handeye found nothing). The repo's own docs say the opposite: scripts/tiles_pose.py line 7-8 says 'On our side one hand-eye gives world -> robot base', docs/pilot-task.md lines 41-43 say 'tiles→robot from our hand-eye', and scripts/README.md lines 179 and 210-211 say hand-eye and robot-side tooling are not in this repo. So the tile-to-base link is produced by an external robot-side hand-eye calibration that is not in forward-cam-umi, and the method used there is not identified. Either the paper should cite the hand-eye solver actually used, or the claim should say the link comes from an external hand-eye calibration. The repo also does not say the link is fitted from a ball-carrying session."

## S17 (§2)

**Claim the citation must support:** SO-101 follower: printed, six STS3215 servos, about $120 of parts.

**Current text** (`sections/system.tex`):

> six-joint SO-101 follower arm \citep{so101}, printed and driven by six Feetech STS3215 servos (\$13.89 each;

**Verdict:** partial

**Resolution:** Fixed: official README gives STS3215 at $13.89 and a follower parts total of $121.94; numbers and footnote updated.

**Sources:**

- `so101`: `library/so101/README.md`; https://raw.githubusercontent.com/TheRobotStudio/SO-ARM100/main/README.md — README.md from the default branch of TheRobotStudio/SO-ARM100 (fetched via raw.githubusercontent.com). The BOM is embedded in the README's 'Sourcing Parts' section; no separate BOM file is linked. Plain-text copy saved as text.txt alongside.

**Quotes:**

- `so101`, README.md, section 'Sourcing Parts', heading above the follower BOM table (line 92) — supports: Identifies the follower-only BOM, separate from the two-arm bundle — *verified*

  > Parts for One Follower Arm:

- `so101`, README.md, 'Parts for One Follower Arm' table, row 1 (line 96); the Amount column in the same row reads 6 — supports: The follower arm uses six STS3215 servos (Amount = 6 in the follower table) — *verified*

  > STS3215 Servo 7.4V, 1/345 gear (C001)

- `so101`, README.md, 'Parts for One Follower Arm' table, Unit Cost (US) column of the STS3215 row (line 96) — supports: Per-servo unit cost of about $14 (US) — *verified*

  > $13.89

- `so101`, README.md, 'Parts for One Follower Arm' table, Total row, Unit Cost (US) column (line 102) — supports: Official follower-only BOM total of $121.94, which covers the servos plus a motor control board, USB-C cable, power supply, table clamp and screwdriver set — *verified*

  > $121.94

- `so101`, README.md, page title <h1> (line 3) — supports: Only source wording for 'open': the title says Open. The README does not state a license for the hardware. — *verified*

  > Standard Open SO-100 & SO-101 Arms

- `so101`, README.md, intro paragraph (line 25) — supports: Negative check: the open-source wording here refers to the LeRobot software library, not the arm hardware — *verified*

  > These arms are designed to work seamlessly with the open‑source 🤗 LeRobot library.

- `so101`, README.md, section 'Printing the Parts' (line 108) — supports: The arm parts are 3D printed — *verified*

  > A variety of 3D printers are acceptable to print the parts necessary of the follower and leader arm.

**Agent's note:** Supported: six STS3215 servos in the follower arm, about $14 per servo ($13.89 US unit cost), 3D printed parts, and an official follower-only BOM total of $121.94 (the paper's "about $120" is consistent with this). Not supported by the README: (1) "serial" bus servos. The word "serial" does not appear in the README; it only names the STS3215 servos and a Feetech software link. (2) "open-source" for the arm. The only open-source wording is in the title "Standard Open SO-100 & SO-101 Arms", and the intro's "open-source" refers to the LeRobot library. (3) "low-cost" is not stated as a claim, although a retailer link name reads "Low-Cost-AI-Arm-Kit". Also, the $121.94 total is for all follower parts, not servos alone, so "about $120 in parts" is accurate but should not be read as servo cost. Minimal rewording the sources support: "A six-joint SO-101 follower arm \citep{so101}, 3D printed and driven by six Feetech STS3215 servos (about \$14 each; about \$120 for the full follower parts list, including control board, power supply and clamps)." If "serial" and "open-source" are kept, they need a different source, such as Feetech's datasheet or the repo's license file.

## S18 (§2)

**Claim the citation must support:** ACT is the policy introduced by Zhao et al.

**Current text** (`sections/system.tex`):

> Every policy is ACT \citep{zhao2023act} trained with LeRobot \citep{lerobot2024}: one recipe, 50k steps, joint-space actions, best checkpoint by validation loss on the robot's held-out episodes.

**Verdict:** supported

**Sources:**

- `zhao2023act`: `library/zhao2023act/paper.pdf`; https://arxiv.org/pdf/2304.13705 — arXiv v1 preprint (23 Apr 2023) of Zhao, Kumar, Levine, Finn, RSS 2023 paper 'Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware'. Text extracted to /home/x1/github/yam-umi/paper-headcam/resources/library/zhao2023act/text.txt via gs txtwrite.

**Quotes:**

- `zhao2023act`, Abstract (p. 1) — supports: ACT is the imitation-learning algorithm introduced in this paper, named Action Chunking with Transformers. — *verified by hand*

  > we develop a simple yet novel algorithm, Action Chunking with Transformers (ACT), which learns a generative model over action sequences

- `zhao2023act`, Section I (Introduction), contributions paragraph, left column (p. 1) — supports: The paper itself names the proposed imitation-learning method ACT, supporting that ACT is introduced in this paper. — *verified*

  > We name our method Action Chunking with Transformers (ACT)

**Agent's note:** Both quotes establish that ACT (Action Chunking with Transformers) is the imitation-learning algorithm introduced in the cited paper, which matches the required support. The quotes are verbatim from the arXiv v1 PDF text layer; line-break hyphenation and column interleaving were handled by taking contiguous left-column spans. The paper's sentence "Every policy is ACT \citep{zhao2023act} trained with LeRobot" is supported as far as the ACT attribution goes. The claim about training with LeRobot is not a property of this source and is outside this citation check.

## S19 (§2)

**Claim the citation must support:** LeRobot is an open PyTorch robot-learning library with ACT.

**Current text** (`sections/system.tex`):

> Every policy is ACT \citep{zhao2023act} trained with LeRobot \citep{lerobot2024}: one recipe, 50k steps, joint-space actions, best checkpoint by validation loss on the robot's held-out episodes.

**Verdict:** supported

**Sources:**

- `lerobot2024`: `library/lerobot2024/README.md`; https://raw.githubusercontent.com/huggingface/lerobot/main/README.md — README.md from the default branch (main) of github.com/huggingface/lerobot, fetched with curl -L. A plain-text copy is saved alongside as text.txt in the same directory. The README is the repository's own documentation, not a peer-reviewed paper.

**Quotes:**

- `lerobot2024`, README.md, intro paragraph under the logo — supports: LeRobot is a PyTorch library for real-world robotics — *verified*

  > LeRobot aims to provide models, datasets, and tools for real-world robotics in PyTorch.

- `lerobot2024`, README.md, footer — supports: LeRobot is Hugging Face's library — *verified*

  > Built by the <a href="https://huggingface.co/lerobot">LeRobot</a> team at <a href="https://huggingface.co">Hugging Face</a> with ❤️

- `lerobot2024`, README.md, BibTeX citation block (title field) — supports: open-source library for robot learning — *verified*

  > LeRobot: An Open-Source Library for End-to-End Robot Learning

- `lerobot2024`, README.md, section 'SoTA Models' — supports: provides policy implementations (general, including imitation learning) — *verified*

  > LeRobot implements state-of-the-art policies in pure PyTorch, covering Imitation Learning, Reinforcement Learning, Vision-Language-Action (VLA) models, World Models, and Reward Models, with more coming soon.

- `lerobot2024`, README.md, policy table under 'SoTA Models' — supports: ACT is among the policies LeRobot implements — *verified*

  > | **Imitation Learning**     | [ACT](./docs/source/policy_act_README.md)

- `lerobot2024`, README.md, 'SoTA Models' section, code block 'lerobot-train' — supports: ACT training is run through LeRobot (lerobot-train command) — *verified*

  > --policy.type=act

**Agent's note:** The claim is supported by the README. 'PyTorch library for real-world robot learning' is backed by 'LeRobot aims to provide models, datasets, and tools for real-world robotics in PyTorch.' 'Hugging Face's' is backed by the footer 'Built by the LeRobot team at Hugging Face'. 'Open-source' is backed by the BibTeX title 'An Open-Source Library for End-to-End Robot Learning' and the Apache 2.0 license badge. 'Provides an ACT policy implementation and training' is backed by the policy table listing ACT and the 'lerobot-train --policy.type=act' example. The README does not describe the ACT implementation's internals, and the README is documentation rather than a paper. The statement is supported as worded for the citation's purpose (library and ACT training). Note: the quote at the table row is a truncated fragment of a longer markdown table row; the quoted substring itself appears verbatim in the file.

## S20 (§2)

**Claim the citation must support:** The device paper paced the glove timeline and mapped measured width to commanded width.

**Current text** (`sections/system.tex`):

> The glove timeline is resampled to teleoperation pace and the measured width is mapped to the robot's commanded value, as in \citet{yamumi2026}, with one change that mattered: the closed-on-object anchor of that map is the squeeze level teleoperators actually command (the per-episode minimum, 0.22 of the stroke), not their median grasp command (0.25).

**Verdict:** supported

**Sources:**

- `yamumi2026`: `library/yamumi2026/paper.tex`; local repository file /home/x1/github/yam-umi/paper/main.tex (no public URL checked) — Copy of the project's device paper LaTeX source (unpublished working draft, titled 'YAM-UMI: A Fiducial-Tracked Glove that Collects Metrically Labelled Demonstrations for the YAM'), not a preprint or published version. refs.bib lists yamumi2026 as a misc entry titled 'YAM-UMI: hand-worn data collection device for the I2RT YAM linear gripper' (author Yosub Shin, github.com/YosubShin/yam-umi); I did not verify that the bib entry and the local draft are the same document, only that they describe the same project.

**Quotes:**

- `yamumi2026`, Results section, paragraph 'Policies from glove data.' (paper.tex, line ~80) — supports: Both parts of the claim: the glove timeline was resampled to teleoperation pace, and the measured width was mapped to the commanded value. — *verified*

  > resampling the glove timeline to teleop pace and mapping measured width to the commanded value through the robot's own fiducial-to-command relation

- `yamumi2026`, Table tab:policies caption (paper.tex, Results section) — supports: Confirms the same two operations as the definition of the 'paced' corpus used in the reported results. — *verified*

  > ``Paced'': glove corpus resampled to teleop pace with measured width mapped to the commanded value.

**Agent's note:** Supported. Both parts of the claim appear in the source. The source additionally says the width mapping goes 'through the robot's own fiducial-to-command relation', a detail the claim does not mention, so the sentence stays accurate as written. Two caveats: the source is an unpublished working draft in the repository, and the refs.bib entry for yamumi2026 has a different title, so confirm that the key points to this document before submission.

## S21 (§3)

**Claim the citation must support:** UMI observes through a wrist-mounted fisheye camera.

**Current text** (`sections/experiments.tex`):

> arms 5, 7 and 8 compare cameras, arm 5 being the conventional wrist-camera recipe \citep{chi2024umi}.

**Verdict:** partial

**Resolution:** No change needed: "conventional" is our own characterisation; UMI supports the wrist-camera recipe.

**Sources:**

- `chi2024umi`: `library/chi2024umi/paper.pdf`; https://arxiv.org/pdf/2402.10329 — arXiv 2402.10329 PDF (UMI, Chi et al., RSS 2024), downloaded with curl and moved into place; text extracted to resources/library/chi2024umi/text.txt. The directory already held a same-size paper.pdf and text.txt from another agent, which my download overwrote with an identical-size file.

**Quotes:**

- `chi2024umi`, Fig. 2 caption, Section I (Introduction) — supports: UMI's data collection hardware uses a wrist-mounted GoPro camera as the only sensor — *verified*

  > Left: Hand-held grippers for data collection, with a GoPro as the only sensor and recording device.

- `chi2024umi`, Section III, HD1 'Wrist-mounted cameras as input observation' — supports: The policy observation in UMI is the wrist-mounted camera, with no external camera — *verified*

  > We rely solely on wrist-mounted cameras, without the need for any external camera setups.

- `chi2024umi`, Section III, HD2 'Fisheye Lens for visual context' — supports: The wrist-mounted camera is a GoPro with a fisheye lens, used for the visual context of the policy — *verified*

  > We use a 155-degree Fisheye lens attachment on wrist-mounted GoPro camera, which provides sufficient visual context for a wide range of tasks, as shown in Fig. 2.

- `chi2024umi`, Section I (Introduction), contributions paragraph — supports: UMI's manipulation capability is demonstrated with only a wrist-mounted camera — *verified*

  > With just a wrist-mounted camera on the hand-held gripper (Fig. 2), we show that UMI is capable of achieving a wide range of manipulation tasks

**Agent's note:** The wrist-camera part is supported: UMI's policy observes through a wrist-mounted GoPro with a 155-degree fisheye lens, and the paper states it relies solely on wrist-mounted cameras. The word 'conventional' is not supported. UMI never calls the wrist-camera recipe conventional, so that characterization is ours, not the source's. Minimal rewording that the quotes support: 'arm 5 being the wrist-camera recipe of UMI \\citep{chi2024umi}' (or 'the UMI recipe, which observes through a wrist-mounted fisheye camera \\citep{chi2024umi}'). Quote text was taken from the two-column PDF extraction; the sentences read contiguously in the PDF.

## S22 (§3)

**Claim the citation must support:** Mobile ALOHA and EgoMimic co-train one policy on data from different sources.

**Current text** (`sections/experiments.tex`):

> love and teleoperated episodes are co-trained as one merged dataset, as data from different sources has been co-trained before: static and mobile robot data \citep{fu2024mobilealoha}, human and robot data \citep{kareer2025egomimic}.

**Verdict:** partial

**Resolution:** Fixed: EgoMimic co-trains human and robot data, not robot data from different sources; sentence now names both.

**Sources:**

- `fu2024mobilealoha`: `library/fu2024mobilealoha/paper.pdf`; https://arxiv.org/pdf/2401.02117 — arXiv 2401.02117v1 preprint of the CoRL 2024 paper; text extracted to /home/x1/github/yam-umi/paper-headcam/resources/library/fu2024mobilealoha/text.txt via gs
- `kareer2025egomimic`: `library/kareer2025egomimic/paper.pdf`; https://arxiv.org/pdf/2410.24221 — arXiv 2410.24221v1 preprint; existing text extract at /home/x1/github/yam-umi/paper-headcam/resources/library/kareer2025egomimic/text.txt was reused (garbled two-column text, quotes below checked against the PDF pages via gs)

**Quotes:**

- `fu2024mobilealoha`, Section 4 'Co-training with Static ALOHA Data', p. 5 — supports: Mobile ALOHA co-trains a single policy on a mixture of its own robot data and existing static ALOHA data from a different platform — *verified*

  > We sample with equal probability from the static ALOHA data Dstatic and the Mobile ALOHA data Dm .

- `fu2024mobilealoha`, Section 4 'Co-training with Static ALOHA Data', p. 5 — supports: Mobile ALOHA co-trains with existing static ALOHA data — *verified*

  > In this work, we use a co-training pipeline that leverages the existing static ALOHA datasets to improve the performance of imitation learning for mobile manipulation

- `kareer2025egomimic`, Abstract, p. 1 — supports: EgoMimic co-trains on human and robot data — *verified*

  > (4) an imitation learning architecture that co-trains on human and robot data.

- `kareer2025egomimic`, Abstract, p. 1 — supports: EgoMimic trains one unified policy on the combined human and robot data sources — *verified*

  > our approach treats human and robot data equally as embodied demonstration data and learns a unified policy from both data sources.

- `kareer2025egomimic`, Section I (Introduction), p. 2 — supports: Single-policy co-training across data sources — *verified*

  > unify and treat human and robot data as equals and co-train from both data sources with a single end-to-end policy.

**Agent's note:** Mobile ALOHA fully supports the claim: it co-trains one policy on its own data plus the existing static ALOHA datasets, sampling from the two with equal probability. EgoMimic supports the co-training of a single policy across two sources, but its second source is human egocentric video with 3D hand tracking, not robot data, so 'robot data from different sources' is not accurate for EgoMimic. Minimal rewording the quotes support: "Glove and teleoperated episodes are co-trained as one merged dataset, as data from different sources (static robot data in Mobile ALOHA, human and robot data in EgoMimic) has been before \\citep{fu2024mobilealoha,kareer2025egomimic}." A shorter alternative: "...as data from different sources has been co-trained before \\citep{...}."

## S23 (§3)

**Claim the citation must support:** Validation loss is a poor predictor of rollout success.

**Current text** (`sections/experiments.tex`):

> offline loss is known to be a weak proxy for rollout success \citep{mandlekar2021robomimic}.

**Verdict:** supported

**Sources:**

- `mandlekar2021robomimic`: `library/mandlekar2021robomimic/paper.pdf`; https://arxiv.org/pdf/2108.03298 — arXiv 2108.03298 preprint of the CoRL 2021 paper (not the publisher's version). Extracted text saved alongside at /home/x1/github/yam-umi/paper-headcam/resources/library/mandlekar2021robomimic/text.txt. Ligatures (ﬁ, ﬂ) corrected in quotes.

**Quotes:**

- `mandlekar2021robomimic`, Appendix G, 'Additional Results on Policy Selection', paragraph 'Success rate can increase even while validation loss increases substantially.' — supports: Offline/validation loss is a poor predictor of rollout success: the sentence is the paper's own conclusion from the checkpoint analysis, supporting 'offline loss is known to be a weak proxy for rollout success'. — *verified*

  > This further shows that validation loss is a poor measure of policy performance.

- `mandlekar2021robomimic`, Section 4.5, 'Selecting a Policy to Evaluate (C4)' — supports: Checkpoint selection by lowest validation loss (common in supervised learning) underperforms selection by online rollouts; the quote covers the comparison, since the sentence refers to selecting by best validation loss versus the best checkpoint evaluated by rollouts. — *verified*

  > the selected policy is significantly worse than the best one (10% to 100% decrease).

- `mandlekar2021robomimic`, Appendix G, 'Additional Results on Policy Selection', paragraph 'Increasing the amount of validation data does not improve policy selection using validation loss.' — supports: Concrete numerical evidence that the lowest-validation-loss policy has a much lower success rate than the best policy (Square PH: 80.7 vs 2.7). Note that the PDF text extraction merges some words; the spaced form is 'the best policy on Square (PH) achieves 80.7 ± 0.9, while the policy achieving the lowest validation loss achieves 2.7 ± 1.9'. — *verified*

  > the best policy onSquare(PH)achieves 80.7±0.9, while the policy achieving the lowest validation loss achieves 2.7±1.9

**Agent's note:** The cited source supports the claim as worded. Section 4.5 states that selecting by lowest validation loss yields a policy significantly worse than the best checkpoint (10% to 100% decrease), and Appendix G concludes that validation loss is a poor measure of policy performance, with a worked Square (PH) example (80.7 vs 2.7 success rate). The paper's sentence says 'offline loss is known to be a weak proxy', which the source backs; the phrase 'known to be' is the paper's framing and is supported by the authors' own empirical finding rather than a prior-literature claim. Optional minimal tightening: 'offline validation loss was a poor proxy for rollout success in robomimic' if the authors want to attribute only the empirical finding. The third quote is a verbatim-as-extracted copy with a merged word ('onSquare(PH)achieves'); use the spaced form when quoting in the paper.

## S24 (§4)

**Claim the citation must support:** Bundle adjustment jointly refines structure and cameras by minimising reprojection error.

**Current text** (`sections/limitations.tex`):

> he tile layout is refit from one session by median single-tile poses rather than bundle-adjusted \citep{triggs2000bundle};

**Verdict:** supported

**Sources:**

- `triggs2000bundle`: `library/triggs2000bundle/paper.pdf`; https://inria.hal.science/inria-00548290/document — Open HAL copy of Triggs, McLauchlan, Hartley, Fitzgibbon, 'Bundle Adjustment - A Modern Synthesis' (Vision Algorithms 2000, LNCS 1883). Text extracted with gs to text.txt in the same directory.

**Quotes:**

- `triggs2000bundle`, Abstract, p. 1 — supports: Definition: bundle adjustment is joint nonlinear refinement of 3D structure and camera (viewing) parameters. — *verified*

  > Bundle adjustment is the problem of refining a visual reconstruction to produce jointly optimal structure and viewing parameter estimates.

- `triggs2000bundle`, Section 2.1 The Projection Model, p. 5 — supports: Structure and camera parameters are estimated jointly by minimising a total error over the observations. — *verified*

  > To estimate the unknown 3D feature and camera parameters from the observations, and hence reconstruct the scene, we minimize some measure (discussed in §3) of their total prediction error.

- `triggs2000bundle`, Section 2.1 The Projection Model, p. 5 — supports: For image observations the prediction error is the image-projection residual, i.e. reprojection error. — *verified*

  > In the case of image observations the predictive model is image projection

- `triggs2000bundle`, Section 2.1 The Projection Model, p. 5 — supports: Bundle adjustment is a nonlinear optimisation over scene (structure) and camera parameters. — *verified*

  > optimizing a complicated nonlinear cost function (the total prediction error) over a large nonlinear parameter space (the scene and camera parameters).

**Agent's note:** The source supports the claim as worded. Bundle adjustment is defined as refining structure and viewing parameters to jointly optimal estimates (Abstract), it is a nonlinear minimisation of total prediction error over the scene and camera parameters (Sec. 2.1), and for image observations the predictive model is image projection, which is reprojection error. The paper does not use the phrase 'reprojection error' verbatim, and it speaks of 'total prediction error' rather than 'over all observations'. The 'landmark/marker' wording maps onto the paper's 3D feature points X_p. The sentence in the paper needs no rewording, though the local judgment of the phrase 'reprojection error' is an inference from the image-projection model, not a quoted phrase.

## S25 (§4)

**Claim the citation must support:** YAM-UMI hardware and forward-cam-umi software are openly released.

**Current text** (`sections/limitations.tex`):

> Hardware \citep{yamumi2026} and the calibration, recording and tracking code \citep{forwardcamumi2026} are open under MIT;

**Verdict:** partial

**Resolution:** Fixed: forward-cam-umi says dataset construction and hand-eye are not in the repo; sentence now says which parts are open.

**Sources:**

- `yamumi2026`: `library/yamumi2026/README.md`; https://github.com/YosubShin/yam-umi (local repo /home/x1/github/yam-umi, README.md and LICENSE) — Local working copy of the repo (README.md, LICENSE, bom/README.md, hardware/STEP and hardware/STL). A LICENSE copy was saved at /home/x1/github/yam-umi/paper-headcam/resources/library/yamumi2026/LICENSE. The README.md already in that directory was written by another agent and was reused, not overwritten. The public GitHub copy was not separately fetched.
- `forwardcamumi2026`: `library/forwardcamumi2026/README.md`; https://raw.githubusercontent.com/YosubShin/forward-cam-umi/HEAD/README.md; https://raw.githubusercontent.com/YosubShin/forward-cam-umi/HEAD/LICENSE; https://raw.githubusercontent.com/YosubShin/forward-cam-umi/HEAD/scripts/README.md — Default branch (HEAD) of the public repo, downloaded during this run. Saved as README.md, LICENSE and scripts_README.md in the library directory.

**Quotes:**

- `yamumi2026`, README.md, section 'Parts', subsection 'Gripper body' — supports: Hardware design files are published openly as STEP and STL — *verified*

  > Printed parts are provided as STEP and STL. The STEP files are the source of

- `yamumi2026`, bom/README.md, opening paragraph (library copy: library/yamumi2026/bom_README.md) — supports: A bill of materials (BOM) is published — *verified*

  > Parts needed for **one** YAM-UMI gripper.

- `yamumi2026`, README.md, section 'License and attribution'; LICENSE file opens 'MIT License' — supports: Open licence for the hardware and software in the repository (the LICENSE text explicitly covers 'associated hardware design files') — *verified*

  > This project is released under the [MIT License](LICENSE).

- `yamumi2026`, README.md, section 'What it records' (the quote continues on the next line with '[forward-cam-umi]') — supports: YAM-UMI itself points to forward-cam-umi for the recording/labelling/dataset software; this is a yamumi statement about forwardcamumi2026, not a yamumi release of that software — *verified*

  > Recording, calibration, labelling, and dataset construction are provided by

- `forwardcamumi2026`, README.md, section 'Software' — supports: Recording and calibration software is published in the repository — *verified*

  > The calibration, recording and tracking code lives in

- `forwardcamumi2026`, README.md, section 'License' — supports: The software is under an open licence (MIT) — *verified*

  > MIT. See [LICENSE](LICENSE).

- `forwardcamumi2026`, scripts_README.md, section 'Where to edit' — supports: Counter-evidence: dataset construction is NOT published in forward-cam-umi, so the claim that its dataset software is open is not supported — *verified*

  > Robot-only tooling (hand-eye, gap bench, dataset construction, training) is not here.

- `forwardcamumi2026`, scripts_README.md, section 'What to send back for dataset building' (the quote continues with 'the robot's hand-eye and kinematics, so it runs on the robot side.') — supports: Counter-evidence: dataset construction runs on the robot side and is not part of the released code — *verified*

  > Dataset construction (labels → joint actions via IK) needs

**Agent's note:** The hardware half is supported. YAM-UMI publishes STEP/STL hardware files and a BOM under MIT, which covers hardware design files. The software half is only partly supported. forward-cam-umi publishes calibration, recording and tracking code under MIT, and labelling is partly there (labels_lib.py is in scripts/). Dataset construction is explicitly not released ("Robot-only tooling (hand-eye, gap bench, dataset construction, training) is not here"). The claim that it publishes the labelling/recording/dataset software openly therefore overstates. A minimal rewording the quotes support: "Hardware and software are open \citep{yamumi2026,forwardcamumi2026}; dataset construction is not part of the released software \citep{forwardcamumi2026}." A more precise option: "Hardware design files are open \citep{yamumi2026}, and the calibration, recording and tracking code is open under MIT \citep{forwardcamumi2026}; dataset construction is not released there."
