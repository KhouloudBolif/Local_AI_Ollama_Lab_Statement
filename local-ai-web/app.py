from flask import Flask, render_template, request
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3.5:0.8b"


@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""

    if request.method == "POST":
        question = request.form["question"]
        data = {
            "model": MODEL,
            "prompt": question,
            "stream": False,
            "think": False,
        }
        response = requests.post(OLLAMA_URL, json=data, timeout=600)
        payload = response.json()
        answer = payload.get("response") or payload.get("error") or str(payload)

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)
