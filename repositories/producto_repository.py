from mysqlx import Error
from entities.producto import Producto
from access.mysql_connection import MySQLConnection

class ProductoRepository:
    def __init__(self):
        self.connection = MySQLConnection.get_connection()

    def insertarProducto(self, producto):
        sql = "INSERT INTO productos(Codigo, Nombre, PrecioCompra, PrecioVenta, CantStock, Categoria, Impuestos, Descuentos, Proveedor, FechaVenc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (producto.get_codigo(), producto.get_nombre(), producto.get_precioCompra(), producto.get_precioVenta(), producto.get_cantStock(), producto.get_categoria(), producto.get_impuestos(), producto.get_descuentos(), producto.get_proveedor(), producto.get_fechaVenc()))
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
                    impuestos = row[6]
                    descuentos = row[7]
                    proveedor = row[8]
                    fecha_venc = row[9]

                    nuevo_producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, impuestos, descuentos, proveedor, fecha_venc)
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
                    impuestos = row[6]
                    descuentos = row[7]
                    proveedor = row[8]
                    fecha_venc = row[9]

                    producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, impuestos, descuentos, proveedor, fecha_venc)
            return producto
        except Error as e:
            raise RuntimeError(f"Error al obtener el producto con el código {codigo}", e)
        
    def obtenerProductoPorProveedor(self, proveedor_id):
        productos = []
        query = "SELECT * FROM productos WHERE proveedor = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (proveedor_id,))
                row = cursor.fetchone()
                if row:
                    codigo = row[0]
                    nombre = row[1]
                    precioCompra = row[2]
                    precioVenta = row[3]
                    cant_stock = row[4]
                    categoria = row[5]
                    impuestos = row[6]
                    descuentos = row[7]
                    proveedor = row[8]
                    fecha_venc = row[9]
                    producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, impuestos, descuentos, proveedor, fecha_venc)
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
                    impuestos = row[6]
                    descuentos = row[7]
                    proveedor = row[8]
                    fecha_venc = row[9]

                    producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, impuestos, descuentos, proveedor, fecha_venc)
            return producto
        except Error as e:
            raise RuntimeError(f"Error al obtener el producto con el nombre {nombre}", e)



    def actualizarProducto(self, nuevoCodigo, nuevoNombre, nuevoPrecioCompra, nuevoPrecioVenta, nuevaCantStock, nuevaCategoria, nuevosImpuestos, nuevosDescuentos, nuevoProveedor, nuevaFechaVenc, codigo):
        query = "UPDATE productos SET Codigo = %s, Nombre = %s, PrecioCompra = %s, PrecioVenta = %s, CantStock = %s, Categoria = %s, Impuestos = %s, Descuentos = %s, Proveedor = %s, FechaVenc = %s WHERE Codigo = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (nuevoCodigo, nuevoNombre, nuevoPrecioCompra, nuevoPrecioVenta, nuevaCantStock, nuevaCategoria, nuevosImpuestos, nuevosDescuentos, nuevoProveedor, nuevaFechaVenc, codigo))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al actualizar el producto {codigo}") from e

    # Metodo para actualizar el precio de venta cuando cambia el porcentaje de una categoria asociada a productos
    def actualizarPrecioVenta(self, porcentaje, idCategoria):
        query = "UPDATE productos SET PrecioVenta = PrecioCompra * (1 + %s/100) WHERE Categoria = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (porcentaje, idCategoria))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al actualizar el precio de venta de los productos asociados a la categoria.") from e

    def actualizarStock(self, codigo, cantidadVendida):
        query = "UPDATE productos SET CantStock = CantStock - %s WHERE Codigo = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (cantidadVendida, codigo))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al actualizar el stock del producto {codigo}") from e

    def eliminarProducto(self, codigo):
        query = "DELETE FROM productos WHERE Codigo = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (codigo,))
                self.connection.commit()
        except Exception as e:
            raise RuntimeError(f"Error al eliminar el producto {codigo}") from e
        
    def ExisteProductosConCategoria(self, codigo):
        query = "SELECT COUNT(*) FROM productos WHERE categoria = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (codigo,))
                result = cursor.fetchone()
                return result[0]
        except Exception as e:
            raise RuntimeError(f"Error al eliminar la categoria {codigo} ya que tiene productos asociados") from e    
