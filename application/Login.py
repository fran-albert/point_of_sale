import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from servicios.vendedor_service import VendedorService
from utils.Utils import Utils
import Main


class LoginWindow(QWidget):
    def __init__(self, app=None):
        super().__init__()
        self.app = app
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

        vendedor_service = VendedorService()

        if vendedor_service.validarLogin(usuario, contrasena):
            self.hide()
            self.main_window = Main.MainWindow(usuario, self.app)
            self.main_window.show()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrecto")

    def salir(self):
        """Cierra la aplicación."""
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("img/icons8-market-64.png"))  
    login_window = LoginWindow(app)
    login_window.show()
    sys.exit(app.exec_())
