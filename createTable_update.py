import psycopg2

try:
    conn = psycopg2.connect(  
        database = "eduardo",
        user="postgres",
        password="eck",
        host="localhost",
        port="5432"
    )
except:
    print("I am unable to connect to the database") 

cur = psycopg2.connect(  
        database = "eduardo",
        user="postgres",
        password="eck",
        host="localhost",
        port="5432"
    ).cursor()
try:
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
except:
    print("I can't drop our test database!")

conn.commit() # <--- makes sure the change is shown in the database
conn.close()
cur.close()



import psycopg2
table = 'example'

conn = psycopg2.connect(database = "example", user="postgres", password="eck", host="localhost", port="5432")
conn.autocommit = True
cur = conn.cursor()
cur.execute('CREATE table IF NOT EXISTS table')
cur.execute("""CREATE TABLE HARMKA
                         (ID INT PRIMARY KEY NOT NULL,
                         PHARMACY_LICENSE CHAR(100),
                         STREET CHAR(150),
                         CITY CHAR(30));""")
cur.execute("INSERT INTO HARMKA VALUES(%s, %s, %s, %s)", (1, '12345', 'street', 'Denwer'))
cur.close()
conn.close()