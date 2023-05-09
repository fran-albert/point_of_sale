from mysqlx import Error
from entities.ticket import Ticket
from access.mysql_connection import MySQLConnection

class TicketRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarTicket(self, ticket):
        sql = "INSERT INTO ticket(usuario, total, tipo_de_pago, fecha) VALUES (%s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (ticket.get_usuario(),ticket.get_total(),ticket.get_tipo_de_pago(),ticket.get_fecha()))
            self.connection.commit()
        except Error as e:
            raise RuntimeError("Error al insertar el nuevo ticket", e)
                
    def obtenerTickets(self, fechaDesde, fechaHasta):
        tickets = []
        query = "SELECT * FROM tickets WHERE fecha => %s AND fecha <= %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, fechaDesde, fechaHasta)
                for row in cursor.fetchall():
                    idTicket = row[0]
                    usuario = row[1]
                    total = row[2]
                    tipo_de_pago = row[3]
                    fecha = row[4]
                    nuevoTicket = Ticket(idTicket, usuario, total, tipo_de_pago, fecha)
                    tickets.append(nuevoTicket)
            return tickets
        except Error as e:
            raise RuntimeError("Error al obtener los tickets", e)
