class Categoria:
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_porcentaje(self):
        return self.porcentaje

    def set_porcentaje(self, porcentaje):
        self.porcentaje = porcentaje

    def __init__(self, id, descripcion, porcentaje):
        self.id = id
        self.descripcion = descripcion
        self.porcentaje = porcentaje