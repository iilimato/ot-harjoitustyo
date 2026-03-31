import os
import sqlite3

DATABASE_PATH = os.path.join(os.path.dirname(
    __file__), "..", "data", "treeni.db")


def get_database_connection():
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database(connection):
    connection.executescript("""
        CREATE TABLE IF NOT EXISTS exercise (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            muscle_group TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS workout (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS workout_set (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workout_id INTEGER NOT NULL REFERENCES workout(id),
            exercise_id INTEGER NOT NULL REFERENCES exercise(id),
            weight REAL NOT NULL,
            reps INTEGER NOT NULL
        );
    """)
    connection.commit()


def seed_exercises(connection):
    cursor = connection.execute("SELECT COUNT(*) FROM exercise")
    if cursor.fetchone()[0] > 0:
        return

    exercises = [
        ("Penkkipunnerrus", "Rinta"),
        ("Maastaveto", "Selkä"),
        ("Kyykky", "Jalat"),
        ("Pystypunnerrus", "Olkapäät"),
        ("Hauiskääntö", "Kädet"),
        ("Ojentajapunnerrus", "Kädet"),
        ("Leuanveto", "Selkä"),
        ("Dippi", "Kädet"),
    ]

    connection.executemany(
        "INSERT INTO exercise (name, muscle_group) VALUES (?, ?)",
        exercises,
    )
    connection.commit()
