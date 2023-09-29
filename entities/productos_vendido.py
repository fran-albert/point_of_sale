class ProductosVendido:
    def __init__(self, idProdVendido, id_ticket, producto_vendido, codigo, cantidad_vendida, precio_venta, precio_venta_total):
        self.idProdVendido = idProdVendido
        self.id_ticket = id_ticket
        self.producto_vendido = producto_vendido
        self.codigo = codigo
        self.cantidad_vendida = cantidad_vendida
        self.precio_venta = precio_venta
        self.precio_venta_total = precio_venta_total

    def get_idProdVendido(self):
        return self.idProdVendido

    def set_idProdVendido(self, idProdVendido):
        self.idProdVendido = idProdVendido

    def get_id_ticket(self):
        return self.id_ticket

    def set_id_ticket(self, id_ticket):
        self.id_ticket = id_ticket

    def get_producto_vendido(self):
        return self.producto_vendido

    def set_producto_vendido(self, producto_vendido):
        self.producto_vendido = producto_vendido

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_cantidad_vendida(self):
        return self.cantidad_vendida

    def set_cantidad_vendida(self, cantidad_vendida):
        self.cantidad_vendida = cantidad_vendida

    def get_precio_venta(self):
        return self.precio_venta

    def set_precio_venta(self, precio_venta):
        self.precio_venta = precio_venta

    def get_precio_venta_total(self):
        return self.precio_venta_total

    def set_precio_venta_total(self, precio_venta_total):
        self.precio_venta_total = precio_venta_total

