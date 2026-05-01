from flask import Flask, render_template, request, redirect, session, url_for
from models import db, User, Project, Task

app = Flask(__name__)
app.secret_key = "secret123"

# DB config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# ---------------- ROOT ----------------
@app.route("/")
def root():
    if 'user_id' in session:
        return redirect("/dashboard")
    return redirect("/signup")


# ---------------- SIGNUP ----------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user = User(
            name=request.form['name'],
            email=request.form['email'],
            password=request.form['password'],
            role=request.form['role']
        )
        db.session.add(user)
        db.session.commit()
        return redirect("/login")

    return render_template("signup.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(
            email=request.form['email'],
            password=request.form['password']
        ).first()

        if user:
            session['user_id'] = user.id
            session['name'] = user.name
            session['role'] = user.role
            return redirect("/dashboard")

    return render_template("login.html")


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/signup")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect("/login")

    projects = Project.query.all()
    tasks = Task.query.all()

    return render_template(
        "dashboard.html",
        name=session['name'],
        role=session['role'],
        projects=projects,
        tasks=tasks,
        total_projects=Project.query.count(),
        total_tasks=Task.query.count(),
        pending_tasks=Task.query.filter_by(status="Pending").count(),
        completed_tasks=Task.query.filter_by(status="Completed").count()
    )


# ---------------- CREATE PROJECT ----------------
@app.route("/create_project", methods=["GET", "POST"])
def create_project():
    if 'user_id' not in session or session.get('role') != "Admin":
        return redirect("/dashboard")

    if request.method == "POST":
        project = Project(
            name=request.form['name'],
            description=request.form['description'],
            user_id=session['user_id']
        )
        db.session.add(project)
        db.session.commit()
        return redirect("/dashboard")

    return render_template("create_project.html")


# ---------------- CREATE TASK ----------------
@app.route("/create_task", methods=["GET", "POST"])
def create_task():
    if 'user_id' not in session or session.get('role') != "Admin":
        return redirect("/dashboard")

    projects = Project.query.all()
    users = User.query.all()

    if request.method == "POST":
        task = Task(
            title=request.form['title'],
            description=request.form['description'],
            status="Pending",
            project_id=request.form['project_id'],
            assigned_to=request.form['assigned_to']
        )
        db.session.add(task)
        db.session.commit()
        return redirect("/dashboard")

    return render_template("create_task.html", projects=projects, users=users)


# ---------------- TOGGLE TASK ----------------
@app.route("/toggle_task/<int:id>")
def toggle_task(id):
    if 'user_id' not in session:
        return redirect("/login")

    task = Task.query.get(id)

    if task.status == "Pending":
        task.status = "In Progress"
    elif task.status == "In Progress":
        task.status = "Completed"
    else:
        task.status = "Pending"

    db.session.commit()
    return redirect("/dashboard")


# ---------------- TASK LIST PAGE ----------------
@app.route("/tasks")
def tasks_page():
    if 'user_id' not in session:
        return redirect("/login")

    tasks = Task.query.all()
    return render_template("tasks.html", tasks=tasks)


if __name__ == "__main__":
    app.run()