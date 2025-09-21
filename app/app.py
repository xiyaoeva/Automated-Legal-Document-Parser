
import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from .ml import ModelService
from .nlp import extract_key_info, summarize_text

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/legalsvc")
client = MongoClient(MONGO_URI)
db = client.get_default_database()
docs = db["documents"]

model_service = ModelService()

def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.post("/extract")
    def extract():
        text = request.json.get("text","")
        info = extract_key_info(text)
        docs.insert_one({"text": text, "extraction": info})
        return jsonify(info)

    @app.post("/summarize")
    def summarize():
        text = request.json.get("text","")
        return jsonify({"summary": summarize_text(text)})

    @app.post("/categorize")
    def categorize():
        text = request.json.get("text","")
        label, proba = model_service.predict(text)
        return jsonify({"label": label, "proba": proba})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
