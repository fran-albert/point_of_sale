from mysqlx import Error
from entities.orden_compra import OrdenCompra
from access.mysql_connection import MySQLConnection

class OrdenCompraRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarOrden(self, ordenCompra):
        sql = "INSERT INTO orden_compra(id, idProveedor, precioCompra, precioTotal, fechaRecepcion, recibido) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (ordenCompra.get_id(), ordenCompra.get_idProveedor(), ordenCompra.get_precioCompra(), ordenCompra.get_precioTotal(), ordenCompra.get_fechaRecepcion(), ordenCompra.get_recibido()))
            self.connection.commit()
        except Error as e:
            raise RuntimeError("Error al insertar la orden de compra", e)

    def obtenerProductosVendidos(self, id):
        ordenesCompra = []
        query = "SELECT * FROM orden_compra WHERE id = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (id,))
                for row in cursor.fetchall():
                    id = row[0]
                    idProovedor = row[1]
                    precioCompra = row[2]
                    precioTotal = row[3]
                    fechaRecepcion = row[4]
                    recibido = row[5]
                    nuevaOrdenCompra = OrdenCompra(id, idProovedor, precioCompra, precioTotal, fechaRecepcion, recibido)
                    ordenesCompra.append(nuevaOrdenCompra)
            return ordenesCompra
        except Error as e:
            raise RuntimeError("Error al obtener las órdenes de compra", e)

