import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def extract_features(file):
    df = pd.read_csv(file)
    return [
        df["signal"].mean(),
        df["signal"].std(),
        df["signal"].max() - df["signal"].min()
    ]

# Dataset
X = [
    extract_features("empty.csv"),
    extract_features("moving.csv")
]
y = [0, 1]  # 0 = No Human, 1 = Human

# Model
model = RandomForestClassifier()
model.fit(X, y)

# Test
print("Prediction empty:", model.predict([extract_features("empty.csv")]))
print("Prediction moving:", model.predict([extract_features("moving.csv")]))
