"""
Este script proporciona una interfaz basada en menús para gestionar una base de datos MySQL e interactuar con datos MQTT.
Funciones:
    menu_inicial(): Muestra el menú inicial con opciones para operaciones de base de datos y MQTT.
    signal_handler(signum, frame): Maneja la señal SIGINT para salir del programa de manera ordenada en caso de presionar Ctrl + C.
    main(): La función principal que ejecuta el bucle del menú y maneja la entrada del usuario.
"""
from MySQL.MySQL_create_db import create_db_table
from MySQL.MySQL_select_db import select_db
from MySQL.MySQL_truncate_table import truncate_table
from MySQL.MySQL_drop_database import drop_database
from MQTT.MQTT_insert_db import insert_mqtt_to_db
import signal

def menu_inicial():
    print(f"""
          « Conexión de base de datos y MQTT »
          
            1. Crear base de datos y tabla
          
            2. Insertar datos del simulador de frecuencia cardíaca en la tabla 
          
            3. Mostrar datos de la tabla
          
            4. Eliminar todos los datos de la tabla
          
            5. Eliminar la base de datos
          
            6. Salir
        """)
    

def signal_handler(signum, frame):
    quit(f"El programa cerro correctamente\n")


def main():
    while True:
        signal.signal(signal.SIGINT, signal_handler)
        try:
            menu_inicial()
            choice = input("Ingrese el número de la opción que desea ejecutar: ")
            
            match choice:
                case '1':
                    create_db_table()
                case '2':
                    insert_mqtt_to_db()
                case '3':
                    select_db()
                case '4':
                    truncate_table()
                case '5':
                    drop_database()
                case '6':
                    quit(f"\nEl programa cerro correctamente\n")
                case _:
                    print(f"\nOpción invalida, intente nuevamente.\n")
                    continue
        
        except KeyboardInterrupt:
            continue

            
            
if __name__ == "__main__":
    main()