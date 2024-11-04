""" 
    Conexión a MySQL y eliminación de una base de datos.
"""

from util.db_config import db_config, database
import mysql.connector
import time
from util.confirm import confirm

        
def drop_database():
    drop = confirm(f"\n¿Está seguro que desea eliminar la base de datos? (si/no): ")
    if drop:
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute(f"DROP DATABASE `{database}`")
            connection.commit()

            print("Base de datos eliminada con éxito.")
            time.sleep(1)

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            cursor.close()
            connection.close()
    else:
        print(f"\nOperación cancelada")
