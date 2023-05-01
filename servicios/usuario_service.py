from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def validate_login(self, username, password):
        return self.usuario_repository.validate_login(username, password)
    
    def get_username(self, login_username, login_password):
        if self.validate_login(login_username, login_password):
            usuarios = self.usuario_repository.obtenerUsuario()
            for usuario in usuarios:
                if usuario.username == login_username:
                    return usuario.username
        else:
            raise ValueError("Error en el inicio de sesión")

