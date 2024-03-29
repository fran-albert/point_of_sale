from repositories.producto_repository import ProductoRepository

class ProductoService:
    def __init__(self):
        self.producto_repository = ProductoRepository()

    def insertarProducto(self, producto):
        return self.producto_repository.insertarProducto(producto)
    
    def actualizarProducto(self, nuevoCodigo, nuevoNombre, nuevoPrecioCompra, nuevoPrecioVenta, nuevaCantStock, nuevaCategoria, nuevoProveedor, codigo):
        return self.producto_repository.actualizarProducto(nuevoCodigo, nuevoNombre, nuevoPrecioCompra, nuevoPrecioVenta, nuevaCantStock, nuevaCategoria, nuevoProveedor, codigo)
    
    def eliminarProducto(self, codigo):
        return self.producto_repository.eliminarProducto(codigo)
    
    def obtenerProductos(self):
        return self.producto_repository.obtenerProductos()
    
    def obtenerProducto(self, codigo):
        return self.producto_repository.obtenerProducto(codigo)
    
    def obtenerProductoPorProveedor(self, proveedor_id):
        return self.producto_repository.obtenerProductoPorProveedor(proveedor_id)
    
    def obtenerProductoPorNombre(self, nombre):
        return self.producto_repository.obtenerProductoPorNombre(nombre)
    
    def obtenerProductosStockMinimo(self):
        return self.producto_repository.obtenerProductosStockMinimo()
    
    def actualizarStock(self, codigo, cantidadVendida):
        return self.producto_repository.actualizarStock(codigo, cantidadVendida)
    
    def actualizarStockOrdenCompra(self, codigo, cantidadPedida):
        return self.producto_repository.actualizarStockOrdenCompra(codigo, cantidadPedida)
    
    def actualizarPrecioVenta(self, porcentaje, idCategoria):
        return self.producto_repository.actualizarPrecioVenta(porcentaje, idCategoria)
    
    def existeProductosConCategoria(self, idCategoria):
        return self.producto_repository.ExisteProductosConCategoria(idCategoria)