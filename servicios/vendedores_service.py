from repositories.vendedor_repository import VendedorRepository

class VendedorService:
    def __init__(self):
        self.vendedor_repository = VendedorRepository()
    
    def insertarVendedor(self, vendedor):
        return self.vendedor_repository.insertarVendedor(vendedor)
    
    def obtenerVendedores(self):
        return self.vendedor_repository.obtenerVendedores()
    
    def actualizarVendedor(self, nuevoDNI, nuevoNombre, nuevoApellido, nuevoTelefono, nuevoCorreo, nuevaFechaNac, fecha_alta, id):
        return self.vendedor_repository.actualizarVendedor(nuevoDNI, nuevoNombre, nuevoApellido, nuevoTelefono, nuevoCorreo, nuevaFechaNac, fecha_alta, id)
    
    def eliminarVendedor(self, id):
        return self.vendedor_repository.eliminarVendedor(id)