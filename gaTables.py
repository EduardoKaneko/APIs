from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from pandas.io.json import json_normalize
from sqlalchemy import create_engine


# Auth and connect with ga api

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

def get_report(analytics):
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
            {
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': '2015-05-01', 'endDate': 'yesterday'}],
            'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:newUsers'}, {'expression': 'ga:users'}],
            'dimensions': [{'name': 'ga:source'}, {'name': 'ga:sourceMedium'}]
            }]
            }
        ).execute()


def parse_data(response):
    
  reports = response['reports'][0]
  columnHeader = reports['columnHeader']['dimensions']
  metricHeader = reports['columnHeader']['metricHeader']['metricHeaderEntries']

  columns = columnHeader
  for metric in metricHeader:
    columns.append(metric['name'])

  data = json_normalize(reports['data']['rows'])
  data_dimensions = pd.DataFrame(data['dimensions'].tolist())
  data_metrics = pd.DataFrame(data['metrics'].tolist())
  data_metrics = data_metrics.applymap(lambda x: x['values'])
  data_metrics = pd.DataFrame(data_metrics[0].tolist())
  result = pd.concat([data_dimensions, data_metrics], axis=1, ignore_index=True)

  return result

def main():
    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    response = parse_data(response)
    response.to_sql('full_sessions', engine)


if __name__ == '__main__':
  main()


