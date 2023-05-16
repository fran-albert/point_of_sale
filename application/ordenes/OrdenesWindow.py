from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QHBoxLayout, QSpinBox, QTableWidget, QHeaderView, QSizePolicy, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QDialog, QMessageBox
from servicios.producto_service import ProductoService
from utils.Utils import Utils
from ventas.ventas_utils_buttons import VentasUtilsButtons

class OrdenesWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)

        self.app = app

        # Configurar ventana
        self.setWindowTitle("Órdenes de Compra")
        self.setGeometry(100, 100, 600, 300)

        # Crear elementos gráficos
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        title_label = QLabel("Órdenes de Compra")
        title_label.setAlignment(Qt.AlignCenter)
        font = title_label.font()
        font.setPointSize(24)  # Cambiar el tamaño de la fuente
        font.setBold(True)     # Establecer el estilo en negrita
        title_label.setFont(font)
        main_layout.addWidget(title_label)

        # Agregar los botones debajo del título "Ventas"
        buttons_layout = QHBoxLayout()
        for button_text in ["Vendedor", "Clientes", "Mov. de Caja", "Corte Caja", "Cancelar"]:
            button = QPushButton(button_text)
            button.setFixedWidth(120)  # Ajustar el ancho de los botones
            buttons_layout.addWidget(button)
        buttons_layout.addStretch()  # Agregar un espacio flexible para alinear a la izquierda

        # Agregar el contador de ventas alineado a la derecha
        self.venta_numero_label = QLabel("Venta N°: ")
        buttons_layout.addWidget(self.venta_numero_label)
        main_layout.addLayout(buttons_layout)

        input_layout = QHBoxLayout()

        self.codigo_input = QLineEdit()
        self.codigo_input.setPlaceholderText("Código del producto")
        input_layout.addWidget(self.codigo_input)

        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre del producto")
        input_layout.addWidget(self.nombre_input)

        main_layout.addLayout(input_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Código", "Descripción", "Cantidad", "Precio Unitario", "Precio Total"])
        # Ajustar el ancho de cada columna
        self.table.setColumnWidth(0, 100)  # Código
        self.table.setColumnWidth(1, 400)  # Descripción
        self.table.setColumnWidth(2, 80)   # Cantidad
        self.table.setColumnWidth(3, 100)  # Precio
        self.table.setColumnWidth(4, 100)  # Precio Total
        main_layout.addWidget(self.table)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Configurar el tamaño y posición de la tabla
        self.table.setMinimumWidth(800)
        self.table.setMaximumHeight(300)

        # Agregar Subtotal, IVA y Total debajo de la tabla
        totals_layout = QVBoxLayout()

        self.subtotal_label = QLabel("Subtotal: ")
        self.iva_label = QLabel("I.V.A: ")
        self.total_label = QLabel("Total: ")

        totals_layout.addWidget(self.subtotal_label, alignment=Qt.AlignRight)
        totals_layout.addWidget(self.iva_label, alignment=Qt.AlignRight)
        totals_layout.addWidget(self.total_label, alignment=Qt.AlignRight)

        main_layout.addLayout(totals_layout)

        # Mover el botón "Cobrar" debajo de Subtotal, IVA y Total
        cobrar_button = QPushButton("Cobrar")
        cobrar_button.clicked.connect(lambda: VentasUtilsButtons.show_payment_window('test', self.total, self, self.lista_productos_vendidos(self.table)))

        main_layout.addWidget(cobrar_button, alignment=Qt.AlignRight)

