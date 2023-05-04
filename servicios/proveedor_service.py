from repositories.proveedor_repository import ProveedorRepository

class ProveedorService:
    def __init__(self):
        self.proveedor_repository = ProveedorRepository()
    
    def insertarProveedor(self, proveedor):
        return self.proveedor_repository.insertarProveedor(proveedor)
    
    def obtenerProveedor(self):
        return self.proveedor_repository.obtenerProveedor()
    
    def actualizarProveedor(self, nuevoNombre, nuevaDireccion, nuevoCodPostal, nuevaCiudad, nuevaProvincia, nuevoTelefono, nuevoCorreo, nuevoComentario, nuevaCBU):
        return self.proveedor_repository.actualizarProveedor(nuevoNombre, nuevaDireccion, nuevoCodPostal, nuevaCiudad, nuevaProvincia, nuevoTelefono, nuevoCorreo, nuevoComentario, nuevaCBU)
    
    def eliminarProveedor(self, id):
        return self.proveedor_repository.eliminarProveedor(id)