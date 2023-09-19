class Vendedor:
    def __init__(self, dni, nombre, apellido, telefono, correo, fecha_nac, fecha_alta, admin, id= None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.fecha_nac = fecha_nac
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

    def get_correo(self):
        return self.correo

    def set_correo(self, correo):
        self.correo = correo

    def get_fecha_nac(self):
        return self.fecha_nac

    def set_fecha_nac(self, fecha_nac):
        self.fecha_nac = fecha_nac

    def get_fecha_alta(self):
        return self.fecha_alta

    def set_fecha_alta(self, fecha_alta):
        self.fecha_alta = fecha_alta

    def get_admin(self):
        return self.admin

    def set_admin(self, admin):
        self.admin = admin

                