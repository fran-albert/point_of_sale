import sys
from pathlib import Path
from application.ventas.CierreCajonDinero import CierreCajonDinero
from entities.productos_vendido import ProductosVendido
ruta_principal = str(Path(__file__).parent.parent.resolve())
if ruta_principal not in sys.path:
    sys.path.append(ruta_principal)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QSpinBox, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QMessageBox
from servicios.producto_service import ProductoService
from utils.Utils import Utils
from ventas.ventas_utils_buttons import VentasUtilsButtons

class VentasWindow(QMainWindow):
    def __init__(self, usuario, app, parent=None):
        super().__init__(parent)

        self.app = app
        self.producto_service = ProductoService()
        self.Utils = Utils()
        self.total = 0
        self.ventas_utils_buttons = VentasUtilsButtons(self)

        self.setWindowTitle("Ventas")
        self.setGeometry(100, 100, 600, 300)

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        title_label = QLabel("Ventas")
        title_label.setAlignment(Qt.AlignCenter)
        font = title_label.font()
        font.setPointSize(24)  
        font.setBold(True)    
        title_label.setFont(font)
        main_layout.addWidget(title_label)

        buttons_layout = QHBoxLayout()
        for button_text in ["Mov. de Caja", "Cierre Cajón Dinero", "Cancelar"]:
            button = QPushButton(button_text)
            button.setFixedWidth(120)
            buttons_layout.addWidget(button)
            if button_text == "Cierre Cajón Dinero":
                button.clicked.connect(self.mostrar_ventana_cierre_cajon_dinero) 
            if button_text == "Cancelar":
                button.clicked.connect(self.close)
        buttons_layout.addStretch()  

        main_layout.addLayout(buttons_layout)

        input_layout = QHBoxLayout()

        self.codigo_input = QLineEdit()
        self.codigo_input.setPlaceholderText("Código del producto")
        input_layout.addWidget(self.codigo_input)

        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre del producto")
        input_layout.addWidget(self.nombre_input)

        main_layout.addLayout(input_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Código", "Descripción", "Cantidad", "Precio Unitario", "Precio Total"])
        self.table.setColumnWidth(0, 100) 
        self.table.setColumnWidth(1, 400)  
        self.table.setColumnWidth(2, 80)   
        self.table.setColumnWidth(3, 100)  
        self.table.setColumnWidth(4, 100) 
        main_layout.addWidget(self.table)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.table.setMinimumWidth(800)
        self.table.setMaximumHeight(300)

        totals_layout = QVBoxLayout()

        self.subtotal_label = QLabel("Subtotal: ")
        self.iva_label = QLabel("I.V.A: ")
        self.total_label = QLabel("Total: ")

        totals_layout.addWidget(self.subtotal_label, alignment=Qt.AlignRight)
        totals_layout.addWidget(self.iva_label, alignment=Qt.AlignRight)
        totals_layout.addWidget(self.total_label, alignment=Qt.AlignRight)

        main_layout.addLayout(totals_layout)

        cobrar_button = QPushButton("Cobrar")
        cobrar_button.clicked.connect(lambda: self.ventas_utils_buttons.show_payment_window(usuario, self.total, self, self.lista_productos_vendidos(self.table)))

        main_layout.addWidget(cobrar_button, alignment=Qt.AlignRight)

        self.codigo_input.textChanged.connect(self.on_codigo_input_text_changed)
    def lista_productos_vendidos(self, table) :
        productos_vendidos = []
        for row in range(table.rowCount()):
            row_data = []
            for column in range(table.columnCount()):
                cell = table.item(row, column)
                if cell is not None:
                    cell_value = str(table.item(row, column).text())
                    row_data.append(cell_value)
                else:
                    cantidad_spinbox = table.cellWidget(row, column)
                    cantidad_spinbox.value()
                    row_data.append(cantidad_spinbox.value())
            producto_vendido = ProductosVendido(None, None, row_data[1],  row_data[0],  row_data[2],  row_data[3],  row_data[4])
            productos_vendidos.append(producto_vendido)
        return productos_vendidos

    def show_payment_window(self):
        VentasUtilsButtons.show_payment_window(self)

    def on_codigo_input_text_changed(self, text):
        if self.sender() and self.sender().objectName() == "codigo_input_clear":
            return

        if text:  
            producto = self.producto_service.obtenerProducto(text)

            if producto is not None:
                if self.producto_ya_existe(producto):
                    QMessageBox.warning(self, "Error", "El producto ya está ingresado.")
                else:
                    self.agregar_producto_a_tabla(producto)
                    self.codigo_input.setObjectName("codigo_input_clear")  
                    self.codigo_input.clear()
                    self.nombre_input.clear()
                    self.codigo_input.setObjectName("") 

    def producto_ya_existe(self, producto):
        for row in range(self.table.rowCount()):
            if self.table.item(row, 0).text() == producto.codigo:
                return True
        return False

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            selected_rows = sorted(set(item.row() for item in self.table.selectedItems()))
            for row in reversed(selected_rows):
                self.table.removeRow(row)
            self.update_totals()

    def agregar_producto_a_tabla(self, producto):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, self.create_read_only_table_widget_item(producto.codigo))
        self.table.setItem(row_count, 1, self.create_read_only_table_widget_item(producto.nombre))

        cantidad_spinbox = QSpinBox()
        cantidad_spinbox.setValue(1)
        cantidad_spinbox.valueChanged.connect(lambda value, row=row_count: self.update_precio_total(value, row))
        self.table.setCellWidget(row_count, 2, cantidad_spinbox)

        self.table.setItem(row_count, 3, self.create_read_only_table_widget_item(str(producto.precioVenta)))

        precio_total = producto.precioVenta
        self.table.setItem(row_count, 4, self.create_read_only_table_widget_item(str(precio_total)))

        self.update_totals()  

    def create_read_only_table_widget_item(self, text):
        item = QTableWidgetItem(text)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        return item

    def update_precio_total(self, cantidad, row):
        precio_unitario = float(self.table.item(row, 3).text())
        precio_total = precio_unitario * cantidad
        precio_total_str = "{:.2f}".format(precio_total)  
        self.table.setItem(row, 4, self.create_read_only_table_widget_item(precio_total_str))
        self.update_totals()  

    def update_totals(self):
        subtotal = 0.0
        for row in range(self.table.rowCount()):
            precio_total = float(self.table.item(row, 4).text())
            subtotal += precio_total

        iva = subtotal * 0.21
        total = subtotal + iva

        self.subtotal_label.setText("Subtotal: {:.2f}".format(subtotal))
        self.iva_label.setText("I.V.A: {:.2f}".format(iva))
        self.total_label.setText("Total: {:.2f}".format(total))

        self.total = total

    def mostrar_ventana_cierre_cajon_dinero(self):
        cierre_cajon_dinero = CierreCajonDinero(self)
        cierre_cajon_dinero.exec_()