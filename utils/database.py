import sqlite3

import os

DB_DIR = "db"
os.makedirs(DB_DIR, exist_ok=True)

DB_PATH = os.path.join(DB_DIR, "clinical_risk.db")


def get_connection():
    return sqlite3.connect(DB_PATH)
