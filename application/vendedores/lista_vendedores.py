from PyQt5.QtWidgets import QDialog, QDateEdit, QAbstractItemView, QSizePolicy, QHeaderView, QVBoxLayout, QLabel, QCheckBox, QTableWidget, QHBoxLayout, QLineEdit, QPushButton, QCalendarWidget, QFrame, QGridLayout, QTableWidgetItem
from PyQt5.QtCore import Qt
from servicios.vendedores_service import VendedorService


class ListaVendedoresDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.vendedores_service = VendedorService()
        self.vendedores = self.vendedores_service.obtenerVendedores()

        self.setWindowTitle("Lista de Vendedores")

        layout = QVBoxLayout()

        title_label = QLabel("Lista de Vendedores")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #4C4C6D; font-size: 24px; font-weight: bold")

        rectangle_frame = QFrame()
        rectangle_frame.setFrameShape(QFrame.StyledPanel)
        rectangle_frame.setFrameShadow(QFrame.Sunken)
        rectangle_frame.setLineWidth(1)

        layout.addWidget(title_label)
        layout.addWidget(rectangle_frame)

        self.table = QTableWidget(len(self.vendedores), 10)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido", "DNI", "Teléfono", "Correo Electrónico", "Fecha Nacimiento", "Fecha Alta", "", ""])
        self.table.setColumnWidth(0, 20)
        self.table.setColumnWidth(5, 150)
        self.table.setColumnWidth(6, 120)

        for i, vend in enumerate(self.vendedores):
            item_id = QTableWidgetItem(str(vend.id))
            item_nombre = QTableWidgetItem(vend.nombre)
            item_apellido = QTableWidgetItem(vend.apellido)
            item_dni = QTableWidgetItem(str(vend.dni))
            item_telefono = QTableWidgetItem(str(vend.telefono))
            item_correo = QTableWidgetItem(vend.correo)
            item_fecha_nacimiento = QTableWidgetItem(vend.fechaNac.strftime("%Y-%m-%d"))
            item_fecha_alta = QTableWidgetItem(vend.fechaAlta.strftime("%Y-%m-%d"))

            self.table.setItem(i, 0, item_id)
            self.table.setItem(i, 1, item_nombre)
            self.table.setItem(i, 2, item_apellido)
            self.table.setItem(i, 3, item_dni)
            self.table.setItem(i, 4, item_telefono)
            self.table.setItem(i, 5, item_correo)
            self.table.setItem(i, 6, item_fecha_nacimiento)
            self.table.setItem(i, 7, item_fecha_alta)

            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.on_edit_button_clicked)
            self.table.setCellWidget(i, 8, edit_button)

            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.on_delete_button_clicked)
            self.table.setCellWidget(i, 9, delete_button)

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        layout.addWidget(self.table)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(layout)
        self.resize(1000, 500)
    
    def on_edit_button_clicked(self):
        print('EDITAR')
    
    def on_delete_button_clicked(self):
        print('ELIMINAR')