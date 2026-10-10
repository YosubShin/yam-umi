#!/bin/bash
# Assemble the Track-2 video (~2 min, 1280x720, 30 fps). Sources: yam-umi repo media,
# pipeline.png and the third-person grid clips in clips/. Output: yam-umi-track2.mp4 (copy to ../../media/yam-umi-paper-video.mp4)
set -e
F=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
HERE=$(cd "$(dirname "$0")" && pwd)
M=$HERE/../../media
TP=$HERE/clips
cap() { echo "drawtext=fontfile=$F:text='$1':fontsize=26:fontcolor=white:box=1:boxcolor=black@0.55:boxborderw=12:x=24:y=h-th-24"; }
V="-c:v libx264 -pix_fmt yuv420p -r 30 -an"

# A title 5 s
ffmpeg -v error -y -f lavfi -i color=c=0x1a1a1a:s=1280x720:d=5 -vf "drawtext=fontfile=$F:text='YAM-UMI':fontsize=96:fontcolor=white:x=(w-tw)/2:y=200,drawtext=fontfile=$F:text='A fiducial-tracked glove that collects':fontsize=32:fontcolor=white:x=(w-tw)/2:y=320,drawtext=fontfile=$F:text='metrically labelled demonstrations for the YAM arm':fontsize=32:fontcolor=white:x=(w-tw)/2:y=365,drawtext=fontfile=$F:text='CoRL 2026 UMI Arena - Track 2 (device)':fontsize=28:fontcolor=0xbbbbbb:x=(w-tw)/2:y=420" $V segA.mp4

# B collection demo, 0-44 s at 2x
ffmpeg -v error -y -ss 0 -t 44 -i $M/glove-collection-demo.mp4 -vf "setpts=0.5*PTS,scale=1280:720,$(cap '30 demos in 10-12 min; pose tracked by the fiducials on the glove'),drawtext=fontfile=$F:text='Collecting with the glove (2x speed)':fontsize=26:fontcolor=white:box=1:boxcolor=black@0.55:boxborderw=12:x=24:y=h-th-76" $V segB.mp4

# C pipeline still 7 s
ffmpeg -v error -y -loop 1 -t 7 -i $HERE/pipeline.png -vf "crop=1283:640:0:0,scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:color=0x1a1a1a,$(cap 'Labels - fixed 4K camera decodes the ball (pose), wrist fisheye the tip tags (width)')" $V segC.mp4

# D1 establishing shot from the phone, 10 s at 1.5x (the policy running is the teleop reference)
ffmpeg -v error -y -ss 35 -t 60 -i $M/rollout-demo-1x-720p.mp4 -vf "setpts=PTS/2.5,scale=1280:720,$(cap 'Running - co-trained wrist-cam policy, teleop 185 + ~70 glove episodes'),drawtext=fontfile=$F:text='The rig (2.5x speed) - YAM arm, fixed 4K camera over the table, bin and blocks':fontsize=26:fontcolor=white:box=1:boxcolor=black@0.55:boxborderw=12:x=24:y=h-th-76" $V segD1.mp4
# D2 co-trained forward-camera policy, two placements, 2x, from the grid's third-person stream
ffmpeg -v error -y -i $TP/mix_Bj_s_S14r0_success.mp4 -i $TP/mix_Bj_s_S15r0_success.mp4 -i $TP/mix_Aj_s_S15r0_success.mp4 -filter_complex "[0:v]setpts=0.5*PTS,scale=1280:720,$(cap 'Co-trained (teleop 185 + glove 165), obs forward cam - placement 14 (2x speed)')[a];[1:v]setpts=0.5*PTS,scale=1280:720,$(cap 'Co-trained (teleop 185 + glove 165), obs forward cam - placement 15 (2x speed)')[b];[2:v]setpts=0.5*PTS,scale=1280:720,$(cap 'Co-trained (teleop 185 + glove 165), obs wrist cam - placement 15 (2x speed)')[c];[a][b][c]concat=n=3:v=1:a=0[out]" -map "[out]" $V segD2.mp4

# E/F 2x2 mosaics of one placement, 2x speed, padded to the longest tile
mosaic() {  # out scene label1 clip1 label2 clip2 label3 clip3 label4 clip4
  local out=$1 scene=$2; shift 2
  local args=() fc="" i=0 maxd=0
  for ((k=0;k<4;k++)); do
    local lab=$1 clip=$2; shift 2
    local d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$clip")
    maxd=$(python3 -c "print(max($maxd,$d/2))")
    args+=(-i "$clip")
    fc+="[$k:v]setpts=0.5*PTS,scale=640:360,drawtext=fontfile=$F:text='$lab':fontsize=20:fontcolor=white:box=1:boxcolor=black@0.55:boxborderw=8:x=12:y=12,tpad=stop_mode=clone:stop_duration=30[v$k];"
  done
  fc+="[v0][v1][v2][v3]xstack=inputs=4:layout=0_0|640_0|0_360|640_360,trim=duration=$(python3 -c "print($maxd+1.0)"),drawtext=fontfile=$F:text='Placement grid, scene $scene, block re-placed to the pixel for every policy (2x speed)':fontsize=26:fontcolor=white:box=1:boxcolor=black@0.55:boxborderw=10:x=(w-tw)/2:y=h-th-16[out]"
  ffmpeg -v error -y "${args[@]}" -filter_complex "$fc" -map "[out]" $V $out
}
mosaic segE.mp4 15 \
  "teleop-only (185), obs wrist cam - success" $TP/Aj_S15r0_success.mp4 \
  "co-trained (185+165), obs forward cam - success" $TP/mix_Bj_s_S15r0_success.mp4 \
  "co-trained (185+165), obs wrist cam - dropped at bin" $TP/mix_Aj_s_S15r1_dropped_at_bin.mp4 \
  "teleop 92 + glove 93, obs wrist cam - dropped" $TP/Aj_glove50_s_S15r0_dropped_before_bin.mp4
