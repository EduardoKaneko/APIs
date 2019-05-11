# Import the psycopg2 module in our program. 
# Using the classes and method defined psycopg2 module we can communicate with PostgreSQL.
import psycopg2

# Using the connect() method we can create a connection to a PostgreSQL database instance. 
# This returns a PostgreSQL Connection Object.
try:
    connection = psycopg2.connect(  
        database = "ga",
        user="postgres",
        password="eck",
        host="localhost",
        port="5432"
    )

    cursor = connection.cursor()
    # Print PostgreSQL connection properties
    print(connection.get_dsn_parameters(), "\n")
    
    # Print postgres version
    cursor.execute("""CREATE TABLE Traffic(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)""")
#    record = cursor.fetchone()
    connection.commit()

#    print("You are connected to - ", record, "\n")

except(Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # Closing database connection
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
