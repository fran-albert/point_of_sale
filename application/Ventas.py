from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from Login import LoginWindow
from servicios.usuario_service import UsuarioService
from utils.Utils import init_header,  create_main_window_menu, show_reports_window, generate_sales_report, generate_stock_report, init_right_side_buttons, show_payment_window
from categorias.abm_categorias import ABMCategoriasWindow
from productos.abm_productos import ABMProductosWindow
from proveedores.abm_proveedores import ABMProveedoresWindow
import sys

class MainWindow(QMainWindow):

    logged_out = pyqtSignal()  # Crea una nueva señal personalizada

    def init_header(self, username):
        init_header(self, self.width(), username)

    def show_categories_window(self):
        self.categoria_window = ABMCategoriasWindow(self.app)
        self.categoria_window.show()

    def show_products_window(self):
        self.product_window = ABMProductosWindow(self.app)
        self.product_window.show()

    def show_proveedores_window(self):
        self.proveedores_window = ABMProveedoresWindow(self.app)
        self.proveedores_window.show()

    def show_reports_window(self):
        show_reports_window(self)

    def generate_sales_report_wrapper(self):
        generate_sales_report(self)

    def generate_stock_report_wrapper(self):
        generate_stock_report(self)

    def generate_stock_report(self):
        generate_stock_report(self)

    def generate_sales_report(self):
        generate_sales_report(self)

    def init_right_side_buttons(self):
        init_right_side_buttons(self)
    
    def show_payment_window(self):
        show_payment_window(self)

    def __init__(self, current_username, current_password, app):
        self.usuario_service = UsuarioService()
        super().__init__()
        self.setWindowTitle("Point Of Sale")
        self.current_username = self.usuario_service.get_username(current_username, current_password)
        self.setWindowIcon(QIcon("img/icons8-market-64.png"))
        self.setFixedSize(1000, 900)
        self.categoria_window = None
        self.app = app
        create_main_window_menu(self)
        init_header(self, self.width(), self.current_username, self.menuBar().height())
        self.init_right_side_buttons()
        self.logged_out.connect(self.open_login_window)
        self.login_window = None
        self.init_right_side_buttons()

    def resizeEvent(self, event):
        init_header(self, self.width(), self.current_username, self.menuBar().height())
        super().resizeEvent(event)

    def cerrar_sesion(self):
        respuesta = QMessageBox.question(
            self, "Cerrar sesión", "¿Está seguro de que desea cerrar sesión?",
            QMessageBox.No | QMessageBox.Yes, QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            self.hide()
            self.login_window = LoginWindow()  # Crea una nueva instancia de LoginWindow
            self.login_window.show()  # Muestra la ventana de inicio de sesión
            self.close()  # Cierra la ventana de Ventas
   
    def open_login_window(self):
        self.close()  # Cierra la ventana actual (Ventas)
        login_window = LoginWindow()  # Crea una nueva instancia de LoginWindow
        login_window.show()  # Muestra la ventana de inicio de sesión

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("img/icons8-market-64.png"))  # Establece el icono de la aplicación
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())