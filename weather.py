try:
    import urllib.request as b
except:
    import urllib2 as b
from geopy.geocoders import Nominatim
import json

geolocator = Nominatim()
API_KEY = open('API_KEY').readline() # Place your Forecast.IO API Key here

userInput = input("Location? ")
loc = geolocator.geocode(userInput)

queryString = "https://api.forecast.io/forecast/%s/%s,%s" %(API_KEY, loc.latitude, loc.longitude)
print(queryString)

rawData = b.urlopen(queryString)
print(rawData.readline())