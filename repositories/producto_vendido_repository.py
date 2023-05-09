from mysqlx import Error
from entities.productos_vendidos import ProductosVendidos
from access.mysql_connection import MySQLConnection

class CategoriaRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarProdVendido(self, prod_vendido):
        sql = "INSERT INTO productos_vendidos(idTicket, prod_vendido, codigo, cant_vendida, precio_venta, precio_venta_total) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (prod_vendido.get_idTicket(), prod_vendido.get_prod_vendido(), prod_vendido.get_codigo(), prod_vendido.get_cant_vendida(), prod_vendido.get_precio_venta(), prod_vendido.get_precio_venta_total()))
            self.connection.commit()
        except Error as e:
            raise RuntimeError("Error al insertar el producto vendido", e)
        
    def obtenerProductosVendidos(self):
        prodVendidos = []
        query = "SELECT * FROM productos_vendidos"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    idProdVendido = row[0]
                    idTicket = row[1]
                    prod_vendido = row[2]
                    codigo = row[3]
                    cant_vendida = row[4]
                    precio_venta = row[5]
                    precio_venta_total = row[6]
                    nuevaProdVendido = ProductosVendidos(idProdVendido, idTicket, prod_vendido, codigo, cant_vendida, precio_venta, precio_venta_total)
                    prodVendidos.append(nuevaProdVendido)
            return prodVendidos
        except Error as e:
            raise RuntimeError("Error al obtener los productos vendidos", e)