import httplib2
import json

def getGeocodeLocation(inputString):
        gmaps_key = 'AIzaSyAhQcvVYyfVaLuQdDyLck-ohewCxqAg5uo'
        locationString = inputString.replace(" ", "+")
        url = ('https://maps.googleapis.com/maps/api/geocode/json?adress=%s&key=%s'% (
                locationString, gmaps_key))
        h = httplib2.Http()
        reponse, content = h.request(url, 'GET')
        result = json.loads(content)
        print("response header: %s \n \n" % response)
        return result
    
    
    
    
import httplib2
import json

def getGeocodeLocation(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    google_api_key = "AIzaSyAhQcvVYyfVaLuQdDyLck-ohewCxqAg5uo"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)
        