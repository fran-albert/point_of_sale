from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QScrollArea, QTableWidget, QHeaderView, QSizePolicy, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QDialog, QMessageBox
from servicios.proveedor_service import ProveedorService
from entities.proveedor import Proveedor
from .agregar_proveedor import AgregarProveedorDialog
from .editar_proveedor import EditarProveedorDialog

class ABMProveedoresWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)    

        self.app = app
        self.proveedor_service = ProveedorService()
        self.proveedores = self.proveedor_service.obtenerProveedores()

        self.table = QTableWidget(len(self.proveedores), 13)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Dirección", "Código Postal", "Ciudad", "Provincia", "Teléfono", "Correo Electrónico", "Comentario", "Cuenta Bancaria", "Fecha de Alta", "", ""])

        # Rellena la tabla con los proveedores actualizados
        for i, prov in enumerate(self.proveedores):
            item_id = QTableWidgetItem(str(prov.id))
            item_nombre = QTableWidgetItem(prov.nombre)
            item_direccion = QTableWidgetItem(prov.direccion)
            item_cod_postal = QTableWidgetItem(str(prov.cod_postal))
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
            self.table.setItem(i, 3, item_cod_postal)
            self.table.setItem(i, 4, item_ciudad)
            self.table.setItem(i, 5, item_provincia)
            self.table.setItem(i, 6, item_telefono)
            self.table.setItem(i, 7, item_correo_electronico)
            self.table.setItem(i, 8, item_comentario)
            self.table.setItem(i, 9, item_cuenta_bancaria)
            self.table.setItem(i, 10, item_fecha_alta)

            # Botón Editar
            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.on_edit_button_clicked)
            self.table.setCellWidget(i, 11, edit_button)

            # Botón Eliminar
            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.on_delete_button_clicked)
            self.table.setCellWidget(i, 12, delete_button)

        # Crear un botón Agregar Proveedor
        add_proveedor_button = QPushButton("Agregar Proveedor")
        add_proveedor_button.clicked.connect(self.on_agregar_proveedor_clicked)

        # Crear un layout vertical
        layout = QVBoxLayout()

        # Crear un QLabel para el título
        title_label = QLabel("Proveedores")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: green; font-size: 24px")

        #Crear un QFrame para el rectángulo
        rectangle_frame = QFrame()
        rectangle_frame.setFrameShape(QFrame.StyledPanel)
        rectangle_frame.setFrameShadow(QFrame.Sunken)
        rectangle_frame.setLineWidth(1)

        # Crear un QVBoxLayout para el rectángulo y agregar el campo de búsqueda y el botón
        rectangle_layout = QVBoxLayout(rectangle_frame)
        search_field = QLineEdit()
        search_field.setPlaceholderText("Buscar proveedores...")
        rectangle_layout.addWidget(search_field)
        rectangle_layout.addWidget(add_proveedor_button)

        # Ajustar el tamaño de las columnas automáticamente para ajustarse al contenido
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # Evitar que las columnas se puedan estirar
        self.table.horizontalHeader().setStretchLastSection(False)

        # Evitar que las filas se puedan estirar
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        # Establecer la selección a nivel de fila y deshabilitar la edición de celdas
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Crear una QScrollArea y establecer la tabla como su widget interno
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.table)
        scroll_area.setWidgetResizable(True)

        # Modificar la política de tamaño de la tabla
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.table.setMinimumHeight(300)  # Cambia este valor según tus necesidades

        # Añadir el título, el rectángulo y el scroll_area al layout
        layout.addWidget(title_label)
        layout.addWidget(rectangle_frame)
        layout.addWidget(scroll_area)
        layout.addStretch(1)  # Añade un espacio flexible para pegar la tabla a la parte inferior de la pantalla

        # Crear un widget central y establecer el layout
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Establecer el widget central en la ventana
        self.setCentralWidget(central_widget)

        # Establece el título de la ventana
        self.setWindowTitle("Proveedores")

        self.setGeometry(100, 100, 900, 400)  # x, y, ancho, alto
        # Obtener la geometría de la pantalla y calcular la posición central
        screen = QDesktopWidget().availableGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2

        # Establecer la posición de la ventana en el centro de la pantalla
        self.move(x, y)


    def actualizar_tabla(self):
        
        self.proveedores = self.proveedor_service.obtenerProveedores()
        
        self.table.setRowCount(0)
        self.table.setRowCount(len(self.proveedores))

        for i, prov in enumerate(self.proveedores):
            item_id = QTableWidgetItem(prov.id)
            item_nombre = QTableWidgetItem(prov.nombre)
            item_direccion = QTableWidgetItem(prov.direccion)
            item_cod_postal = QTableWidgetItem(str(prov.cod_postal))
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
            self.table.setItem(i, 3, item_cod_postal)
            self.table.setItem(i, 4, item_ciudad)
            self.table.setItem(i, 5, item_provincia)
            self.table.setItem(i, 6, item_telefono)
            self.table.setItem(i, 7, item_correo_electronico)
            self.table.setItem(i, 8, item_comentario)
            self.table.setItem(i, 9, item_cuenta_bancaria)
            self.table.setItem(i, 10, item_fecha_alta)

            # Botón Editar
            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.on_edit_button_clicked)
            self.table.setCellWidget(i, 11, edit_button)

            # Botón Eliminar
            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.on_delete_button_clicked)
            self.table.setCellWidget(i, 12, delete_button)

    def on_agregar_proveedor_clicked(self):
        dialog = AgregarProveedorDialog(self.proveedor_service)
        result = dialog.exec()

        if result == QDialog.Accepted:
            self.actualizar_tabla()

    def on_edit_button_clicked(self):

        button = self.app.sender()
        index = self.table.indexAt(button.pos())
        proveedor = None
        
        id = self.table.item(index.row(), 0).text()
        nombre = self.table.item(index.row(), 1).text()
        direccion = self.table.item(index.row(), 2).text()
        cod_postal = self.table.item(index.row(), 3).text()
        ciudad = self.table.item(index.row(), 4).text()
        provincia = self.table.item(index.row(), 5).text()
        telefono = self.table.item(index.row(), 6).text()
        correo_electronico = self.table.item(index.row(), 7).text()
        comentario = self.table.item(index.row(), 8).text()
        cuenta_bancaria = self.table.item(index.row(), 9).text()
        fecha_alta = self.table.item(index.row(), 10).text()     

        proveedor = Proveedor(nombre, direccion, cod_postal, ciudad, provincia, telefono, correo_electronico, comentario, cuenta_bancaria, fecha_alta)
        
        dialog = EditarProveedorDialog(proveedor)
        result = dialog.exec()

        if result == QDialog.Accepted:
            # Actualiza el producto en la base de datos
            # self.proveedor_service.actualizarProveedor(
            #     producto.codigo,
            #     producto.nombre,
            #     producto.precioCompra,
            #     producto.precioVenta,
            #     producto.cantStock,
            #     producto.categoria,
            #     producto.impuestos,
            #     producto.descuentos,
            #     producto.proveedor,
            #     producto.fechaVenc,
            #     producto.codigo
            # )
            # Actualiza la tabla para mostrar los cambios
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