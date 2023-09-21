from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QLabel
from servicios.producto_service import ProductoService
from servicios.categoria_service import CategoriaService
from .agregar_categoria import AgregarCategoriaDialog
from .lista_categorias import ListaCategoriasDialog

class CategoriasWindow(QMainWindow):
    def __init__(self, app, rol, parent=None):
        super().__init__(parent)

        self.app = app
        self.rol = rol
        self.categoria_service = CategoriaService()
        self.producto_service = ProductoService()

        self.setWindowTitle("Categorías")
        self.setGeometry(100, 100, 150, 150)

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        title_label = QLabel("Categorías")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #025464; font-size: 24px; font-weight: bold")
        font = title_label.font()
        font.setPointSize(24)  
        font.setBold(True)     
        title_label.setFont(font)
        main_layout.addWidget(title_label)

        buttons_layout = QHBoxLayout()
        for button_text in ["Alta Categoría", "Listado de Categorías", "Cancelar"]:

            if button_text == "Alta Categoría" and self.rol == 0:
                continue
            button = QPushButton(button_text)
            button.setFixedWidth(200)  
            button.setFixedHeight(50)  
            button.setStyleSheet("font-size: 14px")  
            buttons_layout.addWidget(button)

            if button_text == "Alta Categoría":
                button.clicked.connect(self.on_agregar_categoria_clicked)
            if button_text == "Listado de Categorías":
                button.clicked.connect(self.on_ver_lista_categorias_clicked) 
            if button_text == "Cancelar":
                button.clicked.connect(self.on_cancelar_clicked)

        buttons_layout.addStretch()  
        main_layout.addLayout(buttons_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def on_agregar_categoria_clicked(self):
        dialog = AgregarCategoriaDialog(self.producto_service, self.categoria_service)
        result = dialog.exec()

    def on_ver_lista_categorias_clicked(self):
        dialog = ListaCategoriasDialog(self.app, self.rol)
        result = dialog.exec()

    def on_cancelar_clicked(self):
        self.close()  

