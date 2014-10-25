from geopy.geocoders import Nominatim 

geolocator = Nominatim()
API_KEY = open('API_KEY').readline() # Place your Forecast.IO API Key here

userInput = input("Location? ")
location = geolocator.geocode(userInput)

print(location.latitude, location.longitude)
