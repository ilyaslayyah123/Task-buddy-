# 🤖 TaskBuddy – AI Assistant

TaskBuddy is a smart, real-time AI assistant built with Flask that helps users ask questions, set task reminders, use voice commands, and receive push notifications. It features a clean web UI with login, logout, and profile support.

![TaskBuddy Screenshot](static/preview.jpg)

---

## 🚀 Features

- ✅ Ask AI questions and get intelligent responses
- 🎤 Voice input using JavaScript Speech API
- 🕑 Add, view, and delete reminders
- 🔔 Real-time push notifications
- 🎨 Light/Dark mode toggle
- 👤 Login, Logout & Profile system
- 📅 Google Calendar integration (optional)
- 💬 Responsive and user-friendly interface

---

## 📁 Project Structure

taskbuddy/
├── app.py # Flask backend
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── profile.html
├── static/
│ ├── style.css
│ ├── project_pic.jpg
├── reminders.json # Reminder storage
├── users.json # User login data
├── requirements.txt
└── README.md

---

## 💻 Installation

### Clone the repo
    ```bash
     git clone https://github.com/ilyaslayyah123/Task-buddy-.git
    cd Task-buddy-

### Install dependencies
    ```bash
    pip install -r requirements.txt
### 🧪 Run the App Locally
     python app.py
    Visit: http://127.0.0.1:5000 in your browser.
### 🔔 Push Notifications
    To enable push notifications:
    Use pywebpush with VAPID keys.
    Generate keys
           ```bash
           from pywebpush import generate_vapid_private_key, generate_vapid_public_key
     Configure in app.py and service worker.
### 📦 Deployment (Render)
     Create a GitHub repository and push the project.
     Create a render.yaml:
     ```bash
        services:
      - type: web
        name: taskbuddy
        runtime: python
        buildCommand: "pip install -r requirements.txt"
        startCommand: "python app.py"
        envVars:
          - key: FLASK_ENV
            value: production
      Deploy at https://render.com
  ### 🙌 Author
    Muhammad Ilyas – AI Developer & Python Enthusiast
    📧 Connect on  www.linkedin.com/in/muhammad-ilyas-a59bb0289
    🧠 Built with Flask, JS, and 💙 for AI.
    

