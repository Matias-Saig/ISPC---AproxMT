""" 
    Conexión a la base de datos MySQL y eliminación de todos los datos de la tabla
"""

from util.db_config import db_config, database, table
import mysql.connector
import time
from MySQL.MySQL_select_db import select_db
from util.confirm import confirm


def truncate_table():
    truncate = confirm(f"\n¿Está seguro que desea eliminar todos los datos de la tabla? (si/no): ")
    if truncate:
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute(f"TRUNCATE `{database}`.`{table}`")
            connection.commit()

            print("Verificando...")
            time.sleep(1)

            check = select_db()
            if check == False:
                print("El contenido de la tabla ha sido borrado")
            else:
                print("Hubo un error al borrar los datos")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            cursor.close()
            connection.close()
    else:
        print(f"\nOperación cancelada")