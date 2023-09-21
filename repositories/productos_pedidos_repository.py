from mysqlx import Error
from entities.productos_pedidos import ProductosPedidos
from access.mysql_connection import MySQLConnection

class ProductoPedidoRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarProdPedido(self, prod_pedido):
        sql = "INSERT INTO productos_pedidos(id_orden_compra, producto_pedido, codigo, cantidad_pedida, precio_compra, precio_total) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (prod_pedido.get_id_orden_compra(), prod_pedido.get_producto_pedido(), prod_pedido.get_codigo(), prod_pedido.get_cantidad_pedida(), prod_pedido.get_precio_compra(), prod_pedido.get_precio_total()))
            self.connection.commit()
        except Error as e:
            raise RuntimeError("Error al insertar el producto pedido", e)

    def obtenerProductosPedidos(self, idOrdenCompra):
        prodPedidos = []
        query = "SELECT * FROM productos_pedidos WHERE idOrdenCompra = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (idOrdenCompra,))
                for row in cursor.fetchall():
                    idProdPedido = row[0]
                    idOrdenCompra = row[1]
                    prod_pedido = row[2]
                    codigo = row[3]
                    cant_pedida = row[4]
                    precio_compra = row[5]
                    precio_total = row[6]
                    nuevoProdPedido = ProductosPedidos(idProdPedido, idOrdenCompra, prod_pedido, codigo, cant_pedida, precio_compra, precio_total)
                    prodPedidos.append(nuevoProdPedido)
            return prodPedidos
        except Error as e:
            raise RuntimeError("Error al obtener los productos pedidos", e)

