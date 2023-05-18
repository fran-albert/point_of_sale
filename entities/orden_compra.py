class OrdenCompra:
    def __init__(self, idProveedor, precioTotalOrden, fechaRecepcion, recibido, idOrdenCompra = None):
        self.idOrdenCompra = idOrdenCompra
        self.idProveedor = idProveedor
        self.precioTotalOrden = precioTotalOrden
        self.fechaRecepcion = fechaRecepcion
        self.recibido = recibido

    def get_idOrdenCompra(self):
        return self.idOrdenCompra

    def set_idOrdenCompra(self, idOrdenCompra):
        self.idOrdenCompra = idOrdenCompra

    def get_idProveedor(self):
        return self.idProveedor

    def set_idProveedor(self, idProveedor):
        self.idProveedor = idProveedor

    def get_precioTotalOrden(self):
        return self.precioTotalOrden

    def set_precioTotalOrden(self, precioTotalOrden):
        self.precioTotalOrden = precioTotalOrden

    def get_fechaRecepcion(self):
        return self.fechaRecepcion

    def set_fechaRecepcion(self, fechaRecepcion):
        self.fechaRecepcion = fechaRecepcion

    def get_recibido(self):
        return self.recibido

    def set_recibido(self, recibido):
        self.recibido = recibido



        


















    