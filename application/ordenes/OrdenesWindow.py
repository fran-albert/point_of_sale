from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QLabel, QDialog
from ordenes.agregar_orden import AgregarOrdenDialog
from ordenes.historial_ordenes import VerOrdenDialog
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

        self.setWindowTitle("Órdenes de Compra")
        self.setGeometry(100, 100, 150, 150)

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        title_label = QLabel("Órdenes de Compra")
        title_label.setAlignment(Qt.AlignCenter)
        font = title_label.font()
        font.setPointSize(24)  
        font.setBold(True)   
        title_label.setFont(font)
        main_layout.addWidget(title_label)

        buttons_layout = QHBoxLayout()
        for button_text in ["Nueva Orden de Compra", "Historial Órdenes de Compra", "Cancelar"]:
            button = QPushButton(button_text)
            button.setFixedWidth(200)  
            button.setFixedHeight(50) 
            button.setStyleSheet("font-size: 14px") 
            buttons_layout.addWidget(button)

            if button_text == "Nueva Orden de Compra":
                button.clicked.connect(self.on_agregar_orden_clicked)  
            if button_text == "Historial Órdenes de Compra":
                button.clicked.connect(self.on_ver_orden_clicked)
            if button_text == "Cancelar":
                button.clicked.connect(self.on_cancelar_clicked) 

        buttons_layout.addStretch() 
        main_layout.addLayout(buttons_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def on_agregar_orden_clicked(self):
        dialog = AgregarOrdenDialog(self.proveedor_service, self.producto_service, self.orden_compra_service)
        result = dialog.exec()

    def on_ver_orden_clicked(self):
        dialog = VerOrdenDialog()
        result = dialog.exec()

    def on_cancelar_clicked(self):
        self.close() 
