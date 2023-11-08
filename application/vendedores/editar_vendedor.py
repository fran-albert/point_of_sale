from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox, QDateEdit, QComboBox
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
            self.id_vendedor_label.setHidden(True)
            self.id_vendedor_input.setHidden(True)


            self.nombre_label = QLabel("Nombre:")
            self.nombre_input = QLineEdit(vendedor.nombre)
            layout.addWidget(self.nombre_label)
            layout.addWidget(self.nombre_input)

            self.apellido_label = QLabel("Apellido:")
            self.apellido_input = QLineEdit(vendedor.apellido)
            layout.addWidget(self.apellido_label)
            layout.addWidget(self.apellido_input)

            self.contrasena_label = QLabel("Contraseña:")
            self.contrasena_input = QLineEdit(vendedor.contraseña)
            self.contrasena_input.setEchoMode(QLineEdit.Password) 
            layout.addWidget(self.contrasena_label)
            layout.addWidget(self.contrasena_input)

            self.dni_label = QLabel("DNI:")
            self.dni_input = QLineEdit(str(vendedor.dni))
            layout.addWidget(self.dni_label)
            layout.addWidget(self.dni_input)

            self.correo_label = QLabel("Correo:")
            self.correo_input = QLineEdit(vendedor.correo_electronico)
            layout.addWidget(self.correo_label)
            layout.addWidget(self.correo_input)

            self.telefono_label = QLabel("Teléfono:")
            self.telefono_input = QLineEdit(str(vendedor.telefono))
            layout.addWidget(self.telefono_label)
            layout.addWidget(self.telefono_input)

            self.fecha_nac_label = QLabel("Fecha Nacimiento:")
            fecha_nac = QDate.fromString(vendedor.fecha_nacimiento, "yyyy-MM-dd")
            self.fecha_nac_input = QDateEdit(fecha_nac)
            layout.addWidget(self.fecha_nac_label)
            layout.addWidget(self.fecha_nac_input)

            self.fecha_alta_label = QLabel("Fecha Alta:")
            fecha_alta = QDate.fromString(vendedor.fecha_alta, "yyyy-MM-dd")
            self.fecha_alta_input = QDateEdit(fecha_alta)
            layout.addWidget(self.fecha_alta_label)
            layout.addWidget(self.fecha_alta_input)

            self.fecha_alta_label.setHidden(True)
            self.fecha_alta_input.setHidden(True)

            self.rol_label = QLabel("Rol:")
            self.rol_combo = QComboBox()
            self.rol_combo.addItem("Selecciona el rol", None)
            self.rol_combo.addItem("Administrador", 1)
            self.rol_combo.addItem("Vendedor", 0)
            vendedores = self.vendedor_service.obtenerVendedores()
            if vendedores:
                primer_vendedor = vendedores[0]
                if primer_vendedor.admin == 1:
                    self.rol_combo.setCurrentIndex(self.rol_combo.findData(1))
                else:
                    self.rol_combo.setCurrentIndex(self.rol_combo.findData(0))

            layout.addWidget(self.rol_label)
            layout.addWidget(self.rol_combo)

            self.rol_label.setHidden(True)
            self.rol_combo.setHidden(True)

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
            nueva_contraseña = self.contrasena_input.text().strip()
            nuevo_telefono = self.telefono_input.text().strip()
            nuevo_correo_electronico = self.correo_input.text().strip()
            nueva_fecha_alta = self.fecha_alta_input.date().toString("yyyy-MM-dd")
            nueva_fecha_nacimiento = self.fecha_nac_input.date().toString("yyyy-MM-dd")
            admin = self.rol_combo.currentData()

            if nuevo_nombre and nuevoDNI and nuevo_apellido and nueva_contraseña and nuevo_telefono and nuevo_correo_electronico and nueva_fecha_alta and nueva_fecha_nacimiento and admin is not None:
                self.vendedor.nombre = nuevo_nombre
                self.vendedor.apellido = nuevo_apellido
                self.vendedor.contraseña = nueva_contraseña
                self.vendedor.dni = nuevoDNI
                self.vendedor.telefono = nuevo_telefono
                self.vendedor.correo_electronico = nuevo_correo_electronico
                nueva_fecha_nacimiento = datetime.strptime(nueva_fecha_nacimiento, "%Y-%m-%d")
                self.vendedor.fecha_nacimiento = nueva_fecha_nacimiento
                nueva_fecha_alta = datetime.strptime(nueva_fecha_alta, "%Y-%m-%d")
                self.vendedor.admin = admin 
                self.vendedor.fecha_alta = nueva_fecha_alta
                QMessageBox.information(self, "Información", "Datos del vendedor editados")
                self.accept() 
            else:
                QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
