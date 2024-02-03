import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")

connection = sqlite3.connect(database=DATABASE_NAME)
cursor = connection.cursor()
cursor.executescript('''
    BEGIN;
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        description TEXT,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    );
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    );
    COMMIT;
''')
connection.close()
