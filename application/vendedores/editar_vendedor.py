from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox, QDateEdit
from PyQt5.QtCore import QDate
from datetime import datetime

class EditarVendedorDialog(QDialog):
        def __init__(self, vendedor, vendedor_service, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Editar Vendedor")

            self.vendedor = vendedor
            self.vendedor_service = vendedor_service
            layout = QVBoxLayout()

            self.id_vendedor_label = QLabel("ID Vendedor:")
            self.id_vendedor_input = QLineEdit(str(vendedor.id))  
            self.id_vendedor_input.setReadOnly(True) 
            layout.addWidget(self.id_vendedor_label)
            layout.addWidget(self.id_vendedor_input)

            self.nombre_label = QLabel("Nombre:")
            self.nombre_input = QLineEdit(vendedor.nombre)
            layout.addWidget(self.nombre_label)
            layout.addWidget(self.nombre_input)

            self.apellido_label = QLabel("Apellido:")
            self.apellido_input = QLineEdit(vendedor.apellido)
            layout.addWidget(self.apellido_label)
            layout.addWidget(self.apellido_input)

            self.dni_label = QLabel("DNI:")
            self.dni_input = QLineEdit(str(vendedor.dni))
            layout.addWidget(self.dni_label)
            layout.addWidget(self.dni_input)

            self.correo_label = QLabel("Correo:")
            self.correo_input = QLineEdit(vendedor.correo)
            layout.addWidget(self.correo_label)
            layout.addWidget(self.correo_input)

            self.telefono_label = QLabel("Teléfono:")
            self.telefono_input = QLineEdit(str(vendedor.telefono))
            layout.addWidget(self.telefono_label)
            layout.addWidget(self.telefono_input)

            self.fechaNac_label = QLabel("Fecha Nacimiento:")
            fechaNac = QDate.fromString(vendedor.fechaNac, "yyyy-MM-dd")
            self.fechaNac_input = QDateEdit(fechaNac)
            layout.addWidget(self.fechaNac_label)
            layout.addWidget(self.fechaNac_input)

            self.fecha_alta_label = QLabel("Fecha Alta:")
            fecha_alta = QDate.fromString(vendedor.fechaAlta, "yyyy-MM-dd")
            self.fecha_alta_input = QDateEdit(fecha_alta)
            layout.addWidget(self.fecha_alta_label)
            layout.addWidget(self.fecha_alta_input)

            self.buttons_layout = QHBoxLayout()
            self.guardar_button = QPushButton("Guardar")
            self.cancelar_button = QPushButton("Cancelar")
            self.buttons_layout.addWidget(self.guardar_button)
            self.buttons_layout.addWidget(self.cancelar_button)

            layout.addLayout(self.buttons_layout)
            self.setLayout(layout)

            self.guardar_button.clicked.connect(self.guardar_vendedor)
            self.cancelar_button.clicked.connect(self.reject)

        def guardar_vendedor(self):
            nuevo_nombre = self.nombre_input.text().strip()
            nuevoDNI = self.dni_input.text().strip()
            nuevo_apellido = self.apellido_input.text().strip()
            nuevo_telefono = self.telefono_input.text().strip()
            nuevo_correo = self.correo_input.text().strip()
            nueva_fecha_alta = self.fecha_alta_input.date().toString("yyyy-MM-dd")
            nueva_fechaNac = self.fechaNac_input.date().toString("yyyy-MM-dd")

            if nuevo_nombre and nuevoDNI and nuevo_apellido  and nuevo_telefono and nuevo_correo and nueva_fecha_alta and nueva_fechaNac:
                self.vendedor.nombre = nuevo_nombre
                self.vendedor.apellido = nuevo_apellido
                self.vendedor.dni = nuevoDNI
                self.vendedor.telefono = nuevo_telefono
                self.vendedor.correo = nuevo_correo
                nueva_fechaNac = datetime.strptime(nueva_fechaNac, "%Y-%m-%d")
                self.vendedor.fechaNac = nueva_fechaNac
                nueva_fecha_alta = datetime.strptime(nueva_fecha_alta, "%Y-%m-%d")
                self.vendedor.fechaAlta = nueva_fecha_alta
                self.accept() 
            else:
                QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
