from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QHBoxLayout

from servicios.ticket_service import TicketService
from servicios.vendedor_service import VendedorService

class CierreCajonDinero(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cierre de Cajón de Dinero")
        self.setGeometry(200, 200, 400, 300)

        main_layout = QVBoxLayout()

        self.ticket_service = TicketService()
        self.vendedor_service = VendedorService()

        tickets = self.ticket_service.obtenerTicketsDelDia()

        table = QTableWidget(len(tickets), 5)
        table.setHorizontalHeaderLabels(['ID Ticket', 'Fecha', 'Vendedor', 'Forma de Pago', 'Total'])

        for i, ticket in enumerate(tickets):
            id_ticket = QTableWidgetItem(str(ticket.id_ticket))
            fecha = QTableWidgetItem(str(ticket.fecha))
            nombre_vendedor = QTableWidgetItem(str(self.vendedor_service.obtenerNombrePorId(ticket.id_vendedor)))
            if ticket.tipo_de_pago == 0:
                tipo_de_pago = QTableWidgetItem('Efectivo')
            total = QTableWidgetItem("{:.2f}".format(float(ticket.total)))

            table.setItem(i, 0, id_ticket)
            table.setItem(i, 1, fecha)
            table.setItem(i, 2, nombre_vendedor)
            table.setItem(i, 3, tipo_de_pago)
            table.setItem(i, 4, total)

        main_layout.addWidget(table)

        button_layout = QHBoxLayout()
        cancel_button = QPushButton("Cancelar")
        accept_button = QPushButton("Aceptar")

        button_layout.addWidget(cancel_button)
        button_layout.addWidget(accept_button)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        total_width = sum([table.columnWidth(i) for i in range(table.columnCount())])
        extra_width = 60  
        extra_height = 100 
        self.resize(total_width + extra_width, self.sizeHint().height() + extra_height) 