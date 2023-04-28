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
    
    def actualizarCategoria(self, nuevaDescripcion, nuevoPorcentaje, descripcion):
        query = "UPDATE categorias SET Descripcion = %s, Porcentaje = %s WHERE Descripcion = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (nuevaDescripcion, nuevoPorcentaje, descripcion))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al actualizar la categoria {descripcion}") from e
