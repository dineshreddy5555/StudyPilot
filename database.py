import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "studypilot.db")


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_tables():
    connection = get_connection()

    try:
        # Users
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                is_admin INTEGER NOT NULL DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Add is_admin to existing databases if missing
        user_columns = {
            row["name"]
            for row in connection.execute(
                "PRAGMA table_info(users)"
            ).fetchall()
        }

        if "is_admin" not in user_columns:
            connection.execute("""
                ALTER TABLE users
                ADD COLUMN is_admin INTEGER NOT NULL DEFAULT 0
            """)

        # Subjects
        connection.execute("""
            CREATE TABLE IF NOT EXISTS subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)

        # Study sessions
        connection.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject TEXT NOT NULL,
                study_date TEXT NOT NULL,
                study_time TEXT NOT NULL
            )
        """)

        # Tasks
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0,
                completed_date TEXT
            )
        """)

        # Ensure completed_date exists in older databases
        task_columns = {
            row["name"]
            for row in connection.execute(
                "PRAGMA table_info(tasks)"
            ).fetchall()
        }

        if "completed_date" not in task_columns:
            connection.execute("""
                ALTER TABLE tasks
                ADD COLUMN completed_date TEXT
            """)

        # Daily goals
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

        # Course progress
        table_exists = connection.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name = 'course_progress'
        """).fetchone()

        if table_exists:
            columns = {
                row["name"]
                for row in connection.execute(
                    "PRAGMA table_info(course_progress)"
                ).fetchall()
            }

            unique_indexes = []

            for index in connection.execute(
                "PRAGMA index_list(course_progress)"
            ).fetchall():

                if index["unique"]:
                    index_name = index["name"].replace('"', '""')

                    index_columns = tuple(
                        row["name"]
                        for row in connection.execute(
                            f'PRAGMA index_info("{index_name}")'
                        ).fetchall()
                    )

                    unique_indexes.append(index_columns)

            required_unique_index = (
                "user_id",
                "course_name",
                "lesson_id"
            )

            if (
                "user_id" not in columns
                or required_unique_index not in unique_indexes
            ):
                connection.execute("""
                    ALTER TABLE course_progress
                    RENAME TO course_progress_old_migration
                """)

                connection.execute("""
                    CREATE TABLE course_progress (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        course_name TEXT NOT NULL,
                        lesson_id INTEGER NOT NULL,
                        completed INTEGER NOT NULL DEFAULT 0,
                        completed_at TEXT,
                        UNIQUE(user_id, course_name, lesson_id)
                    )
                """)

                if "user_id" in columns:
                    connection.execute("""
                        INSERT OR IGNORE INTO course_progress (
                            user_id,
                            course_name,
                            lesson_id,
                            completed,
                            completed_at
                        )
                        SELECT
                            user_id,
                            course_name,
                            lesson_id,
                            completed,
                            completed_at
                        FROM course_progress_old_migration
                    """)
                else:
                    connection.execute("""
                        INSERT INTO course_progress (
                            user_id,
                            course_name,
                            lesson_id,
                            completed,
                            completed_at
                        )
                        SELECT
                            NULL,
                            course_name,
                            lesson_id,
                            completed,
                            completed_at
                        FROM course_progress_old_migration
                    """)

                connection.execute(
                    "DROP TABLE course_progress_old_migration"
                )

        else:
            connection.execute("""
                CREATE TABLE course_progress (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    course_name TEXT NOT NULL,
                    lesson_id INTEGER NOT NULL,
                    completed INTEGER NOT NULL DEFAULT 0,
                    completed_at TEXT,
                    UNIQUE(user_id, course_name, lesson_id)
                )
            """)

        # Quiz scores
        connection.execute("""
            CREATE TABLE IF NOT EXISTS quiz_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                course_id TEXT NOT NULL,
                lesson_id INTEGER NOT NULL,
                score INTEGER NOT NULL DEFAULT 0,
                total_questions INTEGER NOT NULL DEFAULT 0,
                percentage INTEGER NOT NULL DEFAULT 0,
                completed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Certificates
        connection.execute("""
            CREATE TABLE IF NOT EXISTS certificates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                course_id TEXT NOT NULL,
                course_name TEXT NOT NULL,
                certificate_code TEXT NOT NULL UNIQUE,
                issued_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, course_id)
            )
        """)

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def create_admin_tables():
    connection = get_connection()

    try:
        # Website visitor tracking
        connection.execute("""
            CREATE TABLE IF NOT EXISTS website_visits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                visitor_session TEXT,
                page TEXT NOT NULL,
                visited_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Assignments
        connection.execute("""
            CREATE TABLE IF NOT EXISTS assignments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                course_name TEXT,
                due_date TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Assignment submissions
        connection.execute("""
            CREATE TABLE IF NOT EXISTS assignment_submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                assignment_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                submission_text TEXT,
                submitted_at TEXT DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (assignment_id)
                    REFERENCES assignments(id)
                    ON DELETE CASCADE,

                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE,

                UNIQUE(assignment_id, user_id)
            )
        """)

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()