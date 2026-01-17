import sqlite3
import os

DB_PATH = os.path.join("db", "clinical_risk.db")

def get_connection():
    os.makedirs("db", exist_ok=True)
    return sqlite3.connect(DB_PATH, check_same_thread=False)
