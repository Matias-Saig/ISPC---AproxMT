

"""
Este módulo se encarga de insertar datos recibidos a través de MQTT en la base de datos MySQL.

Funciones:
- insert_db(db_config, data, table, column): Inserta datos en una tabla específica de la base de datos MySQL.
- on_connect(client, userdata, flags, rc): Callback que se ejecuta cuando el cliente se conecta al broker MQTT.
- on_message(client, userdata, msg): Callback que se ejecuta cuando se recibe un mensaje en el tópico suscrito.
- signal_handler(signum, frame): Maneja la señal SIGINT para desconectar el cliente MQTT y detener el bucle de ejecución cuando se presiona Ctrl + c.
- insert_mqtt_to_db(): Configura el cliente MQTT, maneja la conexión y el bucle principal para recibir e insertar datos en la base de datos.

Variables:
- client: Instancia del cliente MQTT.
- running: Variable global que controla el bucle principal de ejecución.
"""

from util.db_config import db_config, table, column
from util.mqtt_config import MQTT
import mysql.connector
import paho.mqtt.client as mqtt
import signal

client = mqtt.Client()

def insert_db(db_config, data, table, column):
    try:        
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = f"INSERT INTO {table} ({column}) VALUES (%s)"
        cursor.execute(query, (data))
        connection.commit()
        print(f"Datos guardados: {data}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()


def on_connect(client, userdata, flags, rc):
    print(f"Conectado al broker MQTT con codigo: {rc}")
    client.subscribe(MQTT['topic'])


def on_message(client, userdata, msg):

    data_int = int(msg.payload.decode())
    data = [data_int]
    try:
        insert_db(db_config, data, table, column)
    except Exception as e:
        print(f"Error procesando el mensaje: {e}")


def signal_handler(signum, frame):
    print(f'Volviendo al menú inicial...\n')
    client.disconnect()
    global running
    running = False


def insert_mqtt_to_db():
    global running
    running = True
    client.on_connect = on_connect
    client.on_message = on_message

    signal.signal(signal.SIGINT, signal_handler)
    try:
        client.connect(MQTT['broker'], MQTT['port'], MQTT['keepalive'])
        print(f"\nEsperando conexión...\n( Ctrl + C para volver al menu de inicio )\n")
        while running:
            client.loop()
    except KeyboardInterrupt:
        print("Regresando al programa principal...")
        return None
