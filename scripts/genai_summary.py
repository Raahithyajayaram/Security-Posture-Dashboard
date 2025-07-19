# scripts/genai_summary.py

import os
import requests
from dotenv import load_dotenv
from load_cve_data import load_cve_data  # adjust if needed

# Load the Hugging Face API key from .env
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def summarize(text):
    payload = {
        "inputs": f"Summarize the following: {text}",
        "parameters": {"max_new_tokens": 100}
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"❌ API Error {response.status_code} for text:\n{text}\n")
        return None

    try:
        return response.json()[0]["summary_text"]
    except Exception as e:
        print(f"❌ Error parsing response: {e}")
        return None

if __name__ == "__main__":
    json_file_path = "data/nvdcve-1.1-2024.json"  # adjust if needed
    df = load_cve_data(json_file_path)

    for idx, row in df.iterrows():  # limit to first 10 rows

        print(f"\n🔹 CVE ID: {row['CVE_ID']}")
        print(f"📄 Original Description:\n{row['Description']}")

        summary = summarize(row['Description'])

        if summary:
            print(f"\n✅ GenAI Summary:\n{summary}")
        else:
            print("⚠️ Failed to generate summary.")
