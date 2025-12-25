import subprocess
import time
import re
import csv

def get_signal():
    output = subprocess.check_output(
        ["netsh", "wlan", "show", "interfaces"],
        shell=True
    ).decode(errors="ignore")

    match = re.search(r"Signal\s*:\s*(\d+)%", output)
    return int(match.group(1)) if match else None

with open("rssi_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "signal"])

    print("Logging started... Ctrl+C to stop")
    while True:
        signal = get_signal()
        if signal is not None:
            writer.writerow([time.time(), signal])
            print(signal)
        time.sleep(0.1)
