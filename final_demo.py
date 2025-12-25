import pandas as pd

def detect(file):
    df = pd.read_csv(file)
    std = df["signal"].std()

    if std > 1.5:
        print(" Human detected behind wall")
    else:
        print(" No human detected")

detect("moving.csv")
