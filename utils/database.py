import sqlite3
import os

BASE_DIR = os.getenv("RAILWAY_VOLUME_MOUNT_PATH", "/tmp")
DB_PATH = os.path.join(BASE_DIR, "clinical_risk.db")

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)
