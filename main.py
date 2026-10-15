from flask import Flask, render_template, request, redirect, url_for, abort
from datetime import date, timedelta

from database import get_connection, create_tables
from python_course_data import PYTHON_LESSONS

app = Flask(__name__)

# Create database tables
create_tables()


# ==========================================
# PYTHON COURSE PROGRESS TABLE
# ==========================================

def create_course_tables():
    connection = get_connection()
    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS course_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL,
                lesson_id INTEGER NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0,
                completed_at TEXT,
                UNIQUE(course_name, lesson_id)
            )
        """)
        connection.commit()
    finally:
        connection.close()


create_course_tables()


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("welcome.html")


# ==========================================
# SMART DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():
    connection = get_connection()

    try:
        total_subjects = connection.execute(
            "SELECT COUNT(*) AS count FROM subjects"
        ).fetchone()["count"]

        total_tasks = connection.execute(
            "SELECT COUNT(*) AS count FROM tasks"
        ).fetchone()["count"]

        completed_tasks = connection.execute(
            "SELECT COUNT(*) AS count FROM tasks WHERE completed = 1"
        ).fetchone()["count"]

        pending_tasks = total_tasks - completed_tasks

        completion_percentage = (
            int(completed_tasks / total_tasks * 100)
            if total_tasks else 0
        )

        date_rows = connection.execute("""
            SELECT DISTINCT completed_date
            FROM tasks
            WHERE completed = 1
            AND completed_date IS NOT NULL
        """).fetchall()

        studied_dates = [
            row["completed_date"] for row in date_rows
        ]

    finally:
        connection.close()

    streak = calculate_study_streak(studied_dates)

    return render_template(
        "dashboard.html",
        total_subjects=total_subjects,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks,
        completion_percentage=completion_percentage,
        streak=streak
    )


# ==========================================
# SUBJECTS
# ==========================================

@app.route("/subjects", methods=["GET", "POST"])
def subjects():
    connection = get_connection()

    try:
        if request.method == "POST":
            name = request.form.get("name", "").strip()

            if name:
                connection.execute(
                    "INSERT INTO subjects (name) VALUES (?)",
                    (name,)
                )
                connection.commit()

            return redirect(url_for("subjects"))

        all_subjects = connection.execute(
            "SELECT * FROM subjects ORDER BY id DESC"
        ).fetchall()

    finally:
        connection.close()

    return render_template(
        "subjects.html",
        subjects=all_subjects
    )


# Delete a subject
@app.route(
    "/subjects/delete/<int:subject_id>",
    methods=["POST"]
)
def delete_subject(subject_id):
    connection = get_connection()

    try:
        connection.execute(
            "DELETE FROM subjects WHERE id = ?",
            (subject_id,)
        )
        connection.commit()

    finally:
        connection.close()

    return redirect(url_for("subjects"))


# ==========================================
# STUDY TIMETABLE
# ==========================================

@app.route("/timetable", methods=["GET", "POST"])
def timetable():
    connection = get_connection()

    try:
        if request.method == "POST":
            subject = request.form.get("subject", "").strip()
            study_date = request.form.get("study_date", "").strip()
            study_time = request.form.get("study_time", "").strip()

            if subject and study_date and study_time:
                connection.execute("""
                    INSERT INTO sessions
                    (subject, study_date, study_time)
                    VALUES (?, ?, ?)
                """, (subject, study_date, study_time))

                connection.commit()

            return redirect(url_for("timetable"))

        sessions = connection.execute("""
            SELECT *
            FROM sessions
            ORDER BY study_date, study_time
        """).fetchall()

    finally:
        connection.close()

    return render_template(
        "timetable.html",
        sessions=sessions
    )


# ==========================================
# DAILY TASKS
# ==========================================

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    connection = get_connection()

    try:
        if request.method == "POST":
            name = request.form.get("name", "").strip()

            if name:
                connection.execute(
                    "INSERT INTO tasks (name) VALUES (?)",
                    (name,)
                )
                connection.commit()

            return redirect(url_for("tasks"))

        all_tasks = connection.execute("""
            SELECT *
            FROM tasks
            ORDER BY completed ASC, id DESC
        """).fetchall()

    finally:
        connection.close()

    return render_template(
        "tasks.html",
        tasks=all_tasks
    )


# Mark task as completed
@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    connection = get_connection()

    try:
        task = connection.execute(
            "SELECT completed FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()

        if task and task["completed"] == 0:
            connection.execute("""
                UPDATE tasks
                SET completed = 1, completed_date = ?
                WHERE id = ?
            """, (date.today().isoformat(), task_id))

            connection.commit()

    finally:
        connection.close()

    return redirect(url_for("tasks"))


# Undo task completion
@app.route("/undo/<int:task_id>", methods=["POST"])
def undo_task(task_id):
    connection = get_connection()

    try:
        connection.execute("""
            UPDATE tasks
            SET completed = 0, completed_date = NULL
            WHERE id = ?
        """, (task_id,))

        connection.commit()

    finally:
        connection.close()

    return redirect(url_for("tasks"))


# Delete a task
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    connection = get_connection()

    try:
        connection.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        connection.commit()

    finally:
        connection.close()

    return redirect(url_for("tasks"))


# ==========================================
# STUDY STREAK CALCULATION
# ==========================================

def calculate_study_streak(studied_dates):
    if not studied_dates:
        return 0

    today = date.today()
    studied = set(studied_dates)

    if today.isoformat() in studied:
        current_day = today

    elif (today - timedelta(days=1)).isoformat() in studied:
        current_day = today - timedelta(days=1)

    else:
        return 0

    streak = 0

    while current_day.isoformat() in studied:
        streak += 1
        current_day -= timedelta(days=1)

    return streak


# ==========================================
# PROGRESS PAGE
# ==========================================

@app.route("/progress", methods=["GET", "POST"])
def progress():
    connection = get_connection()

    try:
        if request.method == "POST":
            try:
                target = int(
                    request.form.get("daily_target", 3)
                )

                if 1 <= target <= 100:
                    connection.execute(
                        "UPDATE daily_goals SET target = ? WHERE id = 1",
                        (target,)
                    )
                    connection.commit()

            except (ValueError, TypeError):
                pass

            return redirect(url_for("progress"))

        total = connection.execute(
            "SELECT COUNT(*) AS count FROM tasks"
        ).fetchone()["count"]

        completed = connection.execute(
            "SELECT COUNT(*) AS count FROM tasks WHERE completed = 1"
        ).fetchone()["count"]

        today = date.today().isoformat()

        today_completed = connection.execute("""
            SELECT COUNT(*) AS count
            FROM tasks
            WHERE completed = 1 AND completed_date = ?
        """, (today,)).fetchone()["count"]

        goal_row = connection.execute(
            "SELECT target FROM daily_goals WHERE id = 1"
        ).fetchone()

        daily_target = goal_row["target"] if goal_row else 3

        daily_goal_percentage = (
            min(100, int(today_completed / daily_target * 100))
            if daily_target else 0
        )

        remaining_today = max(
            0, daily_target - today_completed
        )

        daily_goal_message = (
            "🎉 Daily goal completed!"
            if remaining_today == 0
            else f"Complete {remaining_today} more task(s) to reach today's goal!"
        )

        date_rows = connection.execute("""
            SELECT DISTINCT completed_date
            FROM tasks
            WHERE completed = 1
            AND completed_date IS NOT NULL
        """).fetchall()

        studied_dates = [
            row["completed_date"] for row in date_rows
        ]

        streak = calculate_study_streak(studied_dates)

        chart_labels = []
        chart_values = []

        for days_ago in range(6, -1, -1):
            day = date.today() - timedelta(days=days_ago)

            count = connection.execute("""
                SELECT COUNT(*) AS count
                FROM tasks
                WHERE completed = 1 AND completed_date = ?
            """, (day.isoformat(),)).fetchone()["count"]

            chart_labels.append(day.strftime("%a"))
            chart_values.append(count)

        pending = total - completed

        percentage = (
            int(completed / total * 100)
            if total else 0
        )

        message = (
            "Great job! Keep learning!"
            if percentage >= 75
            else "Keep going. Every completed task counts!"
        )

        streak_message = (
            f"🔥 Your current study streak is {streak} day(s)!"
            if streak > 0
            else "Complete a task today to start your study streak!"
        )

        # XP and levels
        xp = completed * 10
        level = (xp // 100) + 1
        xp_in_level = xp % 100
        xp_to_next_level = 100 - xp_in_level

        if level < 3:
            level_name = "Beginner"
        elif level < 6:
            level_name = "Intermediate"
        elif level < 10:
            level_name = "Advanced"
        else:
            level_name = "Study Master"

        level_percentage = xp_in_level

        # Achievement badges
        badges = [
            {
                "name": "First Step",
                "icon": "🌱",
                "description": "Complete your first task.",
                "unlocked": completed >= 1
            },
            {
                "name": "Task Starter",
                "icon": "✅",
                "description": "Complete 5 tasks.",
                "unlocked": completed >= 5
            },
            {
                "name": "Task Champion",
                "icon": "🏆",
                "description": "Complete 10 tasks.",
                "unlocked": completed >= 10
            },
            {
                "name": "Task Legend",
                "icon": "👑",
                "description": "Complete 25 tasks.",
                "unlocked": completed >= 25
            },
            {
                "name": "3-Day Streak",
                "icon": "🔥",
                "description": "Study for 3 consecutive days.",
                "unlocked": streak >= 3
            },
            {
                "name": "7-Day Streak",
                "icon": "⚡",
                "description": "Study for 7 consecutive days.",
                "unlocked": streak >= 7
            },
            {
                "name": "Daily Goal Hero",
                "icon": "🎯",
                "description": "Complete today's daily goal.",
                "unlocked": today_completed >= daily_target
            }
        ]

        unlocked_badges = sum(
            1 for badge in badges if badge["unlocked"]
        )

    finally:
        connection.close()

    return render_template(
        "progress.html",
        total=total,
        completed=completed,
        pending=pending,
        percentage=percentage,
        message=message,
        streak=streak,
        streak_message=streak_message,
        chart_labels=chart_labels,
        chart_values=chart_values,
        studied_dates=studied_dates,
        today_completed=today_completed,
        daily_target=daily_target,
        daily_goal_percentage=daily_goal_percentage,
        remaining_today=remaining_today,
        daily_goal_message=daily_goal_message,
        xp=xp,
        level=level,
        level_name=level_name,
        xp_in_level=xp_in_level,
        xp_to_next_level=xp_to_next_level,
        level_percentage=level_percentage,
        badges=badges,
        unlocked_badges=unlocked_badges
    )


# ==========================================
# REWARDS PAGE
# ==========================================

@app.route("/rewards")
def rewards():
    connection = get_connection()

    try:
        completed = connection.execute(
            "SELECT COUNT(*) AS count FROM tasks WHERE completed = 1"
        ).fetchone()["count"]

        studied_dates = [
            row["completed_date"]
            for row in connection.execute("""
                SELECT DISTINCT completed_date
                FROM tasks
                WHERE completed = 1
                AND completed_date IS NOT NULL
            """).fetchall()
        ]

        today = date.today().isoformat()

        today_completed = connection.execute("""
            SELECT COUNT(*) AS count
            FROM tasks
            WHERE completed = 1 AND completed_date = ?
        """, (today,)).fetchone()["count"]

        goal_row = connection.execute(
            "SELECT target FROM daily_goals WHERE id = 1"
        ).fetchone()

        daily_target = goal_row["target"] if goal_row else 3

    finally:
        connection.close()

    xp = completed * 10
    level = (xp // 100) + 1
    xp_in_level = xp % 100
    xp_to_next_level = 100 - xp_in_level

    if level < 3:
        level_name = "Beginner"
    elif level < 6:
        level_name = "Intermediate"
    elif level < 10:
        level_name = "Advanced"
    else:
        level_name = "Study Master"

    streak = calculate_study_streak(studied_dates)

    badges = [
        {
            "name": "First Step",
            "icon": "🌱",
            "description": "Complete your first task.",
            "unlocked": completed >= 1
        },
        {
            "name": "Task Starter",
            "icon": "✅",
            "description": "Complete 5 tasks.",
            "unlocked": completed >= 5
        },
        {
            "name": "Task Champion",
            "icon": "🏆",
            "description": "Complete 10 tasks.",
            "unlocked": completed >= 10
        },
        {
            "name": "Task Legend",
            "icon": "👑",
            "description": "Complete 25 tasks.",
            "unlocked": completed >= 25
        },
        {
            "name": "3-Day Streak",
            "icon": "🔥",
            "description": "Study for 3 consecutive days.",
            "unlocked": streak >= 3
        },
        {
            "name": "7-Day Streak",
            "icon": "⚡",
            "description": "Study for 7 consecutive days.",
            "unlocked": streak >= 7
        },
        {
            "name": "Daily Goal Hero",
            "icon": "🎯",
            "description": "Complete today's daily goal.",
            "unlocked": today_completed >= daily_target
        }
    ]

    return render_template(
        "rewards.html",
        xp=xp,
        level=level,
        level_name=level_name,
        xp_in_level=xp_in_level,
        xp_to_next_level=xp_to_next_level,
        badges=badges
    )


# ==========================================
# COURSES PAGE
# ==========================================

@app.route("/courses")
def courses():
    return render_template("courses.html")


# ==========================================
# PYTHON COURSE
# ==========================================

@app.route("/courses/python")
def python_course():
    connection = get_connection()

    try:
        rows = connection.execute("""
            SELECT lesson_id
            FROM course_progress
            WHERE course_name = ? AND completed = 1
        """, ("Python Basics",)).fetchall()

    finally:
        connection.close()

    completed_ids = [
        row["lesson_id"] for row in rows
    ]

    completed_count = len(completed_ids)
    total_lessons = len(PYTHON_LESSONS)

    percentage = (
        int(completed_count / total_lessons * 100)
        if total_lessons else 0
    )

    return render_template(
        "python_course.html",
        lessons=PYTHON_LESSONS,
        completed_ids=completed_ids,
        completed_count=completed_count,
        total_lessons=total_lessons,
        percentage=percentage
    )


# ==========================================
# PYTHON LESSON PAGE
# ==========================================

@app.route("/courses/python/lesson/<int:lesson_id>")
def python_lesson(lesson_id):
    lesson = next(
        (
            item for item in PYTHON_LESSONS
            if item["id"] == lesson_id
        ),
        None
    )

    if lesson is None:
        abort(404)

    connection = get_connection()

    try:
        row = connection.execute("""
            SELECT completed
            FROM course_progress
            WHERE course_name = ? AND lesson_id = ?
        """, ("Python Basics", lesson_id)).fetchone()

    finally:
        connection.close()

    is_completed = bool(row and row["completed"])

    return render_template(
        "python_lesson.html",
        lesson=lesson,
        is_completed=is_completed,
        total_lessons=len(PYTHON_LESSONS)
    )


# ==========================================
# COMPLETE PYTHON LESSON
# ==========================================

@app.route(
    "/courses/python/lesson/<int:lesson_id>/complete",
    methods=["POST"]
)
def complete_python_lesson(lesson_id):
    lesson_exists = any(
        item["id"] == lesson_id
        for item in PYTHON_LESSONS
    )

    if not lesson_exists:
        abort(404)

    connection = get_connection()

    try:
        connection.execute("""
            INSERT INTO course_progress
                (course_name, lesson_id, completed, completed_at)
            VALUES (?, ?, 1, ?)
            ON CONFLICT(course_name, lesson_id)
            DO UPDATE SET
                completed = 1,
                completed_at = excluded.completed_at
        """, (
            "Python Basics",
            lesson_id,
            date.today().isoformat()
        ))

        connection.commit()

    finally:
        connection.close()

    return redirect(url_for("python_course"))


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)