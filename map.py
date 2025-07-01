import folium
from geopy.geocoders import Nominatim
from IPython.display import display, HTML

# Get location input from user
location_name = input("Enter a location: ")

# Initialize geolocator
geolocator = Nominatim(user_agent="geoapi")
location = geolocator.geocode(location_name)

if location:
    # Get latitude and longitude
    latitude = location.latitude
    longitude = location.longitude

    # Create map centered on the location
    map_obj = folium.Map(location=[latitude, longitude])