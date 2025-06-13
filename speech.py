import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand the audio."
    except sr.RequestError:
        return "Could not request results from Google Speech API."
