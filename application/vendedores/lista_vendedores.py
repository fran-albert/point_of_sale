from PyQt5.QtWidgets import QDialog, QAbstractItemView, QSizePolicy, QHeaderView, QVBoxLayout, QLabel, QMessageBox, QTableWidget, QHBoxLayout, QLineEdit, QPushButton, QCalendarWidget, QFrame, QGridLayout, QTableWidgetItem
from PyQt5.QtCore import Qt
from servicios.vendedores_service import VendedorService
from vendedores.editar_vendedor import EditarVendedorDialog
from entities.vendedor import Vendedor


class ListaVendedoresDialog(QDialog):
    def __init__(self, app, current_username, current_password, parent=None):
        super().__init__(parent)

        self.app = app
        self.vendedores_service = VendedorService()
        self.vendedores = self.vendedores_service.obtenerVendedores()
        self.current_username = current_username
        self.current_password = current_password
        self.vendedor_rol = self.vendedores_service.obtenerRol(current_username, current_password)

        self.setWindowTitle("Lista de Vendedores")

        layout = QVBoxLayout()

        title_label = QLabel("Lista de Vendedores")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #4C4C6D; font-size: 24px; font-weight: bold")

        rectangle_frame = QFrame()
        rectangle_frame.setFrameShape(QFrame.StyledPanel)
        rectangle_frame.setFrameShadow(QFrame.Sunken)
        rectangle_frame.setLineWidth(1)

        layout.addWidget(title_label)
        layout.addWidget(rectangle_frame)

        self.table = QTableWidget(len(self.vendedores), 11)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido", "DNI", "Teléfono", "Correo Electrónico", "Fecha Nacimiento", "Fecha Alta", "Rol", "", ""])
        self.table.setColumnWidth(0, 20)
        self.table.setColumnWidth(5, 150)
        self.table.setColumnWidth(6, 120)
        self.table.hideColumn(0)

        if self.vendedor_rol == 0:
            self.table.hideColumn(9)  
            self.table.hideColumn(10)

        for i, vend in enumerate(self.vendedores):
            item_id = QTableWidgetItem(str(vend.id))
            item_nombre = QTableWidgetItem(vend.nombre)
            item_apellido = QTableWidgetItem(vend.apellido)
            item_dni = QTableWidgetItem(str(vend.dni))
            item_telefono = QTableWidgetItem(str(vend.telefono))
            item_correo = QTableWidgetItem(vend.correo)
            item_fecha_nacimiento = QTableWidgetItem(vend.fecha_nac.strftime("%Y-%m-%d"))
            item_fecha_alta = QTableWidgetItem(vend.fecha_alta.strftime("%Y-%m-%d"))
            item_admin = QTableWidgetItem(str(vend.admin) == "1" and "Administrador" or "Vendedor")

            self.table.setItem(i, 0, item_id)
            self.table.setItem(i, 1, item_nombre)
            self.table.setItem(i, 2, item_apellido)
            self.table.setItem(i, 3, item_dni)
            self.table.setItem(i, 4, item_telefono)
            self.table.setItem(i, 5, item_correo)
            self.table.setItem(i, 6, item_fecha_nacimiento)
            self.table.setItem(i, 7, item_fecha_alta)
            self.table.setItem(i, 8, item_admin)

            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.on_edit_button_clicked)
            self.table.setCellWidget(i, 9, edit_button)

            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.on_delete_button_clicked)
            self.table.setCellWidget(i, 10, delete_button)

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        layout.addWidget(self.table)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(layout)
        self.resize(1000, 500)

    def actualizar_tabla(self):

        self.table.setRowCount(0)
        self.vendedores = self.vendedores_service.obtenerVendedores()
        self.table.setRowCount(len(self.vendedores))

        for i, vend in enumerate(self.vendedores):
            item_id = QTableWidgetItem(str(vend.id))
            item_nombre = QTableWidgetItem(vend.nombre)
            item_apellido = QTableWidgetItem(vend.apellido)
            item_dni = QTableWidgetItem(str(vend.dni))
            item_telefono = QTableWidgetItem(str(vend.telefono))
            item_correo = QTableWidgetItem(vend.correo)
            item_fecha_nacimiento = QTableWidgetItem(vend.fecha_nac.strftime("%Y-%m-%d"))
            item_fecha_alta = QTableWidgetItem(vend.fecha_alta.strftime("%Y-%m-%d"))
            item_admin = QTableWidgetItem(str(vend.admin) == "1" and "Administrador" or "Vendedor")

            self.table.setItem(i, 0, item_id)
            self.table.setItem(i, 1, item_nombre)
            self.table.setItem(i, 2, item_apellido)
            self.table.setItem(i, 3, item_dni)
            self.table.setItem(i, 4, item_telefono)
            self.table.setItem(i, 5, item_correo)
            self.table.setItem(i, 6, item_fecha_nacimiento)
            self.table.setItem(i, 7, item_fecha_alta)
            self.table.setItem(i, 8, item_admin)

            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.on_edit_button_clicked)
            self.table.setCellWidget(i, 9, edit_button)

            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.on_delete_button_clicked)
            self.table.setCellWidget(i, 10, delete_button)

    def on_edit_button_clicked(self):

        button = self.sender()
        index = self.table.indexAt(button.pos())
        vendedor = None

        vendedor_service = VendedorService()
        
        id = int(self.table.item(index.row(), 0).text())
        nombre = self.table.item(index.row(), 1).text()
        apellido = self.table.item(index.row(), 2).text()
        dni = self.table.item(index.row(), 3).text()
        telefono = self.table.item(index.row(), 4).text()
        correo = self.table.item(index.row(), 5).text()
        fecha_nac = self.table.item(index.row(), 6).text()
        fecha_alta = self.table.item(index.row(), 7).text()
        admin = self.table.item(index.row(), 8).text()

        vendedor = Vendedor(dni, nombre, apellido, telefono, correo, fecha_nac, fecha_alta, admin)
        vendedor.set_id(id)

        dialog = EditarVendedorDialog(vendedor, vendedor_service)
        result = dialog.exec()

        if result == QDialog.Accepted:
            self.vendedores_service.actualizarVendedor(
                vendedor.dni,
                vendedor.nombre,
                vendedor.apellido,
                vendedor.telefono,
                vendedor.correo,
                vendedor.fecha_nac,
                vendedor.fecha_alta,
                vendedor.admin,
                vendedor.id
            )
            self.actualizar_tabla()


    def on_delete_button_clicked(self):
        button = self.app.sender()
        index = self.table.indexAt(button.pos())
        
        id = self.table.item(index.row(), 0).text()
        nombre = self.table.item(index.row(), 1).text()

        respuesta = QMessageBox.question(None, "Confirmación de eliminación", f"¿Está seguro de que desea eliminar el vendedor {nombre}?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.vendedores_service.eliminarVendedor(id)
            self.table.removeRow(index.row())