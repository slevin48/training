from urllib.request import urlopen
import json

# def get_current_weather():
url = "https://samples.openweathermap.org/"
res = urlopen(url)
json_data = json.loads(res.read())
print(json_data["products"]["current_weather"]["samples"][0])