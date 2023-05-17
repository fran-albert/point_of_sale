from repositories.productos_pedidos_repository import ProductoPedidoRepository

class ProductoPedidoService:
    def __init__(self):
        self.producto_pedido_repository = ProductoPedidoRepository()

    def insertarProdPedido(self, producto_pedido):
        return self.producto_pedido_repository.insertarProdPedido(producto_pedido)
    
    def obtenerProductosPedidos(self, idOrdenCOmpra):
        return self.producto_pedido_repository.obtenerProductosPedidos(idOrdenCOmpra)

