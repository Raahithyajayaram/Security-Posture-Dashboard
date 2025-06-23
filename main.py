# main.py

import streamlit as st
from dashboard.summary import render_summary_section
from dashboard.vuln_trends import render_vulnerability_trends_section
from dashboard.predictions import render_prediction_section
from dashboard.anomalies import render_anomaly_section
from dashboard.upload import render_upload_section
from dashboard.risk_scores import render_risk_score_section

# Set page configuration
st.set_page_config(
    page_title="Security Posture Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("🔐 Security Dashboard")
selection = st.sidebar.radio("Go to", [
    "Upload Security Data",
    "Summary",
    "Risk Scores",
    "Vulnerability Trends",
    "Predictive Insights",
    "Anomaly Detection"
])

# Main content router
if selection == "Upload Security Data":
    render_upload_section()
elif selection == "Summary":
    render_summary_section()
elif selection == "Risk Scores":
    render_risk_score_section()
elif selection == "Vulnerability Trends":
    render_vulnerability_trends_section()
elif selection == "Predictive Insights":
    render_prediction_section()
elif selection == "Anomaly Detection":
    render_anomaly_section()
