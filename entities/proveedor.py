class Proveedor:
    def __init__(self, id, nombre, direccion, cod_postal, ciudad, provincia, telefono, correo_electronico, comentario, cuenta_bancaria, fecha_alta):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.cod_postal = cod_postal
        self.ciudad = ciudad
        self.provincia = provincia
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.comentario = comentario
        self.cuenta_bancaria = cuenta_bancaria
        self.fecha_alta = fecha_alta

    def set_id(self, id):
        self.id = id

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_cod_postal(self, cod_postal):
        self.cod_postal = cod_postal

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad

    def set_provincia(self, provincia):
        self.provincia = provincia

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_correo_electronico(self, correo_electronico):
        self.correo_electronico = correo_electronico

    def set_comentario(self, comentario):
        self.comentario = comentario

    def set_cuenta_bancaria(self, cuenta_bancaria):
        self.cuenta_bancaria = cuenta_bancaria

    def set_fecha_alta(self, fecha_alta):
        self.fecha_alta = fecha_alta

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_direccion(self):
        return self.direccion

    def get_cod_postal(self):
        return self.cod_postal

    def get_ciudad(self):
        return self.ciudad

    def get_provincia(self):
        return self.provincia

    def get_telefono(self):
        return self.telefono

    def get_correo_electronico(self):
        return self.correo_electronico

    def get_comentario(self):
        return self.comentario

    def get_cuenta_bancaria(self):
        return self.cuenta_bancaria

    def get_fecha_alta(self):
        return self.fecha_alta