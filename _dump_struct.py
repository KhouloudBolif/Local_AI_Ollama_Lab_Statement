import json
nb = json.load(open(r"c:\Users\khouloud.bolif\Documents\PHD\lab2\Local_AI_Ollama_Lab_Statement.ipynb", encoding="utf-8"))
for i, c in enumerate(nb["cells"]):
    src = "".join(c["source"])
    if "structured output" in src.lower() or "format" in src and "json" in src.lower() and i > 55:
        open(r"c:\Users\khouloud.bolif\Documents\PHD\lab2\_struct.txt", "a", encoding="utf-8").write(f"\n\n===== {i} {c['cell_type']} =====\n" + src[:2200])
print("ok")
