import sys
from pathlib import Path
# Agrega la carpeta principal al sys.path
ruta_principal = str(Path(__file__).parent.parent.resolve())
if ruta_principal not in sys.path:
    sys.path.append(ruta_principal)
from PyQt5.QtWidgets import QApplication, QDateEdit, QTableWidget, QComboBox, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox
from PyQt5.QtCore import QDate
from servicios.producto_service import ProductoService
from servicios.categoria_service import CategoriaService
from entities.producto import Producto

# Crear una instancia de QApplication
app = QApplication([])
producto_service = ProductoService()
producto  = producto_service.obtenerProductos()
categoria_service = CategoriaService()

class AgregarProductoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Agregar Producto")

        layout = QVBoxLayout()

        self.codigo_label = QLabel("Código:")
        self.codigo_input = QLineEdit()
        layout.addWidget(self.codigo_label)
        layout.addWidget(self.codigo_input)

        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)

        self.precio_label = QLabel("Precio Compra:")
        self.precio_input = QLineEdit()
        layout.addWidget(self.precio_label)
        layout.addWidget(self.precio_input)

        self.cant_stock_label = QLabel("Cantidad en Stock:")
        self.cant_stock_input = QLineEdit()
        layout.addWidget(self.cant_stock_label)
        layout.addWidget(self.cant_stock_input)

        self.categoria_label = QLabel("Categoría:")
        self.categoria_selector = QComboBox()
        categorias = categoria_service.obtenerCategorias()
        for categoria in categorias:
            self.categoria_selector.addItem(categoria.descripcion, categoria.id)
        layout.addWidget(self.categoria_label)
        layout.addWidget(self.categoria_selector)

        self.impuestos_label = QLabel("Impuestos:")
        self.impuestos_input = QLineEdit()
        layout.addWidget(self.impuestos_label)
        layout.addWidget(self.impuestos_input)

        self.descuentos_label = QLabel("Descuentos:")
        self.descuentos_input = QLineEdit()
        layout.addWidget(self.descuentos_label)
        layout.addWidget(self.descuentos_input)

        self.proveedor_label = QLabel("Proveedor:")
        self.proveedor_input = QLineEdit()
        layout.addWidget(self.proveedor_label)
        layout.addWidget(self.proveedor_input)

        self.fecha_venc_label = QLabel("Fecha de Vencimiento:")
        self.fecha_venc_input = QDateEdit()
        layout.addWidget(self.fecha_venc_label)
        layout.addWidget(self.fecha_venc_input)

        self.buttons_layout = QHBoxLayout()
        self.agregar_button = QPushButton("Agregar")
        self.cancelar_button = QPushButton("Cancelar")
        self.buttons_layout.addWidget(self.agregar_button)
        self.buttons_layout.addWidget(self.cancelar_button)

        layout.addLayout(self.buttons_layout)
        self.setLayout(layout)

        self.agregar_button.clicked.connect(self.agregar_producto)
        self.cancelar_button.clicked.connect(self.reject)

    def agregar_producto(self):
        codigo = self.codigo_input.text().strip()
        nombre = self.nombre_input.text().strip()
        precioCompra = self.precio_input.text().strip()
        cant_stock = self.cant_stock_input.text().strip()
        categoria = self.categoria_selector.currentData()
        impuestos = self.impuestos_input.text().strip()
        descuentos = self.descuentos_input.text().strip()
        proveedor = self.proveedor_input.text().strip()
        fecha_venc = self.fecha_venc_input.date().toString("yyyy-MM-dd")

        if codigo and nombre and precioCompra and cant_stock and categoria and impuestos and descuentos and proveedor and fecha_venc:
            try:
                precioCompra = float(precioCompra)
                cant_stock = int(cant_stock)
                impuestos = float(impuestos)
                descuentos = float(descuentos)
                porcentaje = categoria_service.obtenerPorcentaje(categoria)
                precioVenta = Producto.calculoPrecioVenta(precioCompra, porcentaje)
                producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, impuestos, descuentos, proveedor, fecha_venc)
                producto_service.insertarProducto(producto)
                self.accept()
            except ValueError:
                QMessageBox.warning(self, "Error", "Por favor, ingrese valores válidos.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")


