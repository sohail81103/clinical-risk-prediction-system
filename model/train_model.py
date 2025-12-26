import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from utils.preprocessing import load_and_preprocess_data


# Load and preprocess data
X, y = load_and_preprocess_data("data/breast_cancer.csv")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Model (best params from your notebook)
model = RandomForestClassifier(
    n_estimators=350,
    max_depth=75,
    min_samples_split=8,
    min_samples_leaf=1,
    bootstrap=True,
    random_state=42
)

# Train model
model.fit(X_train_scaled, y_train)

# Save model & scaler
joblib.dump(model, "model/rf_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("Model training completed and saved successfully.")
