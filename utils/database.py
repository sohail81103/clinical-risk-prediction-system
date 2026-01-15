import sqlite3

import os

DB_PATH = os.getenv("DB_PATH", "db/clinical_risk.db")


def get_connection():
    return sqlite3.connect(DB_PATH)
