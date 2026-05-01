from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# USER TABLE
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(20))  # Admin / Member


# PROJECT TABLE
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# TASK TABLE
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    status = db.Column(db.String(20), default="Pending")
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'))