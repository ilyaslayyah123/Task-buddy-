import os
import json
from datetime import datetime

FILE_PATH = 'reminders.json'

def load_reminders():
    if not os.path.exists(FILE_PATH):
        return []  

    with open(FILE_PATH, 'r') as file:
        try:
            return json.load(file)  
        except json.JSONDecodeError:
            return []

def save_reminders(reminders):
    with open(FILE_PATH, 'w') as file:
        json.dump(reminders, file, indent=4)

def set_reminder(task, time):
    reminders = load_reminders()
    reminders.append({'task': task, 'time': time})
    save_reminders(reminders)

def get_reminders():
    return load_reminders()
