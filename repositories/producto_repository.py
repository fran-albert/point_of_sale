from mysqlx import Error
from entities.producto import Producto
from access.mysql_connection import MySQLConnection

class ProductoRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarProducto(self, producto):
        sql = "INSERT INTO productos(Codigo, Nombre, Precio, CantStock, Categoria, Impuestos, Descuentos, Proveedor, FechaVenc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (producto.get_codigo(), producto.get_nombre(), producto.get_precio(), producto.get_cantStock(), producto.get_categoria(), producto.get_impuestos(), producto.get_descuentos(), producto.get_proveedor(), producto.get_fechaVenc()))
            self.connection.commit()
        except Error as e:
            raise RuntimeError("Error al insertar el nuevo producto", e)

            
    def obtenerProductos(self):
        productos = []
        query = "SELECT * FROM productos"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    codigo = row[0]
                    nombre = row[1]
                    precio = row[2]
                    cant_stock = row[3]
                    categoria = row[4]
                    impuestos = row[5]
                    descuentos = row[6]
                    proveedor = row[7]
                    fecha_venc = row[8]

                    nuevo_producto = Producto(codigo, nombre, precio, cant_stock, categoria, impuestos, descuentos, proveedor, fecha_venc)
                    productos.append(nuevo_producto)
            return productos
        except Error as e:
            raise RuntimeError("Error al obtener los productos", e)


    
    def actualizarProducto(self, nuevoCodigo, nuevoNombre, nuevoPrecio, nuevaCantStock, nuevaCategoria, nuevosImpuestos, nuevosDescuentos, nuevoProveedor, nuevaFechaVenc, codigo):
        query = "UPDATE productos SET Codigo = %s, Nombre = %s, Precio = %s, CantStock = %s, Categoria = %s, Impuestos = %s, Descuentos = %s, Proveedor = %s, FechaVenc = %s WHERE Codigo = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (nuevoCodigo, nuevoNombre, nuevoPrecio, nuevaCantStock, nuevaCategoria, nuevosImpuestos, nuevosDescuentos, nuevoProveedor, nuevaFechaVenc, codigo))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al actualizar el producto {codigo}") from e



    def eliminarProducto(self, codigo):
        query = "DELETE FROM productos WHERE Codigo = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (codigo,))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al eliminar el producto {codigo}") from e
