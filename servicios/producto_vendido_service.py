from repositories.producto_vendido_repository import ProductoVendidoRepository

class ProductoVendidoService:
    def __init__(self):
        self.producto_vendido_repository = ProductoVendidoRepository()

    def insertarProdVendido(self, producto_vendido):
        return self.producto_vendido_repository.insertarProdVendido(producto_vendido)
    
    def obtenerProductosVendidos(self):
        return self.producto_vendido_repository.obtenerProductosVendidos()

