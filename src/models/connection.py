import mysql.connector
from mysql.connector import Error
host = 'localhost'
database = 'db_jogopr_dev'
user = 'root'
password = ''


def connect():
    try:
        conn = mysql.connector.connect(
            host=host, database=database, user=user, password=password)
        return conn

    except Error as error:
        return 'error' + error
