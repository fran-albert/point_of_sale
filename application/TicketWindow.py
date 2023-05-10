import os
import sys
# Obtén la ruta absoluta del directorio que contiene el archivo actual
current_directory = os.path.dirname(os.path.abspath(__file__))
# Añade la ruta del directorio raíz (un nivel superior) a sys.path
project_root = os.path.join(current_directory, '..')
sys.path.append(project_root)
from entities.metodo_pago import metodo_pago
from entities.ticket import Ticket
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt
from datetime import datetime
import sys


class TicketWindow(QMainWindow):
    def __init__(self, ticket, total):
        super().__init__()

        self.ticket = ticket
        self.total = total
        self.setWindowTitle("Ticket de Venta")
        
        # Crea un layout vertical
        layout = QVBoxLayout()

        # Crea las etiquetas y añádelas al layout
        titulo = QLabel("Ticket de Venta #" + str(self.ticket.get_idTicket()))
        fecha = QLabel("Fecha: " + str(self.ticket.get_fecha()))
        vendedor = QLabel("Vendedor: " + self.ticket.get_usuario())
        metodo_pago = QLabel("Método de Pago: " + str(self.ticket.get_tipo_de_pago()))
        total_pago = QLabel("Total: $" + str(self.total))  # Etiqueta del total del pago
        # lsita de prod vendidos

        layout.addWidget(titulo)
        layout.addWidget(fecha)
        layout.addWidget(vendedor)
        layout.addWidget(metodo_pago)
        layout.addWidget(total_pago)  # Agrega la etiqueta del total del pago al layout

        # Crea un widget central y configúralo con el layout
        widget_central = QWidget()
        widget_central.setLayout(layout)

        # Establece el widget central de la ventana
        self.setCentralWidget(widget_central)


