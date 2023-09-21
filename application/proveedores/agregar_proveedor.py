import sys
sys.path.append('C:\\Users\\Francisco\\Documents\\point_of_sale')
from PyQt5.QtWidgets import QDateEdit, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QDate
from datetime import datetime
from entities.proveedor import Proveedor

class AgregarProveedorDialog(QDialog):
    def __init__(self, proveedor_service, parent=None):
        super().__init__(parent)

        self.proveedor_service = proveedor_service

        self.setWindowTitle("Agregar Proveedor")

        layout = QVBoxLayout()

        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)

        self.direccion_label = QLabel("Dirección:")
        self.direccion_input = QLineEdit()
        layout.addWidget(self.direccion_label)
        layout.addWidget(self.direccion_input)

        self.codigo_postal_label = QLabel("Código Postal:")
        self.codigo_postal_input = QLineEdit()
        layout.addWidget(self.codigo_postal_label)
        layout.addWidget(self.codigo_postal_input)

        self.ciudad_label = QLabel("Ciudad:")
        self.ciudad_input = QLineEdit()
        layout.addWidget(self.ciudad_label)
        layout.addWidget(self.ciudad_input)

        self.provincia_label = QLabel("Provincia:")
        self.provincia_input = QLineEdit()
        layout.addWidget(self.provincia_label)
        layout.addWidget(self.provincia_input)

        self.telefono_label = QLabel("Teléfono:")
        self.telefono_input = QLineEdit()
        layout.addWidget(self.telefono_label)
        layout.addWidget(self.telefono_input)

        self.email_label = QLabel("Correo Electrónico:")
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.comentario_label = QLabel("Comentario:")
        self.comentario_input = QLineEdit()
        layout.addWidget(self.comentario_label)
        layout.addWidget(self.comentario_input)

        self.cuenta_bancaria_label = QLabel("Cuenta Bancaria:")
        self.cuenta_bancaria_input = QLineEdit()
        layout.addWidget(self.cuenta_bancaria_label)
        layout.addWidget(self.cuenta_bancaria_input)

        self.fecha_alta_label = QLabel("Fecha Alta:")
        self.fecha_alta_input = QDateEdit()
        today = QDate.currentDate()
        self.fecha_alta_input.setDate(today)
        layout.addWidget(self.fecha_alta_label)
        layout.addWidget(self.fecha_alta_input)

        self.buttons_layout = QHBoxLayout()
        self.agregar_button = QPushButton("Agregar")
        self.cancelar_button = QPushButton("Cancelar")
        self.buttons_layout.addWidget(self.agregar_button)
        self.buttons_layout.addWidget(self.cancelar_button)

        layout.addLayout(self.buttons_layout)
        self.setLayout(layout)

        self.agregar_button.clicked.connect(self.agregar_proveedor)
        self.cancelar_button.clicked.connect(self.reject)

    def agregar_proveedor(self):
        nombre = self.nombre_input.text().strip()
        direccion = self.direccion_input.text().strip()
        codigo_postal = self.codigo_postal_input.text().strip()
        ciudad = self.ciudad_input.text().strip()
        provincia = self.provincia_input.text().strip()
        telefono = self.telefono_input.text().strip()
        email = self.email_input.text().strip()
        comentario = self.comentario_input.text().strip()
        cuenta_bancaria = self.cuenta_bancaria_input.text().strip()
        fecha_alta = self.fecha_alta_input.date().toString("yyyy-MM-dd")

        if nombre and direccion and codigo_postal and ciudad and provincia and telefono and email and cuenta_bancaria and fecha_alta:
            try:
                fecha_alta = datetime.strptime(fecha_alta, "%Y-%m-%d")
                proveedor = Proveedor(nombre, direccion, codigo_postal, ciudad, provincia, telefono, email, comentario, cuenta_bancaria, fecha_alta)
                self.proveedor_service.insertarProveedor(proveedor)
                QMessageBox.information(self, "Información", "Nuevo Proveedor Añadido")
                self.accept()
            except ValueError:
                QMessageBox.warning(self, "Error", "Por favor, ingrese una fecha válida en formato YYYY-MM-DD.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
