🩺 Clinical Risk Prediction System (ML + Backend)

A production-ready machine learning–powered backend system that predicts breast cancer risk (Benign / Malignant) based on patient clinical features.
The system exposes a REST API, persists predictions in a database, and is containerized and deployed to the cloud.

🚀 Live API

Base URL: https://clinical-risk-prediction-system-production-7ada.up.railway.app

Swagger Docs: https://clinical-risk-prediction-system-production-7ada.up.railway.app/docs

The Swagger UI allows live testing of the prediction endpoint directly from the browser.

📌 Project Overview

This project demonstrates how a trained machine learning model can be transformed into a scalable backend service.

Key highlights:

Trained ML model is loaded once (no retraining per request)

Input validation using schema-based validation

REST API for inference

Persistent storage of predictions

Containerized deployment

Cloud-hosted and publicly accessible

🧠 Machine Learning Pipeline

Algorithm: Random Forest Classifier

Preprocessing: StandardScaler

Dataset: Breast Cancer Wisconsin Dataset

Model Persistence: joblib

The model and scaler are saved after training and reused during inference to ensure:

Low latency

Consistent predictions

Production-grade behavior

🔄 End-to-End Workflow
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

🏗️ Backend Architecture
clinical-risk-system/
├── api.py                # FastAPI entry point
├── model/
│   ├── train_model.py    # Model training (offline)
│   ├── predict.py        # Inference logic
│   └── rf_model.pkl      # Saved ML model
│   └── scaler.pkl        # Saved scaler
├── utils/
│   ├── preprocessing.py # Feature definitions
│   ├── validators.py    # Input validation
│   ├── database.py      # DB connection
│   ├── init_db.py       # Schema initialization
│   └── predictions_repo.py # DB persistence logic
├── db/                   # Local DB volume
├── Dockerfile
├── requirements.txt
└── README.md

🗄️ Database Design

Local development: SQLite

Cloud deployment: PostgreSQL

Stored fields:

Input features

Prediction result

Confidence score

Timestamp

This enables:

Prediction auditing

Future analytics

Monitoring model behavior

🔌 API Endpoints
1️⃣ Health Check

GET /

{
  "status": "API running"
}

2️⃣ Cancer Risk Prediction

POST /predict

Request
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
{
  "status": "success",
  "diagnosis": "Malignant",
  "confidence": 86.85
}

🐳 Docker & Deployment

Fully containerized using Docker

Environment-based port handling

Compatible with cloud platforms

Deployed using Railway

Docker Run (Local)
docker build -t clinical-risk-api .
docker run -p 8000:8000 clinical-risk-api

🛠️ Tech Stack

ML: Scikit-learn

Backend: FastAPI

Validation: Pydantic

Database: SQLite → PostgreSQL

Deployment: Docker + Railway

Language: Python 3.11

🎯 Why This Project Matters

This project demonstrates:

ML → Backend integration

API-first design

Database-backed inference

Production deployment mindset

Software engineering best practices

It goes beyond notebooks and shows how ML models are actually used in real systems.

👨‍💻 Author

Mohammed Sohail
Final-year B.Tech (ECE)
Interests: Machine Learning, Backend Systems, Distributed Applications

📌 Notes

Authentication and rate limiting can be added for production use

Model retraining pipelines can be integrated in future

Designed for extensibility and scalability