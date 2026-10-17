"""Teaser: (a) collector with the head camera (iPhone video, 26 s), (b) the head camera's own frame with detections
(glove6, 182 s), (c) the YAM with the SO-101 positioner carrying the same camera (iPhone video, 250 s).
Sources in fig/src; originals in ../media/originals (gitignored) and NAS yam-umi-media/originals."""
import cv2, numpy as np
from pathlib import Path
F = Path(__file__).parent
H = 1080
a = cv2.imread(str(F / "src/collector_iphone_26s.jpg"))[100:1900]
c = cv2.imread(str(F / "src/rollout_iphone_250s.jpg"))[180:1900]
b = cv2.imread(str(F / "src/headcam_glove6_182s_overlay.jpg"))[:, 60:1500]  # 1440 x 1080 (4:3)
def fit(im): return cv2.resize(im, (int(round(im.shape[1] * H / im.shape[0])), H), interpolation=cv2.INTER_AREA)
panels = [fit(a), fit(b), fit(c)]
gap = 24
out = np.full((H, sum(p.shape[1] for p in panels) + gap * 2, 3), 255, np.uint8)
x = 0
for p, lab in zip(panels, "abc"):
    out[:, x:x + p.shape[1]] = p
    cv2.rectangle(out, (x, 0), (x + 110, 90), (255, 255, 255), -1)
    cv2.putText(out, f"({lab})", (x + 8, 68), cv2.FONT_HERSHEY_DUPLEX, 2.2, (0, 0, 0), 4, cv2.LINE_AA)
    x += p.shape[1] + gap
cv2.imwrite(str(F / "teaser.jpg"), out, [cv2.IMWRITE_JPEG_QUALITY, 88])
print(out.shape)
