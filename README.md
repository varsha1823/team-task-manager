Team Task Manager (Flask Project)

This is my Team Task Management System built using Flask, SQLite, HTML, CSS, and Python.
It helps in managing projects, assigning tasks, and tracking progress of team members.

Features
User Signup and Login system
Role based access (Admin / Member)
Admin can create projects
Admin can create tasks and assign to users
Members can view assigned tasks
Task status tracking (Pending / In Progress / Completed)
Dashboard with project and task overview
Logout functionality
🛠️ Technologies Used
Python (Flask Framework)
SQLite (Database)
HTML
CSS
Bootstrap (basic styling)
Jinja2 Templates

 Project Structure
team-task-manager/
│
├── app.py
├── models.py
├── database.db
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── tasks.html
│   ├── create_project.html
│   ├── create_task.html
│
├── static/
│   ├── style.css
│
└── README.md

 How to Run This Project
Clone this repository
git clone <your-repo-link>
Go to project folder
cd team-task-manager
Install requirements
pip install -r requirements.txt
Run the project
python app.py
Open in browser
http://127.0.0.1:5000/

 User Roles
Admin
Can create projects
Can create tasks
Can assign tasks to members
Can track all progress
Member
Can view assigned tasks
Can update task status
Can track their work
📊 Project Purpose

This project is made to understand:

Flask backend development
Database handling using SQLAlchemy
Role based authentication
Real-time task tracking system
💡 Future Improvements
Drag & drop task board (like Trello)
Real-time notifications
File upload for tasks
Chat system between team members
Better UI with animations
👨‍💻 Developed By

Varsha
B.Tech CSE Student
Skills: Python, Java, HTML, CSS, Flask
