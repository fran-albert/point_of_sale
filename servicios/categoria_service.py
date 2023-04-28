from repositories.categoria_repository import CategoriaRepository

class CategoriaService:
    def __init__(self):
        self.categoria_repository = CategoriaRepository()

    def obtenerCategorias(self):
        return self.categoria_repository.obtenerCategorias()
