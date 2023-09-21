from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QDialog, QMessageBox
from entities.categoria import Categoria

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
                    QMessageBox.information(self, "Información", "Nueva Categoría Añadido")
                    self.accept()
                except ValueError:
                    QMessageBox.warning(self, "Error", "Por favor, ingrese un porcentaje válido.")
            else:
                QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")

            self.accept()