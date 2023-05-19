class Vendedor:
    def __init__(self, dni, nombre, apellido, telefono, correo, fechaNac, fechaAlta):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.fechaNac = fechaNac
        self.fechaAlta = fechaAlta

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

    def get_fechaNac(self):
        return self.fechaNac

    def set_fechaNac(self, fechaNac):
        self.fechaNac = fechaNac

    def get_fechaAlta(self):
        return self.fechaAlta

    def set_fechaAlta(self, fechaAlta):
        self.fechaAlta = fechaAlta

                