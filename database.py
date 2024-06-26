import os
import sqlite3

from dotenv import load_dotenv

from errors import error_handler

load_dotenv()
database = os.getenv('DATABASE_NAME')


@error_handler
class Database:
    """
    Class for managing all actions related to database operations.
    """

    def __init__(self):
        """
        Sets connection to database.
        """

        self.connection = sqlite3.connect(database=database, check_same_thread=False)
        if len(database) == 0:
            raise ValueError('DATABASE_NAME can not be empty')

        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """
        Creates table if not exists.
        """

        with self.connection:
            self.cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    password TEXT
                );
                '''
            )

    def create_user(self, username: str, password: str) -> bool:
        """
        Creates user.
        """

        with self.connection:
            result = self.cursor.execute(
                '''
                INSERT INTO users (username, password)
                VALUES (?, ?);
                ''', (username, password)
            ).fetchone()
            return True if result is None else False

    def auth_user(self, username: str, password: str) -> bool:
        """
        Check users authentication credentials.
        """

        with self.connection:
            result = self.cursor.execute(
                '''
                SELECT *
                FROM users
                WHERE username = ?
                AND password = ?;
                ''', (username, password)
            ).fetchone()
            return True if result is not None else False
