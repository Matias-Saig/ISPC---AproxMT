

"""
This script connects to a MySQL database and creates a database and a table if they do not already exist.
Functions:
    MySQL_sentence(sentence: str, msg: str) -> None:
        Executes a given SQL sentence and prints a message upon success.
        Args:
            sentence (str): The SQL sentence to execute.
            msg (str): The message to print upon successful execution.
    create_db() -> None:
        Creates the database 'AproxMT_ev2' if it does not already exist.
    create_table() -> None:
        Creates the table 'heart_rate' in the 'AproxMT_ev2' database if it does not already exist.
        The table has two columns:
            - id: INT, AUTO_INCREMENT, PRIMARY KEY
            - bpm: INT, NOT NULL
Execution:
    The script first calls create_db() to ensure the database exists.
    Then, it waits for 1 second before calling create_table() to create the table.
"""

from db_config import initial
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
    MySQL_sentence("CREATE DATABASE IF NOT EXISTS AproxMT_ev2;", "Database created.")
    
def create_table():
    MySQL_sentence("""USE AproxMT_ev2;
                    CREATE TABLE IF NOT EXISTS heart_rate
                    (id INT AUTO_INCREMENT PRIMARY KEY, bpm INT NOT NULL)""",
                     "Table created.")

create_db()
time.sleep(1)
create_table()