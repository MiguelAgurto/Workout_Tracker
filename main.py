import requests
from datetime import datetime

APP_ID = "bc29cce1"
API_KEY = "7fbd81397123af796a1182e3daf01f08"

sheet_endpoint = "https://api.sheety.co/a6eef33048599120dd11f78146cfd764/myWorkouts/workouts"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 95,
    "height_cm": 170,
    "age": 30
}


response = requests.post(exercise_endpoint, json=parameters, headers=headers)
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
