from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from pandas.io.json import json_normalize
from sqlalchemy import create_engine
import urllib.request as urllib2
# from urllib2 import HTTPError


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

# 1. Execute a Metadata Request
# An application can request columns data by calling the list method on the Analytics service object.
# The method requires an reportType parameter that specifies the column data to retrieve.
# For example, the following code requests columns for the ga report type.
try:
 results = service.metadata().columns().list(reportType='ga').execute()
except TypeError as error:
 # Handle errors in constructing a query.
 print ('There was an error in constructing your query : %s' % error)
except urllib2.HTTPError as error:
 # Handle API errors.
 print ('Arg, there was an API error : %s : %s' %
 (error.resp.status, error._get_reason()))
# 2. Print out the Columns data
# The components of the result can be printed out as follows:
def print_metadata_report(results):
    print('Metadata Response Report')
    print_report_info(results)
    print_attributes(results.get('attributeNames'))
    print_columns(results)

def print_report_info(columns):
    print("Metadata Report Info")
    if columns:
        print('Kind = %s' % columns.get('kind'))
        print('Etag = %s' % columns.get('etag'))
        print('Total Results = %s' % columns.get('totalResults'))

def print_attributes(attributes):
    if attributes:
        print('Attribute Names:')
    for attribute in attributes:
        print(attribute)

def print_columns(columns_data):
    if columns_data:
        print('Columns:')
        
        columns = columns_data.get('items', [])
    for column in columns:
        print('%15s = %35s' % ('Column ID', column.get('id')))
        print('%15s = %35s' % ('Kind', column.get('kind')))
        column_attributes = column.get('attributes', [])
    for name, value in column_attributes.iteritems():
        print('%15s = %35s' % (name, value))