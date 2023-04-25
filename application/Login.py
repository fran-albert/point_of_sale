import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit, QPushButton, QLabel, QHBoxLayout, QGridLayout, QSpacerItem, QSizePolicy
from servicios.usuario_service import UsuarioService
import Ventas



class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de sesión")
        self.setFixedSize(325, 160) 
        window_icon = QIcon("img/icons8-usuario-50.png")
        self.setWindowIcon(window_icon)
        self.init_ui()

    def init_ui(self):
        # Agrega un logo
        logo = QPixmap("img/logo2.0.jpg").scaled(300, 250, Qt.KeepAspectRatio)
        logo_mask = logo.createMaskFromColor(Qt.white)
        logo.setMask(logo_mask)
        logo_label = QLabel(self)
        logo_label.setPixmap(logo)

        # Agrega un campo de texto para ingresar el usuario
        self.usuario_edit = QLineEdit(self)
        usuario_label = QLabel("Usuario:", self)

        # Agrega un campo de texto para ingresar la contraseña
        self.contrasena_edit = QLineEdit(self)
        self.contrasena_edit.setEchoMode(QLineEdit.Password)
        contrasena_label = QLabel("Contraseña:", self)

        # Botón "Iniciar sesión"
        iniciar_sesion_btn = QPushButton("Entrar", self)
        iniciar_sesion_btn.setFixedSize(100, 25)  # Establece el tamaño del botón
        iniciar_sesion_btn.clicked.connect(self.iniciar_sesion)

        # Botón "Salir"
        salir_btn = QPushButton("Salir", self)
        salir_btn.setFixedSize(100, 25)  # Establece el tamaño del botón
        salir_btn.clicked.connect(self.salir)

        # Cambia el tamaño de la fuente de los campos de texto
        font = QFont()
        font.setPointSize(14)  # Ajusta el tamaño de la fuente a 14
        self.usuario_edit.setFont(font)
        self.contrasena_edit.setFont(font)

        # Coloca los widgets en un layout de cuadrícula (grid)
        layout = QGridLayout()
        layout.addWidget(logo_label, 0, 0, 1, 2, alignment=Qt.AlignCenter)
        layout.setRowStretch(1, 1)  # Añade una fila para estirar en la parte superior
        layout.addWidget(usuario_label, 2, 0)
        layout.addWidget(self.usuario_edit, 2, 1)
        layout.addWidget(contrasena_label, 3, 0)
        layout.addWidget(self.contrasena_edit, 3, 1)
        layout.setRowStretch(4, 1)  # Añade una fila de estiramiento entre los campos de texto y los botones
        layout.addWidget(iniciar_sesion_btn, 5, 0, alignment=Qt.AlignRight)  # Alinea el botón a la derecha
        layout.addWidget(salir_btn, 5, 1, alignment=Qt.AlignLeft)  # Alinea el botón a la izquierda
        layout.setRowStretch(6, 1)  # Añade una fila para estirar en la parte inferior
        layout.setColumnStretch(2, 1)
        layout.setVerticalSpacing(20)  # Aumenta el espacio vertical entre los widgets

        # Establece el espacio horizontal entre los widgets a 0
        layout.setSpacing(0)

        # Establece el ancho de la primera columna de la cuadrícula
        layout.setColumnMinimumWidth(0, int(self.width() / 2))

        # Alinea los widgets horizontalmente al centro
        layout.setAlignment(Qt.AlignHCenter)

        self.setLayout(layout)

    def iniciar_sesion(self):
        usuario = self.usuario_edit.text()
        contrasena = self.contrasena_edit.text()
    
        # Crea una instancia de UsuarioService
        usuario_service = UsuarioService()

        # Verifica si el usuario y la contraseña son correctos usando la base de datos
        if usuario_service.validate_login(usuario, contrasena):
            self.close()
            self.main_window = Ventas.MainWindow()  # Guarda una referencia al objeto como un atributo de la clase
            self.main_window.show()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")

    def salir(self):
        """Cierra la aplicación."""
        self.close()



# Código para ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("img/icons8-market-64.png"))  # Establece el icono de la aplicación
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
