from PyQt5.QtWidgets import QDialog, QDateEdit, QCompleter, QAbstractItemView, QSizePolicy, QSpinBox, QHeaderView, QVBoxLayout, QLabel, QComboBox, QTableWidget, QHBoxLayout, QLineEdit, QPushButton, QCalendarWidget, QFrame, QGridLayout, QTableWidgetItem
from PyQt5.QtCore import Qt
from servicios.productos_pedidos_service import ProductoPedidoService
from entities.orden_compra import OrdenCompra
from entities.productos_pedidos import ProductosPedidos

class VerOrdenDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
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

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["Id", "Proveedor", "Precio", "Recibido"])
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        layout.addWidget(self.tabla)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(layout)
        self.resize(430, 300)