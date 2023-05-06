class Ticket:
    def __init__(self, idTicket, usuario, total, tipo_de_pago, fecha):
        self.idTicket = idTicket
        self.usuario = usuario
        self.total = total
        self.tipo_de_pago = tipo_de_pago
        self.fecha = fecha
        
    def get_idTicket(self):
        return self.idTicket

    def set_idTicket(self, idTicket):
        self.idTicket = idTicket

    def get_usuario(self):
        return self.usuario

    def set_usuario(self, usuario):
        self.usuario = usuario

    def get_total(self):
        return self.total

    def set_total(self, total):
        self.total = total

    def get_tipo_de_pago(self):
        return self.tipo_de_pago

    def set_tipo_de_pago(self, tipo_de_pago):
        self.tipo_de_pago = tipo_de_pago

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha
