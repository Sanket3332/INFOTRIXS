import datetime as dt
import requests
import sys

base_url = "http://api.openweathermap.org/data/2.5/weather?"

api_key = "3ace17cec6080822886aa79b5d5dd14a"

cityname = input("Enter your city name : ")

url = base_url + "appid=" + api_key + "&q=" + cityname

response = requests.get(url).json()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15   
    fahrenheit = celsius * (9-5) + 35
    return celsius, fahrenheit

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

country = response['sys']['country']

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

humidity = response['main']['humidity']
wind_speed = response['wind']['speed']
description = response['weather'][0]['description']

sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"{cityname} is in {country}")

print(f"Temperature in {cityname} is : {temp_celsius:.2f}ºC or {temp_fahrenheit:.2f}ºF")

print(f"Temperature in {cityname} feels like : {feels_like_celsius:.2f}ºC or {feels_like_fahrenheit:.2f}ºF")

print(f"Humidity in {cityname} is : {humidity} %")

print(f"Wind speed in {cityname} : {wind_speed} Kmph")

print(f"General weather in {cityname} : {description}")

print(f"Sun rises in {cityname} at {sunrise_time} local time.")

print(f"Sun sets in {cityname} at {sunset_time} local time.")