import mysql.connector
from access.mysql_connection import MySQLConnection

class UsuarioRepository:

    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def validate_login(self, username, password):
        valid = False
        query = "SELECT COUNT(*) FROM usuarios WHERE user = %s AND pass = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        if result and result[0] > 0:
            valid = True
        cursor.close()
        return valid
