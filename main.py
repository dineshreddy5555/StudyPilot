import os
import secrets
from functools import wraps
from datetime import date, timedelta

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    abort
)

from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from database import (
    get_connection,
    create_tables,
    create_admin_tables
)

from course_data import COURSES


# ==========================================
# APP CONFIGURATION
# ==========================================

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get(
    "STUDYPILOT_SECRET_KEY",
    "change-this-to-a-long-random-secret-before-deployment"
)

# Initialize database tables
create_tables()
create_admin_tables()


# ==========================================
# LOGIN CONFIGURATION
# ==========================================

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"
login_manager.login_message = "Please log in to continue."


# ==========================================
# ADMIN CONFIGURATION
# ==========================================

ADMIN_EMAIL = os.environ.get(
    "STUDYPILOT_ADMIN_EMAIL",
    ""
).strip().lower()


# ==========================================
# USER MODEL
# ==========================================

class User(UserMixin):

    def __init__(self, user_id, username, email, is_admin=False):
        self.id = str(user_id)
        self.username = username
        self.email = email
        self.is_admin = bool(is_admin)

# ==========================================
# ADMIN ACCESS PROTECTION
# ==========================================

def admin_required(view_function):

    @wraps(view_function)
    @login_required
    def wrapped_view(*args, **kwargs):

        # Check whether the logged-in user is an admin
        if not current_user.is_admin:
            abort(403)

        # Allow access only to admin users
        return view_function(*args, **kwargs)

    return wrapped_view


# ==========================================
# LOAD LOGGED-IN USER
# ==========================================

@login_manager.user_loader
def load_user(user_id):

    connection = get_connection()

    try:
        row = connection.execute(
            """
            SELECT id, username, email, is_admin
            FROM users
            WHERE id = ?
            """,
            (user_id,)
        ).fetchone()

        if row:
            return User(
                row["id"],
                row["username"],
                row["email"],
                row["is_admin"]
            )

        return None

    finally:
        connection.close()

# ==========================================
# HELPER FUNCTIONS
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


def get_course(course_id):

    return next(
        (
            course for course in COURSES
            if course["id"] == course_id
        ),
        None
    )


def get_lesson(course, lesson_id):

    if not course:
        return None

    return next(
        (
            lesson for lesson in course["lessons"]
            if lesson["id"] == lesson_id
        ),
        None
    )


def get_course_progress(connection, course_id):

    rows = connection.execute(
        """
        SELECT lesson_id
        FROM course_progress
        WHERE user_id = ?
          AND course_name = ?
          AND completed = 1
        """,
        (int(current_user.id), course_id)
    ).fetchall()

    return {row["lesson_id"] for row in rows}


def get_course_certificate(connection, course_id):

    return connection.execute(
        """
        SELECT *
        FROM certificates
        WHERE user_id = ?
          AND course_id = ?
        """,
        (int(current_user.id), course_id)
    ).fetchone()


# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    return render_template("welcome.html")

# ==========================================
# REGISTER
# ==========================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    if request.method == "POST":

        username = request.form.get(
            "username", ""
        ).strip()

        email = request.form.get(
            "email", ""
        ).strip().lower()

        password = request.form.get(
            "password", ""
        )

        if not username or not email or not password:

            flash(
                "Please fill in all fields.",
                "error"
            )

            return render_template("register.html")

        if len(password) < 8:

            flash(
                "Password must contain at least 8 characters.",
                "error"
            )

            return render_template("register.html")

        connection = get_connection()

        try:

            connection.execute(
                """
                INSERT INTO users (
                    username,
                    email,
                    password_hash
                )
                VALUES (?, ?, ?)
                """,
                (
                    username,
                    email,
                    generate_password_hash(password)
                )
            )

            connection.commit()

        except Exception as error:

            if "UNIQUE constraint failed" in str(error):

                flash(
                    "That username or email is already registered.",
                    "error"
                )

            else:

                app.logger.exception(
                    "Registration failed"
                )

                flash(
                    "Registration failed. Please try again.",
                    "error"
                )

            return render_template("register.html")

        finally:
            connection.close()

        flash(
            "Registration successful! Please log in.",
            "success"
        )

        return redirect(url_for("login"))

    return render_template("register.html")


