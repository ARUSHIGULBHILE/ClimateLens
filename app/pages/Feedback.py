# app/pages/Feedback.py

import streamlit as st
from core.feedback import save_feedback

st.set_page_config(page_title="Feedback", page_icon="💬")

st.title("💬 Submit Feedback")
st.write("Help us improve the system by sharing your feedback on bias detection results.")

# Input form
with st.form("feedback_form"):
    prompt = st.text_area("🔹 Prompt you tested", height=100)
    response = st.text_area("🔹 AI's Response", height=150)
    rating = st.slider("⭐ Rating (1 = Poor, 5 = Excellent)", 1, 5, 3)
    comments = st.text_area("✍️ Any suggestions or comments?", height=100)

    submitted = st.form_submit_button("Submit Feedback")

    if submitted:
        if prompt.strip() == "" or response.strip() == "":
            st.error("Please provide both the prompt and response.")
        else:
            save_feedback(prompt, response, rating, comments)
            st.success("✅ Feedback submitted! Thank you for helping us improve.")
