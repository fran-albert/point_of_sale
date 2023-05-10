from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox, QDateEdit
from PyQt5.QtGui import QColor, QPalette

class EditarProveedorDialog(QDialog):
        def __init__(self, proveedor, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Editar Proveedor")

            self.proveedor = proveedor
            layout = QVBoxLayout()

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
            self.fecha_alta_input = QDateEdit(proveedor.fecha_alta)
            layout.addWidget(self.fecha_alta_label)
            layout.addWidget(self.fecha_alta_input)

            # palette = self.idProveedor_input.palette()
            # palette.setColor(QPalette.Base, QColor(240, 240, 240))
            # self.idProveedor_input.setPalette(palette)

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
            self.proveedor.nombre = self.nombre_input.text().strip()
            self.proveedor.co = self.codigo_postal_label.text().strip()
            self.proveedor.direccion = self.direccion_label.text().strip()
            # nuevo_precioCompra = self.precioCompra_input.text().strip()
            # nuevo_stock = self.stock_input.text().strip()
            # nueva_categoria = self.categoria_combo.currentData()
            # nuevos_impuestos = self.impuestos_input.text().strip()

            if self.proveedor.nombre: #nuevo_precioCompra and nuevo_stock and nuevos_impuestos:
                try:
                    # nuevo_precioCompra = float(nuevo_precioCompra)
                    # nuevo_stock = int(nuevo_stock)
                    # nuevos_impuestos = float(nuevos_impuestos)
                    # self.producto.precioCompra = nuevo_precioCompra
                    # self.producto.cantStock = nuevo_stock
                    # self.producto.categoria = nueva_categoria
                    # self.producto.impuestos = nuevos_impuestos
                    # porcentaje = self.categoria_service.obtenerPorcentaje(nueva_categoria)
                    # self.producto.precioVenta = Producto.calculoPrecioVenta(nuevo_precioCompra, porcentaje)
                    self.accept()
                except ValueError:
                    QMessageBox.warning(self, "Error", "Por favor, ingrese valores válidos.")
            else:
                QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
