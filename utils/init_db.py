from utils.database import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patient_predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        radius_mean REAL,
        texture_mean REAL,
        perimeter_mean REAL,
        area_mean REAL,
        smoothness_mean REAL,
        compactness_mean REAL,
        concavity_mean REAL,
        concave_points_mean REAL,
        symmetry_mean REAL,
        fractal_dimension_mean REAL,
        radius_se REAL,
        texture_se REAL,
        perimeter_se REAL,
        area_se REAL,
        smoothness_se REAL,
        compactness_se REAL,
        concavity_se REAL,
        concave_points_se REAL,
        symmetry_se REAL,
        diagnosis TEXT,
        confidence REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")



