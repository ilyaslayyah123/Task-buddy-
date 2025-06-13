from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credentials.json'  

def add_event_to_calendar(task, time):
    
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    service = build('calendar', 'v3', credentials=creds)

   
    event_time = datetime.strptime(time, "%Y-%m-%dT%H:%M")
    
    event = {
        'summary': task,
        'start': {
            'dateTime': event_time.isoformat(),
            'timeZone': 'Asia/Karachi'  
        },
        'end': {
            'dateTime': (event_time + timedelta(hours=1)).isoformat(),
            'timeZone': 'Asia/Karachi'
        }
    }

    
    service.events().insert(calendarId='primary', body=event).execute()
