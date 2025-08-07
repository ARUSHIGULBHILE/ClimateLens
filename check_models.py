from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load your Gemini API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=api_key)

# List available models
for model in genai.list_models():
    print(model.name)
