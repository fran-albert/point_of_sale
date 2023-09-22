from mysqlx import Error
from entities.ticket import Ticket
from access.mysql_connection import MySQLConnection

class TicketRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarTicket(self, ticket):
        sql = "INSERT INTO tickets(id_vendedor, total, tipo_de_pago, fecha) VALUES (%s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (ticket.get_id_vendedor(),ticket.get_total(),ticket.get_tipo_de_pago(),ticket.get_fecha()))
                self.connection.commit()
                last_inserted_id = cursor.lastrowid
                return last_inserted_id

        except Error as e:
            raise RuntimeError("Error al insertar el nuevo ticket", e)
                
    def obtenerTickets(self, fechaDesde, fechaHasta):
        tickets = []
        query = "SELECT * FROM tickets WHERE fecha => %s AND fecha <= %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, fechaDesde, fechaHasta)
                for row in cursor.fetchall():
                    id_ticket = row[0]
                    id_vendedor = row[1]
                    total = row[2]
                    tipo_de_pago = row[3]
                    fecha = row[4]
                    nuevoTicket = Ticket(id_vendedor, total, tipo_de_pago, fecha, id_ticket)
                    tickets.append(nuevoTicket)
            return tickets
        except Error as e:
            raise RuntimeError("Error al obtener los tickets", e)
