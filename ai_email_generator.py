import requests

API_KEY = "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"

def generate_email(context, tone, extra):

    prompt = f"""
Write a professional email.

Purpose: {context}
Tone: {tone}
Additional instructions: {extra}

Return only the email body.
"""

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "⚠️ AI generation failed. Please try again."
