from repositories.vendedor_repository import VendedorRepository

class VendedorService:
    def __init__(self):
        self.vendedor_repository = VendedorRepository()
    
    def insertarVendedor(self, vendedor):
        return self.vendedor_repository.insertarVendedor(vendedor)
    
    def obtenerVendedores(self):
        return self.vendedor_repository.obtenerVendedores()
    
    def validate_login(self, nombre, dni):
        return self.vendedor_repository.validate_login(nombre, dni)
    
    def actualizarVendedor(self, nuevoDNI, nuevoNombre, nuevoApellido, nuevoTelefono, nuevoCorreo, nuevafecha_nac, fecha_alta, id):
        return self.vendedor_repository.actualizarVendedor(nuevoDNI, nuevoNombre, nuevoApellido, nuevoTelefono, nuevoCorreo, nuevafecha_nac, fecha_alta, id)
    
    def eliminarVendedor(self, id):
        return self.vendedor_repository.eliminarVendedor(id)
    
    def get_username(self, login_username, login_password):
        if self.validate_login(login_username, login_password):
            usuarios = self.vendedor_repository.obtenerVendedores()
            for usuario in usuarios:
                if usuario.nombre == login_username:
                    return usuario.nombre
        else:
            raise ValueError("Error en el inicio de sesión")