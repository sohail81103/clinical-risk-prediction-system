import pandas as pd

FEATURE_COLUMNS = [
    "radius_mean", "texture_mean", "perimeter_mean", "area_mean",
    "smoothness_mean", "compactness_mean", "concavity_mean",
    "concave_points_mean",   
    "symmetry_mean", "fractal_dimension_mean",
    "radius_se", "texture_se", "perimeter_se", "area_se",
    "smoothness_se", "compactness_se", "concavity_se",
    "concave_points_se",    
    "symmetry_se"
]

def load_and_preprocess_data(csv_path):
    df = pd.read_csv(csv_path)

    df.drop(columns=["id", "Unnamed: 32"], inplace=True)

    df.rename(columns={
        "concave points_mean": "concave_points_mean",
        "concave points_se": "concave_points_se"
    }, inplace=True)

    df["diagnosis"] = df["diagnosis"].map({"M": 1, "B": 0})

    X = df[FEATURE_COLUMNS]
    y = df["diagnosis"]

    return X, y

