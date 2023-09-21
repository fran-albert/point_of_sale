import sys
from pathlib import Path
# Agrega la carpeta principal al sys.path
ruta_principal = str(Path(__file__).parent.parent.resolve())
if ruta_principal not in sys.path:
    sys.path.append(ruta_principal)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QAbstractItemView, QTableWidget, QHeaderView, QSizePolicy, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QDialog, QMessageBox
from servicios.categoria_service import CategoriaService
from servicios.producto_service import ProductoService
from .agregar_categoria import AgregarCategoriaDialog
from .editar_categoria import EditarCategoriaDialog


class ListaCategoriasDialog(QDialog):
    def __init__(self, app, rol, parent=None):
        super().__init__(parent)    

        self.app = app
        self.categoria_service = CategoriaService()
        self.producto_service = ProductoService()
        self.categorias = self.categoria_service.obtenerCategorias()

        self.setWindowTitle("Categorías")

        layout = QVBoxLayout()

        title_label = QLabel("Categorías")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: green; font-size: 24px")

        layout.addWidget(title_label)

        search_label = QLabel("Buscar categorías:")
        search_input = QLineEdit()
        search_input.setPlaceholderText("Ingrese el nombre de la categoría...")
        search_layout = QHBoxLayout()
        search_layout.addWidget(search_label)
        search_layout.addWidget(search_input)

        layout.addLayout(search_layout)

        self.table = QTableWidget(len(self.categorias), 4)
        self.table.setHorizontalHeaderLabels(["ID", "Categoría", "Porcentaje", "", ""])
        self.table.setMinimumHeight(300)  
        self.table.hideColumn(0)
        self.table.setColumnWidth(1, 150)

        if rol == 0:
            self.table.hideColumn(3)  

        for i, categoria in enumerate(self.categorias):
            item_id = QTableWidgetItem(str(categoria.id))
            item_descripcion = QTableWidgetItem(categoria.descripcion)
            item_porcentaje = QTableWidgetItem(str(categoria.porcentaje))

            self.table.setItem(i, 0, item_id)
            self.table.setItem(i, 1, item_descripcion)
            self.table.setItem(i, 2, item_porcentaje)

            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.on_edit_button_clicked)
            self.table.setCellWidget(i, 3, edit_button)

            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.on_delete_button_clicked)
            self.table.setCellWidget(i, 4, delete_button)
        
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        layout.addWidget(self.table)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(layout)
        self.resize(400, 300)


    def actualizar_tabla(self):
            
            self.categorias = self.categoria_service.obtenerCategorias()
            self.table.setRowCount(0)
            self.table.setRowCount(len(self.categorias))

            for i, categoria in enumerate(self.categorias):
                item_descripcion = QTableWidgetItem(categoria.descripcion)
                item_porcentaje = QTableWidgetItem(str(categoria.porcentaje))
                item_id = QTableWidgetItem(str(categoria.id))
                self.table.setItem(i, 1, item_descripcion)
                self.table.setItem(i, 2, item_porcentaje)
                self.table.setItem(i, 0, item_id)

                edit_button = QPushButton("Editar")
                edit_button.clicked.connect(self.on_edit_button_clicked)  # Conectar la señal aquí
                self.table.setCellWidget(i, 3, edit_button)

                delete_button = QPushButton("Eliminar")
                delete_button.clicked.connect(self.on_delete_button_clicked)
                self.table.setCellWidget(i, 4, delete_button)

    def on_agregar_categoria_clicked(self):
        dialog = AgregarCategoriaDialog(self.categoria_service)
        result = dialog.exec()

        if result == QDialog.Accepted:
            self.actualizar_tabla()

    def on_edit_button_clicked(self):
        button = self.app.sender()
        index = self.table.indexAt(button.pos())

        idCategoria = int(self.table.item(index.row(), 0).text())
        descripcion = self.table.item(index.row(), 1).text()
        porcentaje = float(self.table.item(index.row(), 2).text())

        dialog = EditarCategoriaDialog(descripcion, porcentaje, idCategoria)
        result = dialog.exec()

        if result == QDialog.Accepted:
            nueva_descripcion = dialog.nueva_descripcion
            nuevo_porcentaje = dialog.nuevo_porcentaje
            idCategoria = dialog.actual_idcategoria
            
            self.categoria_service.actualizarCategoria(nueva_descripcion, nuevo_porcentaje, idCategoria)

            if porcentaje != nuevo_porcentaje:
                self.producto_service.actualizarPrecioVenta(nuevo_porcentaje, idCategoria)
            self.actualizar_tabla()

    def on_delete_button_clicked(self):
        button = self.app.sender()
        index = self.table.indexAt(button.pos())

        idCategoria = self.table.item(index.row(), 0).text()

        respuesta = QMessageBox.question(None, "Confirmación de eliminación", f"¿Está seguro de que desea eliminar la categoría {idCategoria}?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            productosAsociados = self.producto_service.existeProductosConCategoria(idCategoria)
            if(productosAsociados == 0):
                self.categoria_service.eliminarCategoria(idCategoria)
                self.table.removeRow(index.row())
            else:
                QMessageBox.warning(None, "Advertencia", "La categoría que desea eliminar tiene productos asociados", QMessageBox.Ok)
