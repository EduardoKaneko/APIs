# Libs de Oauth
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

# Libs de extracao do nome das colunas
import requests
import json

# Definindo variaveis
gaURL = "https://www.googleapis.com/analytics/v3/metadata/ga/columns?key=AIzaSyAhQcvVYyfVaLuQdDyLck-ohewCxqAg5uo"

# Autorização de acesso a api

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'client_secrets.json'
VIEW_ID = '109580013'
engine = create_engine('postgresql://postgres:eck@localhost:5432/ga')

def initialize_analyticsreporting():
  """Initializes an Analytics Reporting API V4 service object.

  Returns:
    An authorized Analytics Reporting API V4 service object.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)

  # Build the service object.
  analytics = build('analyticsreporting', 'v4', credentials=credentials)

  return analytics





# Extrair o nome de todas as colunas
def getMetricName():
    r = requests.get(gaURL)
    json_data = r.json()