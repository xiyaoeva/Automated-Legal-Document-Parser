
import json
from app.app import create_app

def test_health():
    app = create_app()
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"

def test_extract_and_summarize():
    app = create_app()
    client = app.test_client()
    text = "Agreement made on January 1, 2024 between Party A and Party B. Confidentiality applies."
    r = client.post("/extract", json={"text": text})
    data = r.get_json()
    assert "confidentiality" in data["clauses"]

    r2 = client.post("/summarize", json={"text": text*10})
    assert "summary" in r2.get_json()

def test_categorize():
    app = create_app()
    client = app.test_client()
    text = "This contract includes termination and indemnification."
    r = client.post("/categorize", json={"text": text})
    data = r.get_json()
    assert data["label"] in ("high-risk","low-risk")
