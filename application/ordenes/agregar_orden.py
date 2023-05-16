import sys
sys.path.append('C:\\Users\\Francisco\\Documents\\point_of_sale')
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QCalendarWidget
from PyQt5.QtCore import Qt


class AgregarOrdenDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)


        self.setWindowTitle("Nueva Orden de Compra")
        layout = QVBoxLayout()

        # Proveedor: QComboBox
        proveedor_label = QLabel("Proveedor:")
        proveedor_combo = QComboBox()
        # Agregar opciones al QComboBox
        proveedor_combo.addItem("Proveedor 1")
        proveedor_combo.addItem("Proveedor 2")

        layout.addWidget(proveedor_label)
        layout.addWidget(proveedor_combo)

        # Tabla
        tabla = QTableWidget()
        tabla.setColumnCount(4)
        tabla.setHorizontalHeaderLabels(["Código", "Cantidad", "Precio Total", "Compra"])

        # Precio Total: QLineEdit
        precio_total_label = QLabel("Precio Total:")
        precio_total_text = QLineEdit()

        layout.addWidget(tabla)
        layout.addWidget(precio_total_label)
        layout.addWidget(precio_total_text)

        # Fecha Recepción: QPushButton y QCalendarWidget
        fecha_recepcion_label = QLabel("Fecha Recepción:")
        fecha_recepcion_button = QPushButton("Seleccionar Fecha")
        fecha_recepcion_calendar = QCalendarWidget()
        fecha_recepcion_calendar.setHidden(True)

        layout.addWidget(fecha_recepcion_label)
        layout.addWidget(fecha_recepcion_button)
        layout.addWidget(fecha_recepcion_calendar)

        self.setLayout(layout)

        # Conectar el botón para mostrar/ocultar el calendario
        fecha_recepcion_button.clicked.connect(fecha_recepcion_calendar.show)

        # Conectar el evento de selección de fecha
        fecha_recepcion_calendar.selectionChanged.connect(lambda: self.insertar_fecha(fecha_recepcion_calendar, fecha_recepcion_button))

    def insertar_fecha(self, calendar, button):
        fecha_seleccionada = calendar.selectedDate()
        fecha_formateada = fecha_seleccionada.toString(Qt.ISODate)
        button.setText(fecha_formateada)
        calendar.hide()