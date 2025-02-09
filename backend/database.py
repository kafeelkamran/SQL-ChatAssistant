import sqlite3
import os

# Get absolute path to the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Backend directory
DB_PATH = os.path.join(BASE_DIR, "../data/company.db")  # Move up one level to 'data'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Enables dictionary-style access
    return conn
