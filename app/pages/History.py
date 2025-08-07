# app/pages/History.py

import streamlit as st
import pandas as pd
import os
import json

st.set_page_config(page_title="History | ClimateLens", page_icon="🕘")

st.title("🕘 Interaction History")
st.markdown("Here are the past prompts and AI responses detected by ClimateLens:")

# File path
log_file = os.path.join("data", "responses.csv")

# Check if file exists
if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
    with open(log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        data = [json.loads(line) for line in lines]

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp", ascending=False)

    # Display table
    st.dataframe(
        df[["timestamp", "prompt", "bias_type"]],
        column_config={
            "timestamp": st.column_config.DatetimeColumn("Date/Time"),
            "prompt": st.column_config.TextColumn("User Prompt"),
            "bias_type": st.column_config.TextColumn("Detected Bias Type"),
        },
        use_container_width=True,
        hide_index=True,
    )

    # Expand to show full AI responses
   
    with st.expander("📋 See AI Responses & Give Feedback"):
          
        for i, row in enumerate(data):
            st.markdown(f"**🕓 {row['timestamp']}**")
            st.markdown(f"**Prompt:** {row['prompt']}")
            st.markdown(f"**Bias Type:** `{row['bias_type']}`")
            st.markdown(f"**AI Response:**\n\n{row['response']}")
   
            feedback_col1, feedback_col2 = st.columns([1, 4])
            with feedback_col1:
                thumbs = st.radio(
                    f"Feedback_{i}",
                    ["👍", "👎", "⏭️"],
                    horizontal=True,
                    label_visibility="collapsed",
            )

            if thumbs in ["👍", "👎"]:
            # Log feedback (optional: save to a new file or future use)
                with open("data/feedback.csv", "a", encoding="utf-8") as fb_file:
                    json.dump({
                        "timestamp": str(row["timestamp"]),
                        "prompt": row["prompt"],
                        "bias_type": row["bias_type"],
                        "response": row["response"],
                        "feedback": thumbs
                    }, fb_file)
                    fb_file.write("\n")

            st.success(f"Feedback recorded: {thumbs}")
        st.markdown("---")


else:
    st.warning("No history found yet. Start analyzing prompts to build history.")
