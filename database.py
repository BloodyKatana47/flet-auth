import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
database = os.getenv('DATABASE_NAME')


class Database:
    def __init__(self):
        """Set connection to database"""
        self.connection = sqlite3.connect(database=database, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_user(self, username, password):
        """Create user"""
        with self.connection:
            result = self.cursor.execute(
                'INSERT INTO users (username, password) VALUES (?, ?)',
                (username, password)
            ).fetchone()
            return True if result is None else False

    def auth_user(self, username, password):
        """Check users authentication credentials"""
        with self.connection:
            result = self.cursor.execute(
                'SELECT * FROM users WHERE username = ? AND password = ?', (username, password)
            ).fetchone()
            return True if result is not None else False

    def create_task(self, user_id, description):
        """Create task"""
        with self.connection:
            result = self.cursor.execute(
                'INSERT INTO tasks (description, user_id) VALUES (?, ?)',
                (description, user_id)
            ).fetchone()
            return True if result is None else False

    def fetch_tasks(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM tasks WHERE user_id = ?', (user_id,)).fetchall()
            return result if len(result) > 0 else None
