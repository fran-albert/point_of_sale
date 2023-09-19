from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QLabel, QDialog
from servicios.producto_service import ProductoService
from servicios.categoria_service import CategoriaService
from servicios.proveedor_service import ProveedorService
from .agregar_producto import AgregarProductoDialog
from .lista_productos import ListaProductosDialog

class ProductosWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)

        self.app = app
        self.producto_service = ProductoService()
        self.categoria_service = CategoriaService()
        self.proveedor_service = ProveedorService()

        self.setWindowTitle("Productos")
        self.setGeometry(100, 100, 150, 150)

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        title_label = QLabel("Productos")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #025464; font-size: 24px; font-weight: bold")
        font = title_label.font()
        font.setPointSize(24)  
        font.setBold(True)     
        title_label.setFont(font)
        main_layout.addWidget(title_label)

        buttons_layout = QHBoxLayout()
        for button_text in ["Alta Producto", "Listado de Productos", "Cancelar"]:
            button = QPushButton(button_text)
            button.setFixedWidth(200)  
            button.setFixedHeight(50)  
            button.setStyleSheet("font-size: 14px")  
            buttons_layout.addWidget(button)

            if button_text == "Alta Producto":
                button.clicked.connect(self.on_agregar_producto_clicked)
            if button_text == "Listado de Productos":
                button.clicked.connect(self.on_ver_lista_productos_clicked) 
            if button_text == "Cancelar":
                button.clicked.connect(self.on_cancelar_clicked)

        buttons_layout.addStretch()  
        main_layout.addLayout(buttons_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def on_agregar_producto_clicked(self):
        dialog = AgregarProductoDialog(self.producto_service, self.categoria_service, self.proveedor_service)
        result = dialog.exec()

    def on_ver_lista_productos_clicked(self):
        dialog = ListaProductosDialog(self.app)
        result = dialog.exec()

    def on_cancelar_clicked(self):
        self.close()  

