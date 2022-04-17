from django.shortcuts import render,redirect
from django.contrib import messages
import datetime,json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def index(request):
    return render(request,'calender/index.html')



def get_calender_event_list(request):
    if(request.session.get('credentials')):
        credentials = request.session.get('credentials')
        try:

            credentials = json.loads(credentials)
            creds = Credentials.from_authorized_user_info(credentials, SCOPES)

            service = build('calendar', 'v3', credentials=creds)

            now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            print('Getting the upcoming 10 events')
            events_result = service.events().list(calendarId='primary', timeMin=now,
                                                maxResults=10, singleEvents=True,
                                                orderBy='startTime').execute()
            # events_result = service.events().list(calendarId='primary').execute()
            events = events_result.get('items', [])

            if not events:
                messages.info(request,"No Events!")
                return redirect('index')

            data = []
            for event in events:
                temp = {}
                start = event['start'].get('dateTime', event['start'].get('date'))
                temp['start'] = start
                temp['summary'] = event['summary']
                data.append(temp)
            
            return render(request,'calender/events.html',{'data':data})

        except HttpError as error:
            print(error)
            messages.error(request,"Error Occured!, Try Again!")
            return redirect('index')

    else:
        messages.info(request,"User Not Authenticated!")
    return redirect('index')


