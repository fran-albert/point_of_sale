from mysqlx import Error
from entities.usuario import Usuario
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

    def obtenerUsuario(self):
        usuarios = []
        query = "SELECT * FROM usuarios"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    id = row[0]
                    username = row[1]
                    password = row[2]
                    nuevoUsuario = Usuario(id, username, password)
                    usuarios.append(nuevoUsuario)
            return usuarios
        except Error as e:
            raise RuntimeError("Error al obtener los usuarios", e)