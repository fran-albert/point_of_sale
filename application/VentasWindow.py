import sys
from pathlib import Path
# Agrega la carpeta principal al sys.path
ruta_principal = str(Path(__file__).parent.parent.resolve())
if ruta_principal not in sys.path:
    sys.path.append(ruta_principal)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QHBoxLayout, QScrollArea, QTableWidget, QHeaderView, QSizePolicy, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QDialog, QMessageBox
from servicios.producto_service import ProductoService

class VentasWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)

        self.app = app
        self.producto_service = ProductoService()

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

        main_layout.addLayout(input_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Código", "Nombre", "Cantidad", "Precio"])
        main_layout.addWidget(self.table)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Conectar la señal editingFinished del QLineEdit codigo_input a la función buscar_producto
        self.codigo_input.editingFinished.connect(self.buscar_producto)

    def buscar_producto(self):        
        codigo = self.codigo_input.text()
        producto = self.producto_service.obtenerProducto(codigo)
        
        if producto is None:
            QMessageBox.warning(self, "Error", "El código ingresado no se encuentra en los productos.")
            return

        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, QTableWidgetItem(producto))
        # self.table.setItem(row_count, 1, QTableWidgetItem(producto.nombre))
        # self.table.setItem(row_count, 2, QTableWidgetItem("1"))  # Puedes establecer una cantidad predeterminada
        # self.table.setItem(row_count, 3, QTableWidgetItem(str(producto.precio)))

        self.codigo_input.clear()
        self.nombre_input.clear()