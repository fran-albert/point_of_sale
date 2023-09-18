from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QLabel, QDialog
from servicios.vendedores_service import VendedorService
from vendedores.agregar_vendedor import AgregarVendedorDialog
from vendedores.lista_vendedores import ListaVendedoresDialog

class VendedoresWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)

        self.app = app
        self.vendedor_service = VendedorService()

        self.setWindowTitle("Vendedores")
        self.setGeometry(100, 100, 150, 150)

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        title_label = QLabel("Vendedores")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #025464; font-size: 24px; font-weight: bold")
        font = title_label.font()
        font.setPointSize(24)  
        font.setBold(True)     
        title_label.setFont(font)
        main_layout.addWidget(title_label)

        buttons_layout = QHBoxLayout()
        for button_text in ["Alta Vendedor", "Listado de Vendedores", "Cancelar"]:
            button = QPushButton(button_text)
            button.setFixedWidth(200)  
            button.setFixedHeight(50)  
            button.setStyleSheet("font-size: 14px")  
            buttons_layout.addWidget(button)

            if button_text == "Alta Vendedor":
                button.clicked.connect(self.on_agregar_vendedor_clicked)
            if button_text == "Listado de Vendedores":
                button.clicked.connect(self.on_ver_lista_vendedores_clicked) 
            if button_text == "Cancelar":
                button.clicked.connect(self.on_cancelar_clicked)

        buttons_layout.addStretch()  
        main_layout.addLayout(buttons_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def on_agregar_vendedor_clicked(self):
        dialog = AgregarVendedorDialog(self.vendedor_service)
        result = dialog.exec()

    def on_ver_lista_vendedores_clicked(self):
        dialog = ListaVendedoresDialog(self.app)
        result = dialog.exec()

    def on_cancelar_clicked(self):
        self.close()  

