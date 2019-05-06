import googlemaps
from datetime import datetime
import json

gmaps = googlemaps.Client(key='AIzaSyAhQcvVYyfVaLuQdDyLck-ohewCxqAg5uo')

location_list = ['Tokyo, Japan', 'Jakarta, Indonesia', 'Maputo, Mozambique', 'Geneva, Switzerland', 'Los Angeles, USA']

geoloc = {}
for location in location_list:
    geocode_result = gmaps.geocode(location)
    s1 = json.dumps(geocode_result)
    geocode_result = json.loads(s1)
    long_name = geocode_result[0]['address_components'][0]['long_name']
    lat = geocode_result[0]['geometry']['bounds']['northeast']['lat']
    lng = geocode_result[0]['geometry']['bounds']['northeast']['lng']
    print(long_name, lat, lng)
#    print("Capital: {1}\n Lat: {}\n Lng: {}".format(long_name, lat, lng))
