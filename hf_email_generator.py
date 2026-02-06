import requests
import time

HF_API_KEY = "PASTE_YOUR_TOKEN_HERE"
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def generate_email(context, tone, extra):
    prompt = f"""
Write a {tone} professional email for:
{context}
Additional instruction: {extra}
"""

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 200}
    }

    # Retry 3 times
    for attempt in range(3):
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()

        # Success case
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]

        # Model loading case
        if isinstance(result, dict) and result.get("error"):
            time.sleep(8)  # wait before retry

    return "⚠️ AI busy"