# ==========================================
# LOGIN
# ==========================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    if request.method == "POST":

        username_or_email = request.form.get(
            "username", ""
        ).strip()

        password = request.form.get(
            "password", ""
        )

        connection = get_connection()

        try:
            row = connection.execute(
                """
                SELECT id, username, email, password_hash, is_admin
                FROM users
                WHERE username = ? OR email = ?
                """,
                (
                    username_or_email,
                    username_or_email.lower()
                )
            ).fetchone()

        finally:
            connection.close()

        if row and check_password_hash(
            row["password_hash"], password
        ):

            login_user(
                User(
                    row["id"],
                    row["username"],
                    row["email"],
                    row["is_admin"]
                )
            )

            return redirect(url_for("dashboard"))

        flash(
            "Invalid username/email or password.",
            "error"
        )

    return render_template("login.html")

# ==========================================
# LOGOUT
# ==========================================

@app.route("/logout", methods=["POST"])
@login_required
def logout():

    logout_user()

    flash(
        "You have been logged out.",
        "success"
    )

    return redirect(url_for("login"))


# ==========================================
# DASHBOARD
# ==========================================

@app.route("/dashboard")
@login_required
def dashboard():

    connection = get_connection()

    try:

        total_subjects = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM subjects
            """
        ).fetchone()["count"]

        total_tasks = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM tasks
            """
        ).fetchone()["count"]

        completed_tasks = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM tasks
            WHERE completed = 1
            """
        ).fetchone()["count"]

        pending_tasks = total_tasks - completed_tasks

        completion_percentage = (
            int(completed_tasks / total_tasks * 100)
            if total_tasks else 0
        )

        date_rows = connection.execute(
            """
            SELECT DISTINCT completed_date
            FROM tasks
            WHERE completed = 1
              AND completed_date IS NOT NULL
            """
        ).fetchall()

        studied_dates = [
            row["completed_date"]
            for row in date_rows
        ]

        completed_lessons = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM course_progress
            WHERE user_id = ?
              AND completed = 1
            """,
            (int(current_user.id),)
        ).fetchone()["count"]

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
        streak=streak,
        completed_lessons=completed_lessons
    )
# ==========================================
# ADMIN DASHBOARD
# ==========================================

@app.route("/admin")
@admin_required
def admin_dashboard():

    connection = get_connection()

    try:
        total_students = connection.execute(
            "SELECT COUNT(*) AS count FROM users"
        ).fetchone()["count"]

        total_visits = connection.execute(
            "SELECT COUNT(*) AS count FROM website_visits"
        ).fetchone()["count"]

        total_assignments = connection.execute(
            "SELECT COUNT(*) AS count FROM assignments"
        ).fetchone()["count"]

    finally:
        connection.close()

    total_courses = len(COURSES)

    return render_template(
        "admin_dashboard.html",
        total_students=total_students,
        total_visits=total_visits,
        total_courses=total_courses,
        total_assignments=total_assignments
    )

# ==========================================
# SUBJECTS
# ==========================================

@app.route("/subjects", methods=["GET", "POST"])
@login_required
def subjects():

    connection = get_connection()

    try:

        if request.method == "POST":

            name = request.form.get(
                "name", ""
            ).strip()

            if name:

                connection.execute(
                    """
                    INSERT INTO subjects (name)
                    VALUES (?)
                    """,
                    (name,)
                )

                connection.commit()

            else:

                flash(
                    "Please enter a subject name.",
                    "error"
                )

            return redirect(url_for("subjects"))

        all_subjects = connection.execute(
            """
            SELECT *
            FROM subjects
            ORDER BY id DESC
            """
        ).fetchall()

    finally:
        connection.close()

    return render_template(
        "subjects.html",
        subjects=all_subjects
    )


@app.route(
    "/subjects/delete/<int:subject_id>",
    methods=["POST"]
)
@login_required
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
# TIMETABLE
# ==========================================

