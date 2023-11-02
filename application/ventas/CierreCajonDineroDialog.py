from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QMessageBox

from servicios.ticket_service import TicketService
from servicios.vendedor_service import VendedorService

class CierreCajonDineroDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cierre de Cajón de Dinero")
        self.setGeometry(200, 200, 400, 300)

        main_layout = QVBoxLayout()

        self.ticket_service = TicketService()
        self.vendedor_service = VendedorService()

        tickets = self.ticket_service.obtenerTicketsDelDia()
        total = 0.0

        table = QTableWidget(len(tickets), 5)
        table.setHorizontalHeaderLabels(['ID Ticket', 'Fecha', 'Vendedor', 'Forma de Pago', 'Total'])

        for i, ticket in enumerate(tickets):
            id_ticket = QTableWidgetItem(str(ticket.id_ticket))
            fecha = QTableWidgetItem(str(ticket.fecha))
            nombre_vendedor = QTableWidgetItem(str(self.vendedor_service.obtenerNombrePorId(ticket.id_vendedor)))
            if ticket.tipo_de_pago == 0:
                tipo_de_pago = QTableWidgetItem('Efectivo')
            total_value = float(ticket.total)
            total += total_value  # Suma el total de cada ticket a la suma total
            total_item = QTableWidgetItem("{:.2f}".format(total_value))

            table.setItem(i, 0, id_ticket)
            table.setItem(i, 1, fecha)
            table.setItem(i, 2, nombre_vendedor)
            table.setItem(i, 3, tipo_de_pago)
            table.setItem(i, 4, total_item)

        main_layout.addWidget(table)

        total_label = QLabel("Total tickets: {:.2f}".format(total))
        main_layout.addWidget(total_label)

        button_layout = QHBoxLayout()
        correct_button = QPushButton("Correcto")
        incorrect_button = QPushButton("No coincide")

        button_layout.addWidget(correct_button)
        button_layout.addWidget(incorrect_button)

        correct_button.clicked.connect(self.mostrar_mensaje_exito)
        incorrect_button.clicked.connect(self.mostrar_mensaje_advertencia)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        total_width = sum([table.columnWidth(i) for i in range(table.columnCount())])
        extra_width = 60  
        extra_height = 100 
        self.resize(total_width + extra_width, self.sizeHint().height() + extra_height) 

    def mostrar_mensaje_exito(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Éxito")
        msg.setText("Cierre de cajón de dinero correcto")
        msg.exec_()

    def mostrar_mensaje_advertencia(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Advertencia")
        msg.setText("El cajón de dinero no coincide. Informar al supervisor")
        msg.exec_()