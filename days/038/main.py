import requests
from  datetime import datetime
APP_ID="####"
API_KEY="#########"

GENDER = "female"
WEIGHT_KG = "53"
HEIGHT_CM = "170"
AGE = "24"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheet_endpoint = "https://api.sheety.co/1982785b24799b84968b1e0d7c895711/myWorkouts/workouts"


exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

# No Authentication
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

# Basic Authentication
'''
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    auth=(
        YOUR USERNAME,
    YOUR PASSWORD,
    )
)
'''


# Bearer Token Authentication

'''
bearer_headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)
'''