class EditarProductoDialog(QDialog):
    def __init__(self, producto, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Editar Producto")

        layout = QVBoxLayout()

        self.codigo_label = QLabel("Código:")
        self.codigo_input = QLineEdit(producto.codigo)
        layout.addWidget(self.codigo_label)
        layout.addWidget(self.codigo_input)

        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit(producto.nombre)
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)

        self.precio_label = QLabel("Precio Venta:")
        self.precio_input = QLineEdit(str(producto.precioVenta))
        layout.addWidget(self.precio_label)
        layout.addWidget(self.precio_input)

        self.cant_stock_label = QLabel("Cantidad en Stock:")
        self.cant_stock_input = QLineEdit(str(producto.cant_stock))
        layout.addWidget(self.cant_stock_label)
        layout.addWidget(self.cant_stock_input)

        self.categoria_label = QLabel("Categoría:")
        self.categoria_selector = QComboBox()
        # Aquí debes llenar el selector de categorías utilizando el método obtenerCategorias
        # y añadir cada categoría al selector.
        categorias = categoria_service.obtenerCategorias()
        for categoria in categorias:
            self.categoria_selector.addItem(categoria.descripcion, categoria.id)
        layout.addWidget(self.categoria_label)
        layout.addWidget(self.categoria_selector)

        self.impuestos_label = QLabel("Impuestos:")
        self.impuestos_input = QLineEdit(str(producto.impuestos))
        layout.addWidget(self.impuestos_label)
        layout.addWidget(self.impuestos_input)

        self.descuentos_label = QLabel("Descuentos:")
        self.descuentos_input = QLineEdit(str(producto.descuentos))
        layout.addWidget(self.descuentos_label)
        layout.addWidget(self.descuentos_input)

        self.proveedor_label = QLabel("Proveedor:")
        self.proveedor_input = QLineEdit(producto.proveedor)
        layout.addWidget(self.proveedor_label)
        layout.addWidget(self.proveedor_input)

        self.fecha_venc_label = QLabel("Fecha de Vencimiento:")
        self.fecha_venc_input = QDateEdit(QDate.fromString(producto.fecha_venc, "yyyy-MM-dd"))
        layout.addWidget(self.fecha_venc_label)
        layout.addWidget(self.fecha_venc_input)

        self.buttons_layout = QHBoxLayout()
        self.guardar_button = QPushButton("Guardar")
        self.cancelar_button = QPushButton("Cancelar")
        self.buttons_layout.addWidget(self.guardar_button)
        self.buttons_layout.addWidget(self.cancelar_button)

        layout.addLayout(self.buttons_layout)
        self.setLayout(layout)

        self.guardar_button.clicked.connect(self.guardar_producto)
        self.cancelar_button.clicked.connect(self.reject)

    def guardar_producto(self):
        nuevo_codigo = self.codigo_input.text().strip()
        nuevo_nombre = self.nombre_input.text().strip()
        nuevo_precio = self.precio_input.text().strip()
        nueva_cant_stock = self.cant_stock_input.text().strip()
        nueva_categoria = self.categoria_selector.currentData()  # Asegúrate de almacenar el ID o un objeto de categoría en lugar del texto, si es necesario
        nuevos_impuestos = self.impuestos_input.text().strip()
        nuevos_descuentos = self.descuentos_input.text().strip()
        nuevo_proveedor = self.proveedor_input.text().strip()
        nueva_fecha_venc = self.fecha_venc_input.date().toString("yyyy-MM-dd")

        if nuevo_codigo and nuevo_nombre and nuevo_precio and nueva_cant_stock and nueva_categoria and nuevos_impuestos and nuevos_descuentos and nuevo_proveedor and nueva_fecha_venc:
            try:
                nuevo_precio = float(nuevo_precio)
                nueva_cant_stock = int(nueva_cant_stock)
                nuevos_impuestos = float(nuevos_impuestos)
                nuevos_descuentos = float(nuevos_descuentos)
                # Asegúrate de usar el ID de la categoría o un objeto de categoría en lugar del texto, si es necesario
                self.nuevo_codigo = nuevo_codigo
                self.nuevo_nombre = nuevo_nombre
                self.nuevo_precio = nuevo_precio
                self.nueva_cant_stock = nueva_cant_stock
                self.nueva_categoria = nueva_categoria
                self.nuevos_impuestos = nuevos_impuestos
                self.nuevos_descuentos = nuevos_descuentos
                self.nuevo_proveedor = nuevo_proveedor
                self.nueva_fecha_venc = nueva_fecha_venc
                self.accept()
            except ValueError:
                QMessageBox.warning(self, "Error", "Por favor, ingrese valores válidos.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")




# Crear una instancia de QTableWidget con cuatro columnas y el número de filas igual a la longitud de la lista de datos
table = QTableWidget(len(producto), 10)

# Definir los encabezados de las columnas
table.setHorizontalHeaderLabels(["Nombre", "Código", "Precio Compra", "Precio Venta", "Cant Stock", "Categoría", "Impuestos", "Descuentos", "Proveedor", "Fecha Venc"])

