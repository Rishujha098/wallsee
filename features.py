import pandas as pd

def extract_stats(file):
    df = pd.read_csv(file)
    return {
        "mean": df["signal"].mean(),
        "std": df["signal"].std(),
        "range": df["signal"].max() - df["signal"].min()
    }

print("EMPTY:", extract_stats("empty.csv"))
print("MOVING:", extract_stats("moving.csv"))
