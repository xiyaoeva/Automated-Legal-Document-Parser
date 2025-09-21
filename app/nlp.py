
import re

CLAUSE_KEYWORDS = ["confidentiality", "termination", "liability", "indemnification", "governing law"]

def extract_key_info(text: str):
    parties = []
    # naive party extraction
    for m in re.finditer(r"between\s+(.*?)\s+and\s+(.*?)[\.,\n]", text, flags=re.IGNORECASE):
        parties = [m.group(1).strip(), m.group(2).strip()]
        break

    # naive date extraction (YYYY or Month day, year)
    dates = re.findall(r"(?:\b\d{4}\b|\b\w+\s+\d{1,2},\s+\d{4}\b)", text)

    clauses = [kw for kw in CLAUSE_KEYWORDS if kw in text.lower()]

    return {"parties": parties, "dates": dates, "clauses": clauses}

def summarize_text(text: str, max_len: int = 220):
    t = " ".join(text.split())
    return t[:max_len] + ("..." if len(t) > max_len else "")
