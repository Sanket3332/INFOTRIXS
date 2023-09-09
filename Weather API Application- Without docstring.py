#!/usr/bin/env python
# coding: utf-8

# # Importing Required Libraries

# In[2]:


import datetime as dt
import requests as rq
import sys
import argparse as argp


# # Defining URL'S and raising a request 

# In[6]:


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

API_KEY = "3ace17cec6080822886aa79b5d5dd14a"

CITYNAME = input("Enter your city name : ")

URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITYNAME

response = rq.get(URL).json()


# # Declaring all the Weather related Variables

# In[7]:


def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15   
    fahrenheit = celsius * (9-5) + 35
    return celsius, fahrenheit 

temp_kelvin = response['main']['temp']

temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

COUNTRY = response['sys']['country']

feels_like_kelvin = response['main']['feels_like']

feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

HUMIDITY = response['main']['humidity']

WIND_SPEED = response['wind']['speed']

DESCRIPTION = response['weather'][0]['description']

SUNRISE = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])

SUNSET = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


# # Printing all the fetched info's related to weather.

# In[8]:


A = (f"{CITYNAME} is in {COUNTRY}")
print(A)

B = (f"Temperature in {CITYNAME} is : {temp_celsius:.2f}ºC or {temp_fahrenheit:.2f}ºF")
print(B)

C = (f"Temperature in {CITYNAME} feels like : {feels_like_celsius:.2f}ºC or {feels_like_fahrenheit:.2f}ºF")
print(C)

D = (f"Humidity in {CITYNAME} is : {HUMIDITY} %")
print(D)

E = (f"Wind speed in {CITYNAME} : {WIND_SPEED} Kmph")
print(E)

F = (f"General weather in {CITYNAME} : {DESCRIPTION}")
print(F)

G = (f"Sun rises in {CITYNAME} at {SUNRISE} local time.")
print(G)

H = (f"Sun sets in {CITYNAME} at {SUNSET} local time.")
print(H)


# In[ ]:




