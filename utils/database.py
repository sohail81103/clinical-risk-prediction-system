import sqlite3
import os

BASE_DIR = os.getcwd()
DB_DIR = os.path.join(BASE_DIR, "db")
DB_PATH = os.path.join(DB_DIR, "clinical_risk.db")


def get_connection():
    os.makedirs(DB_DIR, exist_ok=True)

    conn = sqlite3.connect(
        DB_PATH,
        check_same_thread=False,
        timeout=30
    )

    # Recommended SQLite pragmas
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.row_factory = sqlite3.Row

    return conn
