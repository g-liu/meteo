import requests as b
from geopy.geocoders import Nominatim
import json

geolocator = Nominatim()
API_KEY = open('API_KEY').readline() # Place your Forecast.IO API Key here

userInput = input("Location? ")
loc = geolocator.geocode(userInput)

queryString = "https://api.forecast.io/forecast/%s/%s,%s" %(API_KEY, loc.latitude, loc.longitude)

rawData = b.get(queryString)
jsonData = rawData.json()
fc = jsonData['currently']
fd = jsonData['daily']['data'][0]

print()
print("Current conditions at (%f, %f):" %(loc.latitude, loc.longitude))
print("%d degrees and %s" %(fc['temperature'], fc['summary']))
print("Feels like %d degrees" %(fc['apparentTemperature']))
print("High %d, low %d" %(fd['temperatureMax'], fd['temperatureMin']))
