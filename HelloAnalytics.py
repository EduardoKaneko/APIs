"""Hello Analytics Reporting API V4."""

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
import argparse
from csv import writer
from datetime import date, timedelta, datetime
import httplib2
import json
from os import path

from apiclient.discovery import build
from apiclient.errors import HttpError
import gen_utils
from oauth2client import client, file, tools
import psycopg2
import yaml



SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'client_secrets.json'
VIEW_ID = '109580013'


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
  """Queries the Analytics Reporting API V4.

  Args:
    analytics: An authorized Analytics Reporting API V4 service object.
  Returns:
    The Analytics Reporting API V4 response.
  """
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '2019-05-01', 'endDate': 'yesterday'}],
          'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:newUsers'}, {'expression': 'ga:users'}],
          'dimensions': [{'name': 'ga:source'}, {'name': 'ga:sourceMedium'}]
        }]
      }
  ).execute()

# def write_results(report):


def print_response(response):
  """Parses and prints the Analytics Reporting API V4 response.
cd 
  Args:
    response: An Analytics Reporting API V4 response.
  """
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    rows = report.get('data', {}).get('rows', [])

    for row in rows:
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])

      dimension[0] = datetime.strptime(str(dimensions[0], '%Y%m%d').strftime("%Y-%m-%d"))
      insert_query= "insert into " + table + " VALUES ("+ value_string(col) + ")"

      for header, dimension in zip(dimensionHeaders, dimensions):
        cities.append(dimensions)

      for i, values in enumerate(dateRangeValues):
         insert_data = (insert_date, webpropertyid, profileid, dimensions[0], dimensions[1], values.get('values')[0], values.get('values')[1], values.get('values')[2], values.get('values')[3], values.get('values')[4], values.get('values')[5], values.get('values')[6]) # adjust per number of columns needed
         print(insert_data)
                
                try:
                    cur.execute(insert_query, insert_data)
                    conn.commit()

                except psycopg2.Error, e:
                    print 'line skipped: ' + str(e)
                    conn.rollback()
                    with open(dir + 'badLines_' + str(date.today())+ '.csv', 'a') as csvout:
                        outfile = writer(csvout, delimiter=',')
                        outfile.writerow(insert_data)

        for metricHeader, value in zip(metricHeaders, values.get('values')):
          val.append(int(value))
  print(cities, val)
        

def main():
  analytics = initialize_analyticsreporting()
  response = get_report(analytics)
  print_response(response)


if __name__ == '__main__':
  main()
