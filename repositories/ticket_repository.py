from mysqlx import Error
from entities.ticket import Ticket
from access.mysql_connection import MySQLConnection

class TicketRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarTicket(self, ticket):
        sql = "INSERT INTO ticket(idTicket, usuario, total, tipo_de_pago, fecha) VALUES (%s, %s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (ticket.get_idTicket(), ticket.get_usuario(),ticket.get_total(),ticket.get_tipo_de_pago(),ticket.get_fecha()))
            self.connection.commit()
        except Error as e:
            raise RuntimeError("Error al insertar el nuevo ticket", e)
                
    def obtenerTickets(self):
        tickets = []
        query = "SELECT * FROM tickets"
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
