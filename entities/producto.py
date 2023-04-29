class Producto:

    def __init__(self, codigo, nombre, precio, cant_stock, categoria, impuestos, descuentos, proveedor, fecha_venc):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantStock = cant_stock
        self.categoria = categoria
        self.impuestos = impuestos
        self.descuentos = descuentos
        self.proveedor = proveedor
        self.fechaVenc = fecha_venc

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_precio(self, precio):
        self.precio = precio

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

    def get_precio(self):
        return self.precio

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
















    