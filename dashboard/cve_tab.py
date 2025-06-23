# dashboard/cve_tab.py

import streamlit as st
import pandas as pd
from scripts.load_cve_data import load_cve_data

def cve_tab():
    st.title("CVE Vulnerability Viewer (2024)")

    df = load_cve_data("data/nvdcve-1.1-2024.json")

    st.subheader("🔎 Search & Filter")
    cve_id = st.text_input("Search by CVE ID")
    min_score = st.slider("Minimum CVSS Score", 0.0, 10.0, 5.0)

    filtered = df[df['Score'].fillna(0) >= min_score]
    if cve_id:
        filtered = filtered[filtered['CVE_ID'].str.contains(cve_id, case=False)]

    st.write(f"Total matching records: {len(filtered)}")
    st.dataframe(filtered, use_container_width=True)

    st.subheader("📊 Attack Vector Distribution")
    st.bar_chart(filtered['Attack Vector'].value_counts())

