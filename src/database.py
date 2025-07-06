import sqlite3
from datetime import datetime

DB_NAME = "water_tracker.db"


def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor("""
    CREATE A TABLE IF NOT EXITS water_tracker.bd(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        intake_ml INTEGER,
        date TEXT
    )
    """)