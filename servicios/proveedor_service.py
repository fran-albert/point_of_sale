from repositories.proveedor_repository import ProveedorRepository

class ProveedorService:
    def __init__(self):
        self.proveedor_repository = ProveedorRepository()
    
    def insertarProveedor(self, proveedor):
        return self.proveedor_repository.insertarProveedor(proveedor)
    
    def obtenerProveedores(self):
        return self.proveedor_repository.obtenerProveedores()
    
    def actualizarProeedor(self, nuevoNombre, nuevaDireccion, nuevoCodPostal, nuevaCiudad, nuevaProvincia, nuevoTelefono, nuevoCorreo, nuevoComentario, nuevaCBU):
        return self.proveedor_repository.actualizarProveedor(nuevoNombre, nuevaDireccion, nuevoCodPostal, nuevaCiudad, nuevaProvincia, nuevoTelefono, nuevoCorreo, nuevoComentario, nuevaCBU)
    
    def eliminarProveedor(self, id):
        return self.proveedor_repository.eliminarProveedor(id)