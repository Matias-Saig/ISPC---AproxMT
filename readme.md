# Conexión de Base de Datos y MQTT
Este programa proporciona una interfaz basada en menús para gestionar una base de datos MySQL e interactuar con datos MQTT provenientes de Wowki (simulador de ESP32) 

## Estructura del Proyecto

## Archivos y Funciones

### `main.py`

- `menu_inicial()`: Muestra el menú inicial con opciones para operaciones de base de datos y MQTT.
- `signal_handler(signum, frame)`: Maneja la señal SIGINT para salir del programa de manera ordenada en caso de presionar Ctrl + C.
- `main()`: La función principal que ejecuta el bucle del menú y maneja la entrada del usuario.

### `MQTT/MQTT_insert_db.py`

- `insert_db(db_config, data, table, column)`: Inserta datos en una tabla específica de la base de datos MySQL.
- `on_connect(client, userdata, flags, rc)`: Callback que se ejecuta cuando el cliente se conecta al broker MQTT.
- `on_message(client, userdata, msg)`: Callback que se ejecuta cuando se recibe un mensaje en el tópico suscrito.
- `signal_handler(signum, frame)`: Maneja la señal SIGINT para desconectar el cliente MQTT y detener el bucle de ejecución cuando se presiona Ctrl + C.
- `insert_mqtt_to_db()`: Configura el cliente MQTT, maneja la conexión y el bucle principal para recibir e insertar datos en la base de datos.

### `MySQL/MySQL_create_db.py`

- `MySQL_sentence(sentence, msg)`: Ejecuta una sentencia SQL y muestra un mensaje.
- `create_db()`: Crea la base de datos si no existe.
- `create_table()`: Crea la tabla en la base de datos si no existe.
- `create_db_table()`: Crea la base de datos y la tabla.

### `MySQL/MySQL_drop_database.py`

- `drop_database()`: Elimina la base de datos después de confirmar la acción con el usuario.

### `MySQL/MySQL_select_db.py`

- `select_db()`: Consulta la base de datos y muestra los registros de la tabla.

### `MySQL/MySQL_truncate_table.py`

- `truncate_table()`: Elimina todos los datos de la tabla después de confirmar la acción con el usuario.

### `util/confirm.py`

- `confirm(msg)`: Solicita confirmación del usuario para realizar una acción.

### `util/db_config.py`

- Contiene la configuración de la conexión con MySQL y para la creación la base de datos, tabla y columna.

### `util/mqtt_config.py`

- Contiene la configuración de la conexión MQTT.

## Uso

1. Ejecuta el script `main.py`.
2. Selecciona una opción del menú para realizar la operación deseada:
    - Crear base de datos y tabla
    - Insertar datos del simulador de frecuencia cardíaca en la tabla
    - Mostrar datos de la tabla
    - Eliminar todos los datos de la tabla
    - Eliminar la base de datos
    - Salir

## Requisitos

- Python 3.x
- MySQL
- Librerías: `mysql-connector-python`, `paho-mqtt`
