from mysqlx import Error
from entities.orden_compra import OrdenCompra
from access.mysql_connection import MySQLConnection

class OrdenCompraRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarOrden(self, ordenCompra):
        sql = "INSERT INTO ordenes_compra(id_proveedor, precio_total_orden, fecha_recepcion, recibido) VALUES (%s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (ordenCompra.get_id_proveedor(), ordenCompra.get_precio_total_orden(), ordenCompra.get_fecha_recepcion(), ordenCompra.get_recibido()))
            self.connection.commit()
            last_inserted_id = cursor.lastrowid
            return last_inserted_id
        except Error as e:
            raise RuntimeError("Error al insertar la orden de compra", e)
    
    def obtenerOrden(self, idOrdenCompra):
        orden = None
        query = "SELECT * FROM ordenes_compra WHERE id = %s"
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
        
    def obtenerOrdenes(self, fecha_desde, fecha_hasta):
        ordenesCompra = []
        query = "SELECT * FROM ordenes_compra WHERE fecha_recepcion BETWEEN %s AND %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (fecha_desde, fecha_hasta))
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

    def actualizarOrden(self, idOrdenCompra, recibido):
        query = "UPDATE ordenes_compra SET recibido = %s WHERE id = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (recibido, idOrdenCompra))
                self.connection.commit()
        except Error as e:
            raise RuntimeError(f"Error al actualizar la orden de compra con el id {idOrdenCompra}", e)

