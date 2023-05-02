from mysqlx import Error
from entities.proveedor import Proveedor
from access.mysql_connection import MySQLConnection

class ProveedorRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarProveedor(self, proveedor):
        sql = "INSERT INTO proveedores(id, nombre, direccion, cod_postal, ciudad, provincia, telefono, correo_electronico, comentario, cuenta_bancaria, fecha_alta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (proveedor.get_id(),proveedor.get_nombre(), proveedor.get_direccion(),proveedor.get_cod_postal(),proveedor.get_ciudad(),proveedor.get_provincia(),proveedor.get_telefono(),proveedor.get_correo_electronico(),proveedor.get_comentario(),proveedor.get_cuenta_bancaria(),proveedor.get_fecha_alta(),))
            self.connection.commit()
        except Error as e:
            raise RuntimeError("Error al insertar el nuevo proveedor", e)

    def obtenerProveedor(self):
        proveedor = []
        query = "SELECT * FROM proveedores"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    id = row[0]
                    nombre = row[1]
                    direccion = row[2]
                    cod_postal = row[3]
                    ciudad = row[4]
                    provincia = row[5]
                    telefono = row[6]
                    correo_electronico = row[7]
                    comentario = row[8]
                    cuenta_bancaria = row[9]
                    fecha_alta = row[10]
                    nuevoProveedor = Proveedor(id, nombre, direccion, cod_postal, ciudad, provincia, telefono, correo_electronico, comentario, cuenta_bancaria, fecha_alta)
                    proveedor.append(nuevoProveedor)
            return proveedor
        except Error as e:
            raise RuntimeError("Error al obtener los proveedores", e)
    
    def actualizarProveedor(self, nuevoNombre, nuevaDireccion, nuevoCodPostal, nuevaCiudad, nuevaProvincia, nuevoTelefono, nuevoCorreo, nuevoComentario, nuevaCBU, fecha_alta, id):
        query = "UPDATE proveedores SET nombre = %s, direccion = %s, cod_postal = %s, ciudad = %s, provincia = %s, telefono = %s, correo_electronico = %s, comentario = %s, cuenta_bancaria = %s, fecha_alta = %s WHERE id = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (nuevoNombre, nuevaDireccion, nuevoCodPostal, nuevaCiudad, nuevaProvincia, nuevoTelefono, nuevoCorreo, nuevoComentario, nuevaCBU, fecha_alta, id))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al actualizar el proveedor con ID {id}") from e


    def eliminarProveedor(self, id):
        query = "DELETE FROM proveedores WHERE id = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (id,))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al eliminar el proveedor con ID {id}") from e
