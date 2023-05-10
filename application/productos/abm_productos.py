import sys
from pathlib import Path
# Agrega la carpeta principal al sys.path
ruta_principal = str(Path(__file__).parent.parent.resolve())
if ruta_principal not in sys.path:
    sys.path.append(ruta_principal)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QScrollArea, QTableWidget, QHeaderView, QSizePolicy, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QDialog, QMessageBox
from servicios.categoria_service import CategoriaService
from servicios.producto_service import ProductoService
from servicios.proveedor_service import ProveedorService
from .agregar_producto import AgregarProductoDialog
from .editar_producto import EditarProductoDialog
from entities.producto import Producto

class ABMProductosWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)    
        # Crear una instancia de QApplication
        self.app = app
        self.producto_service = ProductoService()
        self.proveedor_service = ProveedorService()
        self.categoria_service = CategoriaService()
        self.producto  = self.producto_service.obtenerProductos()
        # En el método __init__ de la clase ABMProductosWindow
        self.categorias = self.categoria_service.obtenerCategorias()
        self.proveedores = self.proveedor_service.obtenerProveedores()

        # Crear un diccionario que mapee los IDs de las categorías a sus descripciones
        self.categoria_descripcion_map = {categoria.id: categoria.descripcion for categoria in self.categorias}
        self.proveedor_nombre_map = {proveedor.id: proveedor.nombre for proveedor in self.proveedores}




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
            item_categoria = QTableWidgetItem(self.categoria_descripcion_map.get(int(float(prod.categoria)), "Desconocida"))
            # Usa el diccionario para obtener la descripción y Convierte la clave en entero
            item_impuestos = QTableWidgetItem(str(prod.impuestos))
            item_descuentos = QTableWidgetItem(str(prod.descuentos))
            item_proveedor = QTableWidgetItem(self.proveedor_nombre_map.get(int(prod.proveedor), "Desconocido"))
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

        self.setGeometry(100, 100, 900, 400)  # x, y, ancho, alto
        # Obtener la geometría de la pantalla y calcular la posición central
        screen = QDesktopWidget().availableGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2

        # Establecer la posición de la ventana en el centro de la pantalla
        self.move(x, y)


    def actualizar_tabla(self):
        # Obtén la lista actualizada de productos
        self.productos = self.producto_service.obtenerProductos()
        self.proveedores = self.proveedor_service.obtenerProveedores()
        # Obtén una lista de categorías y crea un diccionario que mapee los IDs a las descripciones
        self.categorias = self.categoria_service.obtenerCategorias()
        categoria_descripcion_map = {categoria.id: categoria.descripcion for categoria in self.categorias}
        proveedor_nombre_map = {proveedor.id: proveedor.nombre for proveedor in self.proveedores}

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
            item_categoria = QTableWidgetItem(categoria_descripcion_map.get(int(float(prod.categoria)), "Desconocida"))
            # Usa el diccionario para obtener la descripción y Convierte la clave en entero
            item_impuestos = QTableWidgetItem(str(prod.impuestos))
            item_descuentos = QTableWidgetItem(str(prod.descuentos))
            item_proveedor = QTableWidgetItem(proveedor_nombre_map.get(int(prod.proveedor), "Desconocido"))
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
        dialog = AgregarProductoDialog(self.producto_service, self.categoria_service, self.proveedor_service)
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
        categoria_service = CategoriaService()
        producto_service = ProductoService()
        # Crea un diccionario que mapee las descripciones de las categorías a sus IDs
        categoria_descripcion_id_map = {categoria.descripcion: categoria.id for categoria in categorias}

        
        nombre = self.table.item(index.row(), 0).text()
        codigo = self.table.item(index.row(), 1).text()
        precioCompra = self.table.item(index.row(), 2).text()
        precioVenta = self.table.item(index.row(), 3).text()
        cant_stock = self.table.item(index.row(), 4).text()
        categoria_descripcion = self.table.item(index.row(), 5).text()
        categoria_id = categoria_descripcion_id_map.get(categoria_descripcion)
        impuestos = self.table.item(index.row(), 6).text()
        descuentos = self.table.item(index.row(), 7).text()
        proveedor = self.table.item(index.row(), 8).text()
        fecha_venc = self.table.item(index.row(), 9).text()          
        producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria_id, impuestos, descuentos, proveedor, fecha_venc)
        # Muestra la ventana de edición y obtén el resultado
        dialog = EditarProductoDialog(producto, producto_service, categoria_service, categorias )
        result = dialog.exec()

        if result == QDialog.Accepted:
            # Actualiza el producto en la base de datos
            self.producto_service.actualizarProducto(
                producto.codigo,
                producto.nombre,
                producto.precioCompra,
                producto.precioVenta,
                producto.cantStock,
                producto.categoria,
                producto.impuestos,
                producto.descuentos,
                producto.proveedor,
                producto.fechaVenc,
                producto.codigo
            )
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