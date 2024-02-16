from repositories.categoria_repository import CategoriaRepository

class CategoriaService:
    def __init__(self):
        self.categoria_repository = CategoriaRepository()

    def insertarCategoria(self, categoria):
        return self.categoria_repository.insertarCategoria(categoria)
    
    def obtenerCategorias(self):
        return self.categoria_repository.obtenerCategorias()

    def ObtenerCategoria(self, id):
        return self.categoria_repository.obtenerCategoria(id)

    def obtenerPorcentaje(self, descripcion):
        return self.categoria_repository.obtenerPorcentaje(descripcion)

    def actualizarCategoria(self, nuevaDescripcion, nuevoPorcentaje, descripcion):
        return self.categoria_repository.actualizarCategoria(nuevaDescripcion, nuevoPorcentaje, descripcion)
    
    def eliminarCategoria(self, descripcion):
        return self.categoria_repository.eliminarCategoria(descripcion)
