import sys
sys.path.append('C:\\Users\\Francisco\\Documents\\point_of_sale')
from PyQt5.QtWidgets import QDialog, QDesktopWidget, QCompleter, QAbstractItemView, QSizePolicy, QSpinBox, QHeaderView, QVBoxLayout, QLabel, QComboBox, QTableWidget, QHBoxLayout, QLineEdit, QPushButton, QCalendarWidget, QFrame, QGridLayout, QTableWidgetItem
from PyQt5.QtCore import Qt, QStringListModel

class AgregarOrdenDialog(QDialog):
    def __init__(self, proveedor_service, producto_service, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nueva Orden de Compra")

        self.proveedor_service = proveedor_service
        self.producto_service = producto_service

        # Layout principal
        layout = QVBoxLayout()

        # Crear un QLabel para el título
        title_label = QLabel("Nueva Orden de Compra")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: green; font-size: 24px; font-weight: bold")

        # Crear un QFrame para el rectángulo
        rectangle_frame = QFrame()
        rectangle_frame.setFrameShape(QFrame.StyledPanel)
        rectangle_frame.setFrameShadow(QFrame.Sunken)
        rectangle_frame.setLineWidth(1)

        # Layout para el rectángulo
        rectangle_layout = QGridLayout(rectangle_frame)

        # Proveedor: QComboBox
        proveedor_label = QLabel("Proveedor:")
        self.proveedor_combo = QComboBox()
        self.proveedor_combo.addItem("Selecciona el Proveedor", None)
        proveedores = self.proveedor_service.obtenerProveedores()
        for proveedor in proveedores:
            self.proveedor_combo.addItem(proveedor.nombre, proveedor.id)
        rectangle_layout.addWidget(proveedor_label, 0, 0)
        rectangle_layout.addWidget(self.proveedor_combo, 0, 1)

        # Input para buscar productos
        buscar_productos_label = QLabel("Buscar Productos:")
        self.buscar_productos_input = QLineEdit()
        self.completer = QCompleter()
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.buscar_productos_input.setCompleter(self.completer)
        rectangle_layout.addWidget(buscar_productos_label, 1, 0)
        rectangle_layout.addWidget(self.buscar_productos_input, 1, 1)

        # Agregar el rectángulo al layout principal
        layout.addWidget(title_label)
        layout.addWidget(rectangle_frame)

        # Tabla
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["Código",  "Producto", "Cantidad", "Precio Compra", "Precio Total"])
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Cambiar la política de tamaño de las cabeceras horizontales
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        layout.addWidget(self.tabla)

        # Precio Total: QLineEdit
        precio_total_layout = QHBoxLayout()
        precio_total_label = QLabel("Total:")
        self.precio_total_text = QLabel()
        self.precio_total_text.setAlignment(Qt.AlignCenter)
        self.precio_total_text.setStyleSheet("color: black; font-size: 20px; font-weight: bold")
        precio_total_layout.addWidget(precio_total_label)
        precio_total_layout.addWidget(self.precio_total_text)
        layout.addLayout(precio_total_layout)

        # Fecha Recepción: QPushButton y QCalendarWidget
        fecha_recepcion_layout = QHBoxLayout()
        fecha_recepcion_label = QLabel("Fecha Recepción:")
        fecha_recepcion_button = QPushButton("Seleccionar Fecha")
        fecha_recepcion_calendar = QCalendarWidget()
        fecha_recepcion_calendar.setHidden(True)
        fecha_recepcion_layout.addWidget(fecha_recepcion_label)
        fecha_recepcion_layout.addWidget(fecha_recepcion_button)
        layout.addLayout(fecha_recepcion_layout)
        layout.addWidget(fecha_recepcion_calendar)

        # Botón Confirmar Orden
        confirmar_orden_button = QPushButton("Confirmar Orden")
        confirmar_orden_button.clicked.connect(self.nueva_orden)
        layout.addWidget(confirmar_orden_button)

        # Cambiar la política de tamaño de la ventana
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(layout)
        self.resize(730, 300)
        self.centerOnScreen()

        # Conectar los productos a la tabla
        self.completer.activated.connect(self.agregar_producto_a_tabla)

        # Conectar la señal currentIndexChanged del QComboBox al slot update_product_list
        self.proveedor_combo.currentIndexChanged.connect(self.update_product_list)

        # Conectar el botón para mostrar/ocultar el calendario
        fecha_recepcion_button.clicked.connect(fecha_recepcion_calendar.show)

        # Conectar el evento de selección de fecha
        fecha_recepcion_calendar.selectionChanged.connect(lambda: self.insertar_fecha(fecha_recepcion_calendar, fecha_recepcion_button))

    def nueva_orden(self):
        print('holamudno')

    # Actualizar la lista de productos cuando cambia el proveedor seleccionado
    def update_product_list(self):
        # Obtén el proveedor seleccionado
        selected_provider_id = self.proveedor_combo.currentData()
        # Si no se ha seleccionado ningún proveedor, vacía la lista de productos
        if selected_provider_id is None:
            self.completer.setModel(QStringListModel([]))
            return
        # En base al proveedor seleccionado, obtén la lista de productos correspondiente
        new_product_list = [producto.nombre for producto in self.producto_service.obtenerProductoPorProveedor(selected_provider_id)]
        # Actualiza el modelo de datos del QCompleter con la nueva lista de productos
        self.completer.setModel(QStringListModel(new_product_list))

    def agregar_producto_a_tabla(self):
        producto_nombre = self.buscar_productos_input.text()
        producto = self.producto_service.obtenerProductoPorNombre(producto_nombre)

        if producto:
            row_position = self.tabla.rowCount()
            self.tabla.insertRow(row_position)

            self.tabla.setItem(row_position, 0, QTableWidgetItem(producto.codigo))
            self.tabla.setItem(row_position, 1, QTableWidgetItem(producto.nombre))

            cantidad_spinbox = QSpinBox()
            cantidad_spinbox.valueChanged.connect(self.actualizar_total)  # Conectar valueChanged a actualizar_total
            self.tabla.setCellWidget(row_position, 2, cantidad_spinbox)

            item = QTableWidgetItem(str(producto.precioCompra))
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.tabla.setItem(row_position, 3, item)

            self.actualizar_total()

    def actualizar_total(self):
        total = 0.0

        for row in range(self.tabla.rowCount()):
            cantidad = self.tabla.cellWidget(row, 2).value()
            precio_compra = float(self.tabla.item(row, 3).text())
            total += cantidad * precio_compra

        self.precio_total_text.setText("{:.2f}".format(total))

    def insertar_fecha(self, calendar, button):
        fecha_seleccionada = calendar.selectedDate()
        fecha_formateada = fecha_seleccionada.toString(Qt.ISODate)
        button.setText(fecha_formateada)
        calendar.hide()

    def centerOnScreen(self):
        resolution = QDesktopWidget().screenGeometry()
        self.move(round((resolution.width() / 2) - (self.frameSize().width() / 2)),
                round((resolution.height() / 2) - (self.frameSize().height() / 2)))