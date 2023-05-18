from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QLabel, QDialog
from ordenes.agregar_orden import AgregarOrdenDialog
from servicios.producto_service import ProductoService
from servicios.proveedor_service import ProveedorService
from servicios.orden_compra_service import OrdenCompraService

class OrdenesWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)

        self.app = app
        self.proveedor_service = ProveedorService()
        self.producto_service = ProductoService()
        self.orden_compra_service = OrdenCompraService()

        # Configurar ventana
        self.setWindowTitle("Órdenes de Compra")
        self.setGeometry(100, 100, 150, 150)

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
        for button_text in ["Nueva Orden de Compra", "Historial Órdenes de Compra", "Cancelar"]:
            button = QPushButton(button_text)
            button.setFixedWidth(200)  # Ajustar el ancho de los botones
            button.setFixedHeight(50)  # Establecer altura fija
            button.setStyleSheet("font-size: 14px")  # Ajustar tamaño de fuente
            buttons_layout.addWidget(button)

            if button_text == "Nueva Orden de Compra":
                button.clicked.connect(self.on_agregar_orden_clicked)  # Conectar al método

        buttons_layout.addStretch()  # Agregar espacio adicional


        main_layout.addLayout(buttons_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def on_agregar_orden_clicked(self):
        dialog = AgregarOrdenDialog(self.proveedor_service, self.producto_service, self.orden_compra_service)
        result = dialog.exec()
