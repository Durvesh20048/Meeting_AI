import requests

def analyze_text(text):
    prompt = f"""
You are an AI meeting assistant.

ONLY use the transcript below.
DO NOT add extra information.

Transcript:
{text}

Give:
1. Summary (only based on transcript)
2. Key points (only if present)
3. Action items (only if present)

If information is missing, say "Not available".
"""


    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]