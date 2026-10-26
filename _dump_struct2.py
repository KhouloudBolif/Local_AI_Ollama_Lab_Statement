import json
nb = json.load(open(r"c:\Users\khouloud.bolif\Documents\PHD\lab2\Local_AI_Ollama_Lab_Statement.ipynb", encoding="utf-8"))
parts = []
for i in range(59, 65):
    c = nb["cells"][i]
    src = "".join(c["source"])
    chunks = []
    for o in c.get("outputs", []):
        if o.get("output_type") == "stream":
            chunks.append("".join(o.get("text", []))[:1500])
        elif o.get("output_type") == "error":
            chunks.append(str(o.get("evalue", ""))[:400])
        elif o.get("output_type") in ("execute_result", "display_data"):
            t = o.get("data", {}).get("text/plain", "")
            if isinstance(t, list):
                t = "".join(t)
            chunks.append(t[:1500])
    parts.append(f"\n\n===== {i} =====\n" + src[:1800])
    if chunks:
        parts.append("\n---OUT---\n" + "\n".join(chunks)[:2000])
open(r"c:\Users\khouloud.bolif\Documents\PHD\lab2\_struct2.txt", "w", encoding="utf-8").write("".join(parts))
print("ok")
