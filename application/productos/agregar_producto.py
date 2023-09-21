from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox
from entities.producto import Producto
from utils.Utils import Utils

class AgregarProductoDialog(QDialog):
    def __init__(self, producto_service, categoria_service, proveedor_service, parent=None):
        super().__init__(parent)

        self.producto_service = producto_service
        self.categoria_service = categoria_service
        self.proveedor_service = proveedor_service

        self.setWindowTitle("Agregar Producto")
        layout = QVBoxLayout()

        nombre = Utils.nombre_usuario

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

        self.proveedor_label = QLabel("Proveedor:")
        self.proveedor_selector = QComboBox()
        proveedores = self.proveedor_service.obtenerProveedores()
        for proveedor in proveedores:
            self.proveedor_selector.addItem(proveedor.nombre, proveedor.id)
        layout.addWidget(self.proveedor_label)
        layout.addWidget(self.proveedor_selector)

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
        proveedor = self.proveedor_selector.currentData()

        if codigo and nombre and precioCompra and cant_stock and categoria and proveedor:
            try:
                precioCompra = float(precioCompra)
                cant_stock = int(cant_stock)
                porcentaje = self.categoria_service.obtenerPorcentaje(categoria)
                precioVenta = Producto.calculoPrecioVenta(precioCompra, porcentaje)
                producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria, proveedor)
                self.producto_service.insertarProducto(producto)
                QMessageBox.information(self, "Información", "Nuevo Producto Añadido")
                self.accept()
            except ValueError:
                QMessageBox.warning(self, "Error", "Por favor, ingrese valores válidos.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