def actualizar_tabla():
    # Obtén la lista actualizada de productos
    productos = producto_service.obtenerProductos()

    # Limpia la tabla antes de agregar nuevas filas
    table.setRowCount(0)

    # Establece el número de filas en la tabla según la longitud de la lista de productos
    table.setRowCount(len(productos))

    # Rellena la tabla con los productos actualizados
    for i, prod in enumerate(productos):
        item_nombre = QTableWidgetItem(prod.nombre)
        item_codigo = QTableWidgetItem(prod.codigo)
        item_precioCompra = QTableWidgetItem(str(prod.precioCompra))
        item_precioVenta = QTableWidgetItem(str(prod.precioVenta))
        item_cant_stock = QTableWidgetItem(str(prod.cantStock))
        item_categoria = QTableWidgetItem(prod.categoria)
        item_impuestos = QTableWidgetItem(str(prod.impuestos))
        item_descuentos = QTableWidgetItem(str(prod.descuentos))
        item_proveedor = QTableWidgetItem(prod.proveedor)
        item_fecha_venc = QTableWidgetItem(prod.fechaVenc.strftime("%Y-%m-%d"))

        table.setItem(i, 0, item_nombre)
        table.setItem(i, 1, item_codigo)
        table.setItem(i, 2, item_precioCompra)
        table.setItem(i, 3, item_precioVenta)
        table.setItem(i, 4, item_cant_stock)
        table.setItem(i, 5, item_categoria)
        table.setItem(i, 6, item_impuestos)
        table.setItem(i, 7, item_descuentos)
        table.setItem(i, 8, item_proveedor)
        table.setItem(i, 9, item_fecha_venc)

# Llama a actualizar_tabla() para llenar la tabla con los productos iniciales
actualizar_tabla()

def on_agregar_producto_clicked():
    dialog = AgregarProductoDialog()
    result = dialog.exec()

    if result == QDialog.Accepted:
            # Actualiza la tabla para mostrar la nueva categoría agregada
        actualizar_tabla()

# def on_edit_button_clicked():
#     # Obtén el botón que emitió la señal
#     button = app.sender()
#     # Obtiene el índice del elemento en la tabla
#     index = table.indexAt(button.pos())

#     # Obtén la descripción y el porcentaje de la categoría seleccionada
#     descripcion = table.item(index.row(), 0).text()
#     porcentaje = float(table.item(index.row(), 1).text())

#     # Muestra la ventana de edición y obtén el resultado
#     dialog = EditarCategoriaDialog(descripcion, porcentaje)
#     result = dialog.exec()

#     if result == QDialog.Accepted:
#         nueva_descripcion = dialog.nueva_descripcion
#         nuevo_porcentaje = dialog.nuevo_porcentaje

#         # Actualiza la categoría en la base de datos
#         categoria_service.actualizarCategoria(nueva_descripcion, nuevo_porcentaje, descripcion)

#         # Actualiza la tabla para mostrar los cambios
#         actualizar_tabla()

    # # En la función `actualizar_tabla`, conecta el botón "Editar" a `on_edit_button_clicked`
    # edit_button.clicked.connect(on_edit_button_clicked)

# def on_delete_button_clicked():
#     # Obtén el botón que emitió la señal
#     button = app.sender()
#     # Obtiene el índice del elemento en la tabla
#     index = table.indexAt(button.pos())

#     # Obtén la descripción de la categoría seleccionada
#     descripcion = table.item(index.row(), 0).text()

#     respuesta = QMessageBox.question(None, "Confirmación de eliminación", f"¿Está seguro de que desea eliminar la categoría {descripcion}?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#     if respuesta == QMessageBox.Yes:
#         # Aquí va el código para eliminar la categoría de la base de datos utilizando la descripción
#         categoria_service.eliminarCategoria(descripcion)

#         # Elimina la fila seleccionada de la tabla
#         table.removeRow(index.row())

# Agregar los elementos y botones a la tabla
# for i, categoria in enumerate(categorias):
#     item_descripcion = QTableWidgetItem(categoria.descripcion)
#     item_porcentaje = QTableWidgetItem(str(categoria.porcentaje))
#     table.setItem(i, 0, item_descripcion)
#     table.setItem(i, 1, item_porcentaje)

#     # Botón Editar
#     edit_button = QPushButton("Editar")
#     edit_button.clicked.connect(on_edit_button_clicked)
#     table.setCellWidget(i, 2, edit_button)

#     # Botón Eliminar
#     delete_button = QPushButton("Eliminar")
#     delete_button.clicked.connect(on_delete_button_clicked)
#     table.setCellWidget(i, 3, delete_button)

# Crear un botón Agregar Categoría
add_product_button = QPushButton("Agregar Producto")
add_product_button.clicked.connect(on_agregar_producto_clicked)

# Crear un layout vertical
layout = QVBoxLayout()

# Agregar la tabla y el botón al layout
layout.addWidget(table)
layout.addWidget(add_product_button)

# Crear un widget central y establecer el layout
central_widget = QWidget()
central_widget.setLayout(layout)

# Mostrar el widget en pantalla
central_widget.show()

# Ejecutar la aplicación
app.exec_()