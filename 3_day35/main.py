import requests
from twilio.rest import Client
import os

URL="http://api.openweathermap.org/data/2.5/forecast"
API_KEY="3f6c191ebc22ffb1b1d15dabeafff115"

TWILIO_KEY="H2UR23FYP4451X191VH8CT7J"

LAT=41.008240
LON=28.978359

params_weather={
    "lat":LAT,
    "lon":LON,
    "appid":API_KEY,
    "cnt":4
}

response=requests.get(URL,params=params_weather)

# print(response.status_code)
weather_data=response.json()
# print(weather_data["list"][0]["weather"][0]["id"])


account_sid = 'AC40a447f94ce52da3e5cb5bbea3842f52'  # it should be your accound_sid, it is not gonna work
auth_token = '12417009cf872bef0cc630cb43580dfd' # it should be your auth_token

will_rain=False
for hour_data in weather_data["list"]:
    condition= hour_data["weather"][0]["id"]

    if int(condition)<900:
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='+19283797635',
        to='####your phone number###'
    )

    print(message.status)

