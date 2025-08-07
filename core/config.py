# core/config.py

import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "models/gemini-1.5-flash"
FEEDBACK_FILE = "data/feedback.jsonl"
RESPONSE_LOG = "data/responses.csv"
