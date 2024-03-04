import requests
import json
import pyttsx3

city = input("Enter the city:\n")

url = f"https://api.weatherapi.com/v1/current.json?key=d37b0c9e5d784503a0b142701240403&q={city}"

r = requests.get(url)
# print(r.text)
w_dict = json.loads(r.text)
w = w_dict["current"]["temp_c"]

engine = pyttsx3.init()
engine.say(f"The current weather in {city} is {w} degrees")
engine.runAndWait()