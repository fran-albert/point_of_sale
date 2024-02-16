from repositories.orden_compra_repository import OrdenCompraRepository

class OrdenCompraService:
    def __init__(self):
        self.orden_compra_repository = OrdenCompraRepository()

    def insertarOrden(self, ordenCompra):
        return self.orden_compra_repository.insertarOrden(ordenCompra)
    
    def obtenerOrdenes(self, fecha_desde, fecha_hasta):
        return self.orden_compra_repository.obtenerOrdenes(fecha_desde, fecha_hasta)
    
    def obtenerOrden(self, idOrdenCompra):
        return self.orden_compra_repository.obtenerOrden(idOrdenCompra)
    
    def actualizarOrden(self, idOrdenCompra, recibido):
        return self.orden_compra_repository.actualizarOrden(idOrdenCompra, recibido)