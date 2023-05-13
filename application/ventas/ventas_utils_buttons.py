from PyQt5.QtWidgets import QLabel, QWidget,QCheckBox, QDialog, QSpacerItem, QSizePolicy, QPushButton, QVBoxLayout, QHBoxLayout, QFrame,  QTabWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from utils.Utils import Utils
from servicios.producto_vendido_service import ProductoVendidoService
from datetime import datetime
from servicios.ticket_service import TicketService
from entities.ticket import Ticket
from entities.productos_vendido import ProductosVendido


class VentasUtilsButtons:

    # PAYMENT WINDOW
    @staticmethod
    def show_payment_window(usuario, total, parent, productos_vendidos):

        ticket_service = TicketService()
        producto_vendido_service = ProductoVendidoService()

        payment_window = QDialog(parent)
        payment_window.setWindowTitle("Pago")
        payment_window.setFixedSize(400, 280)  # Cambiar el tamaño de la ventana
        payment_window.setStyleSheet("background-color: #FFFFFF;")  # Cambiar el color de fondo

        # Crear el QLabel para mostrar el mensaje "TOTAL:"
        total_label = QLabel(f"TOTAL: {total:.2f}")
        total_label.setAlignment(Qt.AlignCenter)

        # Establecer el estilo de total_label con fuente en negrita y tamaño de fuente 3 px más grande
        total_label.setStyleSheet("""
            QLabel {
                font-weight: bold;
                font-size: 16px larger;
            }
        """)
        # Layout superior
        top_layout = QVBoxLayout()
        top_layout.addWidget(total_label)

        # Línea divisoria
        divider = QFrame()
        divider.setFrameShape(QFrame.HLine)
        divider.setFrameShadow(QFrame.Sunken)
        divider.setStyleSheet("color: #BDBDBD;")

        # Crear el widget de pestañas y agregar pestañas
        tab_widget = QTabWidget()

        efectivo_tab = QWidget()
        tarjeta_tab = QWidget()
        transferencia_tab = QWidget()

        def create_tab_content():
            # Crear el botón "Cobrar YA" y aplicar estilo personalizado
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

            # Crear un checkbox para "Guardar Ticket"
            save_ticket_checkbox = QCheckBox("Guardar Ticket")

            # Crear un QHBoxLayout para centrar el botón y el checkbox horizontalmente
            buttons_layout = QHBoxLayout()
            buttons_layout.addStretch()
            buttons_layout.addWidget(cobrar_button)
            buttons_layout.addWidget(save_ticket_checkbox)
            buttons_layout.addStretch()

            # Crear un QVBoxLayout para la pestaña
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
            total = round(total, 2)
            fecha = datetime.now()
            ticket = Ticket(usuario, total, tipo_de_pago, fecha)
            idTicket_generado = ticket_service.insertarTicket(ticket)
            # Aquí puedes insertar cada producto comprado en la base de datos
            for producto in productos_vendidos:
                producto_vendido = ProductosVendido(
                    None,  # idProdVendido se establecerá automáticamente en la base de datos
                    idTicket_generado,  # idTicket se establecerá después de insertar el ticket
                    producto.get_prod_vendido(),  
                    producto.get_codigo(),  
                    producto.get_cant_vendida(),  
                    producto.get_precio_venta(),  
                    producto.get_precio_venta_total() * producto.get_cant_vendida()  # precio_venta_total es el precio de venta por la cantidad
                )
                producto_vendido_service.insertarProdVendido(producto_vendido)
            # Luego, puedes llamar a cobrar_ya para guardar el ticket
            #cobrar_ya(usuario, tipo_de_pago, total, guardar_ticket)

        # Función para manejar el clic en el botón "Cobrar YA"
        # def cobrar_ya(usuario, tipo_de_pago, total, guardar_ticket):
        #     total = round(total, 2)
        #     fecha = datetime.now()
        #     ticket = Ticket(usuario, total, tipo_de_pago, fecha)
        #     idTicket_generado = ticket_service.insertarTicket(ticket)

        #     # Obtén la lista de productos vendidos
        #     productos_vendidos = producto_vendido_service.obtenerProductosVendidos(idTicket_generado)

        #     if guardar_ticket:
        #         with open('C:/Users/Francisco/Desktop/ticket.txt', 'w') as f:
        #             f.write(f"Usuario: {usuario}\nTotal: {total}\nId: {idTicket_generado}\nTipo de Pago: {tipo_de_pago}\nFecha: {fecha}\n")
        #             # Aquí puedes escribir la lista de productos vendidos en el archivo de alguna manera
        #             for producto in productos_vendidos:
        #                 f.write(f"Producto Vendido: {producto.get_nombre()}\n")
        #                 f.write(f"Codigo: {producto.get_codigo()}\n")
        #                 f.write(f"Cantidad Vendida: {producto.get_cantStock()}\n")
        #                 f.write(f"Precio de Venta: {producto.get_precioVenta()}\n")
        #                 f.write(f"Precio Total de Venta: {producto.get_precioVenta() * producto.get_cantStock()}\n\n")
        #     print("Venta realizada")


        # Crear un QHBoxLayout para centrar el botón horizontalmente
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addStretch()

        # Añadir los widgets al layout de la pestaña de efectivo
        efectivo_layout = QVBoxLayout()
        
        efectivo_layout.addLayout(buttons_layout)
        efectivo_tab.setLayout(efectivo_layout)

        # Agregamos iconos a los selectores de pestañas
        tab_widget.tabBar().setTabIcon(0, QIcon("img/icons8-efectivo-96.png"))
        tab_widget.tabBar().setTabIcon(1, QIcon("img/icons8-visa-96.png"))
        tab_widget.tabBar().setTabIcon(2, QIcon("img/icons8-edificio-del-banco-96.png"))

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