# utils/logger.py

import json
from datetime import datetime

def log_interaction(prompt, response, bias_type="unknown"):
    log = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "response": response,
        "bias_type": bias_type
    }

    with open("data/responses.csv", "a", encoding="utf-8") as f:
        f.write(json.dumps(log) + "\n")
