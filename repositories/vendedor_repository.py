from mysqlx import Error
from entities.vendedor import Vendedor
from access.mysql_connection import MySQLConnection

class VendedorRepository:

    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarVendedor(self, vendedor):
            sql = "INSERT INTO vendedores(dni, nombre, apellido, telefono, correo, fecha_nac, fecha_alta) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute(sql, (vendedor.get_dni(), vendedor.get_nombre(), vendedor.get_apellido(), vendedor.get_telefono(), vendedor.get_correo(), vendedor.get_fechaNac(), vendedor.get_fechaAlta()))
                self.connection.commit()
            except Error as e:
                raise RuntimeError("Error al insertar el nuevo vendedor", e)
            
    def validate_login(self, nombre, dni):
        valid = False
        query = "SELECT COUNT(*) FROM vendedores WHERE nombre = %s AND dni = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (nombre, dni))
        result = cursor.fetchone()
        if result and result[0] > 0:
            valid = True
        cursor.close()
        return valid

    def obtenerVendedores(self):
        vendedores = []
        query = "SELECT * FROM vendedores"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    id = row[0]
                    dni = row[1]
                    nombre = row[2]
                    apellido = row[3]
                    telefono = row[4]
                    correo = row[5]
                    fechaNac = row[6]
                    fechaAlta = row[7]
                    nuevoVendedor = Vendedor(dni, nombre, apellido, telefono, correo, fechaNac, fechaAlta, id)
                    vendedores.append(nuevoVendedor)
            return vendedores
        except Error as e:
            raise RuntimeError("Error al obtener los vendedores", e)
        
    def actualizarVendedor(self, nuevoDNI, nuevoNombre, nuevoApellido, nuevoTelefono, nuevoCorreo, nuevaFechaNac, fecha_alta, id):
        query = "UPDATE vendedores SET dni = %s, nombre = %s, apellido = %s, telefono = %s, correo = %s, fecha_nac = %s, fecha_alta = %s WHERE id = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (nuevoDNI, nuevoNombre, nuevoApellido, nuevoTelefono, nuevoCorreo, nuevaFechaNac, fecha_alta, id))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al actualizar el vendedor con ID {id}") from e

    def eliminarVendedor(self, id):
            query = "DELETE FROM vendedores WHERE id = %s"
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute(query, (id,))
                    self.connection.commit()
            except Exception as e:
                raise RuntimeError(f"Error al eliminar el vendedor con ID {id}") from e

            