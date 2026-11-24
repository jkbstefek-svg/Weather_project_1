import json
import datetime

with open ("Weather_report.json", "r", encoding="utf-8") as file:
    data = json.load(file)

now = datetime.datetime.now()
offset_seconds = data["timezone"]

local_tz = datetime.timezone(datetime.timedelta(seconds=offset_seconds))

ts_r = int(data["sys"]["sunrise"])
utc_time_sunrise = datetime.datetime.fromtimestamp(ts_r, tz=local_tz)
ts_s = int(data["sys"]["sunset"])
utc_time_sunset = datetime.datetime.fromtimestamp(ts_s, tz=local_tz)


print(f"{now}")
print(f"City: {data["name"]}")
print(f"Temperature now: {data["main"]["temp"]} °C")
print(f"Temperature feels like: {data["main"]["feels_like"]} °C")
print(f"Weather now: {data["weather"][0]["description"]}, {data["clouds"]["all"]}%")
print(f"Wind-speed is: {data["wind"]["speed"]*3.6} km/h")
print(f"Sunrise time is: {utc_time_sunrise}")
print(f"Sunset time is: {utc_time_sunset}")