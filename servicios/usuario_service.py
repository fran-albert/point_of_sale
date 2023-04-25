from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def validate_login(self, username, password):
        return self.usuario_repository.validate_login(username, password)
    
