

<body>

<h1>📡 Through-Wall Human Detection using Wi-Fi Signals</h1>
<p><strong>RSSI • Machine Learning • OpenCV • Streamlit</strong></p>

<div class="note">
  <strong>Important:</strong> This system does <u>not</u> generate real images.
  All visualizations represent <strong>Wi-Fi signal disturbance intensity</strong>,
  similar to radar / RF sensing.
</div>

<h2>📌 Overview</h2>
<p>
This project demonstrates a <strong>low-cost, non-intrusive system</strong> to detect
<strong>human presence behind a wall</strong> using Wi-Fi signal disturbances and
Machine Learning.
</p>

<h2>🧠 Key Idea</h2>
<ul>
  <li>Smartphone acts as a Wi-Fi transmitter</li>
  <li>Wi-Fi signals pass through a wall</li>
  <li>Human body disturbs the signal</li>
  <li>Laptop captures RSSI over time</li>
  <li>Statistical features are extracted</li>
  <li>ML model detects human presence</li>
  <li>Results are visualized using OpenCV & Streamlit</li>
</ul>

<h2>🏗️ System Architecture</h2>
<pre>
Phone (Wi-Fi Hotspot)
        ↓
      Wall
        ↓
   Human Presence
        ↓
Laptop (RSSI Capture)
        ↓
Signal Processing
        ↓
Feature Extraction
        ↓
ML Classifier
        ↓
Visualization Dashboard
</pre>

<h2>🧰 Tech Stack</h2>
<table>
  <tr>
    <th>Layer</th>
    <th>Technology</th>
  </tr>
  <tr>
    <td>Signal Source</td>
    <td>Smartphone (Wi-Fi Hotspot)</td>
  </tr>
  <tr>
    <td>Receiver</td>
    <td>Laptop (RSSI)</td>
  </tr>
  <tr>
    <td>ML</td>
    <td>Random Forest</td>
  </tr>
  <tr>
    <td>Visualization</td>
    <td>OpenCV</td>
  </tr>
  <tr>
    <td>Dashboard</td>
    <td>Streamlit</td>
  </tr>
</table>

<h2>📂 Project Structure</h2>
<pre>
PROJECT-WALLSE/
├── empty.csv
├── moving.csv
├── rssi_logger.py
├── features.py
├── detect_rule.py
├── train_ml.py
├── heatmap_fixed.py
├── app.py
└── README.html
</pre>

<h2>📊 Feature Extraction</h2>
<p>The following features are extracted from RSSI time-series:</p>
<ul>
  <li>Mean RSSI</li>
  <li>Standard Deviation</li>
  <li>Signal Range</li>
</ul>

<table>
  <tr>
    <th>Feature</th>
    <th>Empty Room</th>
    <th>Human Moving</th>
  </tr>
  <tr>
    <td>Mean</td>
    <td>~94.9</td>
    <td>~86.7</td>
  </tr>
  <tr>
    <td>Std Deviation</td>
    <td>0.42</td>
    <td>3.94</td>
  </tr>
  <tr>
    <td>Range</td>
    <td>2</td>
    <td>12</td>
  </tr>
</table>

<div class="success">
  Human motion causes a <strong>significant increase</strong> in RSSI variance.
</div>

<h2>🤖 Machine Learning</h2>
<ul>
  <li>Algorithm: Random Forest</li>
  <li>Input: Mean, Std Dev, Range</li>
  <li>Output: Human Present / Not Present</li>
</ul>

<pre>
Prediction empty: [0]
Prediction moving: [1]
</pre>

<h2>🎨 OpenCV Pseudo-Vision</h2>
<p>
RSSI variations are converted into a heatmap:
</p>
<ul>
  <li>🔴 Red / Yellow → High disturbance</li>
  <li>🔵 Blue → Low disturbance</li>
</ul>

<p>
This creates a <strong>radar-like visualization</strong> of human presence.
</p>

<h2>🖥️ Streamlit Dashboard</h2>
<ul>
  <li>Radar-style scanning animation</li>
  <li>Live RSSI graph</li>
  <li>Signal statistics</li>
  <li>Human detected / Area clear status</li>
</ul>

<h2>🚀 How to Run</h2>

<h3>1️⃣ Install Dependencies</h3>
<pre>
pip install numpy pandas scikit-learn opencv-python streamlit
</pre>

<h3>2️⃣ Collect RSSI Data</h3>
<pre>
python rssi_logger.py
</pre>

<h3>3️⃣ Train ML Model</h3>
<pre>
python train_ml.py
</pre>

<h3>4️⃣ Generate Heatmap</h3>
<pre>
python heatmap_fixed.py
</pre>

<h3>5️⃣ Launch Dashboard</h3>
<pre>
streamlit run app.py
</pre>

<h2>⚠️ Limitations</h2>
<ul>
  <li>RSSI-based sensing (no CSI)</li>
  <li>No real image reconstruction</li>
  <li>Environment-dependent accuracy</li>
</ul>

<h2>🔮 Future Work</h2>
<ul>
  <li>CSI-based sensing</li>
  <li>Multi-antenna RF tomography</li>
  <li>Multi-person detection</li>
  <li>Real-time streaming</li>
</ul>

<h2>📌 Key Takeaway</h2>
<p>
<strong>Wi-Fi does not “see” humans — it reveals their presence through disturbance patterns.</strong>
</p>

<footer>
  Built during a late-night curiosity sprint — just before a Maths exam 😄
</footer>

</body>
</html>
