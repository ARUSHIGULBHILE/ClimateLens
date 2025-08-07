
# bias_engine/bias_detector.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
import google.generativeai as genai

from core.logger import log_interaction
from core.feedback import classify_bias_type
from core.config import GEMINI_API_KEY, MODEL_NAME

# Load environment variables
load_dotenv()

if not GEMINI_API_KEY:
    raise Exception("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load model
model = genai.GenerativeModel(MODEL_NAME)

def query_gemini(prompt):
    try:
        response = model.generate_content(
            f"""
You are a climate-aware assistant.
Detect if the following prompt contains any bias (e.g., political, regional, economic, or gender).
Explain the bias, if any, and suggest a better, neutral rewrite.

Prompt: {prompt}
"""
        )
        return response.text
    except Exception as e:
        return f"[ERROR] {str(e)}"

# Test Run
if __name__ == "__main__":
    prompt = "Is climate change mainly caused by developing nations?"
    result = query_gemini(prompt)
    print("User Prompt:", prompt)
    print("AI Response:", result)

    # Bias classification + logging
    bias_type = classify_bias_type(result)
    log_interaction(prompt, result, bias_type=bias_type)
