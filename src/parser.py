# src/parser.py

import re
import os
import pdfplumber

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def load_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return clean_text(f.read())


def load_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return clean_text(text)


def load_resume(file_path: str) -> str:
    ext = file_path.lower()

    if ext.endswith(".pdf"):
        return load_pdf(file_path)

    elif ext.endswith(".txt"):
        return load_txt(file_path)

    else:
        raise ValueError("Unsupported file format")
