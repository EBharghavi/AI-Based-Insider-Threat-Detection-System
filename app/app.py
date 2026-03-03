import streamlit as st
import sys
import os

sys.path.append("../src")

from detect_anomaly import detect
from alert_system import generate_alerts

st.title("🔐 AI Insider Threat Detection Dashboard")

df = detect()

total = len(df)
threats = len(df[df["Anomaly"] == "Threat"])

st.metric("Total Employees", total)
st.metric("Detected Threats", threats)

st.subheader("Employee Activity Data")
st.dataframe(df)

if threats > 0:
    st.error("⚠️ Threats Detected!")
else:
    st.success("✅ System Secure")
