from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from pandas.io.json import json_normalize
from sqlalchemy import create_engine

import subprocess
from airflow.hooks.postgres_hook import PostgresHook
from psycopg2.extras import execute_values, Json, register_json
from psycopg2.extensions import register_adapter
from astropy.table import Table, Column

# Analytics Variables
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'client_secrets.json'
VIEW_ID = '109580013'

#SQL Variable
pg_ds_conn_id = 'datascience'
SCHEMA = 'analytics_TESTE'
tName = 'user_teste'
dest_conn = PostgresHook(postgres_conn_id=pg_ds_conn_id).get_conn()



pg_ds_conn_id = 'datascience'
SCHEMA = 'analytics_tr'
tName = 'user_teste1'

def createTable(dest_conn,tName):
    dest_cursor = dest_conn.cursor()    
    dest_cursor.execute(f'CREATE SCHEMA IF NOT EXISTS {SCHEMA}')
    dest_cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {SCHEMA}.{tName}(
        userType     CHAR(40),
        sessionCount INTEGER,
        daysSinceLastSession INTEGER,
        users INTEGER 
    );
  ''')
    dest_conn.commit()
    dest_conn.close()



def updateTable():
    dest_conn = PostgresHook(postgres_conn_id=pg_ds_conn_id).get_conn()
    createTable(dest_conn, tName)




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
            'pageSize': 10000,
            'dateRanges': [{'startDate': '2015-05-01', 'endDate': 'yesterday'}],
            'metrics': [{'expression': 'ga:users'}],
            'dimensions': [{'name': 'ga:userType'}, {'name': 'ga:sessionCount'}, {'name': 'ga:daysSinceLastSession'}],
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

def insertData(result):
    dest_cursor = dest_conn.cursor()
    for row in result:
        dest_cursor.execute('''INSERT INTO {SCHEMA}.{tName} 
                            VALUES(%s, %s, %s, %s)''', [row])
        dest_cursor.commit()



def updateTable():
    dest_conn = PostgresHook(postgres_conn_id=pg_ds_conn_id).get_conn()
    createTable(dest_conn, tName)

def main():
    updateTable()
    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    response = parse_data(response)
    insertData(response)
#   print(response)
#   response.to_sql('test-v4', engine)


if __name__ == '__main__':
  main()






#def insertData(result):
 #   dest_cursor = dest_conn.cursor()
#    for row in result:
#        dest_cursor = dest_conn.cursor()    
#        dest_cursor.execute('''INSERT INTO {SCHEMA}.{tName} 
 #                           VALUES(%s, %s, %s, %s)''', row)
#        dest_cursor.commit()



#args_str = ','.join(cur.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s)", x) for x in tup)
#cur.execute("INSERT INTO table VALUES " + args_str) 