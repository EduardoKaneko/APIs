
import subprocess
from airflow.hooks.postgres_hook import PostgresHook
from psycopg2.extras import execute_values, Json, register_json
from psycopg2.extensions import register_adapter


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



