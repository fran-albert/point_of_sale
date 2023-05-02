from PyQt5.QtWidgets import QDateEdit, QComboBox, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox
from entities.producto import Producto

class AgregarProductoDialog(QDialog):
    def __init__(self, producto_service, categoria_service, parent=None):
        super().__init__(parent)

        self.producto_service = producto_service
        self.categoria_service = categoria_service

        self.setWindowTitle("Agregar Producto")
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
        self.proveedor_input = QLineEdit()
        layout.addWidget(self.proveedor_label)
        layout.addWidget(self.proveedor_input)

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

    def agregar_producto(self):
        codigo = self.codigo_input.text().strip()
        nombre = self.nombre_input.text().strip()
        precioCompra = self.precio_input.text().strip()
        cant_stock = self.cant_stock_input.text().strip()
        categoria = self.categoria_selector.currentData()
        impuestos = self.impuestos_input.text().strip()
        descuentos = self.descuentos_input.text().strip()
        proveedor = self.proveedor_input.text().strip()
        fecha_venc = self.fecha_venc_input.date().toString("yyyy-MM-dd")

        if codigo and nombre and precioCompra and cant_stock and categoria and impuestos and descuentos and proveedor and fecha_venc:
            try:
                precioCompra = float(precioCompra)
                cant_stock = int(cant_stock)
                impuestos = float(impuestos)
                descuentos = float(descuentos)
                porcentaje = self.categoria_service.obtenerPorcentaje(categoria)
                precioVenta = Producto.calculoPrecioVenta(precioCompra, porcentaje)
                producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, impuestos, descuentos, proveedor, fecha_venc)
                self.producto_service.insertarProducto(producto)
                self.accept()
            except ValueError:
                QMessageBox.warning(self, "Error", "Por favor, ingrese valores válidos.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
