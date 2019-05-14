import requests
import json

r = requests.get("https://www.googleapis.com/analytics/v3/metadata/ga/columns?key=AIzaSyAhQcvVYyfVaLuQdDyLck-ohewCxqAg5uo")
data = r.json()
print(data)