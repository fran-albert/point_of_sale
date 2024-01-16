from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QAbstractItemView, QTableWidget, QHeaderView, QSizePolicy, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QDialog, QMessageBox
from servicios.proveedor_service import ProveedorService
from entities.proveedor import Proveedor
from .agregar_proveedor import AgregarProveedorDialog
from .editar_proveedor import EditarProveedorDialog

class ListaProveedoresDialog(QDialog):
    def __init__(self, app, rol, parent=None):
        super().__init__(parent)    

        self.app = app
        self.proveedor_service = ProveedorService()
        self.proveedores = self.proveedor_service.obtenerProveedores()

        self.setWindowTitle("Proveedores")

        layout = QVBoxLayout()

        title_label = QLabel("Proveedores")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: green; font-size: 24px")

        layout.addWidget(title_label)

        self.table = QTableWidget(len(self.proveedores), 13)
        self.table.setHorizontalHeaderLabels(["", "Nombre", "Dirección", "Código Postal", "Ciudad", "Provincia", "Teléfono", "Correo Electrónico", "Comentario", "Cuenta Bancaria", "Fecha de Alta", "", ""])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.table.setMinimumHeight(300) 

        for i, prov in enumerate(self.proveedores):
            item_id = QTableWidgetItem(str(prov.id))
            item_nombre = QTableWidgetItem(prov.nombre)
            item_direccion = QTableWidgetItem(prov.direccion)
            item_codigo_postal = QTableWidgetItem(str(prov.codigo_postal))
            item_ciudad = QTableWidgetItem(str(prov.ciudad))
            item_provincia = QTableWidgetItem(str(prov.provincia))
            item_telefono = QTableWidgetItem(str(prov.telefono))
            item_correo_electronico = QTableWidgetItem(str(prov.correo_electronico))
            item_comentario = QTableWidgetItem(str(prov.comentario))
            item_cuenta_bancaria = QTableWidgetItem(prov.cuenta_bancaria)
            item_fecha_alta = QTableWidgetItem(prov.fecha_alta.strftime("%Y-%m-%d"))

            self.table.setItem(i, 0, item_id)
            self.table.setItem(i, 1, item_nombre)
            self.table.setItem(i, 2, item_direccion)
            self.table.setItem(i, 3, item_codigo_postal)
            self.table.setItem(i, 4, item_ciudad)
            self.table.setItem(i, 5, item_provincia)
            self.table.setItem(i, 6, item_telefono)
            self.table.setItem(i, 7, item_correo_electronico)
            self.table.setItem(i, 8, item_comentario)
            self.table.setItem(i, 9, item_cuenta_bancaria)
            self.table.setItem(i, 10, item_fecha_alta)

            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.on_edit_button_clicked)
            self.table.setCellWidget(i, 11, edit_button)

            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.on_delete_button_clicked)
            self.table.setCellWidget(i, 12, delete_button)

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        layout.addWidget(self.table)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(layout)
        self.table.hideColumn(0)
        self.resize(1000, 300)

    def actualizar_tabla(self):
        
        self.proveedores = self.proveedor_service.obtenerProveedores()
        
        self.table.setRowCount(0)
        self.table.setRowCount(len(self.proveedores))

        for i, prov in enumerate(self.proveedores):
            item_id = QTableWidgetItem(str(prov.id))
            item_nombre = QTableWidgetItem(prov.nombre)
            item_direccion = QTableWidgetItem(prov.direccion)
            item_codigo_postal = QTableWidgetItem(str(prov.codigo_postal))
            item_ciudad = QTableWidgetItem(str(prov.ciudad))
            item_provincia = QTableWidgetItem(str(prov.provincia))
            item_telefono = QTableWidgetItem(str(prov.telefono))
            item_correo_electronico = QTableWidgetItem(str(prov.correo_electronico))
            item_comentario = QTableWidgetItem(str(prov.comentario))
            item_cuenta_bancaria = QTableWidgetItem(prov.cuenta_bancaria)
            item_fecha_alta = QTableWidgetItem(prov.fecha_alta.strftime("%Y-%m-%d"))

            self.table.setItem(i, 0, item_id)
            self.table.setItem(i, 1, item_nombre)
            self.table.setItem(i, 2, item_direccion)
            self.table.setItem(i, 3, item_codigo_postal)
            self.table.setItem(i, 4, item_ciudad)
            self.table.setItem(i, 5, item_provincia)
            self.table.setItem(i, 6, item_telefono)
            self.table.setItem(i, 7, item_correo_electronico)
            self.table.setItem(i, 8, item_comentario)
            self.table.setItem(i, 9, item_cuenta_bancaria)
            self.table.setItem(i, 10, item_fecha_alta)

            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.on_edit_button_clicked)
            self.table.setCellWidget(i, 11, edit_button)

            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.on_delete_button_clicked)
            self.table.setCellWidget(i, 12, delete_button)

    def on_edit_button_clicked(self):

        button = self.app.sender()
        index = self.table.indexAt(button.pos())
        proveedor = None

        proveedor_service = ProveedorService()
        
        id = int(self.table.item(index.row(), 0).text())
        nombre = self.table.item(index.row(), 1).text()
        direccion = self.table.item(index.row(), 2).text()
        codigo_postal = self.table.item(index.row(), 3).text()
        ciudad = self.table.item(index.row(), 4).text()
        provincia = self.table.item(index.row(), 5).text()
        telefono = self.table.item(index.row(), 6).text()
        correo_electronico = self.table.item(index.row(), 7).text()
        comentario = self.table.item(index.row(), 8).text()
        cuenta_bancaria = self.table.item(index.row(), 9).text()
        fecha_alta = self.table.item(index.row(), 10).text()     

        proveedor = Proveedor(nombre, direccion, codigo_postal, ciudad, provincia, telefono, correo_electronico, comentario, cuenta_bancaria, fecha_alta)
        proveedor.set_id(id)
        dialog = EditarProveedorDialog(proveedor, proveedor_service)
        result = dialog.exec()

        if result == QDialog.Accepted:
            self.proveedor_service.actualizarProveedor(
                proveedor.nombre,
                proveedor.direccion,
                proveedor.codigo_postal,
                proveedor.ciudad,
                proveedor.provincia,
                proveedor.telefono,
                proveedor.correo_electronico,
                proveedor.comentario,
                proveedor.cuenta_bancaria,
                proveedor.fecha_alta,
                proveedor.id
            )
            self.actualizar_tabla()

    def on_delete_button_clicked(self):
        button = self.app.sender()
        index = self.table.indexAt(button.pos())
        
        id = self.table.item(index.row(), 0).text()
        nombre = self.table.item(index.row(), 1).text()

        respuesta = QMessageBox.question(None, "Confirmación de eliminación", f"¿Está seguro de que desea eliminar el proveedor {nombre}?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.proveedor_service.eliminarProveedor(id)
            self.table.removeRow(index.row())