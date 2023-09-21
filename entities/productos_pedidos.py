class ProductosPedidos:
    def __init__(self, id, id_orden_compra, producto_pedido, codigo, cantidad_pedida, precio_compra, precio_total):
        self.id = id
        self.id_orden_compra = id_orden_compra
        self.producto_pedido = producto_pedido
        self.codigo = codigo
        self.cantidad_pedida = cantidad_pedida
        self.precio_compra = precio_compra
        self.precio_total = precio_total

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_id_orden_compra(self):
        return self.id_orden_compra

    def set_id_orden_compra(self, id_orden_compra):
        self.id_orden_compra = id_orden_compra

    def get_producto_pedido(self):
        return self.producto_pedido

    def set_producto_pedido(self, producto_pedido):
        self.producto_pedido = producto_pedido

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_cantidad_pedida(self):
        return self.cantidad_pedida

    def set_cantidad_pedida(self, cantidad_pedida):
        self.cantidad_pedida = cantidad_pedida

    def get_precio_compra(self):
        return self.precio_compra

    def set_precio_compra(self, precio_compra):
        self.precio_compra = precio_compra

    def get_precio_total(self):
        return self.precio_total

    def set_precio_total(self, precio_total):
        self.precio_total = precio_total

