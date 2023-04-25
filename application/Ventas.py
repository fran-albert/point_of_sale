from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QAction, QWidget, QMessageBox, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtCore import pyqtSignal, Qt, QDateTime, QDate
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QIcon, QPixmap
from Login import LoginWindow
import sys



class AgregarProductoExitoso(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Producto Agregado")
        self.setText("El producto ha sido agregado exitosamente.")
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
        self.exec_()

class ModificarProductoExitoso(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Producto Modificado")
        self.setText("El producto ha sido modificado exitosamente.")
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
        self.exec_()

class EliminarProductoExitoso(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Producto Eliminado")
        self.setText("El producto ha sido eliminado exitosamente.")
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
        self.exec_()

class AgregarProductoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agregar Producto")
        self.setFixedSize(400, 400)  # Establece el tamaño de la ventana a 400x400
        self.init_ui()

    def init_ui(self):
        # Agrega un campo de texto para ingresar el nombre del producto
        self.nombre_edit = QLineEdit(self)
        self.nombre_edit.move(50, 50)
        self.nombre_edit.resize(300, 30)
        nombre_label = QLabel("Nombre del Producto:", self)
        nombre_label.move(50, 30)

        # Agrega un campo de texto para ingresar el código de barras
        self.codigo_edit = QLineEdit(self)
        self.codigo_edit.move(50, 100)
        self.codigo_edit.resize(300, 30)
        codigo_label = QLabel("Código de Barras:", self)
        codigo_label.move(50, 80)

        # Agrega un campo de texto para ingresar el costo
        self.costo_edit = QLineEdit(self)
        self.costo_edit.move(50, 150)
        self.costo_edit.resize(300, 30)
        costo_label = QLabel("Costo:", self)
        costo_label.move(50, 130)

        # Agrega un campo de texto para ingresar la descripción
        self.descripcion_edit = QLineEdit(self)
        self.descripcion_edit.move(50, 200)
        self.descripcion_edit.resize(300, 30)
        descripcion_label = QLabel("Descripción:", self)
        descripcion_label.move(50, 180)

        # Agrega un campo de texto para ingresar la categoría
        self.categoria_edit = QLineEdit(self)
        self.categoria_edit.move(50, 250)
        self.categoria_edit.resize(300, 30)
        categoria_label = QLabel("Categoría:", self)
        categoria_label.move(50, 230)

        # Agrega un campo de texto para ingresar la cantidad de stock
        self.stock_edit = QLineEdit(self)
        self.stock_edit.move(50, 300)
        self.stock_edit.resize(300, 30)
        stock_label = QLabel("Cantidad de Stock:", self)
        stock_label.move(50, 280)

        # Botones

        agregar_btn = QPushButton("Agregar Producto", self)
        agregar_btn.move(50, 350)
        agregar_btn.resize(150, 30)
        agregar_btn.clicked.connect(self.agregar_producto)

        cancelar_btn = QPushButton("Cancelar", self)
        cancelar_btn.move(200, 350)
        cancelar_btn.resize(150, 30)
        cancelar_btn.clicked.connect(self.cancelar_agregar_producto)

    def agregar_producto(self):
        nombre = self.nombre_edit.text()
        codigo = self.codigo_edit.text()
        costo = self.costo_edit.text()
        descripcion = self.descripcion_edit.text()
        categoria = self.categoria_edit.text()
        stock = self.stock_edit.text()
        # Haz algo con la descripción del producto, como agregarla a una base de datos
        # ...

        if not all([nombre, codigo, costo, descripcion, categoria, stock]):
            QMessageBox.warning(self, "Error", "Debe completar todos los campos.")
            return

        # Muestra un mensaje de éxito
        AgregarProductoExitoso()

        # Cierra la ventana
        self.close()

    def cancelar_agregar_producto(self):
        self.close()

class ModificarProductoWindow(QWidget):  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modificar Producto")
        self.setFixedSize(300, 200)  # Establece el tamaño de la ventana a 300x300
        self.init_ui()

    def init_ui(self):
        # Agrega un campo de texto para ingresar el nombre del producto
        self.nombre_edit = QLineEdit(self)
        self.nombre_edit.move(50, 50)
        self.nombre_edit.resize(200, 30)
        nombre_label = QLabel("Nombre del Producto:", self)
        nombre_label.move(50, 30)

        # Agrega un campo de texto para ingresar el código de barras
        self.codigo_edit = QLineEdit(self)
        self.codigo_edit.move(50, 100)
        self.codigo_edit.resize(200, 30)
        codigo_label = QLabel("Código de Barras:", self)
        codigo_label.move(50, 80)

        # Botones
        modificar_btn = QPushButton("Modificar", self)
        modificar_btn.move(50, 150)
        modificar_btn.resize(100, 30)
        modificar_btn.clicked.connect(self.eliminar_producto)

        cancelar_btn = QPushButton("Cancelar", self)
        cancelar_btn.move(150, 150)
        cancelar_btn.resize(100, 30)
        cancelar_btn.clicked.connect(self.cancelar_eliminar_producto)

    def eliminar_producto(self):
        nombre = self.nombre_edit.text()
        codigo = self.codigo_edit.text()

        # Haz algo con el nombre y código de barras para eliminar el producto
        # ...

        if not all([nombre, codigo]):
            QMessageBox.warning(self, "Error", "Debe completar todos los campos.")
            return
        ModificarProductoExitoso()
        self.close()

    def cancelar_eliminar_producto(self):
        self.close()

class EliminarProductoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eliminar Producto")
        self.setFixedSize(300, 200)  # Establece el tamaño de la ventana a 300x300
        self.init_ui()

    def init_ui(self):
        # Agrega un campo de texto para ingresar el nombre del producto
        self.nombre_edit = QLineEdit(self)
        self.nombre_edit.move(50, 50)
        self.nombre_edit.resize(200, 30)
        nombre_label = QLabel("Nombre del Producto:", self)
        nombre_label.move(50, 30)

        # Agrega un campo de texto para ingresar el código de barras
        self.codigo_edit = QLineEdit(self)
        self.codigo_edit.move(50, 100)
        self.codigo_edit.resize(200, 30)
        codigo_label = QLabel("Código de Barras:", self)
        codigo_label.move(50, 80)

        # Botones
        eliminar_btn = QPushButton("Eliminar", self)
        eliminar_btn.move(50, 150)
        eliminar_btn.resize(100, 30)
        eliminar_btn.clicked.connect(self.eliminar_producto)

        cancelar_btn = QPushButton("Cancelar", self)
        cancelar_btn.move(150, 150)
        cancelar_btn.resize(100, 30)
        cancelar_btn.clicked.connect(self.cancelar_eliminar_producto)

    def eliminar_producto(self):
        nombre = self.nombre_edit.text()
        codigo = self.codigo_edit.text()

        # Haz algo con el nombre y código de barras para eliminar el producto
        # ...

        if not all([nombre, codigo]):
            QMessageBox.warning(self, "Error", "Debe completar todos los campos.")
            return
        EliminarProductoExitoso()
        self.close()

    def cancelar_eliminar_producto(self):
        self.close()

class MainWindow(QMainWindow):

    logged_out = pyqtSignal()  # Crea una nueva señal personalizada
    
    def init_header(self):
        header = QFrame(self)
        header.setGeometry(0, 20, self.width(), 100)
        header.setStyleSheet("background-color: #F9F5EB;")

        # Lado izquierdo
        left_layout = QVBoxLayout()

        # Parte 1: Logo
        logo_label = QLabel(header)
        pixmap = QPixmap("img/logosinfondo.png").scaled(300, 250, Qt.KeepAspectRatio)
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(logo_label)

        # Parte 2: Rosario, Argentina y Login y Cajero
        info_layout = QHBoxLayout()

        # Rosario, Argentina
        location_label = QLabel("Rosario, Argentina", header)
        location_label.setStyleSheet("color: black;")
        font = location_label.font()
        font.setPointSize(12)  # Ajusta el tamaño de la fuente aquí
        location_label.setFont(font)
        location_label.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(location_label, alignment=Qt.AlignCenter)

        # Login y Cajero
        login_cajero_layout = QVBoxLayout()
        login_label = QLabel("Login: Admin", header)
        login_label.setStyleSheet("color: black;")
        cajero_label = QLabel("Cajero: Juan", header)
        cajero_label.setStyleSheet("color: black;")
        login_cajero_layout.addWidget(login_label)
        login_cajero_layout.addWidget(cajero_label)
        info_layout.addLayout(login_cajero_layout)

        left_layout.addLayout(info_layout)


        # Lado derecho
        right_layout = QVBoxLayout()

        # Factura layout
        factura_layout = QHBoxLayout()
        factura_label = QLabel("Factura:", header)
        factura_label.setStyleSheet("color: black;")
        factura_layout.addWidget(factura_label)
        factura_num_label = QLabel("12345", header)
        factura_num_label.setStyleSheet("color: black;")
        factura_layout.addWidget(factura_num_label)

        # Fecha layout
        fecha_layout = QHBoxLayout()
        fecha_label = QLabel("Fecha:", header)
        fecha_label.setStyleSheet("color: black;")
        fecha_layout.addWidget(fecha_label)
        fecha = QDateTime.currentDateTime().toString("dd-MM-yyyy hh:mm:ss")
        fecha_num_label = QLabel(fecha, header)
        fecha_num_label.setStyleSheet("color: black;")
        fecha_layout.addWidget(fecha_num_label)

        factura_fecha_layout = QHBoxLayout()
        factura_fecha_layout.addLayout(factura_layout)
        factura_fecha_layout.addSpacing(20)
        factura_fecha_layout.addLayout(fecha_layout)

        right_layout.addLayout(factura_fecha_layout)

        # Barcode
        barcode_layout = QHBoxLayout()
        barcode_label = QLabel("Código de Barras:", header)
        barcode_label.setStyleSheet("color: black;")
        barcode_textbox = QLineEdit(header)
        barcode_layout.addWidget(barcode_label)
        barcode_layout.addWidget(barcode_textbox)
        right_layout.addLayout(barcode_layout)
        right_layout.addSpacing(10)

        # Item Name
        item_layout = QHBoxLayout()
        item_label = QLabel("Nombre del Producto:", header)
        item_label.setStyleSheet("color: black;")
        item_textbox = QLineEdit(header)
        item_layout.addWidget(item_label)
        item_layout.addWidget(item_textbox)
        right_layout.addLayout(item_layout)
        right_layout.addSpacing(10)

        barcode_textbox.setFixedWidth(400)
        item_textbox.setFixedWidth(400)


        # Layout principal
        main_layout = QHBoxLayout(header)
        main_layout.addLayout(left_layout)
        main_layout.setStretchFactor(left_layout, 1)
        main_layout.addLayout(right_layout)
        main_layout.setStretchFactor(right_layout, 1)
        header.setLayout(main_layout)






    def __init__(self):
        super().__init__()
        self.setWindowTitle("Point Of Sale")
        self.logged_out.connect(self.open_login_window)  # Conecta la señal a la función open_login_window
        self.login_window = None  # Añade un atributo para almacenar la referencia de la ventana de inicio de sesión
        self.setWindowIcon(QIcon("img/icons8-market-64.png"))  # Establece el icono de la ventan
        self.setFixedSize(1000, 900)  # Establece el tamaño de la ventana a 800x600
        self.init_menu()
        self.init_header()

    def init_menu(self):
        # Crea la barra de menú
        menu_bar = self.menuBar()

        # Crea los menús y añádelos a la barra de menú
        usuarios_menu = QMenu("Usuarios", self)
        abm_productos_menu = QMenu("ABM Productos", self)
        reportes_menu = QMenu("Reportes", self)
        menu_bar.addMenu(usuarios_menu)
        menu_bar.addMenu(abm_productos_menu)
        menu_bar.addMenu(reportes_menu)

        # Aquí puedes agregar acciones a cada menú si lo deseas
        # Por ejemplo, para agregar una acción al menú Usuarios:
        action = QAction("Cerrar Sesión", self)
        action.triggered.connect(self.cerrar_sesion)  # Conecta la acción a un método
        usuarios_menu.addAction(action)

        # Agrega una acción para abrir la ventana de agregar productos
        action = QAction("Agregar Producto", self)
        action.triggered.connect(self.abrir_ventana_agregar_producto)
        abm_productos_menu.addAction(action)

        # Modificar Productos
        action = QAction("Modificar Producto", self)
        action.triggered.connect(self.abrir_ventana_modificar_producto)
        abm_productos_menu.addAction(action)

        # Eliminar Productos
        action = QAction("Eliminar Producto", self)
        action.triggered.connect(self.abrir_ventana_eliminar_producto)
        abm_productos_menu.addAction(action)

        
    def abrir_ventana_agregar_producto(self):
        self.agregar_producto_window = AgregarProductoWindow()
        self.agregar_producto_window.show()

    def abrir_ventana_modificar_producto(self):
        self.modificar_producto_window = ModificarProductoWindow()
        self.modificar_producto_window.show()

    def abrir_ventana_eliminar_producto(self):
        self.eliminar_producto_window = EliminarProductoWindow()
        self.eliminar_producto_window.show()

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