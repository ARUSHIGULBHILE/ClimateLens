# utils/feedback.py

bias_keywords = {
    "political": ["political", "ideological", "partisan"],
    "regional": ["regional", "geographic", "country", "continent", "location"],
    "economic": ["economic", "wealth", "income", "financial"],
    "gender": ["gender", "male", "female", "woman", "man"],
    "racial": ["racial", "ethnicity", "race"],
}

def classify_bias_type(response_text):
    detected_types = set()

    for bias_type, keywords in bias_keywords.items():
        for keyword in keywords:
            if keyword.lower() in response_text.lower():
                detected_types.add(bias_type)

    if not detected_types:
        return "unknown"

    return "/".join(sorted(detected_types))
# utils/feedback.py

import json
from datetime import datetime
import os

def save_feedback(prompt, response, rating, comments):
    feedback_entry = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "response": response,
        "rating": rating,
        "comments": comments
    }

    os.makedirs("data", exist_ok=True)
    with open("data/feedback.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(feedback_entry) + "\n")
