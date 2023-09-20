class Vendedor:
    def __init__(self, dni, nombre, apellido, telefono, correo_electronico, fecha_nacimiento, fecha_alta, admin, id= None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_alta = fecha_alta
        self.admin = admin
        self.id = id

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_correo_electronico(self):
        return self.correo_electronico

    def set_correo_electronico(self, correo_electronico):
        self.correo_electronico = correo_electronico

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def get_fecha_alta(self):
        return self.fecha_alta

    def set_fecha_alta(self, fecha_alta):
        self.fecha_alta = fecha_alta

    def get_admin(self):
        return self.admin

    def set_admin(self, admin):
        self.admin = admin

                