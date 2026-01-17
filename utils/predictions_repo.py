from sqlalchemy.orm import Session
from utils.models import PatientPrediction

def save_prediction(db: Session, features, diagnosis, confidence):
    record = PatientPrediction(
        radius_mean=features[0],
        texture_mean=features[1],
        perimeter_mean=features[2],
        area_mean=features[3],
        smoothness_mean=features[4],
        compactness_mean=features[5],
        concavity_mean=features[6],
        concave_points_mean=features[7],
        symmetry_mean=features[8],
        fractal_dimension_mean=features[9],
        radius_se=features[10],
        texture_se=features[11],
        perimeter_se=features[12],
        area_se=features[13],
        smoothness_se=features[14],
        compactness_se=features[15],
        concavity_se=features[16],
        concave_points_se=features[17],
        symmetry_se=features[18],
        diagnosis=diagnosis,
        confidence=confidence
    )

    db.add(record)
    db.commit()
