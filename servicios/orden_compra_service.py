from repositories.orden_compra_repository import OrdenCompraRepository

class OrdenCompraService:
    def __init__(self):
        self.orden_compra_repository = OrdenCompraRepository()

    def insertarOrden(self, ordenCompra):
        return self.orden_compra_repository.insertarOrden(ordenCompra)
    
    def obtenerOrdenes(self):
        return self.orden_compra_repository.obtenerOrdenes()
    
    def obtenerOrden(self, idOrdenCompra):
        return self.orden_compra_repository.obtenerOrden(idOrdenCompra)