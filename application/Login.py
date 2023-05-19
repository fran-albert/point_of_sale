import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from servicios.usuario_service import UsuarioService
from utils.Utils import Utils
import Main


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de sesión")
        self.setFixedSize(325, 160) 
        window_icon = QIcon("img/icons8-usuario-50.png")
        self.setWindowIcon(window_icon)
        self.init_ui()

    def init_ui(self):
        Utils.create_login_ui(self)
    
    def enter_pressed(self):
        self.iniciar_sesion()
    
    def iniciar_sesion(self):
        usuario = self.usuario_edit.text()
        contrasena = self.contrasena_edit.text()

        # Crea una instancia de UsuarioService
        usuario_service = UsuarioService()

        # Verifica si el usuario y la contraseña son correctos usando la base de datos
        if usuario_service.validate_login(usuario, contrasena):
            self.hide()
            # Pasa las credenciales del usuario al constructor de la clase Ventas
            self.main_window = Main.MainWindow(usuario, contrasena, app)
            self.main_window.show()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrecto")

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
