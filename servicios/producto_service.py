from repositories.producto_repository import ProductoRepository

class ProductoService:
    def __init__(self):
        self.producto_repository = ProductoRepository()

    def insertarProducto(self, producto):
        return self.producto_repository.insertarProducto(producto)
    
    def obtenerProductos(self):
        return self.producto_repository.obtenerProductos()

    def actualizarProducto(self, nuevoCodigo, nuevoNombre, nuevoPrecio, nuevaCantStock, nuevaCategoria, nuevosImpuestos, nuevosDescuentos, nuevoProveedor, nuevaFechaVenc, codigo):
        return self.producto_repository.actualizarProducto(nuevoCodigo, nuevoNombre, nuevoPrecio, nuevaCantStock, nuevaCategoria, nuevosImpuestos, nuevosDescuentos, nuevoProveedor, nuevaFechaVenc, codigo)
    
    def eliminarProducto(self, codigo):
        return self.producto_repository.eliminarProducto(codigo)
