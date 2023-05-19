from PyQt5.QtWidgets import QDialog, QDateEdit, QAbstractItemView, QSizePolicy, QHeaderView, QVBoxLayout, QLabel, QCheckBox, QTableWidget, QHBoxLayout, QLineEdit, QPushButton, QCalendarWidget, QFrame, QGridLayout, QTableWidgetItem
from PyQt5.QtCore import Qt
from servicios.orden_compra_service import OrdenCompraService
import datetime

class VerOrdenDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.orden_compra_service = OrdenCompraService()
        self.orden_compra = self.orden_compra_service.obtenerOrdenes()

        self.setWindowTitle("Historial de Órdenes de Compra")

        layout = QVBoxLayout()

        title_label = QLabel("Historial de Órdenes de Compra")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: blue; font-size: 24px; font-weight: bold")

        rectangle_frame = QFrame()
        rectangle_frame.setFrameShape(QFrame.StyledPanel)
        rectangle_frame.setFrameShadow(QFrame.Sunken)
        rectangle_frame.setLineWidth(1)

        rectangle_layout = QGridLayout(rectangle_frame)

        desde_fecha_label = QLabel("Fecha desde:")
        self.desde_fecha_input = QDateEdit()
        self.desde_fecha_input.setCalendarPopup(True)

        hasta_fecha_label = QLabel("Fecha hasta:")
        self.hasta_fecha_input = QDateEdit()
        self.hasta_fecha_input.setCalendarPopup(True)

        rectangle_layout.addWidget(desde_fecha_label, 0, 0)
        rectangle_layout.addWidget(self.desde_fecha_input, 0, 1)
        rectangle_layout.addWidget(hasta_fecha_label, 1, 0)
        rectangle_layout.addWidget(self.hasta_fecha_input, 1, 1)

        layout.addWidget(title_label)
        layout.addWidget(rectangle_frame)

        self.tabla = QTableWidget(len(self.orden_compra), 5)
        self.tabla.setHorizontalHeaderLabels(["Id", "Proveedor", "Precio", "Fecha Recepción", "Recibido"])

        for i, orden in enumerate(self.orden_compra):
            item_id = QTableWidgetItem(str(orden.idOrdenCompra))
            item_idProveedor = QTableWidgetItem(str(orden.idProveedor))
            item_precioTotalOrden = QTableWidgetItem("{:.2f}".format(float(orden.precioTotalOrden)))
            item_fechaRecepcion = QTableWidgetItem(orden.fechaRecepcion.strftime("%d-%m-%Y"))

            checkbox_recibido = QCheckBox()
            checkbox_recibido.setChecked(orden.recibido)  # Set checkbox to the value of 'orden.recibido'
            checkbox_recibido.setStyleSheet("margin-left:50%; margin-right:50%;") 

            self.tabla.setItem(i, 0, item_id)
            self.tabla.setItem(i, 1, item_idProveedor)
            self.tabla.setItem(i, 2, item_precioTotalOrden)
            self.tabla.setItem(i, 3, item_fechaRecepcion)
            self.tabla.setCellWidget(i, 4, checkbox_recibido)

        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        layout.addWidget(self.tabla)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(layout)
        self.resize(430, 300)
