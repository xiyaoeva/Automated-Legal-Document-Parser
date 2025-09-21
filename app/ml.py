
from pathlib import Path
from typing import Tuple
from joblib import dump, load
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import numpy as np

MODEL_PATH = Path(__file__).parent / "model.joblib"

LABELS = ["low-risk", "high-risk"]

class ModelService:
    def __init__(self):
        if MODEL_PATH.exists():
            self.pipeline = load(MODEL_PATH)
        else:
            # fallback simple model
            self.pipeline = Pipeline([
                ("tfidf", TfidfVectorizer(ngram_range=(1,2))),
                ("clf", LogisticRegression(max_iter=300))
            ])
            # Train quick demo model
            X = [
                "agreement with confidentiality and termination",
                "breach, indemnification, liability cap exceeded",
                "friendly memo about schedule",
                "meeting notes without legal terms",
            ]
            y = [1,1,0,0]
            self.pipeline.fit(X,y)

    def predict(self, text: str) -> Tuple[str, float]:
        proba = self.pipeline.predict_proba([text])[0][1]
        label = LABELS[1] if proba >= 0.5 else LABELS[0]
        return label, float(np.round(proba, 4))

def train_default():
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1,2))),
        ("clf", LogisticRegression(max_iter=500))
    ])
    X = [
        "This contract includes confidentiality, termination, and penalty clauses.",
        "Indemnification and liability provisions apply upon breach.",
        "Schedule for delivery and meeting logistics.",
        "Casual email about team lunch.",
        "NDA with strict confidentiality obligations.",
        "Service agreement with limited liability and governing law New York.",
        "Hello world unrelated text",
        "Project update without legal language",
    ]
    y = [1,1,0,0,1,1,0,0]
    pipeline.fit(X,y)
    dump(pipeline, MODEL_PATH)
