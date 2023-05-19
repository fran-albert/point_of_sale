from mysqlx import Error
from entities.orden_compra import OrdenCompra
from access.mysql_connection import MySQLConnection

class OrdenCompraRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarOrden(self, ordenCompra):
        sql = "INSERT INTO orden_compra(idProveedor, precioTotalOrden, fechaRecepcion, recibido) VALUES (%s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (ordenCompra.get_idProveedor(), ordenCompra.get_precioTotalOrden(), ordenCompra.get_fechaRecepcion(), ordenCompra.get_recibido()))
            self.connection.commit()
            last_inserted_id = cursor.lastrowid
            return last_inserted_id
        except Error as e:
            raise RuntimeError("Error al insertar la orden de compra", e)
    
    #OBTENER 1 ORDEN CON EL IDORDENCOMPRA PARA VER EN HISTORIAL DE ORDENES Y SELECCIONAR UNA ORDEN Y MODIFICAR EL RECIBIDO
    def obtenerOrden(self, idOrdenCompra):
        orden = None
        query = "SELECT * FROM orden_compra WHERE idOrdenCompra = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (idOrdenCompra,))
                row = cursor.fetchone()
                if row:
                    idOrdenCompra = row[0]
                    idProveedor = row[1]
                    precioTotalOrden = row[2]
                    fechaRecepcion = row[3]
                    recibido = row[4]
                    orden = OrdenCompra(idOrdenCompra, idProveedor, precioTotalOrden, fechaRecepcion, recibido)
            return orden
        except Error as e:
            raise RuntimeError(f"Error al obtener la orden de compra con el id {idOrdenCompra}", e)
        
    def obtenerOrdenes(self):
        ordenesCompra = []
        query = "SELECT * FROM orden_compra"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    id = row[0]
                    idProveedor = row[1]
                    precioTotalOrden = row[2]
                    fechaRecepcion = row[3]
                    recibido = row[4]
                    nuevaOrdenCompra = OrdenCompra(idProveedor, precioTotalOrden, fechaRecepcion, recibido, id)
                    ordenesCompra.append(nuevaOrdenCompra)
            return ordenesCompra
        except Error as e:
            raise RuntimeError("Error al obtener las órdenes de compra", e)

