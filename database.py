import sqlite3

DATABASE = "studypilot.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            study_date TEXT NOT NULL,
            study_time TEXT NOT NULL
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0,
            completed_date TEXT
        )
    """)

    columns = connection.execute(
        "PRAGMA table_info(tasks)"
    ).fetchall()

    column_names = [column["name"] for column in columns]

    if "completed_date" not in column_names:
        connection.execute(
            "ALTER TABLE tasks ADD COLUMN completed_date TEXT"
        )

    connection.execute("""
        CREATE TABLE IF NOT EXISTS daily_goals (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            target INTEGER NOT NULL DEFAULT 3
        )
    """)

    connection.execute("""
        INSERT OR IGNORE INTO daily_goals (id, target)
        VALUES (1, 3)
    """)

    connection.commit()
    connection.close()