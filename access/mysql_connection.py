import mysql.connector
from mysql.connector import Error

class MySQLConnection:

    _connection = None

    @staticmethod
    def _create_connection():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="point_of_sale"
            )
            return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def get_connection():
        if MySQLConnection._connection is None:
            MySQLConnection._connection = MySQLConnection._create_connection()
        return MySQLConnection._connection

