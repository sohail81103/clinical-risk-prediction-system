from model.predict import predict_cancer_risk

# Sample patient input (same order as training features)
patient_features = [
    17.99, 10.38, 122.8, 1001.0, 0.1184,
    0.2776, 0.3001, 0.1471, 0.2419,
    0.07871, 1.095, 0.9053, 8.589,
    153.4, 0.006399, 0.04904,
    0.05373, 0.01587, 0.03003
]

result = predict_cancer_risk(patient_features)
print(result)
from utils.predictions_repo import get_recent_predictions

print("\nRecent prediction history:")

records = get_recent_predictions(limit=5)
for record in records:
    print(record)
