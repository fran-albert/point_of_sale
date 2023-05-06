class ProductosVendidos:
    def __init__(self, idProdVendido, idTicket, prod_vendido, codigo, cant_vendida, precio_venta, precio_venta_total):
        self.idProdVendido = idProdVendido
        self.idTicket = idTicket
        self.prod_vendido = prod_vendido
        self.codigo = codigo
        self.cant_vendida = cant_vendida
        self.precio_venta = precio_venta
        self.precio_venta_total = precio_venta_total

    def get_idProdVendido(self):
        return self.idProdVendido

    def set_idProdVendido(self, idProdVendido):
        self.idProdVendido = idProdVendido

    def get_idTicket(self):
        return self.idTicket

    def set_idTicket(self, idTicket):
        self.idTicket = idTicket

    def get_prod_vendido(self):
        return self.prod_vendido

    def set_prod_vendido(self, prod_vendido):
        self.prod_vendido = prod_vendido

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_cant_vendida(self):
        return self.cant_vendida

    def set_cant_vendida(self, cant_vendida):
        self.cant_vendida = cant_vendida

    def get_precio_venta(self):
        return self.precio_venta

    def set_precio_venta(self, precio_venta):
        self.precio_venta = precio_venta

    def get_precio_venta_total(self):
        return self.precio_venta_total

    def set_precio_venta_total(self, precio_venta_total):
        self.precio_venta_total = precio_venta_total

