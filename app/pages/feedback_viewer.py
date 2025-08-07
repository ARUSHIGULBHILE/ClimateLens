# app/pages/feedback_viewer.py

import streamlit as st
import json
import pandas as pd
import os

st.set_page_config(page_title="Feedback Viewer", page_icon="📊")

st.title("📊 User Feedback Dashboard")

feedback_path = "data/feedback.jsonl"

if not os.path.exists(feedback_path):
    st.warning("No feedback data found yet.")
    st.stop()

# Load feedback entries
with open(feedback_path, "r", encoding="utf-8") as f:
    entries = [json.loads(line.strip()) for line in f if line.strip()]

df = pd.DataFrame(entries)

# Sidebar filters
st.sidebar.header("🔎 Filter Feedback")
rating_filter = st.sidebar.selectbox("Filter by rating", ["All"] + sorted(df["rating"].unique()))
keyword = st.sidebar.text_input("Search in comments")

filtered_df = df.copy()

if rating_filter != "All":
    filtered_df = filtered_df[filtered_df["rating"] == rating_filter]

if keyword:
    filtered_df = filtered_df[filtered_df["comment"].str.contains(keyword, case=False)]

# Display results
st.dataframe(filtered_df, use_container_width=True)

# Optionally export
st.download_button("⬇️ Download CSV", data=filtered_df.to_csv(index=False), file_name="filtered_feedback.csv")
