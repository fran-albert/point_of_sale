from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox
from entities.producto import Producto

class EditarProductoDialog(QDialog):
    def __init__(self, producto, producto_service, categoria_service, proveedor_service, categorias, proveedores, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Editar Producto")

        self.producto_service = producto_service
        self.categoria_service = categoria_service
        self.proveedor_service = proveedor_service

        self.producto = producto
        self.categorias = categorias
        self.proveedores = proveedores
        layout = QVBoxLayout()

        self.codigo_label = QLabel("Código:")
        self.codigo_input = QLineEdit(str(producto.codigo))
        self.codigo_input.setReadOnly(True)
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

        self.proveedor_label = QLabel("Proveedor:")
        self.proveedor_selector = QComboBox()
        for proveedor in self.proveedores:
            self.proveedor_selector.addItem(proveedor.nombre, proveedor.id)
        indice_proveedor = self.proveedor_selector.findData(producto.proveedor)  
        self.proveedor_selector.setCurrentIndex(indice_proveedor) 
        layout.addWidget(self.proveedor_label)
        layout.addWidget(self.proveedor_selector)

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
        nuevo_proveedor = self.proveedor_selector.currentData()

        if nuevo_precioCompra and nuevo_stock and nueva_categoria and nuevo_proveedor and self.producto.codigo and self.producto.nombre:
            try:
                nuevo_precioCompra = float(nuevo_precioCompra)
                nuevo_stock = int(nuevo_stock)

                if nuevo_stock <= 0:
                    QMessageBox.warning(self, "Error", "Cantidad: Debe ser mayor a 0")
                    return
                        
                if nuevo_precioCompra <= 0:
                    QMessageBox.warning(self, "Error", "Precio: Debe ser mayor a 0")
                    return

                self.producto.precioCompra = nuevo_precioCompra
                self.producto.cantStock = nuevo_stock
                self.producto.categoria = nueva_categoria
                self.producto.proveedor = nuevo_proveedor
                porcentaje = self.categoria_service.obtenerPorcentaje(nueva_categoria)
                self.producto.precioVenta = Producto.calculoPrecioVenta(nuevo_precioCompra, porcentaje)
                QMessageBox.information(self, "Información", "Producto Modificado correctamente")
                self.accept()
            except ValueError:
                QMessageBox.warning(self, "Error", "Por favor, ingrese valores válidos.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")

