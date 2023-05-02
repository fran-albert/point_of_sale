import sys
from pathlib import Path
# Agrega la carpeta principal al sys.path
ruta_principal = str(Path(__file__).parent.parent.resolve())
if ruta_principal not in sys.path:
    sys.path.append(ruta_principal)
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QScrollArea, QTableWidget, QHeaderView, QSizePolicy, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox
from servicios.categoria_service import CategoriaService
from servicios.producto_service import ProductoService
from entities.categoria import Categoria



class EditarCategoriaDialog(QDialog):
        def __init__(self, descripcion, porcentaje, idCategoria, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Editar Categoría")

            layout = QVBoxLayout()

            self.descripcion_label = QLabel("Descripción:")
            self.descripcion_input = QLineEdit(descripcion)
            layout.addWidget(self.descripcion_label)
            layout.addWidget(self.descripcion_input)

            self.porcentaje_label = QLabel("Porcentaje:")
            self.porcentaje_input = QLineEdit(str(porcentaje))
            layout.addWidget(self.porcentaje_label)
            layout.addWidget(self.porcentaje_input)

            self.idCategoria_label = QLabel("Id Categoria:")
            self.idCategoria_input = QLineEdit(str(idCategoria))
            self.idCategoria_input.setReadOnly(True)
            layout.addWidget(self.idCategoria_label)
            layout.addWidget(self.idCategoria_input)

            palette = self.idCategoria_input.palette()
            palette.setColor(QPalette.Base, QColor(240, 240, 240))
            self.idCategoria_input.setPalette(palette)

            self.buttons_layout = QHBoxLayout()
            self.guardar_button = QPushButton("Guardar")
            self.cancelar_button = QPushButton("Cancelar")
            self.buttons_layout.addWidget(self.guardar_button)
            self.buttons_layout.addWidget(self.cancelar_button)

            layout.addLayout(self.buttons_layout)
            self.setLayout(layout)

            self.guardar_button.clicked.connect(self.guardar_categoria)
            self.cancelar_button.clicked.connect(self.reject)

        def guardar_categoria(self):
            nueva_descripcion = self.descripcion_input.text().strip()
            nuevo_porcentaje = self.porcentaje_input.text().strip()
            actual_idcategoria = self.idCategoria_input.text().strip()

            if nueva_descripcion and nuevo_porcentaje and actual_idcategoria:
                try:
                    nuevo_porcentaje = float(nuevo_porcentaje)
                    self.nueva_descripcion = nueva_descripcion
                    self.nuevo_porcentaje = nuevo_porcentaje
                    self.actual_idcategoria = actual_idcategoria
                    self.accept()
                except ValueError:
                    QMessageBox.warning(self, "Error", "Por favor, ingrese un porcentaje válido.")
            else:
                QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")

class AgregarCategoriaDialog(QDialog):
        def __init__(self, categoria_service, parent=None):
            super().__init__(parent)

            self.categoria_service = categoria_service

            self.setWindowTitle("Agregar Categoría")

            layout = QVBoxLayout()

            self.descripcion_label = QLabel("Descripción:")
            self.descripcion_input = QLineEdit()
            layout.addWidget(self.descripcion_label)
            layout.addWidget(self.descripcion_input)

            self.porcentaje_label = QLabel("Porcentaje:")
            self.porcentaje_input = QLineEdit()
            layout.addWidget(self.porcentaje_label)
            layout.addWidget(self.porcentaje_input)

            self.buttons_layout = QHBoxLayout()
            self.agregar_button = QPushButton("Agregar")
            self.cancelar_button = QPushButton("Cancelar")
            self.buttons_layout.addWidget(self.agregar_button)
            self.buttons_layout.addWidget(self.cancelar_button)

            layout.addLayout(self.buttons_layout)
            self.setLayout(layout)

            self.agregar_button.clicked.connect(self.agregar_categoria)
            self.cancelar_button.clicked.connect(self.reject)

        def agregar_categoria(self):
            descripcion = self.descripcion_input.text().strip()
            porcentaje = self.porcentaje_input.text().strip()

            if descripcion and porcentaje:
                try:
                    porcentaje = float(porcentaje)
                    categoria = Categoria(1, descripcion, porcentaje)
                    self.categoria_service.insertarCategoria(categoria)
                    self.accept()
                except ValueError:
                    QMessageBox.warning(self, "Error", "Por favor, ingrese un porcentaje válido.")
            else:
                QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")

            self.accept()

    # Crear una instancia de QTableWidget con cuatro columnas y el número de filas igual a la longitud de la lista de datos

class ABMCategoriasWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)

        # Mueve el código que estaba en la función abmCategorias() aquí
        self.app = app
        self.categoria_service = CategoriaService()
        self.producto_service = ProductoService()
        self.categorias = self.categoria_service.obtenerCategorias()

        # El resto del código en la función abmCategorias se coloca aquí.
        self.table = QTableWidget(len(self.categorias), 5)

        # Definir los encabezados de las columnas
        self.table.setHorizontalHeaderLabels(["ID", "Categoría", "Porcentaje", "", "", ])

        # Agregar los elementos y botones a la tabla
        for i, categoria in enumerate(self.categorias):
            item_id = QTableWidgetItem(str(categoria.id))
            item_descripcion = QTableWidgetItem(categoria.descripcion)
            item_porcentaje = QTableWidgetItem(str(categoria.porcentaje))

            self.table.setItem(i, 0, item_id)
            self.table.setItem(i, 1, item_descripcion)
            self.table.setItem(i, 2, item_porcentaje)

            # Botón Editar
            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.on_edit_button_clicked)
            self.table.setCellWidget(i, 3, edit_button)

            # Botón Eliminar
            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.on_delete_button_clicked)
            self.table.setCellWidget(i, 4, delete_button)

        # Crear un botón Agregar Categoría
        add_category_button = QPushButton("Agregar Categoría")
        add_category_button.clicked.connect(self.on_agregar_categoria_clicked)

        # Crear un layout vertical
        layout = QVBoxLayout()

        # Crear un QLabel para el título
        title_label = QLabel("Categorías")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: green; font-size: 24px")

        # Crear un QFrame para el rectángulo
        rectangle_frame = QFrame()
        rectangle_frame.setFrameShape(QFrame.StyledPanel)
        rectangle_frame.setFrameShadow(QFrame.Sunken)
        rectangle_frame.setLineWidth(1)

        # Crear un QVBoxLayout para el rectángulo y agregar el campo de búsqueda y el botón
        rectangle_layout = QVBoxLayout(rectangle_frame)
        search_field = QLineEdit()
        search_field.setPlaceholderText("Buscar categorías...")
        rectangle_layout.addWidget(search_field)
        rectangle_layout.addWidget(add_category_button)

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
        self.setWindowTitle("Categorías")

        # Establece el tamaño y la posición de la ventana
        self.setGeometry(100, 100, 450, 500)  # x, y, ancho, alto

    def actualizar_tabla(self):
            # Obtén la lista actualizada de categorías
            self.categorias = self.categoria_service.obtenerCategorias()

            # Limpia la tabla antes de agregar nuevas filas
            self.table.setRowCount(0)

            # Establece el número de filas en la tabla según la longitud de la lista de categorías
            self.table.setRowCount(len(self.categorias))

            # Rellena la tabla con las categorías actualizadas
            for i, categoria in enumerate(self.categorias):
                item_descripcion = QTableWidgetItem(categoria.descripcion)
                item_porcentaje = QTableWidgetItem(str(categoria.porcentaje))
                item_id = QTableWidgetItem(str(categoria.id))
                self.table.setItem(i, 1, item_descripcion)
                self.table.setItem(i, 2, item_porcentaje)
                self.table.setItem(i, 0, item_id)

                # Botón Editar
                edit_button = QPushButton("Editar")
                edit_button.clicked.connect(self.on_edit_button_clicked)  # Conectar la señal aquí
                self.table.setCellWidget(i, 3, edit_button)

                # Botón Eliminar
                delete_button = QPushButton("Eliminar")
                delete_button.clicked.connect(self.on_delete_button_clicked)
                self.table.setCellWidget(i, 4, delete_button)

    def on_agregar_categoria_clicked(self):
        dialog = AgregarCategoriaDialog(self.categoria_service)
        result = dialog.exec()

        if result == QDialog.Accepted:
            # Actualiza la tabla para mostrar la nueva categoría agregada
            self.actualizar_tabla()

    def on_edit_button_clicked(self):
        # Obtén el botón que emitió la señal
        button = self.app.sender()
        # Obtiene el índice del elemento en la tabla
        index = self.table.indexAt(button.pos())

        # Obtén la descripción y el porcentaje de la categoría seleccionada
        idCategoria = int(self.table.item(index.row(), 0).text())
        descripcion = self.table.item(index.row(), 1).text()
        porcentaje = float(self.table.item(index.row(), 2).text())

        # Muestra la ventana de edición y obtén el resultado
        dialog = EditarCategoriaDialog(descripcion, porcentaje, idCategoria)
        result = dialog.exec()

        if result == QDialog.Accepted:
            nueva_descripcion = dialog.nueva_descripcion
            nuevo_porcentaje = dialog.nuevo_porcentaje
            idCategoria = dialog.actual_idcategoria
            
            # Actualiza la categoría en la base de datos
            self.categoria_service.actualizarCategoria(nueva_descripcion, nuevo_porcentaje, idCategoria)

            if porcentaje != nuevo_porcentaje:
                self.producto_service.actualizarPrecioVenta(nuevo_porcentaje, idCategoria)
            
            # Actualiza la tabla para mostrar los cambios
            self.actualizar_tabla()

    def on_delete_button_clicked(self):
        # Obtén el botón que emitió la señal
        button = self.app.sender()
        # Obtiene el índice del elemento en la tabla
        index = self.table.indexAt(button.pos())

        # Obtén el ID de la categoría seleccionada
        categoria_id = self.table.item(index.row(), 0).text()

        respuesta = QMessageBox.question(None, "Confirmación de eliminación", f"¿Está seguro de que desea eliminar la categoría {categoria_id}?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            # Aquí va el código para eliminar la categoría de la base de datos utilizando el ID
            self.categoria_service.eliminarCategoria(categoria_id)

            # Elimina la fila seleccionada de la tabla
            self.table.removeRow(index.row())




