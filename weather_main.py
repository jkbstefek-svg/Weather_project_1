import os
import requests
from dotenv import load_dotenv, dotenv_values
import json

load_dotenv()
WEATHER_API_KEY = dotenv_values("WEATHER_API_KEY.env")
res = WEATHER_API_KEY.popitem(last=True)
key = res[1]

url = f"https://api.openweathermap.org/data/2.5/weather?q=Brno,cz&units=metric&APPID={key}"

def download(url):
    try:
        response = requests.get(url)
        data = response.json()
        with open('Weather_report.json', 'w') as f:
            json.dump(data, f)
    except:
        pass

download(url)