mosaic segF.mp4 14 \
  "teleop-only (185), obs wrist cam - no grasp" $TP/Aj_S14r1_no_grasp.mp4 \
  "co-trained (185+165), obs forward cam - success" $TP/mix_Bj_s_S14r0_success.mp4 \
  "co-trained (185+165), obs wrist cam - dropped" $TP/mix_Aj_s_S14r0_dropped_before_bin.mp4 \
  "teleop 92 + glove 93, obs wrist cam - success" $TP/Aj_glove50_s_S14r0_success.mp4

# G end card 12 s: the paper's table — wrist block sorted by val loss (worst to best), best per column in bold; forward row below a divider
FR=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
WRIST=("teleop 46 + glove 139|0.271|15/30|6/30" "teleop 92 + glove 93|0.267|22/30|5/30" "teleop-only 185 (reference)|0.247|26/30|16/30" "teleop 185 + glove 165|0.236|28/30|12/30")
FWD=("teleop 185 + glove 165|0.260|20/30|14/30")
BEST=("0.236" "28/30" "16/30")
XS=(760 920 1080)
G="drawtext=fontfile=$F:text='Rollout evaluation - 15 placements x 2 repeats, 30 trials per policy':fontsize=30:fontcolor=white:x=(w-tw)/2:y=60"
G+=",drawtext=fontfile=$FR:text='observation / training episodes':fontsize=24:fontcolor=0xbbbbbb:x=120:y=130"
G+=",drawtext=fontfile=$FR:text='val loss':fontsize=24:fontcolor=0xbbbbbb:x=760:y=130,drawtext=fontfile=$FR:text='grasped':fontsize=24:fontcolor=0xbbbbbb:x=920:y=130,drawtext=fontfile=$FR:text='success':fontsize=24:fontcolor=0xbbbbbb:x=1080:y=130"
G+=",drawbox=x=120:y=165:w=1060:h=1:color=0x777777:t=fill"
row() { # $1 label $2 y $3 bold(1/0) $4 vl $5 gr $6 su
  G+=",drawtext=fontfile=$FR:text='$1':fontsize=28:fontcolor=white:x=120:y=$2"
  local i=0; for cell in "$4" "$5" "$6"; do
    local fnt=$FR; [ "$3" = 1 ] && [ "$cell" = "${BEST[$i]}" ] && fnt=$F
    G+=",drawtext=fontfile=$fnt:text='$cell':fontsize=28:fontcolor=white:x=${XS[$i]}:y=$2"; i=$((i+1))
  done
}
y=180
G+=",drawtext=fontfile=$FR:text='wrist fisheye':fontsize=22:fontcolor=0xbbbbbb:x=120:y=$y"; y=$((y+34))
for r in "${WRIST[@]}"; do IFS='|' read -r lab vl gr su <<< "$r"; row "$lab" $y 1 "$vl" "$gr" "$su"; y=$((y+44)); done
G+=",drawbox=x=120:y=$((y+2)):w=1060:h=1:color=0x777777:t=fill"; y=$((y+16))
G+=",drawtext=fontfile=$FR:text='forward + fovea':fontsize=22:fontcolor=0xbbbbbb:x=120:y=$y"; y=$((y+34))
for r in "${FWD[@]}"; do IFS='|' read -r lab vl gr su <<< "$r"; row "$lab" $y 0 "$vl" "$gr" "$su"; y=$((y+44)); done
G+=",drawbox=x=120:y=$((y+2)):w=1060:h=1:color=0x777777:t=fill"
G+=",drawtext=fontfile=$FR:text='val loss - ACT validation loss on the robot held-out episodes (lower is better); bold - best per column':fontsize=20:fontcolor=0x999999:x=120:y=$((y+16))"
G+=",drawtext=fontfile=$FR:text='Adding glove episodes lowers val loss and keeps the grasp rate; success is statistically indistinguishable (paired).':fontsize=22:fontcolor=0xbbbbbb:x=(w-tw)/2:y=575"
G+=",drawtext=fontfile=$FR:text='Replacing teleop with glove episodes at the same budget costs 33-37 points (p<0.01).':fontsize=22:fontcolor=0xbbbbbb:x=(w-tw)/2:y=607"
G+=",drawtext=fontfile=$FR:text='github.com/YosubShin/yam-umi      github.com/YosubShin/forward-cam-umi':fontsize=24:fontcolor=0xbbbbbb:x=(w-tw)/2:y=665"
ffmpeg -v error -y -f lavfi -i color=c=0x1a1a1a:s=1280x720:d=12 -vf "$G" $V segG.mp4

printf "file 'seg%s.mp4'\n" A B C D1 D2 E F G > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt -c copy yam-umi-track2.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 yam-umi-track2.mp4
