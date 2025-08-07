# app/main.py

import os
import sys
import streamlit as st

# Make parent directory importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bias_engine.bias_detector import query_gemini
from core.logger import log_interaction
from core.feedback import classify_bias_type

st.set_page_config(page_title="🌍 ClimateLens", layout="centered")

st.title("🌍 ClimateLens: Bias Detection on Climate Prompts")

# Input prompt
user_input = st.text_area("Enter a climate-related prompt:", height=150)

if st.button("Detect Bias"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Analyzing with Gemini..."):
            response = query_gemini(user_input)
            bias_type = classify_bias_type(response)
            log_interaction(user_input, response, bias_type=bias_type)

        st.success("Analysis complete.")
        st.subheader("📢 AI Response:")
        st.markdown(response)

        st.subheader("🧠 Detected Bias Type:")
        st.code(bias_type)
