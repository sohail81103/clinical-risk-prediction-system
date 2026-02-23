## 🩺 Clinical Risk Prediction System (ML + Backend)

A production-ready machine learning–powered backend system that predicts breast cancer risk (Benign / Malignant) using patient clinical features.

The system exposes a REST API, stores predictions in a database, and is containerized and deployed to the cloud.

---

## 🚀 Live API

**Base URL**  
https://clinical-risk-prediction-system.onrender.com

**Swagger API Docs**  
https://clinical-risk-prediction-system.onrender.com/docs

The Swagger UI allows live testing of the prediction endpoint directly from the browser.

---

## 📌 Project Overview

This project demonstrates how a trained machine learning model can be transformed into a scalable backend service.

**Key highlights:**
- ML model trained offline and reused for inference

- Schema-based input validation using Pydantic

- REST API for prediction

- Persistent storage of predictions

- Dockerized application

- Cloud deployment using Render

---

## 🧠 Machine Learning Pipeline

- **Algorithm:** Random Forest Classifier  
- **Preprocessing:** StandardScaler  
- **Dataset:** Breast Cancer Wisconsin Dataset  
- **Model Persistence:** joblib  

The trained model and scaler are serialized and loaded during runtime to ensure:
- Low latency inference
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
```
---

## 📂 Backend Architecture

```text
clinical-risk-system/
├── api.py                # FastAPI entry point
├── model/
│   ├── train_model.py    # Offline model training
│   ├── predict.py        # Inference logic
│   ├── rf_model.pkl      # Saved ML model
│   └── scaler.pkl        # Saved scaler
├── utils/
│   ├── preprocessing.py # Feature definitions
│   ├── validators.py    # Input validation
│   ├── database.py      # DB connection logic
│   ├── init_db.py       # DB schema initialization
│   └── predictions_repo.py # Persistence layer
├── db/                   # Local database volume
├── Dockerfile
├── requirements.txt
└── README.md
```
---

## 🗄️ Database Design
```text
Local development: SQLite
Cloud deployment (Render): SQLite (file-based)

Stored information:

Patient feature values

Prediction result (Benign / Malignant)

Confidence score

Timestamp

This enables auditing, tracking, and future analytics.
```

Render note:
- Set `SQLITE_DB_PATH` to your persistent disk path (example: `/var/data/clinical_risk.db`)

---

## 🔌 API Endpoints
```text

1️⃣ Health Check
GET /

json
Copy code
{
  "status": "API running"
}
2️⃣ Cancer Risk Prediction
POST /predict

Request

json
Copy code
{
  "features": [
    17.99, 10.38, 122.8, 1001.0, 0.1184,
    0.2776, 0.3001, 0.1471, 0.2419,
    0.07871, 1.095, 0.9053, 8.589,
    153.4, 0.006399, 0.04904,
    0.05373, 0.01587, 0.03003
  ]
}
Response

json
Copy code
{
  "status": "success",
  "diagnosis": "Malignant",
  "confidence": 86.85
}
```
---

## 🐳 Docker & Deployment
```text
Fully containerized using Docker

Environment-based port handling

Deployed on Render Cloud Platform

Publicly accessible API

Run locally

bash
Copy code
docker build -t clinical-risk-api .
docker run -p 8000:8000 clinical-risk-api
🛠️ Tech Stack
Machine Learning: Scikit-learn

Backend API: FastAPI

Validation: Pydantic

Database: SQLite (`sqlite3` raw SQL)

Deployment: Docker + Render

Language: Python 3.11
```
---

## 🎯 Why This Project Matters
```text
This project demonstrates:

ML → Backend system integration

API-first backend design

Database-backed inference

Cloud deployment experience

Software engineering best practices

It goes beyond notebooks and shows how ML models are used in real-world systems.
```
----
👨‍💻 Author
Mohammed Sohail
