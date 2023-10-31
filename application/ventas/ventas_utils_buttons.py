from PyQt5.QtWidgets import QLabel, QWidget,QCheckBox, QDialog, QSpacerItem, QSizePolicy, QPushButton, QVBoxLayout, QHBoxLayout, QFrame,  QTabWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from utils.Utils import Utils
from servicios.producto_vendido_service import ProductoVendidoService
from datetime import datetime
from servicios.ticket_service import TicketService
from servicios.producto_service import ProductoService
from entities.ticket import Ticket
from entities.productos_vendido import ProductosVendido
import tkinter as tk
from tkinter import messagebox

class VentasUtilsButtons:
 
    def __init__(self, ventas_window):
        self.ventas_window = ventas_window

    # PAYMENT WINDOW
    def show_payment_window(self, usuario, total, parent, productos_vendidos):

        ticket_service = TicketService()
        producto_vendido_service = ProductoVendidoService()

        payment_window = QDialog(parent)
        payment_window.setWindowTitle("Pago")
        payment_window.setFixedSize(400, 280)  
        payment_window.setStyleSheet("background-color: #FFFFFF;")  

        total_label = QLabel(f"TOTAL: {total:.2f}")
        total_label.setAlignment(Qt.AlignCenter)

        total_label.setStyleSheet("""
            QLabel {
                font-weight: bold;
                font-size: 16px larger;
            }
        """)
        top_layout = QVBoxLayout()
        top_layout.addWidget(total_label)

        # Línea divisoria
        divider = QFrame()
        divider.setFrameShape(QFrame.HLine)
        divider.setFrameShadow(QFrame.Sunken)
        divider.setStyleSheet("color: #BDBDBD;")

        tab_widget = QTabWidget()

        efectivo_tab = QWidget()
        tarjeta_tab = QWidget()
        transferencia_tab = QWidget()

        def create_tab_content():
            cobrar_button = QPushButton("Cobrar YA")
            cobrar_button.setStyleSheet("""
                QPushButton {
                    font-weight: bold;
                    background-color: #3498db;
                    border: 1px solid #2980b9;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
                QPushButton:pressed {
                    background-color: #1c6ba0;
                }
            """)

            save_ticket_checkbox = QCheckBox("Guardar Ticket")

            buttons_layout = QHBoxLayout()
            buttons_layout.addStretch()
            buttons_layout.addWidget(cobrar_button)
            buttons_layout.addWidget(save_ticket_checkbox)
            buttons_layout.addStretch()

            tab_layout = QVBoxLayout()
            tab_layout.addStretch()
            tab_layout.addLayout(buttons_layout)
            tab_layout.addStretch()

            return tab_layout, cobrar_button, save_ticket_checkbox 


        # Crear contenido para cada pestaña
        tab_layout_efectivo, cobrar_button_efectivo, save_ticket_checkbox_efectivo = create_tab_content()
        efectivo_tab.setLayout(tab_layout_efectivo)
        cobrar_button_efectivo.clicked.connect(lambda: realizar_venta_y_cobrar(usuario, 0, total, save_ticket_checkbox_efectivo.isChecked(), productos_vendidos))

        tab_layout_tarjeta, cobrar_button_tarjeta, save_ticket_checkbox_tarjeta = create_tab_content()
        tarjeta_tab.setLayout(tab_layout_tarjeta)
        cobrar_button_tarjeta.clicked.connect(lambda: realizar_venta_y_cobrar(usuario, 1, total, save_ticket_checkbox_tarjeta.isChecked(), productos_vendidos))

        tab_layout_transferencia, cobrar_button_transferencia, save_ticket_checkbox_transferencia = create_tab_content()
        transferencia_tab.setLayout(tab_layout_transferencia)
        cobrar_button_transferencia.clicked.connect(lambda: realizar_venta_y_cobrar(usuario, 2, total, save_ticket_checkbox_transferencia.isChecked(), productos_vendidos))

        # Agregar las pestañas al widget de pestañas
        tab_widget.addTab(efectivo_tab, "Efectivo")
        tab_widget.addTab(tarjeta_tab, "Débito/Crédito")
        tab_widget.addTab(transferencia_tab, "Transferencia")

        def realizar_venta_y_cobrar(usuario, tipo_de_pago, total, guardar_ticket, productos_vendidos): 
            id_usuario = Utils.id_usuario
            total = round(total, 2)
            fecha = datetime.now().date()
            ticket = Ticket(id_usuario, total, tipo_de_pago, fecha)
            idTicket_generado = ticket_service.insertarTicket(ticket)

            producto_service = ProductoService()
            
            for producto in productos_vendidos:
                previo_venta = float(producto.get_precio_venta())
                previo_venta = "{:.2f}".format(previo_venta)
                precio_venta_total = float(producto.get_precio_venta()) * float(producto.get_cantidad_vendida())
                precio_venta_total = "{:.2f}".format(precio_venta_total) 
                producto_vendido = ProductosVendido(
                    None,  
                    idTicket_generado,  
                    producto.get_producto_vendido(),  
                    producto.get_codigo(),  
                    producto.get_cantidad_vendida(),  
                    previo_venta,  
                    precio_venta_total
                )
                producto_vendido_service.insertarProdVendido(producto_vendido)
                producto_service.actualizarStock(producto_vendido.get_codigo(), producto_vendido.get_cantidad_vendida())
            productos_vendidos = producto_vendido_service.obtenerProductosVendidos(idTicket_generado)
            
            if guardar_ticket:
                with open('C:/Users/Francisco/Desktop/ticket.txt', 'w') as f:
                    f.write(f"Usuario: {usuario}\nTotal: {total}\n")
                    if tipo_de_pago == 0:
                        metodo_pago = 'Efectivo'
                    elif tipo_de_pago == 1:
                        metodo_pago = 'Tarjeta'
                    elif tipo_de_pago == 2:
                        metodo_pago = 'Transferencia'
                    else:
                        metodo_pago = str(tipo_de_pago)  
                    f.write(f"Tipo de Pago: {metodo_pago}\n")
                    f.write(f"Fecha: {fecha}\n")
                    
                    # # Aquí puedes escribir la lista de productos vendidos en el archivo de alguna manera
                    for producto in productos_vendidos:
                        f.write(f"Producto: {producto.get_producto_vendido()}\n")
                        f.write(f"Cantidad: {producto.get_cantidad_vendida()}\n")
                        f.write(f"Precio Unitario: {producto.get_precio_venta()}\n")
                        f.write(f"Precio Total {producto.get_precio_venta() * producto.get_cantidad_vendida()}\n\n")
            root = tk.Tk()
            root.withdraw() 
            messagebox.showinfo("Información", "Venta realizada")


        # Crear un QHBoxLayout para centrar el botón horizontalmente
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addStretch()

        # Añadir los widgets al layout de la pestaña de efectivo
        efectivo_layout = QVBoxLayout()
        
        efectivo_layout.addLayout(buttons_layout)
        efectivo_tab.setLayout(efectivo_layout)

        # Agregamos iconos a los selectores de pestañas
        tab_widget.tabBar().setTabIcon(0, QIcon("utils/img/icons8-efectivo-96.png"))
        tab_widget.tabBar().setTabIcon(1, QIcon("utils/img/icons8-visa-96.png"))
        tab_widget.tabBar().setTabIcon(2, QIcon("utils/img/icons8-edificio-del-banco-96.png"))

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(divider)
        main_layout.addWidget(tab_widget)

        # Función para manejar el cambio de pestaña
        def tab_changed(index):
            if index == 0:  # Pestaña "Efectivo"
                print('efectivo')
            elif index == 1: 
                print('tarjeta')
            else: 
                print('transferencia')

        # Conectar el cambio de pestaña a la función tab_changed
        tab_widget.currentChanged.connect(tab_changed)

        # Inicializar el estado de los widgets según la pestaña actual
        tab_changed(tab_widget.currentIndex())

        # Espaciadores
        spacer_top = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        spacer_bottom = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addSpacerItem(spacer_top)
        main_layout.addSpacerItem(spacer_bottom)

        # Aplicar el layout a la ventana de pago
        payment_window.setLayout(main_layout)

        # Mostrar la ventana de pago
        payment_window.exec_()
    
    def create_efectivo_tab_label():
        # Crear un QWidget personalizado para la etiqueta de la pestaña
        custom_widget = QWidget()
        custom_layout = QHBoxLayout()

        # Crear QLabel para el texto de efectivo en negrita
        efectivo_label = QLabel()
        efectivo_label.setText("<span style='font-weight: bold;'>Efectivo</span>")

        # Crear QLabel para el ícono
        icono_efectivo = QPixmap("icono_efectivo.png")
        efectivo_icon = QLabel()
        efectivo_icon.setPixmap(icono_efectivo)
        efectivo_icon.setFixedSize(24, 24)

        # Agregar el texto y el ícono al layout personalizado
        custom_layout.addWidget(efectivo_label)
        custom_layout.addWidget(efectivo_icon)
        custom_widget.setLayout(custom_layout)

        return custom_widget