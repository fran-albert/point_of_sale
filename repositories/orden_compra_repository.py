from mysqlx import Error
from entities.orden_compra import OrdenCompra
from access.mysql_connection import MySQLConnection

class OrdenCompraRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarOrden(self, ordenCompra):
        sql = "INSERT INTO orden_compra(idProveedor, precioTotalOrden, fechaRecepcion, recibido) VALUES  %s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (ordenCompra.get_idProveedor(), ordenCompra.get_precioTotalOrden(), ordenCompra.get_fechaRecepcion(), ordenCompra.get_recibido()))
            self.connection.commit()
        except Error as e:
            raise RuntimeError("Error al insertar la orden de compra", e)

    #OBTENER 1 ORDEN CON EL IDORDENCOMPRA

    def obtenerOrdenes(self):
        ordenesCompra = []
        query = "SELECT * FROM orden_compra"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    id = row[0]
                    idProovedor = row[1]
                    precioTotalOrden = row[2]
                    fechaRecepcion = row[3]
                    recibido = row[4]
                    nuevaOrdenCompra = OrdenCompra(id, idProovedor, precioTotalOrden, fechaRecepcion, recibido)
                    ordenesCompra.append(nuevaOrdenCompra)
            return ordenesCompra
        except Error as e:
            raise RuntimeError("Error al obtener las órdenes de compra", e)

