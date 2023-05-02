from repositories.producto_repository import ProductoRepository

class ProductoService:
    def __init__(self):
        self.producto_repository = ProductoRepository()

    def insertarProducto(self, producto):
        return self.producto_repository.insertarProducto(producto)
    
    def obtenerProductos(self):
        return self.producto_repository.obtenerProductos()
    
    def obtenerProducto(self, codigo):
        return self.producto_repository.obtenerProducto(codigo)

    def actualizarProducto(self, nuevoCodigo, nuevoNombre, nuevoPrecioCompra, nuevoPrecioVenta, nuevaCantStock, nuevaCategoria, nuevosImpuestos, nuevosDescuentos, nuevoProveedor, nuevaFechaVenc, codigo):
        return self.producto_repository.actualizarProducto(nuevoCodigo, nuevoNombre, nuevoPrecioCompra, nuevoPrecioVenta, nuevaCantStock, nuevaCategoria, nuevosImpuestos, nuevosDescuentos, nuevoProveedor, nuevaFechaVenc, codigo)
    
    def actualizarPrecioVenta(self, porcentaje, idCategoria):
        return self.producto_repository.actualizarPrecioVenta(porcentaje, idCategoria)

    def eliminarProducto(self, codigo):
        return self.producto_repository.eliminarProducto(codigo)
