# /scripts/test_gpt.py

import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env
load_dotenv()

# Set your API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file.")

openai.api_key = api_key

# Dummy paragraph for summarization
dummy_text = """
In the past few years, cyber threats have increased dramatically across industries. 
With the growing adoption of cloud services and IoT, attack surfaces have expanded, 
making organizations more vulnerable to ransomware, phishing, and zero-day exploits.
"""

# GPT prompt
messages = [
    {"role": "system", "content": "You are a cybersecurity assistant."},
    {"role": "user", "content": f"Summarize this in 3 bullet points:\n{dummy_text}"}
]

# Call the GPT API
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages
)

# Print the response
print("\nGenerated Summary:\n")
print(response.choices[0].message["content"])

