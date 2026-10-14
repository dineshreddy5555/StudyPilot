from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage
subjects = []
sessions = []
tasks = []

next_task_id = 1


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/subjects", methods=["GET", "POST"])
def manage_subjects():
    if request.method == "POST":
        subject = request.form.get("subject", "").strip()

        if subject and len(subject) <= 100:
            subjects.append(subject)

        return redirect(url_for("manage_subjects"))

    return render_template("subjects.html", subjects=subjects)


@app.route("/timetable", methods=["GET", "POST"])
def timetable():
    if request.method == "POST":
        subject = request.form.get("subject", "").strip()
        study_date = request.form.get("study_date", "")
        study_time = request.form.get("study_time", "")

        if subject and len(subject) <= 100 and study_date and study_time:
            sessions.append({
                "subject": subject,
                "date": study_date,
                "time": study_time
            })

        return redirect(url_for("timetable"))

    return render_template("timetable.html", sessions=sessions)


@app.route("/tasks", methods=["GET", "POST"])
def manage_tasks():
    global next_task_id

    if request.method == "POST":
        task_name = request.form.get("task", "").strip()

        if task_name and len(task_name) <= 150:
            tasks.append({
                "id": next_task_id,
                "name": task_name,
                "completed": False
            })
            next_task_id += 1

        return redirect(url_for("manage_tasks"))

    return render_template("tasks.html", tasks=tasks)


@app.route("/tasks/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            break

    return redirect(url_for("manage_tasks"))


@app.route("/tasks/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    tasks[:] = [
        task for task in tasks
        if task["id"] != task_id
    ]

    return redirect(url_for("manage_tasks"))


@app.route("/progress")
def progress():
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed

    percentage = round((completed / total) * 100) if total else 0

    if total == 0:
        message = "Add some study tasks to start tracking your progress!"
    elif percentage == 100:
        message = "Excellent! You completed all your tasks!"
    elif percentage >= 50:
        message = "Great progress! Keep going!"
    else:
        message = "Keep studying. Every completed task counts!"

    return render_template(
        "progress.html",
        total=total,
        completed=completed,
        pending=pending,
        percentage=percentage,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)