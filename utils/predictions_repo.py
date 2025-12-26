from utils.database import get_connection
from utils.preprocessing import FEATURE_COLUMNS

def save_prediction(features, diagnosis, confidence):
    """
    Saves a prediction record into the database
    """

    conn = get_connection()
    cursor = conn.cursor()

    # Build SQL query dynamically
    columns = ", ".join(FEATURE_COLUMNS) + ", diagnosis, confidence"
    placeholders = ", ".join(["?"] * (len(FEATURE_COLUMNS) + 2))

    sql = f"""
        INSERT INTO patient_predictions ({columns})
        VALUES ({placeholders})
    """

    values = features + [diagnosis, confidence]

    cursor.execute(sql, values)
    conn.commit()
    conn.close()

    
def get_recent_predictions(limit=5):
    """
    Fetch recent prediction records from database
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, diagnosis, confidence, created_at
        FROM patient_predictions
        ORDER BY created_at DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return rows
