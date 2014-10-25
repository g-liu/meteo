import requests as b
from geopy.geocoders import Nominatim
import json

geolocator = Nominatim()
API_KEY = open('API_KEY').readline() # Place your Forecast.IO API Key here

userInput = input("Location? ")
print("\nGetting forecast for %s..." %(userInput))


loc = geolocator.geocode(userInput)
if loc is None:
	print("Error: could not find the location of \"%s\"" %(userInput))
	quit()

queryString = "https://api.forecast.io/forecast/%s/%s,%s" %(API_KEY, loc.latitude, loc.longitude)

rawData = b.get(queryString)
jsonData = rawData.json()
fc = jsonData['currently']
fd = jsonData['daily']['data'][0]
# fa = jsonData['alerts']

print()
print("Current conditions at (%f, %f):" %(loc.latitude, loc.longitude))
print("%d degrees and %s" %(fc['temperature'], fc['summary']))

if int(fc['temperature']) != int(fc['apparentTemperature']):
	print("Feels like %d degrees" %(fc['apparentTemperature']))

print("High %d, low %d" %(fd['temperatureMax'], fd['temperatureMin']))

if float(fc['precipIntensity']) > 0:
	print("%.2f in/hr of %s" %(fc['precipIntensity'], fc['precipType']))

if 'alerts' in jsonData and len(jsonData['alerts']):
	if(input("View %d alerts (Y/N)? " %(len(jsonData['alerts']))).lower() == "y"):
		print()
		for a in jsonData['alerts']:
			print(a['description'])