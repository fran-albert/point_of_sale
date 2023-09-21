class OrdenCompra:
    def __init__(self, id_proveedor, precio_total_orden, fecha_recepcion, recibido, id = None):
        self.id = id
        self.id_proveedor = id_proveedor
        self.precio_total_orden = precio_total_orden
        self.fecha_recepcion = fecha_recepcion
        self.recibido = recibido

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_id_proveedor(self):
        return self.id_proveedor

    def set_id_proveedor(self, id_proveedor):
        self.id_proveedor = id_proveedor

    def get_precio_total_orden(self):
        return self.precio_total_orden

    def set_precio_total_orden(self, precio_total_orden):
        self.precio_total_orden = precio_total_orden

    def get_fecha_recepcion(self):
        return self.fecha_recepcion

    def set_fecha_recepcion(self, fecha_recepcion):
        self.fecha_recepcion = fecha_recepcion

    def get_recibido(self):
        return self.recibido

    def set_recibido(self, recibido):
        self.recibido = recibido



        


















    