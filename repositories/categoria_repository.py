from mysqlx import Error
from entities.categoria import Categoria
from access.mysql_connection import MySQLConnection

class CategoriaRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarCategoria(self, categoria):
        sql = "INSERT INTO categorias(Descripcion, Porcentaje) VALUES (%s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (categoria.get_descripcion(), categoria.get_porcentaje()))
            self.connection.commit()
        except Error as e:
            raise RuntimeError("Error al insertar la nueva categoria", e)
        
    def obtenerPorcentaje(self, descripcion):
        porcentaje = None
        query = "SELECT porcentaje FROM categorias WHERE id = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (descripcion,))
                row = cursor.fetchone()
                if row:
                    porcentaje = row[0]
            return porcentaje
        except Error as e:
            raise RuntimeError(f"Error al obtener el porcentaje de la categoria con ID {descripcion}", e)
        
    def obtenerCategorias(self):
        categorias = []
        query = "SELECT * FROM categorias"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    id = row[0]
                    descripcion = row[1]
                    porcentaje = row[2]
                    nuevaCategoria = Categoria(id, descripcion, porcentaje)
                    categorias.append(nuevaCategoria)
            return categorias
        except Error as e:
            raise RuntimeError("Error al obtener las categorias", e)
    
    def actualizarCategoria(self, nuevaDescripcion, nuevoPorcentaje, idCategoria):
        query = "UPDATE categorias SET Descripcion = %s, Porcentaje = %s WHERE id = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (nuevaDescripcion, nuevoPorcentaje, idCategoria))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al actualizar la categoria con ID {idCategoria}") from e


    def eliminarCategoria(self, categoria_id):
        query = "DELETE FROM categorias WHERE id = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (categoria_id,))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al eliminar la categoria con ID {categoria_id}") from e
