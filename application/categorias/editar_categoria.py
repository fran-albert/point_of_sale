from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox
from PyQt5.QtGui import QColor, QPalette

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
