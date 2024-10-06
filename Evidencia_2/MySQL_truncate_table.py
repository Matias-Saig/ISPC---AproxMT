from db_config import db_config
import mysql.connector

from MySQL_select_db import select_db

def truncate_table():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("TRUNCATE `AproxMT_ev2`.`heart_rate`")
        connection.commit()

        check = select_db()
        if check == False:
            print("Table is empty.")
        else:
            print("Table is not empty.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

print("Checking...")

truncate_table()
