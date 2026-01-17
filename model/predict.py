import joblib
import pandas as pd

from utils.preprocessing import FEATURE_COLUMNS
from utils.predictions_repo import save_prediction
from utils.validators import validate_features
from utils.database import SessionLocal

model = joblib.load("model/rf_model.pkl")
scaler = joblib.load("model/scaler.pkl")

def predict_cancer_risk(features, persist=True):
    validate_features(features)

    input_df = pd.DataFrame([features], columns=FEATURE_COLUMNS)
    scaled_features = scaler.transform(input_df)

    prediction = model.predict(scaled_features)[0]
    confidence = model.predict_proba(scaled_features)[0][prediction]

    diagnosis = "Malignant" if prediction == 1 else "Benign"
    confidence_pct = round(float(confidence) * 100, 2)

    if persist:
        db = SessionLocal()
        try:
            save_prediction(db, features, diagnosis, confidence_pct)
        finally:
            db.close()

    return {
        "status": "success",
        "diagnosis": diagnosis,
        "confidence": confidence_pct
    }
