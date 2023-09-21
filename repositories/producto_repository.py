from mysqlx import Error
from entities.producto import Producto
from access.mysql_connection import MySQLConnection

class ProductoRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarProducto(self, producto):
        sql = "INSERT INTO productos(codigo, nombre, precio_compra, precio_venta, cantidad_stock, id_categoria, id_proveedor) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (producto.get_codigo(), producto.get_nombre(), producto.get_precioCompra(), producto.get_precioVenta(), producto.get_cantStock(), producto.get_categoria(), producto.get_proveedor()))
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
                    precioCompra = row[2]
                    precioVenta = row[3]
                    cant_stock = row[4]
                    categoria = row[5]
                    proveedor = row[6]
                    nuevo_producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, proveedor)
                    productos.append(nuevo_producto)
            return productos
        except Error as e:
            raise RuntimeError("Error al obtener los productos", e)

    def obtenerProducto(self, codigo):
        producto = None
        query = "SELECT * FROM productos WHERE codigo = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (codigo,))
                row = cursor.fetchone()
                if row:
                    codigo = row[0]
                    nombre = row[1]
                    precioCompra = row[2]
                    precioVenta = row[3]
                    cant_stock = row[4]
                    categoria = row[5]
                    proveedor = row[6]
                    producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, proveedor)
            return producto
        except Error as e:
            raise RuntimeError(f"Error al obtener el producto con el código {codigo}", e)
        
    def obtenerProductoPorProveedor(self, proveedor_id):
        productos = []
        query = "SELECT * FROM productos WHERE id_proveedor = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (proveedor_id,))
                rows = cursor.fetchall()  
                for row in rows: 
                    codigo = row[0]
                    nombre = row[1]
                    precioCompra = row[2]
                    precioVenta = row[3]
                    cant_stock = row[4]
                    categoria = row[5]
                    proveedor = row[6]
                    producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, proveedor)
                    productos.append(producto)
            return productos
        except Error as e:
            raise RuntimeError(f"Error al obtener los productos del proveedor con el ID {proveedor_id}", e)
    
    def obtenerProductoPorNombre(self, nombre):
        producto = None
        query = "SELECT * FROM productos WHERE nombre = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (nombre,))
                row = cursor.fetchone()
                if row:
                    codigo = row[0]
                    nombre = row[1]
                    precioCompra = row[2]
                    precioVenta = row[3]
                    cant_stock = row[4]
                    categoria = row[5]
                    proveedor = row[6]
                    producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, proveedor)
            return producto
        except Error as e:
            raise RuntimeError(f"Error al obtener el producto con el nombre {nombre}", e)

    def actualizarProducto(self, nuevoCodigo, nuevoNombre, nuevoPrecioCompra, nuevoPrecioVenta, nuevaCantStock, nuevaCategoria, nuevoProveedor, codigo):
        query = "UPDATE productos SET codigo = %s, nombre = %s, precio_compra = %s, precio_venta = %s, cantidad_stock = %s, id_categoria = %s, id_proveedor = %s WHERE Codigo = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (nuevoCodigo, nuevoNombre, nuevoPrecioCompra, nuevoPrecioVenta, nuevaCantStock, nuevaCategoria, nuevoProveedor, codigo))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al actualizar el producto {codigo}") from e

    def actualizarPrecioVenta(self, porcentaje, idCategoria):
        query = "UPDATE productos SET precio_venta = precio_compra * (1 + %s/100) WHERE id_categoria = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (porcentaje, idCategoria))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al actualizar el precio de venta de los productos asociados a la categoria.") from e

    def actualizarStock(self, codigo, cantidadVendida):
        query = "UPDATE productos SET cantidad_stock = cantidad_stock - %s WHERE codigo = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (cantidadVendida, codigo))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al actualizar el stock del producto {codigo}") from e

    def eliminarProducto(self, codigo):
        query = "DELETE FROM productos WHERE codigo = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (codigo,))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al eliminar el producto {codigo}") from e
        
    def ExisteProductosConCategoria(self, codigo):
        query = "SELECT COUNT(*) FROM productos WHERE id_categoria = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (codigo,))
                result = cursor.fetchone()
                return result[0]
        except Exception as e:
            raise RuntimeError(f"Error al eliminar la categoria {codigo} ya que tiene productos asociados") from e    
