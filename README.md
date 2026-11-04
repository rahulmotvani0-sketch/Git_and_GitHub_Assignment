# DevOps Assignment 4: Git & GitHub Workflow with Flask & MongoDB

This repository demonstrates the comprehensive Git and GitHub workflow including SSH setup, feature branching, merge conflict resolution, sequential commits, git reset (soft), and rebasing on a Flask web application with MongoDB integration.

## Student Information
- **Name:** Rahul Motvani
- **GitHub Username:** `rahulmotvani0-sketch`
- **Repository:** [https://github.com/rahulmotvani0-sketch/Git_and_GitHub_Assignment](https://github.com/rahulmotvani0-sketch/Git_and_GitHub_Assignment)

## Architecture & Features
- **Backend:** Python Flask 3.x
- **Database:** MongoDB 7.x (Collection: `todos` in database `todo_db`)
- **Frontend:** Responsive UI with Bootstrap 5.3, Font Awesome, and dynamic AJAX submission
- **Endpoints:**
  - `GET /`: Dashboard & project overview
  - `GET /api`: Serves JSON data from `data/items.json`
  - `GET /todo`: To-Do creation interface
  - `POST /submittodoitem`: Submits item to MongoDB
  - `GET /api/todos`: Retrieves all submitted items from MongoDB

## Setup Instructions

### 1. Prerequisites
- Python 3.10+
- MongoDB running locally on port 27017 (or Docker: `docker run -d -p 27017:27017 mongo:latest`)

### 2. Installation
```bash
pip install -r requirements.txt
```

### 3. Running Application
```bash
python3 app.py
```
Open [http://localhost:5000](http://localhost:5000) in your browser.