@app.route("/timetable", methods=["GET", "POST"])
@login_required
def timetable():

    connection = get_connection()

    try:

        if request.method == "POST":

            subject = request.form.get(
                "subject", ""
            ).strip()

            study_date = request.form.get(
                "study_date", ""
            ).strip()

            study_time = request.form.get(
                "study_time", ""
            ).strip()

            if subject and study_date and study_time:

                connection.execute(
                    """
                    INSERT INTO sessions (
                        subject,
                        study_date,
                        study_time
                    )
                    VALUES (?, ?, ?)
                    """,
                    (
                        subject,
                        study_date,
                        study_time
                    )
                )

                connection.commit()

            else:

                flash(
                    "Please complete all timetable fields.",
                    "error"
                )

            return redirect(url_for("timetable"))

        sessions = connection.execute(
            """
            SELECT *
            FROM sessions
            ORDER BY study_date, study_time
            """
        ).fetchall()

    finally:
        connection.close()

    return render_template(
        "timetable.html",
        sessions=sessions
    )


# ==========================================
# TASKS
# ==========================================

@app.route("/tasks", methods=["GET", "POST"])
@login_required
def tasks():

    connection = get_connection()

    try:

        if request.method == "POST":

            name = request.form.get(
                "name", ""
            ).strip()

            if name:

                connection.execute(
                    """
                    INSERT INTO tasks (name)
                    VALUES (?)
                    """,
                    (name,)
                )

                connection.commit()

            else:

                flash(
                    "Please enter a task name.",
                    "error"
                )

            return redirect(url_for("tasks"))

        all_tasks = connection.execute(
            """
            SELECT *
            FROM tasks
            ORDER BY completed ASC, id DESC
            """
        ).fetchall()

    finally:
        connection.close()

    return render_template(
        "tasks.html",
        tasks=all_tasks
    )


@app.route(
    "/complete/<int:task_id>",
    methods=["POST"]
)
@login_required
def complete_task(task_id):

    connection = get_connection()

    try:

        connection.execute(
            """
            UPDATE tasks
            SET completed = 1,
                completed_date = ?
            WHERE id = ?
            """,
            (
                date.today().isoformat(),
                task_id
            )
        )

        connection.commit()

    finally:
        connection.close()

    return redirect(url_for("tasks"))


@app.route(
    "/undo/<int:task_id>",
    methods=["POST"]
)
@login_required
def undo_task(task_id):

    connection = get_connection()

    try:

        connection.execute(
            """
            UPDATE tasks
            SET completed = 0,
                completed_date = NULL
            WHERE id = ?
            """,
            (task_id,)
        )

        connection.commit()

    finally:
        connection.close()

    return redirect(url_for("tasks"))


@app.route(
    "/delete/<int:task_id>",
    methods=["POST"]
)
@login_required
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
# PROGRESS
# ==========================================

