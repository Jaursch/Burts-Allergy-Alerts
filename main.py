from dotenv import load_dotenv
import json
import os
import requests

load_dotenv()

API_KEY = os.getenv('GOOGLE_API_KEY')
LAT = 45.5254
LON = -122.6933

def fetch_pollen_forecast():
    url = f'https://pollen.googleapis.com/v1/forecast:lookup'
    params = {
        "key": API_KEY,
        "location.latitude": LAT,
        "location.longitude": LON,
        "days": 5
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)  # For now, just see what we get

if __name__ == "__main__":
    fetch_pollen_forecast()
