from PyQt5.QtWidgets import QDateEdit, QComboBox, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox
from PyQt5.QtCore import  QDate
from entities.producto import Producto


class EditarProductoDialog(QDialog):
    def __init__(self, producto,producto_service, categoria_service, categorias, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Editar Producto")


        self.producto_service = producto_service
        self.categoria_service = categoria_service

        self.producto = producto
        self.categorias = categorias
        layout = QVBoxLayout()

        self.codigo_label = QLabel("Código:")
        self.codigo_input = QLineEdit(str(producto.codigo))
        layout.addWidget(self.codigo_label)
        layout.addWidget(self.codigo_input)

        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit(str(producto.nombre))
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)

        self.precioCompra_label = QLabel("Precio de Compra:")
        self.precioCompra_input = QLineEdit(str(producto.precioCompra))
        layout.addWidget(self.precioCompra_label)
        layout.addWidget(self.precioCompra_input)

        self.stock_label = QLabel("Cantidad en Stock:")
        self.stock_input = QLineEdit(str(producto.cantStock))
        layout.addWidget(self.stock_label)
        layout.addWidget(self.stock_input)

        self.categoria_label = QLabel("Categoría:")
        self.categoria_combo = QComboBox()
        for categoria in self.categorias:
            self.categoria_combo.addItem(categoria.descripcion, categoria.id)
        index = self.categoria_combo.findData(producto.categoria)
        self.categoria_combo.setCurrentIndex(index)
        layout.addWidget(self.categoria_label)
        layout.addWidget(self.categoria_combo)

        self.impuestos_label = QLabel("Impuestos:")
        self.impuestos_input = QLineEdit(str(producto.impuestos))
        layout.addWidget(self.impuestos_label)
        layout.addWidget(self.impuestos_input)

        self.descuentos_label = QLabel("Descuentos:")
        self.descuentos_input = QLineEdit(str(producto.descuentos))
        layout.addWidget(self.descuentos_label)
        layout.addWidget(self.descuentos_input)

        self.proveedor_label = QLabel("Proveedor:")
        self.proveedor_input = QLineEdit(str(producto.proveedor))
        layout.addWidget(self.proveedor_label)
        layout.addWidget(self.proveedor_input)

        self.fechaVenc_label = QLabel("Fecha Vencimiento:")
        self.fechaVenc_input = QDateEdit(QDate.fromString(producto.fechaVenc, "yyyy-MM-dd"))
        layout.addWidget(self.fechaVenc_label)
        layout.addWidget(self.fechaVenc_input)

        self.buttons_layout = QHBoxLayout()
        self.guardar_button = QPushButton("Guardar")
        self.cancelar_button = QPushButton("Cancelar")
        self.buttons_layout.addWidget(self.guardar_button)
        self.buttons_layout.addWidget(self.cancelar_button)

        layout.addLayout(self.buttons_layout)
        self.setLayout(layout)

        self.guardar_button.clicked.connect(self.guardar_producto)
        self.cancelar_button.clicked.connect(self.reject)

    def guardar_producto(self):
        self.producto.codigo = self.codigo_input.text().strip()
        self.producto.nombre = self.nombre_input.text().strip()
        nuevo_precioCompra = self.precioCompra_input.text().strip()
        nuevo_stock = self.stock_input.text().strip()
        nueva_categoria = self.categoria_combo.currentData()
        nuevos_impuestos = self.impuestos_input.text().strip()

        if nuevo_precioCompra and nuevo_stock and nuevos_impuestos:
            try:
                nuevo_precioCompra = float(nuevo_precioCompra)
                nuevo_stock = int(nuevo_stock)
                nuevos_impuestos = float(nuevos_impuestos)
                self.producto.precioCompra = nuevo_precioCompra
                self.producto.cantStock = nuevo_stock
                self.producto.categoria = nueva_categoria
                self.producto.impuestos = nuevos_impuestos
                porcentaje = self.categoria_service.obtenerPorcentaje(nueva_categoria)
                self.producto.precioVenta = Producto.calculoPrecioVenta(nuevo_precioCompra, porcentaje)
                self.accept()
            except ValueError:
                QMessageBox.warning(self, "Error", "Por favor, ingrese valores válidos.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")

