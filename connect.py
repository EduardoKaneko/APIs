
import subprocess
from airflow.hooks.postgres_hook import PostgresHook
from psycopg2.extras import execute_values, Json, register_json
from psycopg2.extensions import register_adapter
from astropy.table import Table, Column

pg_ds_conn_id = 'datascience'
SCHEMA = 'analytics_TESTE'
tName = 'user_teste'
tableFields = ['OneDayUsers', 'SevenDayUsers', 'TwoWeeksUsers', 'MonthlyUsers']

def createTable(dest_conn,tName):
    dest_cursor = dest_conn.cursor()    
    dest_cursor.execute(f'CREATE SCHEMA IF NOT EXISTS {SCHEMA}')
#    tableFields = 'id serial'
    
    dest_cursor.execute(f'''
   CREATE TABLE IF NOT EXISTS {SCHEMA}.{tName}(
     userType     CHAR(40),
     sessionCount CHAR(40),
     daysSinceLastSession CHAR(40),
     users INTEGER,
     newUsers INTEGER,
     {tableFields[0]} INTEGER,
     {tableFields[1]} INTEGER,
     {tableFields[2]} INTEGER,
     {tableFields[3]} INTEGER
     
    );
  ''')
    dest_conn.commit()



def updateTable():
    dest_conn = PostgresHook(postgres_conn_id=pg_ds_conn_id).get_conn()
    
    createTable(dest_conn, tName)
    
