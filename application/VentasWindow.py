from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QWidget, QMessageBox
from PyQt5.QtCore import Qt
import sys

class VentasWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)

        self.app = app

        # Configurar ventana
        self.setWindowTitle("Ventas")
        self.setGeometry(100, 100, 800, 600)

        # Crear elementos gráficos
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        title_label = QLabel("Ventas")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        input_layout = QHBoxLayout()

        self.codigo_input = QLineEdit()
        self.codigo_input.setPlaceholderText("Código del producto")
        input_layout.addWidget(self.codigo_input)

        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre del producto")
        input_layout.addWidget(self.nombre_input)

        self.agregar_button = QPushButton("Agregar")
        self.agregar_button.clicked.connect(self.agregar_producto)
        input_layout.addWidget(self.agregar_button)

        main_layout.addLayout(input_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Código", "Nombre", "Cantidad", "Precio"])
        main_layout.addWidget(self.table)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def agregar_producto(self):
        codigo = self.codigo_input.text()
        nombre = self.nombre_input.text()

        # Aquí puedes buscar el producto en la base de datos usando el código o el nombre
        # producto = buscar_producto(codigo, nombre)

        # Supongamos que obtenemos el siguiente producto:
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "cantidad": 1,
            "precio": 100
        }

        # Agregar producto a la tabla
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(producto["codigo"]))
        self.table.setItem(row_position, 1, QTableWidgetItem(producto["nombre"]))
        self.table.setItem(row_position, 2, QTableWidgetItem(str(producto["cantidad"])))
        self.table.setItem(row_position, 3, QTableWidgetItem(str(producto["precio"])))

        # Limpiar campos de entrada
        self.codigo_input.clear()
        self.nombre_input.clear()

