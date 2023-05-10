from PyQt5.QtWidgets import QLabel, QWidget,QLineEdit, QDialog, QSpacerItem, QSizePolicy, QPushButton, QVBoxLayout, QHBoxLayout, QFrame,  QTabWidget
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

        tab_widget.addTab(efectivo_tab, "Efectivo")
        tab_widget.addTab(tarjeta_tab, "Débito/Crédito")
        tab_widget.addTab(transferencia_tab, "Transferencia")

        # Crear QLineEdit y QLabel para "PAGA CON:" y "VUELTO:"
        paga_con_label = QLabel("PAGA CON:")
        paga_con_edit = QLineEdit()
        vuelto_label = QLabel("VUELTO:")
        vuelto_value_label = QLabel("0.00")

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
        # Función para manejar el clic en el botón "Cobrar YA"
        def cobrar_ya(usuario, tipo_de_pago, total): 
            total = round(total, 2)
            fecha = datetime.now()
            ticket = Ticket(usuario, total, tipo_de_pago, fecha)
            tickets = ticket_service.insertarTicket(ticket)
            #llamar a los services.
            # ALGUN PARAMETRO PARA SABER SI USO 0 EFECTIO 1 CARD o 2 TRANSFE
            # 1) INSERTAR TICKET
            # 2) INSERTAR LOS PRODUCTOS VENDIDOS A PARTIR DEL IDTICKET QUE SE GENERO EN 1)
            # 3) DESCONTAR DEL STOCK DE PRODUCTO (COD DE PRODUCTO)
            print("Venta realizada")

        # Conectar el clic en el botón "Cobrar YA" a la función cobrar_ya
        cobrar_button.clicked.connect(lambda: cobrar_ya(usuario, tab_widget.currentIndex(), total))

        # Crear el botón "Ver Ticket" y aplicar estilo personalizado
        ver_ticket_button = QPushButton("Ver Ticket")
        ver_ticket_button.setStyleSheet("""
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

        # Conectar el clic en el botón "Ver Ticket" a la función show_ticket_window
        #ver_ticket_button.clicked.connect(lambda: VentasUtilsButtons.show_ticket_window(parent, ticket, total ))


        # Crear un QHBoxLayout para centrar el botón horizontalmente
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(cobrar_button)
        buttons_layout.addWidget(ver_ticket_button)
        buttons_layout.addStretch()

        # Centrar los QLabel y el QLineEdit
        paga_con_label.setAlignment(Qt.AlignCenter)
        vuelto_label.setAlignment(Qt.AlignCenter)
        vuelto_value_label.setAlignment(Qt.AlignCenter)
        paga_con_edit.setAlignment(Qt.AlignCenter)

        # Establecer el ancho fijo del QLineEdit y su política de tamaño
        paga_con_edit.setFixedWidth(80)
        paga_con_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Añadir los widgets al layout de la pestaña de efectivo
        efectivo_layout = QVBoxLayout()
        

        # Centrar QLineEdit horizontalmente
        paga_con_edit_layout = QHBoxLayout()
        paga_con_edit_layout.addStretch()
        paga_con_edit_layout.addWidget(paga_con_edit)
        paga_con_edit_layout.addStretch()

        efectivo_layout.addWidget(paga_con_label)
        efectivo_layout.addLayout(paga_con_edit_layout)
        efectivo_layout.addWidget(vuelto_label)
        efectivo_layout.addWidget(vuelto_value_label)
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
                paga_con_label.show()
                paga_con_edit.show()
                vuelto_label.show()
                vuelto_value_label.show()
            else:  # Otras pestañas
                paga_con_label.hide()
                paga_con_edit.hide()
                vuelto_label.hide()
                vuelto_value_label.hide()

        # Conectar el cambio de pestaña a la función tab_changed
        tab_widget.currentChanged.connect(tab_changed)

        # Inicializar el estado de los widgets según la pestaña actual
        tab_changed(tab_widget.currentIndex())

            # Función para manejar el cálculo del vuelto
        def calculate_vuelto():
            try:
                paga_con_str = paga_con_edit.text()
                paga_con = float(paga_con_str) if paga_con_str else 0.0
                total = float(total_label.text().split(": ")[1])
                vuelto = paga_con - total

                if vuelto < 0:
                    vuelto_value_label.setText(" Insuficiente")
                else:
                    vuelto_value_label.setText(" {:.2f}".format(vuelto))
            except ValueError as e:
                print(f"Error al calcular el vuelto: {e}")

        # Conectar el cambio de texto en paga_con_edit a la función calculate_vuelto
        paga_con_edit.textChanged.connect(calculate_vuelto)

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

