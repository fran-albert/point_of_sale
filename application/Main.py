from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from Login import LoginWindow
from servicios.vendedores_service import VendedorService
from utils.Utils import init_header,  create_main_window_menu
from categorias.CategoriasWindow import CategoriasWindow
from utils.Utils import Utils
from productos.ProductosWindow import ProductosWindow
from ventas.VentasWindow import VentasWindow
from ordenes.OrdenesWindow import OrdenesWindow
from vendedores.VendedoresWindow import VendedoresWindow
from proveedores.ProveedoresWindow import ProveedoresWindow
import sys

class MainWindow(QMainWindow):

    logged_out = pyqtSignal() 

    def init_header(self, username):
        init_header(self, self.width(), username)

    def show_categories_window(self):
        self.categoria_window = CategoriasWindow(self.app, self.rol)
        self.categoria_window.show()

    def show_products_window(self):
        self.product_window = ProductosWindow(self.app, self.rol)
        self.product_window.show()

    def show_proveedores_window(self):
        self.proveedores_window = ProveedoresWindow(self.app, self.rol)
        self.proveedores_window.show()

    def show_ventas_window(self):
        self.ventas_window = VentasWindow(self.app)
        self.ventas_window.show()

    def show_ordenes_window(self):
        self.ordenes_window = OrdenesWindow(self.app)
        self.ordenes_window.show()

    def show_vendedores_window(self):
        self.vendedores_window = VendedoresWindow(self.app, self.rol)
        self.vendedores_window.show()

    def generate_sales_report_wrapper(self):
        Utils.generate_sales_report(self)

    def generate_stock_report_wrapper(self):
        Utils.generate_stock_report(self)

    def init_right_side_buttons(self):
        self.init_right_side_buttons(self)
    

    def __init__(self, dni, app):
        self.vendedores_service = VendedorService()
        super().__init__()
        self.setWindowTitle("Point Of Sale")
        self.rol = Utils.obtener_rol(dni)
        self.setWindowIcon(QIcon("img/icons8-market-64.png"))
        self.setFixedSize(800, 500)
        self.categoria_window = None
        self.app = app
        create_main_window_menu(self)
        self.nombre_usuario = Utils.obtener_nombre_usuario(dni)
        init_header(self, self.width(), self.nombre_usuario, self.menuBar().height())
        self.logged_out.connect(self.open_login_window)
        self.login_window = None

    def resizeEvent(self, event):
        init_header(self, self.width(), self.nombre_usuario, self.menuBar().height())
        super().resizeEvent(event)

    def cerrar_sesion(self):
        respuesta = QMessageBox.question(
            self, "Cerrar sesión", "¿Está seguro de que desea cerrar sesión?",
            QMessageBox.No | QMessageBox.Yes, QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            self.hide()
            self.login_window = LoginWindow()  
            self.login_window.show()  
            self.close()  
   
    def open_login_window(self):
        self.close()  
        login_window = LoginWindow()  
        login_window.show()  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("img/icons8-market-64.png"))  
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())