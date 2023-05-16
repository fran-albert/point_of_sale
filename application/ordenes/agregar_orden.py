import sys
sys.path.append('C:\\Users\\Francisco\\Documents\\point_of_sale')
from PyQt5.QtWidgets import QDialog, QDesktopWidget, QSizePolicy, QHeaderView, QVBoxLayout, QLabel, QComboBox, QTableWidget, QHBoxLayout, QLineEdit, QPushButton, QCalendarWidget, QFrame, QGridLayout
from PyQt5.QtCore import Qt


class AgregarOrdenDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nueva Orden de Compra")
        # Cambiar la política de tamaño de la ventana
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

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
        proveedor_combo = QComboBox()
        proveedor_combo.addItem("Proveedor 1")
        proveedor_combo.addItem("Proveedor 2")
        rectangle_layout.addWidget(proveedor_label, 0, 0)
        rectangle_layout.addWidget(proveedor_combo, 0, 1)


        # Input para buscar productos
        buscar_productos_label = QLabel("Buscar Productos:")
        buscar_productos_input = QLineEdit()
        rectangle_layout.addWidget(buscar_productos_label, 1, 0)
        rectangle_layout.addWidget(buscar_productos_input, 1, 1)

        # Agregar el rectángulo al layout principal
        layout.addWidget(title_label)
        layout.addWidget(rectangle_frame)

        # Tabla
        tabla = QTableWidget()
        tabla.setColumnCount(7)
        tabla.setHorizontalHeaderLabels(["ID", "ID Proveedor",  "Cantidad", "Cantidad", "Precio Compra", "Precio Total", "Fecha Recepción", "Recibido"])
        # Cambiar la política de tamaño de las cabeceras horizontales
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        layout.addWidget(tabla)


        # Precio Total: QLineEdit
        precio_total_layout = QHBoxLayout()
        precio_total_label = QLabel("Total:")
        precio_total_text = QLineEdit()
        precio_total_layout.addWidget(precio_total_label)
        precio_total_layout.addWidget(precio_total_text)
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
        layout.addWidget(confirmar_orden_button)

        self.setLayout(layout)
        self.resize(730, 300)
        self.centerOnScreen()

        # Conectar el botón para mostrar/ocultar el calendario
        fecha_recepcion_button.clicked.connect(fecha_recepcion_calendar.show)

        # Conectar el evento de selección de fecha
        fecha_recepcion_calendar.selectionChanged.connect(lambda: self.insertar_fecha(fecha_recepcion_calendar, fecha_recepcion_button))

    def insertar_fecha(self, calendar, button):
        fecha_seleccionada = calendar.selectedDate()
        fecha_formateada = fecha_seleccionada.toString(Qt.ISODate)
        button.setText(fecha_formateada)
        calendar.hide()

    def centerOnScreen(self):
        resolution = QDesktopWidget().screenGeometry()
        self.move(round((resolution.width() / 2) - (self.frameSize().width() / 2)),
                round((resolution.height() / 2) - (self.frameSize().height() / 2)))

