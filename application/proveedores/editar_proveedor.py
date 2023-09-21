from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox, QDateEdit
from PyQt5.QtCore import  QDate
from datetime import datetime

class EditarProveedorDialog(QDialog):
        def __init__(self, proveedor, proveedor_service, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Editar Proveedor")

            self.proveedor = proveedor
            self.proveedor_service = proveedor_service
            layout = QVBoxLayout()

            self.id_proveedor_label = QLabel("ID Proveedor:")
            self.id_proveedor_input = QLineEdit(str(proveedor.id)) 
            self.id_proveedor_input.setReadOnly(True)  
            layout.addWidget(self.id_proveedor_label)
            layout.addWidget(self.id_proveedor_input)

            self.nombre_label = QLabel("Nombre:")
            self.nombre_input = QLineEdit(proveedor.nombre)
            layout.addWidget(self.nombre_label)
            layout.addWidget(self.nombre_input)

            self.direccion_label = QLabel("Dirección:")
            self.direccion_input = QLineEdit(proveedor.direccion)
            layout.addWidget(self.direccion_label)
            layout.addWidget(self.direccion_input)

            self.codigo_postal_label = QLabel("Código Postal:")
            self.codigo_postal_input = QLineEdit(proveedor.cod_postal)
            layout.addWidget(self.codigo_postal_label)
            layout.addWidget(self.codigo_postal_input)

            self.ciudad_label = QLabel("Ciudad:")
            self.ciudad_input = QLineEdit(proveedor.ciudad)
            layout.addWidget(self.ciudad_label)
            layout.addWidget(self.ciudad_input)

            self.provincia_label = QLabel("Provincia:")
            self.provincia_input = QLineEdit(proveedor.provincia)
            layout.addWidget(self.provincia_label)
            layout.addWidget(self.provincia_input)

            self.telefono_label = QLabel("Teléfono:")
            self.telefono_input = QLineEdit(proveedor.telefono)
            layout.addWidget(self.telefono_label)
            layout.addWidget(self.telefono_input)

            self.email_label = QLabel("Correo Electrónico:")
            self.email_input = QLineEdit(proveedor.correo_electronico)
            layout.addWidget(self.email_label)
            layout.addWidget(self.email_input)

            self.comentario_label = QLabel("Comentario:")
            self.comentario_input = QLineEdit(proveedor.comentario)
            layout.addWidget(self.comentario_label)
            layout.addWidget(self.comentario_input)

            self.cuenta_bancaria_label = QLabel("Cuenta Bancaria:")
            self.cuenta_bancaria_input = QLineEdit(proveedor.cuenta_bancaria)
            layout.addWidget(self.cuenta_bancaria_label)
            layout.addWidget(self.cuenta_bancaria_input)

            self.fecha_alta_label = QLabel("Fecha Alta:")
            fecha_alta = QDate.fromString(proveedor.fecha_alta, "yyyy-MM-dd")
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

            self.guardar_button.clicked.connect(self.guardar_proveedor)
            self.cancelar_button.clicked.connect(self.reject)

        def guardar_proveedor(self):
            nuevo_nombre = self.nombre_input.text().strip()
            nuevo_codigo_postal = self.codigo_postal_input.text().strip()
            nueva_direccion = self.direccion_input.text().strip()
            nueva_ciudad = self.ciudad_input.text().strip()
            nueva_provincia = self.provincia_input.text().strip()
            nuevo_telefono = self.telefono_input.text().strip()
            nuevo_correo_electronico = self.email_input.text().strip()
            nuevo_comentario = self.comentario_input.text().strip()
            nueva_cuenta_bancaria = self.cuenta_bancaria_input.text().strip()
            nueva_fecha_alta = self.fecha_alta_input.date().toString("yyyy-MM-dd")

            if nuevo_nombre and nuevo_codigo_postal and nueva_direccion and nueva_ciudad and nueva_provincia and nuevo_telefono and nuevo_correo_electronico and nuevo_comentario and nueva_cuenta_bancaria and nueva_fecha_alta:
                self.proveedor.nombre = nuevo_nombre
                self.proveedor.direccion = nueva_direccion
                self.proveedor.cod_postal = nuevo_codigo_postal
                self.proveedor.ciudad = nueva_ciudad
                self.proveedor.provincia = nueva_provincia
                self.proveedor.telefono = nuevo_telefono
                self.proveedor.correo_electronico = nuevo_correo_electronico
                self.proveedor.comentario = nuevo_comentario
                self.proveedor.cuenta_bancaria = nueva_cuenta_bancaria
                nueva_fecha_alta = datetime.strptime(nueva_fecha_alta, "%Y-%m-%d")
                self.proveedor.fecha_alta = nueva_fecha_alta
                self.accept()  
            else:
                QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
