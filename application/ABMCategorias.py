import sys
from pathlib import Path
# Agrega la carpeta principal al sys.path
ruta_principal = str(Path(__file__).parent.parent.resolve())
if ruta_principal not in sys.path:
    sys.path.append(ruta_principal)
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox
from servicios.categoria_service import CategoriaService
from entities.categoria import Categoria

# Crear una instancia de QApplication
app = QApplication([])

categoria_service = CategoriaService()

categorias = categoria_service.obtenerCategorias()



class EditarCategoriaDialog(QDialog):
    def __init__(self, descripcion, porcentaje, parent=None):
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

        if nueva_descripcion and nuevo_porcentaje:
            try:
                nuevo_porcentaje = float(nuevo_porcentaje)
                self.nueva_descripcion = nueva_descripcion
                self.nuevo_porcentaje = nuevo_porcentaje
                self.accept()
            except ValueError:
                QMessageBox.warning(self, "Error", "Por favor, ingrese un porcentaje válido.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")

class AgregarCategoriaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
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
                categoria_service.insertarCategoria(categoria)
                self.accept()
            except ValueError:
                QMessageBox.warning(self, "Error", "Por favor, ingrese un porcentaje válido.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")

        self.accept()

# Crear una instancia de QTableWidget con cuatro columnas y el número de filas igual a la longitud de la lista de datos
table = QTableWidget(len(categorias), 4)

# Definir los encabezados de las columnas
table.setHorizontalHeaderLabels(["Descripción", "Categoría", "", ""])

def actualizar_tabla():
    # Obtén la lista actualizada de categorías
    categorias = categoria_service.obtenerCategorias()

    # Limpia la tabla antes de agregar nuevas filas
    table.setRowCount(0)

    # Establece el número de filas en la tabla según la longitud de la lista de categorías
    table.setRowCount(len(categorias))

    # Rellena la tabla con las categorías actualizadas
    for i, categoria in enumerate(categorias):
        item_descripcion = QTableWidgetItem(categoria.descripcion)
        item_porcentaje = QTableWidgetItem(str(categoria.porcentaje))
        table.setItem(i, 0, item_descripcion)
        table.setItem(i, 1, item_porcentaje)

        # Botón Editar
        edit_button = QPushButton("Editar")
        edit_button.clicked.connect(on_edit_button_clicked)
        table.setCellWidget(i, 2, edit_button)

        # Botón Eliminar
        delete_button = QPushButton("Eliminar")
        delete_button.clicked.connect(on_delete_button_clicked)
        table.setCellWidget(i, 3, delete_button)

def on_agregar_categoria_clicked():
    dialog = AgregarCategoriaDialog()
    result = dialog.exec()

    if result == QDialog.Accepted:
        # Actualiza la tabla para mostrar la nueva categoría agregada
        actualizar_tabla()

def on_edit_button_clicked():
    # Obtén el botón que emitió la señal
    button = app.sender()
    # Obtiene el índice del elemento en la tabla
    index = table.indexAt(button.pos())

    # Obtén la descripción y el porcentaje de la categoría seleccionada
    descripcion = table.item(index.row(), 0).text()
    porcentaje = float(table.item(index.row(), 1).text())

    # Muestra la ventana de edición y obtén el resultado
    dialog = EditarCategoriaDialog(descripcion, porcentaje)
    result = dialog.exec()

    if result == QDialog.Accepted:
        nueva_descripcion = dialog.nueva_descripcion
        nuevo_porcentaje = dialog.nuevo_porcentaje

        # Actualiza la categoría en la base de datos
        categoria_service.actualizarCategoria(nueva_descripcion, nuevo_porcentaje, descripcion)

        # Actualiza la tabla para mostrar los cambios
        actualizar_tabla()

    # En la función `actualizar_tabla`, conecta el botón "Editar" a `on_edit_button_clicked`
    edit_button.clicked.connect(on_edit_button_clicked)

def on_delete_button_clicked():
    # Obtén el botón que emitió la señal
    button = app.sender()
    # Obtiene el índice del elemento en la tabla
    index = table.indexAt(button.pos())

    # Obtén la descripción de la categoría seleccionada
    descripcion = table.item(index.row(), 0).text()

    respuesta = QMessageBox.question(None, "Confirmación de eliminación", f"¿Está seguro de que desea eliminar la categoría {descripcion}?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if respuesta == QMessageBox.Yes:
        # Aquí va el código para eliminar la categoría de la base de datos utilizando la descripción
        categoria_service.eliminarCategoria(descripcion)

        # Elimina la fila seleccionada de la tabla
        table.removeRow(index.row())

# Agregar los elementos y botones a la tabla
for i, categoria in enumerate(categorias):
    item_descripcion = QTableWidgetItem(categoria.descripcion)
    item_porcentaje = QTableWidgetItem(str(categoria.porcentaje))
    table.setItem(i, 0, item_descripcion)
    table.setItem(i, 1, item_porcentaje)

    # Botón Editar
    edit_button = QPushButton("Editar")
    edit_button.clicked.connect(on_edit_button_clicked)
    table.setCellWidget(i, 2, edit_button)

    # Botón Eliminar
    delete_button = QPushButton("Eliminar")
    delete_button.clicked.connect(on_delete_button_clicked)
    table.setCellWidget(i, 3, delete_button)

# Crear un botón Agregar Categoría
add_category_button = QPushButton("Agregar Categoría")
add_category_button.clicked.connect(on_agregar_categoria_clicked)

# Crear un layout vertical
layout = QVBoxLayout()

# Agregar la tabla y el botón al layout
layout.addWidget(table)
layout.addWidget(add_category_button)

# Crear un widget central y establecer el layout
central_widget = QWidget()
central_widget.setLayout(layout)

# Mostrar el widget en pantalla
central_widget.show()

# Ejecutar la aplicación
app.exec_()