@app.route("/progress", methods=["GET", "POST"])
@login_required
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
                        """
                        UPDATE daily_goals
                        SET target = ?
                        WHERE id = 1
                        """,
                        (target,)
                    )

                    connection.commit()

            except (ValueError, TypeError):
                flash(
                    "Enter a valid daily target.",
                    "error"
                )

            return redirect(url_for("progress"))

        total = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM tasks
            """
        ).fetchone()["count"]

        completed = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM tasks
            WHERE completed = 1
            """
        ).fetchone()["count"]

        today = date.today().isoformat()

        today_completed = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM tasks
            WHERE completed = 1
              AND completed_date = ?
            """,
            (today,)
        ).fetchone()["count"]

        goal_row = connection.execute(
            """
            SELECT target
            FROM daily_goals
            WHERE id = 1
            """
        ).fetchone()

        daily_target = goal_row["target"] if goal_row else 3

        daily_goal_percentage = (
            min(
                100,
                int(today_completed / daily_target * 100)
            )
            if daily_target else 0
        )

        remaining_today = max(
            0,
            daily_target - today_completed
        )

        daily_goal_message = (
            "🎉 Daily goal completed!"
            if remaining_today == 0
            else (
                f"Complete {remaining_today} more task(s) "
                "to reach today's goal!"
            )
        )

        date_rows = connection.execute(
            """
            SELECT DISTINCT completed_date
            FROM tasks
            WHERE completed = 1
              AND completed_date IS NOT NULL
            """
        ).fetchall()

        studied_dates = [
            row["completed_date"]
            for row in date_rows
        ]

        streak = calculate_study_streak(studied_dates)

        chart_labels = []
        chart_values = []

        for days_ago in range(6, -1, -1):

            day = date.today() - timedelta(days=days_ago)

            count = connection.execute(
                """
                SELECT COUNT(*) AS count
                FROM tasks
                WHERE completed = 1
                  AND completed_date = ?
                """,
                (day.isoformat(),)
            ).fetchone()["count"]

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
            1 for badge in badges
            if badge["unlocked"]
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
# REWARDS
# ==========================================

@app.route("/rewards")
@login_required
def rewards():

    connection = get_connection()

    try:

        completed = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM tasks
            WHERE completed = 1
            """
        ).fetchone()["count"]

        studied_dates = [
            row["completed_date"]
            for row in connection.execute(
                """
                SELECT DISTINCT completed_date
                FROM tasks
                WHERE completed = 1
                  AND completed_date IS NOT NULL
                """
            ).fetchall()
        ]

        today = date.today().isoformat()

        today_completed = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM tasks
            WHERE completed = 1
              AND completed_date = ?
            """,
            (today,)
        ).fetchone()["count"]

        goal_row = connection.execute(
            """
            SELECT target
            FROM daily_goals
            WHERE id = 1
            """
        ).fetchone()

        daily_target = goal_row["target"] if goal_row else 3

    finally:
        connection.close()

    xp = completed * 10
    level = (xp // 100) + 1
    xp_in_level = xp % 100
    xp_to_next_level = 100 - xp_in_level

    level_name = (
        "Beginner" if level < 3 else
        "Intermediate" if level < 6 else
        "Advanced" if level < 10 else
        "Study Master"
    )

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
# ALL COURSES
# ==========================================

@app.route("/courses")
@login_required
def courses():

    course_cards = []

    connection = get_connection()

    try:

        for course in COURSES:

            completed_ids = get_course_progress(
                connection,
                course["id"]
            )

            total_lessons = len(course["lessons"])

            completed_count = len(completed_ids)

            percentage = (
                int(completed_count / total_lessons * 100)
                if total_lessons else 0
            )

            course_cards.append({
                **course,
                "completed_count": completed_count,
                "total_lessons": total_lessons,
                "percentage": percentage
            })

    finally:
        connection.close()

    return render_template(
        "courses.html",
        courses=course_cards
    )


# ==========================================
# COURSE DETAILS
# ==========================================

@app.route("/courses/<course_id>")
@login_required
def course_detail(course_id):

    course = get_course(course_id)

    if course is None:
        abort(404)

    connection = get_connection()

    try:

        completed_ids = get_course_progress(
            connection,
            course_id
        )

        total_lessons = len(course["lessons"])
        completed_count = len(completed_ids)

        percentage = (
            int(completed_count / total_lessons * 100)
            if total_lessons else 0
        )

        certificate = get_course_certificate(
            connection,
            course_id
        )

    finally:
        connection.close()

    return render_template(
        "course_detail.html",
        course=course,
        completed_ids=completed_ids,
        completed_count=completed_count,
        total_lessons=total_lessons,
        percentage=percentage,
        certificate=certificate
    )


# ==========================================
# COURSE LESSON
# ==========================================

@app.route("/courses/<course_id>/lesson/<int:lesson_id>")
@login_required
def course_lesson(course_id, lesson_id):

    course = get_course(course_id)

    if course is None:
        abort(404)

    lesson = get_lesson(course, lesson_id)

    if lesson is None:
        abort(404)

    connection = get_connection()

    try:

        completed_ids = get_course_progress(
            connection,
            course_id
        )

    finally:
        connection.close()

    return render_template(
        "course_lesson.html",
        course=course,
        lesson=lesson,
        is_completed=lesson_id in completed_ids
    )

@app.route(
    "/courses/<course_id>/lesson/<int:lesson_id>/complete",
    methods=["POST"]
)
@login_required
def complete_lesson(course_id, lesson_id):
    course = get_course(course_id)
    lesson = get_lesson(course, lesson_id)

    if not course or not lesson:
        abort(404)

    connection = get_connection()

    try:
        connection.execute(
            """
            INSERT OR IGNORE INTO course_progress
                (user_id, course_name, lesson_id, completed)
            VALUES (?, ?, ?, 1)
            """,
            (int(current_user.id), course_id, lesson_id)
        )

        connection.commit()
    finally:
        connection.close()

    flash("Lesson completed successfully!", "success")

    return redirect(
        url_for("course_detail", course_id=course_id)
    )

# ==========================================
# MARK LESSON COMPLETE
# ==========================================

@app.route(
    "/courses/<course_id>/lesson/<int:lesson_id>/complete",
    methods=["POST"]
)
@login_required
def complete_course_lesson(course_id, lesson_id):

    course = get_course(course_id)

    if course is None:
        abort(404)

    lesson = get_lesson(course, lesson_id)

    if lesson is None:
        abort(404)

    connection = get_connection()

    try:

        connection.execute(
            """
            INSERT INTO course_progress (
                user_id,
                course_name,
                lesson_id,
                completed,
                completed_at
            )
            VALUES (?, ?, ?, 1, ?)
            ON CONFLICT(user_id, course_name, lesson_id)
            DO UPDATE SET
                completed = 1,
                completed_at = excluded.completed_at
            """,
            (
                int(current_user.id),
                course_id,
                lesson_id,
                date.today().isoformat()
            )
        )

        connection.commit()

    finally:
        connection.close()

    flash(
        "Lesson marked as completed!",
        "success"
    )

    return redirect(
        url_for(
            "course_lesson",
            course_id=course_id,
            lesson_id=lesson_id
        )
    )


# ==========================================
# QUIZ
# ==========================================

@app.route(
    "/courses/<course_id>/lesson/<int:lesson_id>/quiz",
    methods=["POST"]
)
@login_required
def course_quiz(course_id, lesson_id):

    course = get_course(course_id)

    if course is None:
        abort(404)

    lesson = get_lesson(course, lesson_id)

    if lesson is None:
        abort(404)

    questions = lesson.get("quiz", [])
    score = 0

    for index, question in enumerate(questions):

        submitted_answer = request.form.get(
            f"answer_{index}", ""
        )

        try:
            answer = int(submitted_answer)
        except (ValueError, TypeError):
            continue

        if answer == question["answer"]:
            score += 1

    total_questions = len(questions)

    percentage = (
        int(score / total_questions * 100)
        if total_questions else 0
    )

    connection = get_connection()

    try:

        connection.execute(
            """
            INSERT INTO quiz_scores (
                user_id,
                course_id,
                lesson_id,
                score,
                total_questions,
                percentage
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                int(current_user.id),
                course_id,
                lesson_id,
                score,
                total_questions,
                percentage
            )
        )

        connection.commit()

    finally:
        connection.close()

    return render_template(
        "quiz_result.html",
        course=course,
        lesson=lesson,
        score=score,
        total_questions=total_questions,
        percentage=percentage,
        saved=True
    )


