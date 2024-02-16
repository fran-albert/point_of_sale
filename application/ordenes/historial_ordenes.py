from PyQt5.QtWidgets import QDialog, QDateEdit, QAbstractItemView, QSizePolicy, QHeaderView, QVBoxLayout, QLabel, QCheckBox, QTableWidget, QHBoxLayout, QLineEdit, QPushButton, QCalendarWidget, QFrame, QGridLayout, QTableWidgetItem
from PyQt5.QtCore import Qt
from servicios.orden_compra_service import OrdenCompraService
from servicios.proveedor_service import ProveedorService
from servicios.producto_service import ProductoService
from servicios.productos_pedidos_service import ProductoPedidoService

class VerOrdenDialog(QDialog):
    def __init__(self, fecha_desde, fecha_hasta, parent=None):
        super().__init__(parent)
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta

        self.orden_compra_service = OrdenCompraService()
        self.proveedor_service = ProveedorService()
        self.producto_service = ProductoService()
        self.productos_pedidos = ProductoPedidoService()

        self.proveedores = self.proveedor_service.obtenerProveedores()
        self.orden_compra = self.orden_compra_service.obtenerOrdenes(self.fecha_desde, self.fecha_hasta)

        self.setWindowTitle("Historial de Órdenes de Compra")

        layout = QVBoxLayout()

        title_label = QLabel("Historial de Órdenes de Compra")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: blue; font-size: 24px; font-weight: bold")

        rectangle_frame = QFrame()
        rectangle_frame.setFrameShape(QFrame.StyledPanel)
        rectangle_frame.setFrameShadow(QFrame.Sunken)
        rectangle_frame.setLineWidth(1)

        layout.addWidget(title_label)
        layout.addWidget(rectangle_frame)

        self.tabla = QTableWidget(len(self.orden_compra), 5)
        self.tabla.setHorizontalHeaderLabels(["Id", "Proveedor", "Precio Compra", "Fecha Recepción", "Recibido"])
        self.tabla.setColumnWidth(0, 20)

        fecha_desde_label = QLabel(f"Fecha Desde: {self.fecha_desde}")
        fecha_hasta_label = QLabel(f"Fecha Hasta: {self.fecha_hasta}")
        layout.addWidget(fecha_desde_label)
        layout.addWidget(fecha_hasta_label)

        self.proveedor_nombre_map = {proveedor.id: proveedor.nombre for proveedor in self.proveedores}
        self.ordenes_checkboxes = [] 
        
        for i, orden in enumerate(self.orden_compra):
            item_id = QTableWidgetItem(str(orden.id))
            item_idProveedor = QTableWidgetItem(self.proveedor_nombre_map.get(int(orden.id_proveedor), "Desconocido"))
            item_precioTotalOrden = QTableWidgetItem("{:.2f}".format(float(orden.precio_total_orden)))
            item_fechaRecepcion = QTableWidgetItem(orden.fecha_recepcion.strftime("%d-%m-%Y"))

            checkbox_recibido = QCheckBox()
            checkbox_recibido.setChecked(orden.recibido)  
            checkbox_recibido.setStyleSheet("margin-left:50%; margin-right:50%;")
            
            if orden.recibido:
                checkbox_recibido.setEnabled(False)

            self.ordenes_checkboxes.append(checkbox_recibido)

            self.tabla.setItem(i, 0, item_id)
            self.tabla.setItem(i, 1, item_idProveedor)
            self.tabla.setItem(i, 2, item_precioTotalOrden)
            self.tabla.setItem(i, 3, item_fechaRecepcion)
            self.tabla.setCellWidget(i, 4, checkbox_recibido)

        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        layout.addWidget(self.tabla)

        guardar_btn = QPushButton("Guardar cambios")
        guardar_btn.setFixedWidth(100)
        guardar_btn.setFixedHeight(25)
        layout.addWidget(guardar_btn, alignment=Qt.AlignCenter)
        guardar_btn.clicked.connect(self.guardar_cambios)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(layout)
        self.resize(500, 500)
    
    def guardar_cambios(self):
        for i, checkbox in enumerate(self.ordenes_checkboxes):
            idOrdenCompra = self.orden_compra[i].id
            recibido = checkbox.isChecked()
            if recibido:
                prod_pedidos = self.productos_pedidos.obtenerProductosPedidos(idOrdenCompra)
                for prod_pedido in prod_pedidos:
                    self.producto_service.actualizarStockOrdenCompra(prod_pedido.codigo, prod_pedido.cantidad_pedida)
                self.orden_compra_service.actualizarOrden(idOrdenCompra, recibido)
                checkbox.setEnabled(False)