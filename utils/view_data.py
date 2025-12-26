from utils.database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT id, diagnosis, confidence, created_at FROM patient_predictions")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
