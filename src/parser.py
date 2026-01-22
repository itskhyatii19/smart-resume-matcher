# parser.py
import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def load_resume(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return clean_text(f.read())
