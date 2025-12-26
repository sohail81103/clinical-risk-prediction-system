import sqlite3

DB_PATH = "clinical_risk.db"

def get_connection():
    return sqlite3.connect(DB_PATH)
