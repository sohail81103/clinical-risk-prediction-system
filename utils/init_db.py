from utils.database import get_connection

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS patient_predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    radius_mean REAL NOT NULL,
    texture_mean REAL NOT NULL,
    perimeter_mean REAL NOT NULL,
    area_mean REAL NOT NULL,
    smoothness_mean REAL NOT NULL,
    compactness_mean REAL NOT NULL,
    concavity_mean REAL NOT NULL,
    concave_points_mean REAL NOT NULL,
    symmetry_mean REAL NOT NULL,
    fractal_dimension_mean REAL NOT NULL,
    radius_se REAL NOT NULL,
    texture_se REAL NOT NULL,
    perimeter_se REAL NOT NULL,
    area_se REAL NOT NULL,
    smoothness_se REAL NOT NULL,
    compactness_se REAL NOT NULL,
    concavity_se REAL NOT NULL,
    concave_points_se REAL NOT NULL,
    symmetry_se REAL NOT NULL,
    diagnosis TEXT NOT NULL,
    confidence REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""


def init_db():
    with get_connection() as connection:
        connection.execute(CREATE_TABLE_SQL)
        connection.commit()
