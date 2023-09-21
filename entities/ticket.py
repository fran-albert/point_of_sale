class Ticket:
    def __init__(self, id_vendedor, total, tipo_de_pago, fecha, id_ticket=None):
        self.id_vendedor = id_vendedor
        self.total = total
        self.tipo_de_pago = tipo_de_pago
        self.fecha = fecha
        self.id_ticket = id_ticket
        
    def get_id_ticket(self):
        return self.id_ticket

    def set_id_ticket(self, id_ticket):
        self.id_ticket = id_ticket

    def get_id_vendedor(self):
        return self.id_vendedor

    def set_id_vendedor(self, id_vendedor):
        self.id_vendedor = id_vendedor

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
