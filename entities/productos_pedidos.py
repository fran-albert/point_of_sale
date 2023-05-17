class ProductosPedidos:
    def __init__(self, idProdPedido, idOrdenCompra, prod_pedido, codigo, cant_pedida, precio_compra, precio_total):
        self.idProdPedido = idProdPedido
        self.idOrdenCompra = idOrdenCompra
        self.prod_pedido = prod_pedido
        self.codigo = codigo
        self.cant_pedida = cant_pedida
        self.precio_compra = precio_compra
        self.precio_total = precio_total

    def get_idProdPedido(self):
        return self.idProdPedido

    def set_idProdPedido(self, idProdPedido):
        self.idProdPedido = idProdPedido

    def get_idOrdenCompra(self):
        return self.idOrdenCompra

    def set_idOrdenCompra(self, idOrdenCompra):
        self.idOrdenCompra = idOrdenCompra

    def get_prod_pedido(self):
        return self.prod_pedido

    def set_prod_pedido(self, prod_pedido):
        self.prod_pedido = prod_pedido

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_cant_pedida(self):
        return self.cant_pedida

    def set_cant_pedida(self, cant_pedida):
        self.cant_pedida = cant_pedida

    def get_precio_compra(self):
        return self.precio_compra

    def set_precio_compra(self, precio_compra):
        self.precio_compra = precio_compra

    def get_precio_total(self):
        return self.precio_total

    def set_precio_total(self, precio_total):
        self.precio_total = precio_total

