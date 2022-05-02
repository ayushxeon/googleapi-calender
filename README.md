# Googleapi-calender
An implementation of Google Oauth and Fetching the list of Events in Calender (Without 3rd Party Libraries)

Endpoints: <br>
`/rest/v1/calender/init/` :Login Endpoint

`/rest/v1/calender/logout/` :Logout Endpoint

`/rest/v1/calender/callback/` :Callback Endpoint

`/rest/v1/calendar/redirect/` :List Calender Events

**Local Setup**
---
*Requirements:- Python 3.8+*<br>
1) `git clone https://github.com/ayushxeon/googleapi-calender`
(For Contrituber: Use your Forked URL)
2) `cd trackit2.0`
3) `python -m venv env`
4) `source env/bin/activate` (Mac/Linux)<br>
   `env\Scripts\activate` (Windows-Powershell)
5) `pip install -r requirements.txt`

Start Development Server<br>
---
Running Django Server
1) `source env/bin/activate` (Mac/Linux)<br>
   `env\Scripts\activate` (Windows-Powershell)
2) `python manage.py runserver`
