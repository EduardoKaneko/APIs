import subprocess
from airflow.hooks.postgres_hook import PostgresHook
from psycopg2.extras import execute_values, Json, register_json
from psycopg2.extensions import register_adapter

pg_ds_conn_id = 'datascience'
SCHEMA = 'teste'
tName = 'teste2'

def createTable(dest_conn,tName):
    dest_cursor = dest_conn.cursor()    
    dest_cursor.execute(f'CREATE SCHEMA IF NOT EXISTS {SCHEMA}')
    tableFields = 'id serial'
    
    dest_cursor.execute(f'''
   CREATE TABLE IF NOT EXISTS {SCHEMA}.{tName}(
      {tableFields}
    );
  ''')
    dest_conn.commit()



def updateTable():
    dest_conn = PostgresHook(postgres_conn_id=pg_ds_conn_id).get_conn()
    
    createTable(dest_conn, tName)
    
    dest_conn.close()
    
