""" 
    Consulta a la base de datos MySQL y muestra los registros de la tabla.
"""

from util.db_config import db_config, table, column
import mysql.connector

def select_db():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        result = cursor.fetchall()

        if len(result) == 0:
            print(f"\nVerificación correcta.\nSe restauró la tabla a 0 registros.")
            return False
        else:  
            print("\nBPM log:\n")

            for i in range(len(result)):
                print(f"ID: {result[i][0]} | {column}: {result[i][1 ]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")