🩺 Clinical Risk Prediction System (Breast Cancer Classification)

A full backend ML project that predicts breast cancer risk using a trained Random Forest model.
Includes data preprocessing, ML model training, database storage (SQLite), and a FastAPI REST API for live predictions.

💡 This project is built for interview portfolio use — suitable for backend, ML, and full-stack roles.

🚀 Project Features

✔️ ML Model (Random Forest Classifier)

✔️ Local inference API with FastAPI

✔️ SQLite database storing prediction history

✔️ Input validation before inference

✔️ Model & scaler saved (.pkl) for reuse

✔️ Auto-documentation via Swagger UI (/docs)

🧠 Tech Stack Overview
Layer	Technology
ML Model	Scikit-learn, RandomForestClassifier
API Backend	FastAPI + Uvicorn
Storage	SQLite (local DB)
Model Persistence	Joblib (.pkl files)
Environment	Python 3.11 (venv)
📂 Folder Structure
clinical-risk-prediction-system/
│
├── data/
│   └── breast_cancer.csv                # raw dataset
│
├── model/
│   ├── train_model.py                   # training script
│   ├── predict.py                       # ML inference
│   ├── rf_model.pkl                     # trained model
│   └── scaler.pkl                       # standard scaler
│
├── utils/
│   ├── preprocessing.py                 # feature selection & mapping
│   ├── validators.py                    # input checks
│   ├── database.py                      # DB connection setup
│   ├── predictions_repo.py              # CRUD functions
│   └── init_db.py                       # create DB schema
│
├── api.py                               # FastAPI application
├── main.py                              # local run script
├── clinical_risk.db                     # generated SQLite DB
├── requirements.txt                     # dependencies
└── README.md                            # documentation

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/sohail81103/clinical-risk-prediction-system.git
cd clinical-risk-prediction-system

2️⃣ Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate       # mac / linux
venv\Scripts\activate          # windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Initialize SQLite Database
python utils/init_db.py

5️⃣ Start the FastAPI Server
uvicorn api:app --reload

🌐 Access API
Purpose	URL
API homepage	http://127.0.0.1:8000

API documentation (Swagger UI)	http://127.0.0.1:8000/docs

JSON schema docs	http://127.0.0.1:8000/openapi.json
🧪 Example API Request (POST /predict)

📍 Endpoint:

POST http://127.0.0.1:8000/predict


📨 Request Body:

{
  "features": [
    17.99, 10.38, 122.8, 1001.0, 0.1184,
    0.2776, 0.3001, 0.1471, 0.2419, 0.07871,
    1.095, 0.9053, 8.589, 153.4, 0.006399,
    0.04904, 0.05373, 0.01587, 0.03003
  ]
}


📤 Response:

{
  "status": "success",
  "diagnosis": "Malignant",
  "confidence": 86.85
}

🗃️ Database Usage (SQLite)
View Saved Predictions
python utils/view_data.py


Sample DB row:

(id, diagnosis, confidence, created_at)
(1, 'Malignant', 86.85, '2025-12-25 03:27:46')

📌 Architectural Flow
Patient Input (19 features)
        ↓
 Input Validation (validators.py)
        ↓
 Data Preprocessing & Scaling
        ↓
 ML Model Inference (predict.py)
        ↓
 Prediction Output + Confidence
        ↓
 Stored in Database (predictions_repo.py)
        ↓
 Accessible through REST API (api.py)

🚀 Deployment Options (Next Steps)
Platform	Use-Case	Difficulty
Railway.app	Host API online for free	⭐ Easy
Render.com	Auto deploy backend	⭐⭐ Medium
Docker	Containerized deployment	⭐⭐⭐ Professional
HuggingFace Space	ML + UI showcase	⭐⭐ Medium
📌 Future Enhancements

🔐 Add JWT / API key authentication

📊 Streamlit UI dashboard for doctors

☁️ Migrate DB to PostgreSQL cloud

🐳 Dockerize for production deployment

📱 Mobile app integration via API

👨‍💻 Author

Mohammed Sohail
Final Year ECE | ML • Backend • APIs
📌 GitHub: https://github.com/sohail81103

🎉 Summary

This project proves skills in:
✔ ML model training & inference
✔ Backend development with FastAPI
✔ Database persistence & CRUD
✔ API deployment readiness

A very strong project for internships / placements.

📍 Next Step for You

If you want, I can now help with:
Deploying this online (free URL)
just say:
➡️ Deploy Now