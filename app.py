from flask import Flask, render_template, request, jsonify ,redirect
from ai_response import get_ai_response ,get_latest_tech_news
from tasks import set_reminder, get_reminders
from weather import get_weather
from notifier import send_notification
from calendar_api import add_event_to_calendar
from news_api import get_news_headlines
from textbelt_alerts import send_textbelt_sms
import speech_recognition as sr
from calendar_api import add_event_to_calendar
from auth import login_user, logout_user, is_authenticated
from auth import register_user
import webbrowser
import json 

app = Flask(__name__)

app.secret_key = 'ilyas@taskbuddy2025!#supersecret'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if register_user(username, password):
            return redirect('/')
        else:
            return render_template('register.html', error='Username already exists!')
    return render_template('register.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login_user(username, password):
            return redirect('/home')
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/home')
def home():
    if not is_authenticated():
        return redirect('/')
    return render_template('index.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/query', methods=['POST'])
def query():
    user_query = request.form['query']
    if "weather" in user_query.lower():
        response = get_weather(user_query)
    elif "news" in user_query.lower():
        response = get_news_headlines()
    elif "open youtube" in user_query.lower():
        webbrowser.open("https://youtube.com")
        response = "Opening YouTube..."

    elif "open google" in user_query.lower():
        response = webbrowser.open("google.com")
    elif "open github" in user_query.lower():
        response = webbrowser.open("github.com")
    elif "open linkedin" in user_query.lower():
        response = webbrowser.open("linkedin.com")
    else:
        response = get_ai_response(user_query)
    return jsonify({'response': response})

@app.route('/set_reminder', methods=['POST'])
def set_task():
    task = request.form['task']
    time = request.form['time']
    set_reminder(task, time)
    add_event_to_calendar(task, time)
    send_notification(f"Reminder set: {task} at {time}")
    send_textbelt_sms(f"Reminder: {task} at {time}")
    return jsonify({'message': f'Reminder set for {task} at {time}'})

@app.route('/reminders', methods=['GET'])
def show_reminders():
    reminders = get_reminders()
    return jsonify({'reminders': reminders})

@app.route('/speech', methods=['POST'])
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio)
            response = get_ai_response(query)
            return jsonify({'response': response})
        except sr.UnknownValueError:
            return jsonify({'response': " Sorry, I couldn't understand what you said. Please try again."})
        except sr.RequestError as e:
            return jsonify({'response': f"Could not request results; {e}"})
        except Exception as e:
            return jsonify({'response': f"An error occurred: {str(e)}"})


@app.route('/delete_reminder', methods=['POST'])
def delete_reminder():
    index = int(request.form['index'])
    
    with open('reminders.json', 'r') as f:
        reminders = json.load(f)  

    if 0 <= index < len(reminders):
        removed = reminders.pop(index) 
        with open('reminders.json', 'w') as f:
            json.dump(reminders, f, indent=2)  
        return jsonify({'message': f"Deleted: {removed['task']}"})
    else:
        return jsonify({'message': "Invalid index"})




if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
