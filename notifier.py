import datetime

def send_notification(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[NOTIFICATION - {timestamp}] {message}")


