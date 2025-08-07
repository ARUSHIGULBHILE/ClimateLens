# app/pages/Explorer.py

import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px

st.set_page_config(page_title="Data Explorer", page_icon="📊")

st.title("📊 Bias Analysis Dashboard")
st.write("Explore logged prompts, bias types, and AI responses.")

log_path = "data/responses.csv"

# Check if file exists
if not os.path.exists(log_path):
    st.warning("No data found yet. Try analyzing a prompt first.")
    st.stop()

# Read and parse JSONL rows
with open(log_path, "r", encoding="utf-8") as f:
    logs = [json.loads(line.strip()) for line in f if line.strip()]

# Convert to DataFrame
df = pd.DataFrame(logs)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Filter by bias type
bias_filter = st.multiselect("Filter by Bias Type", options=df["bias_type"].unique(), default=df["bias_type"].unique())
filtered_df = df[df["bias_type"].isin(bias_filter)]

# Show data table
st.subheader("📄 Logged Entries")
st.dataframe(filtered_df.sort_values("timestamp", ascending=False), use_container_width=True)

# Chart: Count by bias type
st.subheader("📈 Bias Type Distribution")
bias_counts = filtered_df["bias_type"].value_counts().reset_index()
bias_counts.columns = ["Bias Type", "Count"]
fig = px.bar(bias_counts, x="Bias Type", y="Count", color="Bias Type", title="Detected Bias Types")
st.plotly_chart(fig, use_container_width=True)

# Optional: Time series
st.subheader("📅 Bias Logging Over Time")
time_series = filtered_df.groupby(filtered_df["timestamp"].dt.date).size().reset_index(name="Count")
fig_time = px.line(time_series, x="timestamp", y="Count", title="Prompt Logs Over Time")
st.plotly_chart(fig_time, use_container_width=True)
