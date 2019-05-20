import subprocess
from airflow.hooks.postgres_hook import PostgresHook
from psycopg2.extras import execute_values, Json, register_json
from psycopg2.extensions import register_adapter

pg_ds_conn_id = 'datascience'
SCHEMA = 'teste1'
tName = 'teste3'
tableFields = ['teste', '1234']

def createTable(dest_conn,tName):
    dest_cursor = dest_conn.cursor()    
    dest_cursor.execute(f'CREATE SCHEMA IF NOT EXISTS {SCHEMA}')
    
    dest_cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {SCHEMA}.{tName}({tableFields});
    ''')
    dest_conn.commit()

def getColumnNames():
      dest_cursor = dest_conn.cursor()
      dest_cursor.execute(
      f'''SELECT column_name
      FROM information_schema.columns
      WHERE table_name = \'{tName}\' AND table_schema = \'{SCHEMA}\';''',
      )
    
      tColumns = dest_cursor.fetchall()
      dest_cursor.close()
      
 
def updateTable():
    dest_conn = PostgresHook(postgres_conn_id=pg_ds_conn_id).get_conn()
    
    createTable(dest_conn, tName)
    
    dest_conn.close()


updateTable()
    
