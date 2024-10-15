import sqlite3


def create_database():
    c = sqlite3.connect("users.db")
    cursor = c.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            age INTEGER,
            sex TEXT,
            weight REAL,
            height REAL
        )
    ''')
    c.commit()
    c.close()

