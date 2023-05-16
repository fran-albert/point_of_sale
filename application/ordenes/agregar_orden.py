import sys
sys.path.append('C:\\Users\\Francisco\\Documents\\point_of_sale')
from PyQt5.QtWidgets import QDateEdit, QComboBox, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from datetime import datetime


class AgregarOrdenDialog(QDialog):
    def __init__(self, producto_service, categoria_service, proveedor_service, parent=None):
        super().__init__(parent)

        self.producto_service = producto_service
        self.categoria_service = categoria_service
        self.proveedor_service = proveedor_service

        self.setWindowTitle("Nueva Orden de Compra")
        layout = QVBoxLayout()

        self.codigo_label = QLabel("Código:")
        self.codigo_input = QLineEdit()
        layout.addWidget(self.codigo_label)
        layout.addWidget(self.codigo_input)

        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)

        self.precio_label = QLabel("Precio Compra:")
        self.precio_input = QLineEdit()
        layout.addWidget(self.precio_label)
        layout.addWidget(self.precio_input)

        self.cant_stock_label = QLabel("Cantidad en Stock:")
        self.cant_stock_input = QLineEdit()
        layout.addWidget(self.cant_stock_label)
        layout.addWidget(self.cant_stock_input)

        self.categoria_label = QLabel("Categoría:")
        self.categoria_selector = QComboBox()
        categorias = self.categoria_service.obtenerCategorias()
        for categoria in categorias:
            self.categoria_selector.addItem(categoria.descripcion, categoria.id)
        layout.addWidget(self.categoria_label)
        layout.addWidget(self.categoria_selector)

        self.impuestos_label = QLabel("Impuestos:")
        self.impuestos_input = QLineEdit()
        layout.addWidget(self.impuestos_label)
        layout.addWidget(self.impuestos_input)

        self.descuentos_label = QLabel("Descuentos:")
        self.descuentos_input = QLineEdit()
        layout.addWidget(self.descuentos_label)
        layout.addWidget(self.descuentos_input)

        self.proveedor_label = QLabel("Proveedor:")
        self.proveedor_selector = QComboBox()
        proveedores = self.proveedor_service.obtenerProveedores()
        for proveedor in proveedores:
            self.proveedor_selector.addItem(proveedor.nombre, proveedor.id)
        layout.addWidget(self.proveedor_label)
        layout.addWidget(self.proveedor_selector)

        self.fecha_venc_label = QLabel("Fecha de Vencimiento:")
        self.fecha_venc_input = QDateEdit()
        layout.addWidget(self.fecha_venc_label)
        layout.addWidget(self.fecha_venc_input)

        self.buttons_layout = QHBoxLayout()
        self.agregar_button = QPushButton("Agregar")
        self.cancelar_button = QPushButton("Cancelar")
        self.buttons_layout.addWidget(self.agregar_button)
        self.buttons_layout.addWidget(self.cancelar_button)

        layout.addLayout(self.buttons_layout)
        self.setLayout(layout)

        self.agregar_button.clicked.connect(self.agregar_producto)
        self.cancelar_button.clicked.connect(self.reject)


    # def agregar_proveedor(self):
    #     nombre = self.nombre_input.text().strip()
    #     direccion = self.direccion_input.text().strip()
    #     codigo_postal = self.codigo_postal_input.text().strip()
    #     ciudad = self.ciudad_input.text().strip()
    #     provincia = self.provincia_input.text().strip()
    #     telefono = self.telefono_input.text().strip()
    #     email = self.email_input.text().strip()
    #     comentario = self.comentario_input.text().strip()
    #     cuenta_bancaria = self.cuenta_bancaria_input.text().strip()
    #     fecha_alta = self.fecha_alta_input.date().toString("yyyy-MM-dd")

    #     if nombre and direccion and codigo_postal and ciudad and provincia and telefono and email and cuenta_bancaria and fecha_alta:
    #         try:
    #             fecha_alta = datetime.strptime(fecha_alta, "%Y-%m-%d")
    #             #proveedor = Proveedor(nombre, direccion, codigo_postal, ciudad, provincia, telefono, email, comentario, cuenta_bancaria, fecha_alta)
    #             #self.proveedor_service.insertarProveedor(proveedor)
    #             self.accept()
    #         except ValueError:
    #             QMessageBox.warning(self, "Error", "Por favor, ingrese una fecha válida en formato YYYY-MM-DD.")
    #     else:
    #         QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
