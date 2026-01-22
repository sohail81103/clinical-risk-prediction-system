## 🩺 Clinical Risk Prediction System (ML + Backend)

A production-ready machine learning–powered backend system that predicts breast cancer risk (Benign / Malignant) using patient clinical features.  
The system exposes a REST API, stores predictions in a database, and is containerized and deployed to the cloud.

---

## 🚀 Live API

**Base URL**  
https://clinical-risk-prediction-system-production-7ada.up.railway.app/

**Swagger API Docs**  
https://clinical-risk-prediction-system-production-7ada.up.railway.app/docs  

The Swagger UI allows live testing of the prediction endpoint directly from the browser.

---

## 📌 Project Overview

This project demonstrates how a trained machine learning model can be transformed into a scalable backend service.

**Key highlights:**
- ML model is trained once and reused for inference
- Schema-based input validation
- REST API for prediction
- Persistent storage of predictions
- Dockerized and cloud deployed
- Accessible from web and mobile

---

## 🧠 Machine Learning Pipeline

- **Algorithm:** Random Forest Classifier  
- **Preprocessing:** StandardScaler  
- **Dataset:** Breast Cancer Wisconsin Dataset  
- **Model Persistence:** joblib  

The trained model and scaler are serialized and loaded during runtime to ensure:
- Low latency
- No repeated training
- Consistent predictions

---

## 🔄 End-to-End Workflow

```text
Client (JSON Request)
        ↓
FastAPI Endpoint
        ↓
Pydantic Validation
        ↓
Feature Preprocessing
        ↓
ML Model Inference
        ↓
Prediction + Confidence
        ↓
Database Persistence
        ↓
JSON Response


clinical-risk-system/
├── api.py                # FastAPI entry point
├── model/
│   ├── train_model.py    # Offline model training
│   ├── predict.py        # Inference logic
│   ├── rf_model.pkl      # Saved ML model
│   └── scaler.pkl        # Saved scaler
├── utils/
│   ├── preprocessing.py  # Feature definitions
│   ├── validators.py     # Input validation
│   ├── database.py       # DB connection logic
│   ├── init_db.py        # DB schema initialization
│   └── predictions_repo.py # Persistence layer
├── db/                   # Local database volume
├── Dockerfile
├── requirements.txt
└── README.md
