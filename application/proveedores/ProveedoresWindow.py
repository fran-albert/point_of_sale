from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QLabel, QDialog
from servicios.proveedor_service import ProveedorService
from .agregar_proveedor import AgregarProveedorDialog
from .lista_proveedores import ListaProveedoresDialog

class ProveedoresWindow(QMainWindow):
    def __init__(self, app, rol, parent=None):
        super().__init__(parent)

        self.app = app
        self.rol = rol
        self.proveedor_service = ProveedorService()

        self.setWindowTitle("Proveedores")
        self.setGeometry(100, 100, 150, 150)

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        title_label = QLabel("Proveedores")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #025464; font-size: 24px; font-weight: bold")
        font = title_label.font()
        font.setPointSize(24)  
        font.setBold(True)     
        title_label.setFont(font)
        main_layout.addWidget(title_label)

        buttons_layout = QHBoxLayout()
        for button_text in ["Alta Proveedor", "Listado de Proveedores", "Cancelar"]:
            if button_text == "Alta Proveedor" and self.rol == 0:
                continue

            button = QPushButton(button_text)
            button.setFixedWidth(200)  
            button.setFixedHeight(50)  
            button.setStyleSheet("font-size: 14px")  
            buttons_layout.addWidget(button)

            if button_text == "Alta Proveedor":
                button.clicked.connect(self.on_agregar_proveedor_clicked)
            if button_text == "Listado de Proveedores":
                button.clicked.connect(self.on_ver_lista_proveedores_clicked) 
            if button_text == "Cancelar":
                button.clicked.connect(self.on_cancelar_clicked)

        buttons_layout.addStretch()  
        main_layout.addLayout(buttons_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def on_agregar_proveedor_clicked(self):
        dialog = AgregarProveedorDialog(self.proveedor_service)
        result = dialog.exec()

    def on_ver_lista_proveedores_clicked(self):
        dialog = ListaProveedoresDialog(self.app, self.rol)
        result = dialog.exec()

    def on_cancelar_clicked(self):
        self.close()

