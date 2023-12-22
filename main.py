import requests

owm_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key="3f6c191ebc22ffb1b1d15dabeafff115"

weather_params={
    "lat": 41.008240,
    "lon": 28.978359,
    "appid": api_key
}
response=requests.get(owm_endpoint, params=weather_params)
print(response.status_code)





