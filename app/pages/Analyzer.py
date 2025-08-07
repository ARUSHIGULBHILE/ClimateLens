# app/pages/Analyzer.py

import streamlit as st
from bias_engine.bias_detector import query_gemini
from core.logger import log_interaction

st.set_page_config(page_title="Prompt Analyzer", page_icon="🕵️‍♀️")

st.title("🕵️‍♀️ Prompt Bias Analyzer")
st.write("Enter a prompt below, and ClimateLens will analyze it for possible bias and suggest neutral alternatives.")

# Input
user_prompt = st.text_area("🔍 Enter your prompt here", height=150)

# Analyze button
if st.button("Analyze Prompt"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Analyzing for bias..."):
            result = query_gemini(user_prompt)
            st.subheader("📘 AI Response")
            st.markdown(result)

            # Optionally detect type of bias
            # You could automate this later; for now, let’s keep it simple
            bias_type = st.selectbox("What type of bias did this address?", ["unknown", "regional", "economic", "political", "gender", "cultural"])

            # Log to CSV
            log_interaction(user_prompt, result, bias_type=bias_type)
            st.success("Response logged successfully.")
