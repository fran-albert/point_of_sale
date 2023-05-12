from PyQt5.QtWidgets import QLabel, QWidget,QCheckBox, QDialog, QSpacerItem, QSizePolicy, QPushButton, QVBoxLayout, QHBoxLayout, QFrame,  QTabWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from utils.Utils import Utils
from TicketWindow import TicketWindow
from datetime import datetime
from servicios.ticket_service import TicketService
from entities.ticket import Ticket



class VentasUtilsButtons:



    # PAYMENT WINDOW
    @staticmethod
    def show_payment_window(usuario, total, parent):

        ticket_service = TicketService()
        
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
            # Conectar el clic en el botón "Cobrar YA" a la función cobrar_ya
            cobrar_button.clicked.connect(lambda: cobrar_ya(usuario, tab_widget.currentIndex(), total, save_ticket_checkbox.isChecked()))


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
        cobrar_button_efectivo.clicked.connect(lambda: cobrar_ya(usuario, 0, total, save_ticket_checkbox_efectivo))

        tab_layout_tarjeta, cobrar_button_tarjeta, save_ticket_checkbox_tarjeta = create_tab_content()
        tarjeta_tab.setLayout(tab_layout_tarjeta)
        cobrar_button_tarjeta.clicked.connect(lambda: cobrar_ya(usuario, 1, total, save_ticket_checkbox_tarjeta))

        tab_layout_transferencia, cobrar_button_transferencia, save_ticket_checkbox_transferencia = create_tab_content()
        transferencia_tab.setLayout(tab_layout_transferencia)
        cobrar_button_transferencia.clicked.connect(lambda: cobrar_ya(usuario, 2, total, save_ticket_checkbox_transferencia))

        # Agregar las pestañas al widget de pestañas
        tab_widget.addTab(efectivo_tab, "Efectivo")
        tab_widget.addTab(tarjeta_tab, "Débito/Crédito")
        tab_widget.addTab(transferencia_tab, "Transferencia")

        
        tab_layout_efectivo, cobrar_button_efectivo, save_ticket_checkbox_efectivo = create_tab_content()
        efectivo_tab.setLayout(tab_layout_efectivo)
        cobrar_button_efectivo.clicked.connect(lambda: cobrar_ya(usuario, 0, total, save_ticket_checkbox_efectivo))


        # Función para manejar el clic en el botón "Cobrar YA"
        def cobrar_ya(usuario, tipo_de_pago, total, guardar_ticket): 
            total = round(total, 2)
            fecha = datetime.now()
            ticket = Ticket(usuario, total, tipo_de_pago, fecha)
            idTicket_generado = ticket_service.insertarTicket(ticket)

            if guardar_ticket:
                with open('C:/Users/Francisco/Desktop/ticket.txt', 'w') as f:
                    f.write(f"Usuario: {usuario}\nTotal: {total}\nTipo de Pago: {tipo_de_pago}\nFecha: {fecha}\n")
            print("Venta realizada")


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

    @staticmethod
    def show_ticket_window(parent, ticket, total):
        # Crear una instancia de TicketWindow con los argumentos requeridos
        ticket_instance = TicketWindow(ticket, total)

        # Mostrar la ventana del ticket
        ticket_instance.show()

