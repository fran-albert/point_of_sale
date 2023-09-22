from PyQt5.QtWidgets import QDateEdit, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox, QComboBox
from PyQt5.QtCore import QDate
from entities.vendedor import Vendedor

class AgregarVendedorDialog(QDialog):
    def __init__(self, vendedor_service, parent=None):
        super().__init__(parent)

        self.vendedor_service = vendedor_service

        self.setWindowTitle("Agregar Vendedor")
        layout = QVBoxLayout()

        self.dni_label = QLabel("Documento:")
        self.dni_input = QLineEdit()
        layout.addWidget(self.dni_label)
        layout.addWidget(self.dni_input)

        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)

        self.apellido_label = QLabel("Apellido:")
        self.apellido_input = QLineEdit()
        layout.addWidget(self.apellido_label)
        layout.addWidget(self.apellido_input)

        self.contrasena_label = QLabel("Contraseña:")
        self.contrasena_input = QLineEdit()
        self.contrasena_input.setEchoMode(QLineEdit.Password) 
        layout.addWidget(self.contrasena_label)
        layout.addWidget(self.contrasena_input)

        self.telefono_label = QLabel("Teléfono:")
        self.telefono_input = QLineEdit()
        layout.addWidget(self.telefono_label)
        layout.addWidget(self.telefono_input)

        self.correo_label = QLabel("Correo:")
        self.correo_input = QLineEdit()
        layout.addWidget(self.correo_label)
        layout.addWidget(self.correo_input)

        self.fecha_nacimiento_label = QLabel("Fecha de Nacimiento:")
        self.fecha_nacimiento_input = QDateEdit()
        layout.addWidget(self.fecha_nacimiento_label)
        layout.addWidget(self.fecha_nacimiento_input)

        self.fecha_alta_label = QLabel("Fecha de Alta:")
        self.fecha_alta_input = QDateEdit()
        today = QDate.currentDate()
        self.fecha_alta_input.setDate(today)
        layout.addWidget(self.fecha_alta_label)
        layout.addWidget(self.fecha_alta_input)

        self.rol_label = QLabel("Rol:")
        self.rol_combo = QComboBox()
        self.rol_combo.addItem("Selecciona el rol", None)
        self.rol_combo.addItem("Administrador", 1)
        self.rol_combo.addItem("Vendedor", 0)
        layout.addWidget(self.rol_label)
        layout.addWidget(self.rol_combo)
        
        self.buttons_layout = QHBoxLayout()
        self.agregar_button = QPushButton("Agregar")
        self.cancelar_button = QPushButton("Cancelar")
        self.buttons_layout.addWidget(self.agregar_button)
        self.buttons_layout.addWidget(self.cancelar_button)

        layout.addLayout(self.buttons_layout)
        self.setLayout(layout)

        self.agregar_button.clicked.connect(self.agregar_vendedor)
        self.cancelar_button.clicked.connect(self.reject)

    def agregar_vendedor(self):
        dni = self.dni_input.text().strip()
        nombre = self.nombre_input.text().strip()
        apellido = self.apellido_input.text().strip()
        contraseña = self.contrasena_input.text().strip()
        telefono = self.telefono_input.text().strip()
        correo = self.correo_input.text().strip()
        fecha_nacimiento = self.fecha_nacimiento_input.date().toString("yyyy-MM-dd")
        fecha_alta = self.fecha_alta_input.date().toString("yyyy-MM-dd")
        admin = self.rol_combo.currentData()

        if dni and nombre and apellido and contraseña and telefono and correo and fecha_nacimiento and fecha_alta and admin is not None:
            try:
                dni = dni
                nombre = nombre
                apellido = apellido
                contraseña = contraseña
                telefono = telefono
                correo = correo
                fecha_nacimiento = fecha_nacimiento
                fecha_alta = fecha_alta
                admin = admin
                vendedor = Vendedor(dni, nombre, apellido, contraseña, telefono, correo, fecha_nacimiento, fecha_alta, admin)
                self.vendedor_service.insertarVendedor(vendedor)
                QMessageBox.information(self, "Información", "Nuevo Vendedor Añadido")
                self.accept()
            except ValueError:
                QMessageBox.warning(self, "Error", "Por favor, ingrese valores válidos.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
