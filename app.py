import streamlit as st
import pandas as pd
import time
from sklearn.ensemble import RandomForestClassifier

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Through-Wall Human Detection",
    layout="centered"
)

# --------------------------------------------------
# CSS FOR MOTION GRAPHICS & ANIMATION
# --------------------------------------------------
st.markdown("""
<style>
.radar {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  border: 3px solid #00ffcc;
  position: relative;
  animation: pulse 2s infinite;
  margin: 20px auto;
}

@keyframes pulse {
  0% { box-shadow: 0 0 5px #00ffcc; }
  50% { box-shadow: 0 0 35px #00ffcc; }
  100% { box-shadow: 0 0 5px #00ffcc; }
}

.detected {
  background-color: #ff4b4b;
  padding: 25px;
  border-radius: 12px;
  text-align: center;
  color: white;
  animation: blink 1s infinite;
  margin-top: 20px;
}

.clear {
  background-color: #00c853;
  padding: 25px;
  border-radius: 12px;
  text-align: center;
  color: white;
  margin-top: 20px;
}

@keyframes blink {
  0% { opacity: 1; }
  50% { opacity: 0.55; }
  100% { opacity: 1; }
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("📡 Through-Wall Human Detection System")
st.write(
    "Motion-graphic based Wi-Fi sensing system to detect human presence "
    "behind a wall using RSSI and Machine Learning."
)

# --------------------------------------------------
# FEATURE EXTRACTION
# --------------------------------------------------
def extract_features(df):
    return [
        df["signal"].mean(),
        df["signal"].std(),
        df["signal"].max() - df["signal"].min()
    ]

# --------------------------------------------------
# TRAIN ML MODEL (USING empty.csv & moving.csv)
# --------------------------------------------------
@st.cache_resource
def train_model():
    empty = pd.read_csv("empty.csv")
    moving = pd.read_csv("moving.csv")

    X = [
        extract_features(empty),
        extract_features(moving)
    ]
    y = [0, 1]  # 0 = No Human, 1 = Human

    model = RandomForestClassifier()
    model.fit(X, y)
    return model

model = train_model()

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------
st.subheader("📂 Upload RSSI CSV File")
uploaded_file = st.file_uploader("Upload a test CSV (RSSI data)", type=["csv"])

# --------------------------------------------------
# MAIN LOGIC
# --------------------------------------------------
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # --- SCANNING ANIMATION ---
    st.markdown("### 🟢 Scanning Wi-Fi Environment")
    st.markdown('<div class="radar"></div>', unsafe_allow_html=True)

    progress = st.progress(0)
    status = st.empty()

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)
        status.text(f"Analyzing signal reflections... {i+1}%")

    # --- PREDICTION ---
    features = extract_features(df)
    prediction = model.predict([features])

    # --- RESULT ---
    st.markdown("## 🔍 Detection Result")

    if prediction[0] == 1:
        st.markdown(
            """
            <div class="detected">
                <h2>👤 HUMAN DETECTED BEHIND WALL</h2>
                <p>Significant Wi-Fi signal disturbance observed</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div class="clear">
                <h2>✅ AREA CLEAR</h2>
                <p>No significant Wi-Fi disturbance detected</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --- METRICS ---
    st.markdown("### 📊 Signal Statistics")
    col1, col2, col3 = st.columns(3)

    col1.metric("Mean RSSI", round(df["signal"].mean(), 2))
    col2.metric("Std Deviation", round(df["signal"].std(), 2))
    col3.metric("Signal Range", int(df["signal"].max() - df["signal"].min()))

    # --- LIVE GRAPH ---
    st.markdown("### 📈 Live Wi-Fi Signal Visualization")
    st.line_chart(df["signal"])

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption(
    "⚠️ Research Prototype | RSSI-based sensing | No imaging | No CSI\n\n"
    "Future Work: CSI-based fine-grained sensing"
)
