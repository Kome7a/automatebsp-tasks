#! python3
# fastWeather.py - Prints the weather for a location from the command line.

import sys
import json
import requests
from datetime import datetime
import os


def humanify(dt):
    return datetime.fromtimestamp(dt).strftime("Time: %H:%M   Date: %d/%m/%Y")


def get_url(api_key, lat, lon):
    return f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric"


# Download the JSON data from OpenWeatherMap.org
def get_weather(api_key, lat, lon):
    url = get_url(api_key, lat, lon)
    res = requests.get(url)
    res.raise_for_status()
    return res.json()


def save_weather(data):
    file = open("weather.json", "w")
    json.dump(data, file)
    file.close()


def load_weather(name):
    path = os.path.abspath(name)
    if not os.path.exists(path):
        return None
    else:
        with open(path, "r") as f:
            return json.load(f)


def get_weather_cached(api_key, lat, lon):
    cached = load_weather("weather.json")
    if cached is None:
        result = get_weather(api_key, lat, lon)
        save_weather(result)
        return result
    else:
        return cached


lat, lon = (42.6975, 23.3242)
if len(sys.argv) < 2:
    print("Usage: quickWeather.py api-key")
    sys.exit()
api_key = sys.argv[1]

if __name__ == '__main__':
    file = get_weather_cached(api_key, lat, lon)
    morning = file["daily"][0]["temp"]["morn"]
    day = file["daily"][0]["temp"]["day"]
    night = file["daily"][0]["temp"]["night"]
    min = file["daily"][0]["temp"]["min"]
    max = file["daily"][0]["temp"]["max"]
    dt = file["daily"][0]["dt"]
    print(humanify(dt))
    print(" - " * 3)
    print("Morning temperature: " + str(morning) + " C")
    print("Day temperature: " + str(day) + " C")
    print("Night temperature: " + str(night) + " C")
    print(" - " * 3)
    print("Minimum temp for the day: " + str(min) + " C")
    print("Maximum temp for the day: " + str(max) + " C")
