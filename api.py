import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from utils.init_db import init_db
from model.predict import predict_cancer_risk

app = FastAPI(title="Clinical Risk Prediction API")

class PatientData(BaseModel):
    features: List[float]

@app.on_event("startup")
def startup():
    init_db()


@app.post("/predict")
def predict(data: PatientData):
    return predict_cancer_risk(data.features)

@app.get("/")
def home():
    return {"status": "API running"}
