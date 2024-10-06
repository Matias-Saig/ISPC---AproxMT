"""
This script connects to an MQTT broker, subscribes to a topic, and inserts received messages into a MySQL database.

Functions:
    insert_db(db_config, data, table, row):
        Inserts data into a specified table and row in the MySQL database.
        Args:
            db_config (dict): Database configuration parameters.
            data (list): Data to be inserted.
            table (str): Name of the table.
            row (str): Name of the row.
        Raises:
            mysql.connector.Error: If there is an error with the MySQL connection or query execution.

    on_connect(client, userdata, flags, rc):
        Callback function that is called when the client connects to the MQTT broker.
        Args:
            client (paho.mqtt.client.Client): The MQTT client instance.
            userdata: The private user data.
            flags (dict): Response flags sent by the broker.
            rc (int): The connection result.

    on_message(client, userdata, msg):
        Callback function that is called when a message is received from the MQTT broker.
        Args:
            client (paho.mqtt.client.Client): The MQTT client instance.
            userdata: The private user data.
            msg (paho.mqtt.client.MQTTMessage): The received message.
        Raises:
            Exception: If there is an error processing the message.

MQTT Client Setup:
    - Connects to the broker at "broker.hivemq.com" on port 1883.
    - Subscribes to the topic "AproxMT/ev2/heart_rate_simulated".
    - Uses the on_connect and on_message callback functions.
    - Enters a blocking loop to process network traffic and dispatch callbacks.
"""
from db_config import db_config
import mysql.connector
import paho.mqtt.client as mqtt

def insert_db(db_config, data, table, row):
    try:        
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        # query = f"INSERT INTO heart_rate (bpm) VALUES (%s)"
        query = f"INSERT INTO {table} ({row}) VALUES (%s)"
        cursor.execute(query, (data))
        connection.commit()
        print(f"Datos guardados: data = {data}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()


def on_connect(client, userdata, flags, rc):
    print(f"Conectado al broker MQTT con codigo: {rc}")
    client.subscribe("AproxMT/ev2/heart_rate_simulated")


def on_message(client, userdata, msg):

    data_int = int(msg.payload.decode())
    data = [data_int]
    try:
        insert_db(db_config, data, "heart_rate", "bpm")
    except Exception as e:
        print(f"Error procesando el mensaje: {e}")


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()
