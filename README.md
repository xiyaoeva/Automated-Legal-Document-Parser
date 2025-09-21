
# Automated Legal Document Parser (Pro)

A more complete **NLP + ML** skeleton for legal docs.

## Highlights
- Flask API (`/health`, `/extract`, `/summarize`, `/categorize`)
- MongoDB persistence (Docker)
- **ML pipeline**: TF‑IDF + LogisticRegression (demo) with saved model
- **Unit tests** with pytest (API + ML)
- Dockerfile + docker-compose (API + Mongo)
- Makefile for quick commands

## Quick Start
```bash
# 1) Start Mongo
docker-compose up -d mongo

# 2) Create & activate venv (optional), then install deps
pip install -r requirements.txt

# 3) Train demo model
python -m app.train

# 4) Run API
python -m app.app

# 5) Test
pytest -q
```

## API
- `GET /health`
- `POST /extract`  -> {"parties":[], "dates":[], "clauses":[]}
- `POST /summarize` -> {"summary": "..."}
- `POST /categorize` -> {"label": "high-risk" | "low-risk", "proba": 0.93}

> Replace demo training data with your own to improve accuracy and realism.
