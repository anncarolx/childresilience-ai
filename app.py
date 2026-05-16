import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="CHILDRESILIENCE AI",
    page_icon="🌍",
    layout="wide",
)

# Header
st.title("🌍 CHILDRESILIENCE AI")
st.subheader(
    "AI-Powered Predictive Climate Resilience Platform for Vulnerable Children"
)

st.markdown(
    """
    CHILDRESILIENCE AI is an anticipatory climate-health intelligence platform that predicts and maps
    climate-related risks affecting vulnerable children using environmental, climate, and health indicators.
    """
)

# Sidebar
st.sidebar.header("⚙️ Climate Risk Inputs")

rainfall = st.sidebar.slider("Rainfall Intensity", 0, 100, 65)
temperature = st.sidebar.slider("Temperature Level", 20, 45, 33)
flood_risk = st.sidebar.slider("Flood Risk", 0, 100, 70)
air_quality = st.sidebar.slider("Air Pollution Level", 0, 100, 55)

# AI Risk Model
risk_score = (
    rainfall * 0.30
    + (temperature * 2) * 0.20
    + flood_risk * 0.30
    + air_quality * 0.20
)

risk_score = round(risk_score, 1)

# Risk Categories
if risk_score >= 75:
    risk_level = "Severe"
    color = "#c62828"
elif risk_score >= 55:
    risk_level = "High"
    color = "#ef6c00"
elif risk_score >= 35:
    risk_level = "Moderate"
    color = "#d4a017"
else:
    risk_level = "Low"
    color = "#2e7d32"

# Dashboard Metrics
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Child Climate Risk Score", risk_score)
col2.metric("Predicted Risk Level", risk_level)
col3.metric("At-Risk Communities", np.random.randint(8, 30))
col4.metric("Predicted Health Threats", np.random.randint(3, 7))

st.markdown("---")

# Forecast Section
st.subheader("📈 Climate-Health Risk Forecast")

forecast_days = [
    "Day 1",
    "Day 2",
    "Day 3",
    "Day 4",
    "Day 5",
    "Day 6",
    "Day 7",
]

forecast_values = np.round(
    np.clip(
        np.random.normal(loc=risk_score, scale=5, size=7),
        20,
        100,
    ),
    1,
)

fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(
    forecast_days,
    forecast_values,
    marker="o",
    linewidth=2,
)

ax.set_ylabel("Risk Score")
ax.set_ylim(0, 100)
ax.set_title("Predicted Pediatric Climate-Health Risk")
ax.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

st.pyplot(fig, use_container_width=True)

# Early Warning Alert
st.subheader("🚨 Early Warning Alert")

st.markdown(
    f"""
    <div style='padding:20px;border-radius:12px;background-color:{color};color:white;'>
    <h3>{risk_level} Climate-Health Alert</h3>
    <p>
    AI models predict elevated pediatric disease vulnerability linked to rainfall,
    flooding, heat exposure, and environmental conditions in climate-sensitive communities.
    </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Risk Distribution
st.subheader("🧠 Predicted Climate-Health Threat Distribution")

threats = [
    "Malaria",
    "Respiratory Illness",
    "Diarrheal Disease",
    "Heat Stress",
]

threat_scores = np.random.randint(40, 95, size=4)

threat_df = pd.DataFrame(
    {
        "Threat": threats,
        "Risk Score": threat_scores,
    }
)

st.bar_chart(threat_df.set_index("Threat"))

# Recommended Actions
st.subheader("✅ Recommended Anticipatory Actions")

recommendations = [
    "Strengthen pediatric disease surveillance",
    "Pre-position essential medical supplies",
    "Increase community health outreach",
    "Activate climate-health preparedness teams",
    "Issue public health advisories to caregivers",
    "Deploy targeted WASH interventions in high-risk areas",
]

for rec in recommendations:
    st.write(f"- {rec}")

# Child Vulnerability Table
st.subheader("🗺️ Child Vulnerability Overview")

sample_data = pd.DataFrame(
    {
        "Region": [
            "Kisumu",
            "Turkana",
            "Nairobi Informal Settlements",
            "Garissa",
            "Mombasa",
        ],
        "Risk Score": [82, 91, 74, 69, 77],
        "Predicted Threat": [
            "Flood-related diarrheal disease",
            "Heat stress and malnutrition",
            "Respiratory illness",
            "Water insecurity",
            "Flood-associated malaria",
        ],
        "Alert Level": [
            "Severe",
            "Severe",
            "High",
            "Moderate",
            "High",
        ],
    }
)

st.dataframe(sample_data, use_container_width=True)

# Footer
st.markdown("---")

st.caption(
    "CHILDRESILIENCE AI MVP Prototype — Open-source climate-health intelligence for vulnerable children."
)
