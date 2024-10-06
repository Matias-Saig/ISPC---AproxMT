"""
This module provides functionality to select and display data from a MySQL database.

Functions:
    select_db(): Connects to the MySQL database using the provided configuration, 
                 executes a SELECT query on the 'heart_rate' table, and prints the results.

Dependencies:
    - db_config: A dictionary containing the database configuration parameters.
    - mysql.connector: A MySQL driver for Python to connect to the MySQL database.

Exceptions:
    - mysql.connector.Error: Catches and prints any errors that occur during the database connection or query execution.
"""


from db_config import db_config
import mysql.connector

def select_db():
    try:

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM heart_rate")
        result = cursor.fetchall()

        if len(result) == 0:
            return False
        else:  
            print("\nBPM log:\n")

            for i in range(len(result)):
                print(f"ID: {result[i][0]} | BPM: {result[i][1 ]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

select_db()

