""" 
    Conexión a MySQL y creación de base de datos y tabla.
"""
from util.db_config import initial, database, table, column
import mysql.connector
import time


def MySQL_sentence(sentence, msg):
    try:
        connection = mysql.connector.connect(**initial)
        cursor = connection.cursor()
        cursor.execute(sentence)
        print(msg)        

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def create_db():
    MySQL_sentence(f"CREATE DATABASE IF NOT EXISTS {database};", f"\nBase de datos creada con éxito.")

    
def create_table():
    MySQL_sentence(f"""USE {database};
                    CREATE TABLE IF NOT EXISTS {table}
                    (id INT AUTO_INCREMENT PRIMARY KEY, {column} INT NOT NULL)""",
                     f"Tabla creada.\n")

def create_db_table():
    create_db()
    time.sleep(1)
    create_table()