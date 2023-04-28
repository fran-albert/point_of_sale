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

class ProductosWindow(QWidget):
    def abrir_ventana_agregar_producto(self):
        self.agregar_producto_window = AgregarProductoWindow()
        self.agregar_producto_window.show()

    def abrir_ventana_modificar_producto(self):
        self.modificar_producto_window = ModificarProductoWindow()
        self.modificar_producto_window.show()

    def abrir_ventana_eliminar_producto(self):
        self.eliminar_producto_window = EliminarProductoWindow()
        self.eliminar_producto_window.show()
