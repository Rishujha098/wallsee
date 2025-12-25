import pandas as pd
import matplotlib.pyplot as plt

# Load data
empty = pd.read_csv("empty.csv")
moving = pd.read_csv("moving.csv")

# Plot
plt.figure(figsize=(10, 5))
plt.plot(empty["signal"], label="Empty Room", linewidth=2)
plt.plot(moving["signal"], label="Human Moving", linewidth=2)

plt.xlabel("Samples (Time)")
plt.ylabel("Wi-Fi Signal Strength (%)")
plt.title("Wi-Fi RSSI Comparison: Empty Room vs Human Moving")
plt.legend()
plt.grid(True)

plt.show()
