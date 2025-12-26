from fastapi import FastAPI
from pydantic import BaseModel
from model.predict import predict_cancer_risk

app = FastAPI(title="Clinical Risk Prediction API")

class PatientData(BaseModel):
    features: list

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
