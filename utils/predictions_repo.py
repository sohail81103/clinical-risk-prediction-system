from utils.database import get_connection

INSERT_PREDICTION_SQL = """
INSERT INTO patient_predictions (
    radius_mean,
    texture_mean,
    perimeter_mean,
    area_mean,
    smoothness_mean,
    compactness_mean,
    concavity_mean,
    concave_points_mean,
    symmetry_mean,
    fractal_dimension_mean,
    radius_se,
    texture_se,
    perimeter_se,
    area_se,
    smoothness_se,
    compactness_se,
    concavity_se,
    concave_points_se,
    symmetry_se,
    diagnosis,
    confidence
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

RECENT_PREDICTIONS_SQL = """
SELECT
    id,
    radius_mean,
    texture_mean,
    perimeter_mean,
    area_mean,
    smoothness_mean,
    compactness_mean,
    concavity_mean,
    concave_points_mean,
    symmetry_mean,
    fractal_dimension_mean,
    radius_se,
    texture_se,
    perimeter_se,
    area_se,
    smoothness_se,
    compactness_se,
    concavity_se,
    concave_points_se,
    symmetry_se,
    diagnosis,
    confidence,
    created_at
FROM patient_predictions
ORDER BY created_at DESC, id DESC
LIMIT ?;
"""


def save_prediction(features, diagnosis, confidence):
    values = tuple(features) + (diagnosis, confidence)
    with get_connection() as connection:
        connection.execute(INSERT_PREDICTION_SQL, values)
        connection.commit()


def get_recent_predictions(limit=5):
    safe_limit = max(1, int(limit))
    with get_connection() as connection:
        cursor = connection.execute(RECENT_PREDICTIONS_SQL, (safe_limit,))
        rows = cursor.fetchall()
    return [dict(row) for row in rows]
