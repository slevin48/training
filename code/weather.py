from urllib.request import urlopen
import json

# def get_current_weather():
url = "https://samples.openweathermap.org/"
samples = urlopen(url).read()
jason = json.loads(samples)
sample_url = jason["products"]["current_weather"]["samples"][0]

res = urlopen(sample_url).read()
json_data = json.loads(res)
print(json_data)
