import os
import sqlite3
from pathlib import Path

DEFAULT_DB_PATH = Path("db/clinical_risk.db")
DB_PATH = Path(os.getenv("SQLITE_DB_PATH", str(DEFAULT_DB_PATH)))


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection
