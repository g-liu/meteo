from geopy.geocoders import Nominatim 

geolocator = Nominatim()
userInput = input("Location? ")
location = geolocator.geocode(userInput)
print(location.latitude, location.longitude)
