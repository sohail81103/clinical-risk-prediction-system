from utils.init_db import init_db
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from model.predict import predict_cancer_risk

app = FastAPI(title="Clinical Risk Prediction API")

@app.on_event("startup")
def startup_event():
    init_db()


class PatientData(BaseModel):
    features: List[float]

@app.post("/predict")
def predict(data: PatientData):
    result = predict_cancer_risk(data.features)
    return result
@app.get("/")
def home():
    return {
        "message": "Clinical Risk Prediction API is running.",
        "routes": {
            "documentation": "/docs",
            "predict_endpoint": "/predict"
        }
    }
