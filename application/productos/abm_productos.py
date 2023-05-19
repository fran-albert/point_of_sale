import sys
from pathlib import Path
ruta_principal = str(Path(__file__).parent.parent.resolve())
if ruta_principal not in sys.path:
    sys.path.append(ruta_principal)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QScrollArea, QTableWidget, QHeaderView, QSizePolicy, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QDialog, QMessageBox
from servicios.categoria_service import CategoriaService
from servicios.producto_service import ProductoService
from servicios.proveedor_service import ProveedorService
from .agregar_producto import AgregarProductoDialog
from .editar_producto import EditarProductoDialog
from entities.producto import Producto

class ABMProductosWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)    

        self.app = app
        self.producto_service = ProductoService()
        self.proveedor_service = ProveedorService()
        self.categoria_service = CategoriaService()

        self.producto  = self.producto_service.obtenerProductos()
        self.categorias = self.categoria_service.obtenerCategorias()
        self.proveedores = self.proveedor_service.obtenerProveedores()

        self.categoria_descripcion_map = {categoria.id: categoria.descripcion for categoria in self.categorias}
        self.proveedor_nombre_map = {proveedor.id: proveedor.nombre for proveedor in self.proveedores}

        self.table = QTableWidget(len(self.producto), 12)
        self.table.setHorizontalHeaderLabels(["Nombre", "Código", "Precio Compra", "Precio Venta", "Cant Stock", "Categoría", "Impuestos", "Descuentos", "Proveedor", "Fecha Venc", "", ""])

        for i, prod in enumerate(self.producto):
            item_nombre = QTableWidgetItem(prod.nombre)
            item_codigo = QTableWidgetItem(prod.codigo)
            item_precioCompra = QTableWidgetItem(str(prod.precioCompra))
            item_precioVenta = QTableWidgetItem("{:.2f}".format(float(prod.precioVenta)))
            item_cant_stock = QTableWidgetItem(str(prod.cantStock))
            item_categoria = QTableWidgetItem(self.categoria_descripcion_map.get(int(float(prod.categoria)), "Desconocida"))
            item_impuestos = QTableWidgetItem(str(prod.impuestos))
            item_descuentos = QTableWidgetItem(str(prod.descuentos))
            item_proveedor = QTableWidgetItem(self.proveedor_nombre_map.get(int(prod.proveedor), "Desconocido"))
            item_fecha_venc = QTableWidgetItem(prod.fechaVenc.strftime("%Y-%m-%d"))

            self.table.setItem(i, 0, item_nombre)
            self.table.setItem(i, 1, item_codigo)
            self.table.setItem(i, 2, item_precioCompra)
            self.table.setItem(i, 3, item_precioVenta)
            self.table.setItem(i, 4, item_cant_stock)
            self.table.setItem(i, 5, item_categoria)
            self.table.setItem(i, 6, item_impuestos)
            self.table.setItem(i, 7, item_descuentos)
            self.table.setItem(i, 8, item_proveedor)
            self.table.setItem(i, 9, item_fecha_venc)

            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.on_edit_button_clicked)
            self.table.setCellWidget(i, 10, edit_button)

            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.on_delete_button_clicked)
            self.table.setCellWidget(i, 11, delete_button)

        add_product_button = QPushButton("Agregar Producto")
        add_product_button.clicked.connect(self.on_agregar_producto_clicked)

        layout = QVBoxLayout()

        title_label = QLabel("Productos")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: green; font-size: 24px")

        rectangle_frame = QFrame()
        rectangle_frame.setFrameShape(QFrame.StyledPanel)
        rectangle_frame.setFrameShadow(QFrame.Sunken)
        rectangle_frame.setLineWidth(1)

        rectangle_layout = QVBoxLayout(rectangle_frame)
        search_field = QLineEdit()
        search_field.setPlaceholderText("Buscar productos...")
        rectangle_layout.addWidget(search_field)
        rectangle_layout.addWidget(add_product_button)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.table.setMinimumHeight(300) 

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.table)
        scroll_area.setWidgetResizable(True)

        layout.addWidget(title_label)
        layout.addWidget(rectangle_frame)
        layout.addWidget(scroll_area)
        layout.addStretch(1) 

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)
        self.setWindowTitle("Productos")
        self.setGeometry(100, 100, 900, 400)  # x, y, ancho, alto
        screen = QDesktopWidget().availableGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)


    def actualizar_tabla(self):

        self.productos = self.producto_service.obtenerProductos()
        self.proveedores = self.proveedor_service.obtenerProveedores()
        self.categorias = self.categoria_service.obtenerCategorias()

        categoria_descripcion_map = {categoria.id: categoria.descripcion for categoria in self.categorias}
        proveedor_nombre_map = {proveedor.id: proveedor.nombre for proveedor in self.proveedores}

        self.table.setRowCount(0)
        self.table.setRowCount(len(self.productos))

        for i, prod in enumerate(self.productos):
            item_nombre = QTableWidgetItem(prod.nombre)
            item_codigo = QTableWidgetItem(prod.codigo)
            item_precioCompra = QTableWidgetItem(str(prod.precioCompra))
            item_precioVenta = QTableWidgetItem("{:.2f}".format(float(prod.precioVenta)))
            item_cant_stock = QTableWidgetItem(str(prod.cantStock))
            item_categoria = QTableWidgetItem(categoria_descripcion_map.get(int(float(prod.categoria)), "Desconocida"))
            item_impuestos = QTableWidgetItem(str(prod.impuestos))
            item_descuentos = QTableWidgetItem(str(prod.descuentos))
            item_proveedor = QTableWidgetItem(proveedor_nombre_map.get(int(prod.proveedor), "Desconocido"))
            item_fecha_venc = QTableWidgetItem(prod.fechaVenc.strftime("%Y-%m-%d"))

            self.table.setItem(i, 0, item_nombre)
            self.table.setItem(i, 1, item_codigo)
            self.table.setItem(i, 2, item_precioCompra)
            self.table.setItem(i, 3, item_precioVenta)
            self.table.setItem(i, 4, item_cant_stock)
            self.table.setItem(i, 5, item_categoria)
            self.table.setItem(i, 6, item_impuestos)
            self.table.setItem(i, 7, item_descuentos)
            self.table.setItem(i, 8, item_proveedor)
            self.table.setItem(i, 9, item_fecha_venc)

            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.on_edit_button_clicked)
            self.table.setCellWidget(i, 10, edit_button)

            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.on_delete_button_clicked)
            self.table.setCellWidget(i, 11, delete_button)

    def on_agregar_producto_clicked(self):
        dialog = AgregarProductoDialog(self.producto_service, self.categoria_service, self.proveedor_service)
        result = dialog.exec()

        if result == QDialog.Accepted:
            self.actualizar_tabla()

    def on_edit_button_clicked(self):
        
        button = self.app.sender()
        index = self.table.indexAt(button.pos())

        producto = None
        
        categorias = self.categoria_service.obtenerCategorias()
        categoria_service = CategoriaService()
        producto_service = ProductoService()
        categoria_descripcion_id_map = {categoria.descripcion: categoria.id for categoria in categorias}
        
        nombre = self.table.item(index.row(), 0).text()
        codigo = self.table.item(index.row(), 1).text()
        precioCompra = self.table.item(index.row(), 2).text()
        precioVenta = self.table.item(index.row(), 3).text()
        cant_stock = self.table.item(index.row(), 4).text()
        categoria_descripcion = self.table.item(index.row(), 5).text()
        categoria_id = categoria_descripcion_id_map.get(categoria_descripcion)
        impuestos = self.table.item(index.row(), 6).text()
        descuentos = self.table.item(index.row(), 7).text()
        proveedor = self.table.item(index.row(), 8).text()
        fecha_venc = self.table.item(index.row(), 9).text()          
        producto = Producto(codigo, nombre, precioCompra, precioVenta, cant_stock, categoria_id, impuestos, descuentos, proveedor, fecha_venc)
        dialog = EditarProductoDialog(producto, producto_service, categoria_service, categorias )
        result = dialog.exec()

        if result == QDialog.Accepted:
            self.producto_service.actualizarProducto(
                producto.codigo,
                producto.nombre,
                producto.precioCompra,
                producto.precioVenta,
                producto.cantStock,
                producto.categoria,
                producto.impuestos,
                producto.descuentos,
                producto.proveedor,
                producto.fechaVenc,
                producto.codigo
            )
            self.actualizar_tabla()

    def on_delete_button_clicked(self):

        button = self.app.sender()
        index = self.table.indexAt(button.pos())
        producto_codigo = self.table.item(index.row(), 1).text()

        respuesta = QMessageBox.question(None, "Confirmación de eliminación", f"¿Está seguro de que desea eliminar el producto con código {producto_codigo}?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.producto_service.eliminarProducto(producto_codigo)
            self.table.removeRow(index.row())