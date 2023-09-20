from repositories.vendedor_repository import VendedorRepository

class VendedorService:
    def __init__(self):
        self.vendedor_repository = VendedorRepository()
    
    def insertarVendedor(self, vendedor):
        return self.vendedor_repository.insertarVendedor(vendedor)
    
    def obtenerVendedores(self):
        return self.vendedor_repository.obtenerVendedores()
    
    def validarLogin(self, nombre, dni):
        return self.vendedor_repository.validarLogin(nombre, dni)
    
    def actualizarVendedor(self, nuevoDNI, nuevoNombre, nuevoApellido, nuevoTelefono, nuevoCorreo, nuevafecha_nac, fecha_alta, admin, id):
        return self.vendedor_repository.actualizarVendedor(nuevoDNI, nuevoNombre, nuevoApellido, nuevoTelefono, nuevoCorreo, nuevafecha_nac, fecha_alta, admin, id)
    
    def eliminarVendedor(self, id):
        return self.vendedor_repository.eliminarVendedor(id)
    
    def obtenerNombre(self, dni):
        usuarios = self.vendedor_repository.obtenerVendedores()
        nombre = ""
        for usuario in usuarios:
            if str(usuario.dni) == dni:
                nombre = usuario.nombre
                return nombre
        if (nombre == ""):
            raise ValueError("Error en el inicio de sesión")
    
    def obtenerRol(self, dni):
        return self.vendedor_repository.obtenerRol(dni)