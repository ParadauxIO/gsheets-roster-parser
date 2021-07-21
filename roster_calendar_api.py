from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


def createCredentials():
    """Authenticates via Google OAuth2"""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar.events'])

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', ['https://www.googleapis.com/auth/calendar.events'])
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds


def createService():
    """Creates a service for the Calender v3 API using the provided credentials."""
    return build('calendar', 'v3', credentials=createCredentials())


def timeParser(date, period):
    hours_minutes = period.split(":")

    return date.replace(hour=int(hours_minutes[0]), minute=int(hours_minutes[1]))


def createEvent(date, time_period, title):
    times = str.split(time_period, "-")
    start = timeParser(date, times[0])
    end = timeParser(date, times[1])
    event = {
        'summary': title,
        'location': 'Virtual Venue',
        'description': 'Go teach kids or something, idk, your job.',
        'start': {
            'dateTime': start.isoformat(),
            'timeZone': 'Europe/Dublin',
        },
        'end': {
            'dateTime': end.isoformat(),
            'timeZone': 'Europe/Dublin',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    createService().events().insert(calendarId='primary', body=event).execute()
    print(f"Creating Event: {date.strftime('%d-%m-%Y')} {title} from {times[0]}-{times[1]}")
