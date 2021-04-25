import requests
from pprint import pprint

API_Key = "639d52b9e0f0f31d21357c3729b821bf"

city = input("Please enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/forecast?appid="+API_Key+"&q="+city
weather_data = requests.get(base_url).json()
pprint(weather_data)