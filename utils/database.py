import os
import sqlite3

DB_PATH = os.path.join("db", "clinical_risk.db")

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)
