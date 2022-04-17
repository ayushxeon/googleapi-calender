from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
import requests,json

import google.oauth2.credentials
from googleapiclient.discovery import build
import google_auth_oauthlib.flow
from google.oauth2.credentials import Credentials

CLIENT_SECRETS_FILE = "client_secrets_file.json"
SCOPES = ['https://www.googleapis.com/auth/calendar.events.readonly']



REDIRECT_URL = "http://localhost:8000/rest/v1/calender/callback/"


def login_view(request):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
    )

    flow.redirect_uri = REDIRECT_URL

    authorization_url, state = flow.authorization_url(
        access_type="offline", include_granted_scopes="true"
    )
    request.session['state'] = state

    return redirect(authorization_url)



def redirected_callback(request):
    state = request.session.get('state',None)

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
      CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)

    flow.redirect_uri = REDIRECT_URL

    authorization_response = request.build_absolute_uri() 
    # authorization_response = request.get_full_path() 
    print(authorization_response)

    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials

    request.session['credentials'] = credentials.to_json()

    messages.success(request, 'Successful Login!')
    return redirect('index')


def revoke(request):
    if(request.session.get('credentials')):

        token = json.loads(request.session.get('credentials'))['token']

        requests.post('https://oauth2.googleapis.com/revoke',
        params={'token': token},
        headers = {'content-type': 'application/x-www-form-urlencoded'})

        del request.session['credentials']
        messages.success(request, 'Logged Out!!')
    else:
        messages.warning(request, 'Already Logged Out!!')
    return redirect('index')





