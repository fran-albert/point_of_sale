from repositories.ticket_repository import TicketRepository

class TicketService:
    def __init__(self):
        self.ticket_repository = TicketRepository()
    
    def insertarTicket(self, ticket):
        return self.ticket_repository.insertarTicket(ticket)
    
    def obtenerTickets(self, fechaDesde, fechaHasta):
        return self.ticket_repository.obtenerTickets(fechaDesde, fechaHasta)
    
    