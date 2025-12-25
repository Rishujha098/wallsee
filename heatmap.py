import cv2
import pandas as pd
import numpy as np


# LOAD info

df = pd.read_csv("moving.csv")   
signal = df["signal"].values.astype(np.float32)


# USE SIGNAL VARIATION (IMPORTANT)

diff_signal = np.abs(signal - np.mean(signal))

# Normalize
diff_signal = diff_signal / np.max(diff_signal)


# CREATE 2D HEATMAP GRID

H, W = 100, 100
heatmap = np.zeros((H, W), dtype=np.float32)

# Place energy in center region ng)
cx, cy = H // 2, W // 2

for i, val in enumerate(diff_signal):
    angle = 2 * np.pi * (i / len(diff_signal))
    radius = int(val * 30)

    x = int(cx + radius * np.cos(angle))
    y = int(cy + radius * np.sin(angle))

    if 0 <= x < H and 0 <= y < W:
        heatmap[x, y] += val * 5


# SMOOTH & NORMALIZE

heatmap = cv2.GaussianBlur(heatmap, (31, 31), 0)
heatmap = cv2.normalize(heatmap, None, 0, 255, cv2.NORM_MINMAX)
heatmap = heatmap.astype(np.uint8)

# COLOR MAP 

colored = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)


# DISPLAY


colored = cv2.resize(colored, (600, 600), interpolation=cv2.INTER_LINEAR)

cv2.imshow("Wi-Fi Through-Wall Heatmap (Pseudo Vision)", colored)
cv2.waitKey(0)
cv2.destroyAllWindows()

