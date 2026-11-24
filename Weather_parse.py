import json

with open ("Weather_report.json", "r", encoding="utf-8") as file:
    data = json.load(file)

#print(data["weather"])

weather_l = {}

for i in data["weather"]:
    print(i)

#print(weather_l)