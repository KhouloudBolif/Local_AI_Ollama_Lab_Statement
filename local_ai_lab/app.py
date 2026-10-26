import sys
import requests

sys.stdout.reconfigure(errors="replace")

url = "http://localhost:11434/api/generate"

data = {
    "model": "qwen3.5:0.8b",
    "prompt": "Explain recursion in Python.",
    "stream": False
}

response = requests.post(url, json=data)
result = response.json()
if "response" not in result:
    raise SystemExit(result.get("error", result))
print(result["response"])
