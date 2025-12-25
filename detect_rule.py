import pandas as pd

THRESHOLD_STD = 1.5 

def detect(file):
    df = pd.read_csv(file)
    std = df["signal"].std()

    if std > THRESHOLD_STD:
        print(file, "→  Human Detected Behind Wall")
    else:
        print(file, "→  No Human Detected")

detect("empty.csv")
detect("moving.csv")
