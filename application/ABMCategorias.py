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


        # Botón Agregar Categoría
        add_category_button = QPushButton("Agregar Categoría")
        add_category_button.clicked.connect(on_agregar_categoria_clicked)

        # Por ejemplo, puedes crear un objeto Categoria con los datos ingresados y
        # llamar a insertarCategoria() para agregarlo a la base de datos.

        self.accept()

def on_agregar_categoria_clicked():
    dialog = AgregarCategoriaDialog()
    result = dialog.exec()

    if result == QDialog.Accepted:
        # Aquí puedes actualizar la tabla para mostrar la nueva categoría agregada
        # categoria_service.insertarCategoria(categoria)
        pass


# Crear una instancia de QTableWidget con cuatro columnas y el número de filas igual a la longitud de la lista de datos
table = QTableWidget(len(categorias), 4)

# Definir los encabezados de las columnas
table.setHorizontalHeaderLabels(["Descripción", "Categoría", "", ""])

def on_button_clicked():
    # Obtén el botón que emitió la señal
    button = app.sender()
    # Obtiene el índice del elemento en la tabla
    index = table.indexAt(button.pos())
    # Imprime el índice de la fila
    print("Botón presionado en la fila:", index.row())

# Agregar los elementos y botones a la tabla
for i, categoria in enumerate(categorias):
    item_descripcion = QTableWidgetItem(categoria.descripcion)
    item_porcentaje = QTableWidgetItem(str(categoria.porcentaje))
    table.setItem(i, 0, item_descripcion)
    table.setItem(i, 1, item_porcentaje)

    # Botón Editar
    edit_button = QPushButton("Editar")
    edit_button.clicked.connect(on_button_clicked)
    table.setCellWidget(i, 2, edit_button)

    # Botón Eliminar
    delete_button = QPushButton("Eliminar")
    delete_button.clicked.connect(on_button_clicked)
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