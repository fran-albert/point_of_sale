from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from Login import LoginWindow
from servicios.vendedores_service import VendedorService
from utils.Utils import init_header,  create_main_window_menu
from categorias.abm_categorias import ABMCategoriasWindow
from utils.Utils import Utils
from productos.abm_productos import ABMProductosWindow
from ventas.VentasWindow import VentasWindow
from ordenes.OrdenesWindow import OrdenesWindow
from vendedores.VendedoresWindow import VendedoresWindow
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

    def show_ventas_window(self):
        self.ventas_window = VentasWindow(self.app)
        self.ventas_window.show()

    def show_ordenes_window(self):
        self.ordenes_window = OrdenesWindow(self.app)
        self.ordenes_window.show()

    def show_vendedores_window(self):
        self.vendedores_window = VendedoresWindow(self.app)
        self.vendedores_window.show()

    def generate_sales_report_wrapper(self):
        Utils.generate_sales_report(self)

    def generate_stock_report_wrapper(self):
        Utils.generate_stock_report(self)

    def init_right_side_buttons(self):
        self.init_right_side_buttons(self)
    

    def __init__(self, current_username, current_password, app):
        self.vendedores_service = VendedorService()
        super().__init__()
        self.setWindowTitle("Point Of Sale")
        self.current_username = self.vendedores_service.get_username(current_username, current_password)
        self.setWindowIcon(QIcon("img/icons8-market-64.png"))
        self.setFixedSize(1000, 900)
        self.categoria_window = None
        self.app = app
        create_main_window_menu(self)
        init_header(self, self.width(), self.current_username, self.menuBar().height())
        self.logged_out.connect(self.open_login_window)
        self.login_window = None

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