# ==========================================
# QUIZ HISTORY
# ==========================================

@app.route("/quiz-history")
@login_required
def quiz_history():

    connection = get_connection()

    try:

        scores = connection.execute(
            """
            SELECT *
            FROM quiz_scores
            WHERE user_id = ?
            ORDER BY completed_at DESC, id DESC
            """,
            (int(current_user.id),)
        ).fetchall()

    finally:
        connection.close()

    return render_template(
        "quiz_history.html",
        scores=scores
    )


# ==========================================
# CERTIFICATES
# ==========================================

@app.route("/courses/<course_id>/certificate")
@login_required
def course_certificate(course_id):

    course = get_course(course_id)

    if course is None:
        abort(404)

    connection = get_connection()

    try:

        completed_ids = get_course_progress(
            connection,
            course_id
        )

        total_lessons = len(course["lessons"])

        if (
            total_lessons == 0
            or len(completed_ids) < total_lessons
        ):

            flash(
                "Complete all course lessons before requesting a certificate.",
                "error"
            )

            return redirect(
                url_for(
                    "course_detail",
                    course_id=course_id
                )
            )

        certificate = get_course_certificate(
            connection,
            course_id
        )

        if certificate is None:

            certificate_code = secrets.token_hex(4).upper()

            connection.execute(
                """
                INSERT OR IGNORE INTO certificates (
                    user_id,
                    course_id,
                    course_name,
                    certificate_code
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    int(current_user.id),
                    course_id,
                    course["name"],
                    certificate_code
                )
            )

            connection.commit()

            certificate = get_course_certificate(
                connection,
                course_id
            )

    finally:
        connection.close()

    return render_template(
        "certificate.html",
        certificate=certificate,
        course=course,
        username=current_user.username
    )


# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)