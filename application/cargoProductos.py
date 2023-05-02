import sys
from pathlib import Path
# Agrega la carpeta principal al sys.path
ruta_principal = str(Path(__file__).parent.parent.resolve())
if ruta_principal not in sys.path:
    sys.path.append(ruta_principal)
from PyQt5.QtWidgets import QMainWindow, QFrame, QHeaderView, QScrollArea, QSizePolicy, QDateEdit, QTableWidget, QComboBox, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox
from PyQt5.QtCore import Qt
from servicios.producto_service import ProductoService
from servicios.categoria_service import CategoriaService
from entities.producto import Producto



class EditarProductoDialog(QDialog):
    def __init__(self, producto, categorias, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Editar Producto")

        self.producto = producto
        self.categorias = categorias
        layout = QVBoxLayout()

        self.precioCompra_label = QLabel("Precio de compra:")
        self.precioCompra_input = QLineEdit(str(producto.precioCompra))
        layout.addWidget(self.precioCompra_label)
        layout.addWidget(self.precioCompra_input)

        self.stock_label = QLabel("Stock:")
        self.stock_input = QLineEdit(str(producto.cantStock))
        layout.addWidget(self.stock_label)
        layout.addWidget(self.stock_input)

        self.categoria_label = QLabel("Categoría:")
        self.categoria_combo = QComboBox()
        for categoria in self.categorias:
            self.categoria_combo.addItem(categoria.descripcion, categoria.id)
        index = self.categoria_combo.findData(producto.categoria)
        self.categoria_combo.setCurrentIndex(index)
        layout.addWidget(self.categoria_label)
        layout.addWidget(self.categoria_combo)

        self.impuestos_label = QLabel("Impuestos:")
        self.impuestos_input = QLineEdit(str(producto.impuestos))
        layout.addWidget(self.impuestos_label)
        layout.addWidget(self.impuestos_input)

        self.buttons_layout = QHBoxLayout()
        self.guardar_button = QPushButton("Guardar")
        self.cancelar_button = QPushButton("Cancelar")
        self.buttons_layout.addWidget(self.guardar_button)
        self.buttons_layout.addWidget(self.cancelar_button)

        layout.addLayout(self.buttons_layout)
        self.setLayout(layout)

        self.guardar_button.clicked.connect(self.guardar_producto)
        self.cancelar_button.clicked.connect(self.reject)

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
        nuevo_precioCompra = self.precioCompra_input.text().strip()
        nuevo_stock = self.stock_input.text().strip()
        nueva_categoria = self.categoria_combo.currentData()
        nuevos_impuestos = self.impuestos_input.text().strip()

        if nuevo_precioCompra and nuevo_stock and nuevos_impuestos:
            try:
                nuevo_precioCompra = float(nuevo_precioCompra)
                nuevo_stock = int(nuevo_stock)
                nuevos_impuestos = float(nuevos_impuestos)
                self.producto.precioCompra = nuevo_precioCompra
                self.producto.cantStock = nuevo_stock
                self.producto.categoria = nueva_categoria
                self.producto.impuestos = nuevos_impuestos
                self.accept()
            except ValueError:
                QMessageBox.warning(self, "Error", "Por favor, ingrese valores válidos.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")

class AgregarProductoDialog(QDialog):
    def __init__(self, producto_service, categoria_service, parent=None):
        super().__init__(parent)

        self.producto_service = producto_service
        self.categoria_service = categoria_service

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
        categorias = self.categoria_service.obtenerCategorias()
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
                porcentaje = self.categoria_service.obtenerPorcentaje(categoria)
                precioVenta = Producto.calculoPrecioVenta(precioCompra, porcentaje)
                producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, impuestos, descuentos, proveedor, fecha_venc)
                self.producto_service.insertarProducto(producto)
                self.accept()
            except ValueError:
                QMessageBox.warning(self, "Error", "Por favor, ingrese valores válidos.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")

class ABMProductosWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)    
        # Crear una instancia de QApplication
        self.app = app
        self.producto_service = ProductoService()
        self.categoria_service = CategoriaService()
        self.producto  = self.producto_service.obtenerProductos()
        # En el método __init__ de la clase ABMProductosWindow
        self.categorias = self.categoria_service.obtenerCategorias()

        # Crear un diccionario que mapee los IDs de las categorías a sus descripciones
        self.categoria_descripcion_map = {categoria.id: categoria.descripcion for categoria in self.categorias}


        # Crear una instancia de QTableWidget con cuatro columnas y el número de filas igual a la longitud de la lista de datos
        self.table = QTableWidget(len(self.producto), 12)

        # Definir los encabezados de las columnas
        self.table.setHorizontalHeaderLabels(["Nombre", "Código", "Precio Compra", "Precio Venta", "Cant Stock", "Categoría", "Impuestos", "Descuentos", "Proveedor", "Fecha Venc", "", ""])

        # Rellena la tabla con los productos actualizados
        for i, prod in enumerate(self.producto):
            item_nombre = QTableWidgetItem(prod.nombre)
            item_codigo = QTableWidgetItem(prod.codigo)
            item_precioCompra = QTableWidgetItem(str(prod.precioCompra))
            item_precioVenta = QTableWidgetItem(str(prod.precioVenta))
            item_cant_stock = QTableWidgetItem(str(prod.cantStock))
            item_categoria = QTableWidgetItem(self.categoria_descripcion_map[prod.categoria])
            # Usa el diccionario para obtener la descripción y Convierte la clave en entero
            item_impuestos = QTableWidgetItem(str(prod.impuestos))
            item_descuentos = QTableWidgetItem(str(prod.descuentos))
            item_proveedor = QTableWidgetItem(prod.proveedor)
            item_fecha_venc = QTableWidgetItem(prod.fechaVenc.strftime("%Y-%m-%d"))

            self.table.setItem(i, 0, item_nombre)
            self.table.setItem(i, 1, item_codigo)
            self.table.setItem(i, 2, item_precioCompra)
            self.table.setItem(i, 3, item_precioVenta)
            self.table.setItem(i, 4, item_cant_stock)
            self.table.setItem(i, 5, item_categoria)
            self.table.setItem(i, 6, item_impuestos)
            self.table.setItem(i, 7, item_descuentos)
            self.table.setItem(i, 8, item_proveedor)
            self.table.setItem(i, 9, item_fecha_venc)

            # Botón Editar
            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.on_edit_button_clicked)
            self.table.setCellWidget(i, 10, edit_button)

            # Botón Eliminar
            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.on_delete_button_clicked)
            self.table.setCellWidget(i, 11, delete_button)

        # Crear un botón Agregar Categoría
        add_product_button = QPushButton("Agregar Producto")
        add_product_button.clicked.connect(self.on_agregar_producto_clicked)

        # Crear un layout vertical
        layout = QVBoxLayout()

        # Crear un QLabel para el título
        title_label = QLabel("Productos")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: green; font-size: 24px")

        #Crear un QFrame para el rectángulo
        rectangle_frame = QFrame()
        rectangle_frame.setFrameShape(QFrame.StyledPanel)
        rectangle_frame.setFrameShadow(QFrame.Sunken)
        rectangle_frame.setLineWidth(1)

        # Crear un QVBoxLayout para el rectángulo y agregar el campo de búsqueda y el botón
        rectangle_layout = QVBoxLayout(rectangle_frame)
        search_field = QLineEdit()
        search_field.setPlaceholderText("Buscar productos...")
        rectangle_layout.addWidget(search_field)
        rectangle_layout.addWidget(add_product_button)

        # Ajustar el tamaño de las columnas automáticamente para ajustarse al contenido
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # Evitar que las columnas se puedan estirar
        self.table.horizontalHeader().setStretchLastSection(False)

        # Evitar que las filas se puedan estirar
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        # Establecer la selección a nivel de fila y deshabilitar la edición de celdas
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Crear una QScrollArea y establecer la tabla como su widget interno
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.table)
        scroll_area.setWidgetResizable(True)

        # Modificar la política de tamaño de la tabla
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.table.setMinimumHeight(300)  # Cambia este valor según tus necesidades

        # Añadir el título, el rectángulo y el scroll_area al layout
        layout.addWidget(title_label)
        layout.addWidget(rectangle_frame)
        layout.addWidget(scroll_area)
        layout.addStretch(1)  # Añade un espacio flexible para pegar la tabla a la parte inferior de la pantalla

        # Crear un widget central y establecer el layout
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Establecer el widget central en la ventana
        self.setCentralWidget(central_widget)

        # Establece el título de la ventana
        self.setWindowTitle("Productos")

        # Establece el tamaño y la posición de la ventana
        self.setGeometry(100, 100, 900, 400)  # x, y, ancho, alto

    def actualizar_tabla(self):
        # Obtén la lista actualizada de productos
        self.productos = self.producto_service.obtenerProductos()

        # Obtén una lista de categorías y crea un diccionario que mapee los IDs a las descripciones
        self.categorias = self.categoria_service.obtenerCategorias()
        categoria_descripcion_map = {categoria.id: categoria.descripcion for categoria in self.categorias}

        # Limpia la tabla antes de agregar nuevas filas
        self.table.setRowCount(0)

        # Establece el número de filas en la tabla según la longitud de la lista de productos
        self.table.setRowCount(len(self.productos))

        # Rellena la tabla con los productos actualizados
        for i, prod in enumerate(self.productos):
            item_nombre = QTableWidgetItem(prod.nombre)
            item_codigo = QTableWidgetItem(prod.codigo)
            item_precioCompra = QTableWidgetItem(str(prod.precioCompra))
            item_precioVenta = QTableWidgetItem(str(prod.precioVenta))
            item_cant_stock = QTableWidgetItem(str(prod.cantStock))
            item_categoria = QTableWidgetItem(categoria_descripcion_map[int(float(prod.categoria))])
    # Usa el diccionario para obtener la descripción y Convierte la clave en entero
            item_impuestos = QTableWidgetItem(str(prod.impuestos))
            item_descuentos = QTableWidgetItem(str(prod.descuentos))
            item_proveedor = QTableWidgetItem(prod.proveedor)
            item_fecha_venc = QTableWidgetItem(prod.fechaVenc.strftime("%Y-%m-%d"))

            self.table.setItem(i, 0, item_nombre)
            self.table.setItem(i, 1, item_codigo)
            self.table.setItem(i, 2, item_precioCompra)
            self.table.setItem(i, 3, item_precioVenta)
            self.table.setItem(i, 4, item_cant_stock)
            self.table.setItem(i, 5, item_categoria)
            self.table.setItem(i, 6, item_impuestos)
            self.table.setItem(i, 7, item_descuentos)
            self.table.setItem(i, 8, item_proveedor)
            self.table.setItem(i, 9, item_fecha_venc)

            # Botón Editar
            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.on_edit_button_clicked)
            self.table.setCellWidget(i, 10, edit_button)

            # Botón Eliminar
            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.on_delete_button_clicked)
            self.table.setCellWidget(i, 11, delete_button)

    def on_agregar_producto_clicked(self):
        dialog = AgregarProductoDialog(self.producto_service, self.categoria_service, self)
        result = dialog.exec()

        if result == QDialog.Accepted:
                # Actualiza la tabla para mostrar la nueva categoría agregada
            self.actualizar_tabla()

    def on_edit_button_clicked(self):
        # Obtén el botón que emitió la señal
        button = self.app.sender()
        # Obtiene el índice del elemento en la tabla
        index = self.table.indexAt(button.pos())

        # Obtén el código del producto seleccionado
        producto = None
        
        # Obtén la lista de categorías
        categorias = self.categoria_service.obtenerCategorias()
        
        nombre = self.table.item(index.row(), 0).text()
        codigo = self.table.item(index.row(), 1).text()
        precioCompra = self.table.item(index.row(), 2).text()
        precioVenta = self.table.item(index.row(), 3).text()
        cant_stock = self.table.item(index.row(), 4).text()
        categoria = self.table.item(index.row(), 5).text()
        impuestos = self.table.item(index.row(), 6).text()
        descuentos = self.table.item(index.row(), 7).text()
        proveedor = self.table.item(index.row(), 8).text()
        fecha_venc = self.table.item(index.row(), 9).text()          
        producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, impuestos, descuentos, proveedor, fecha_venc)

        # Muestra la ventana de edición y obtén el resultado
        dialog = EditarProductoDialog(producto, categorias)
        result = dialog.exec()

        if result == QDialog.Accepted:
            # Actualiza el producto en la base de datos
            self.producto_service.actualizarProducto(producto)

            # Actualiza la tabla para mostrar los cambios
            self.actualizar_tabla()

    def on_delete_button_clicked(self):
        #  Obtén el botón que emitió la señal
        button = self.app.sender()
        #  Obtiene el índice del elemento en la tabla
        index = self.table.indexAt(button.pos())
        # Obtén el código del producto seleccionado
        producto_codigo = self.table.item(index.row(), 1).text()

        respuesta = QMessageBox.question(None, "Confirmación de eliminación", f"¿Está seguro de que desea eliminar el producto con código {producto_codigo}?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            # Aquí va el código para eliminar el producto de la base de datos utilizando el código
            self.producto_service.eliminarProducto(producto_codigo)
            #Elimina la fila seleccionada de la tabla
            self.table.removeRow(index.row())




