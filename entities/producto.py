class Producto:

    def __init__(self, codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, impuestos, descuentos, proveedor, fecha_venc):
        self.codigo = codigo
        self.nombre = nombre
        self.precioCompra = precioCompra
        self.precioVenta = precioVenta
        self.cantStock = cant_stock
        self.categoria = categoria
        self.impuestos = impuestos
        self.descuentos = descuentos
        self.proveedor = proveedor
        self.fechaVenc = fecha_venc


    @staticmethod
    def calculoPrecioVenta(precioCompra, porcentaje):
        precioVenta = precioCompra * (1 + porcentaje / 100)
        return precioVenta

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_precioCompra(self, precioCompra):
        self.precioCompra = precioCompra

    def set_precioVenta(self, precioVenta):
        self.precioVenta = precioVenta

    def set_cantStock(self, cantStock):
        self.cantStock = cantStock

    def set_categoria(self, categoria):
        self.categoria = categoria

    def set_impuestos(self, impuestos):
        self.impuestos = impuestos

    def set_descuentos(self, descuentos):
        self.descuentos = descuentos

    def set_proveedor(self, proveedor):
        self.proveedor = proveedor

    def set_fechaVenc(self, fechaVenc):
        self.fechaVenc = fechaVenc


    def get_codigo(self):
        return self.codigo 
    
    def get_nombre(self):
        return self.nombre

    def get_precioCompra(self):
        return self.precioCompra
    
    def get_precioVenta(self):
        return self.precioVenta

    def get_cantStock(self):
        return self.cantStock
    
    def get_categoria(self):
        return self.categoria 
    
    def get_impuestos(self):
        return self.impuestos

    def get_descuentos(self):
        return self.impuestos

    def get_proveedor(self):
        return self.proveedor
    
    def get_fechaVenc(self):
        return self.fechaVenc
















    