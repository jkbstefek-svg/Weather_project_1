import os
import requests
from dotenv import load_dotenv, dotenv_values

load_dotenv()

print(dotenv_values("WEATHER_API_KEY.env")) 