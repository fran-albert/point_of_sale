from PyQt5.QtWidgets import QLabel, QLineEdit, QDialog, QTableWidget, QMessageBox, QToolButton, QSpacerItem, QSizePolicy, QHeaderView, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtGui import QPixmap, QFont, QIcon
from reportlab.pdfgen import canvas
from PyQt5.QtCore import Qt, QDateTime, QSize
import os
import time

# LOGIN WINDOW
def create_login_ui(self):
        # Agrega un logo
        logo = QPixmap("img/logo2.0.jpg").scaled(300, 250, Qt.KeepAspectRatio)
        logo_mask = logo.createMaskFromColor(Qt.white)
        logo.setMask(logo_mask)
        logo_label = QLabel(self)
        logo_label.setPixmap(logo)

        # Agrega un campo de texto para ingresar el usuario
        self.usuario_edit = QLineEdit(self)
        usuario_label = QLabel("Usuario:", self)
        self.usuario_edit.returnPressed.connect(self.enter_pressed)  # Conecta la señal returnPressed al método enter_pressed

        # Agrega un campo de texto para ingresar la contraseña
        self.contrasena_edit = QLineEdit(self)
        self.contrasena_edit.setEchoMode(QLineEdit.Password)
        contrasena_label = QLabel("Contraseña:", self)
        self.contrasena_edit.returnPressed.connect(self.enter_pressed)  # Conecta la señal returnPressed al método enter_pressed

        # Botón "Iniciar sesión"
        iniciar_sesion_btn = QPushButton("Entrar", self)
        iniciar_sesion_btn.setFixedSize(100, 25)  # Establece el tamaño del botón
        iniciar_sesion_btn.clicked.connect(self.iniciar_sesion)

        # Botón "Salir"
        salir_btn = QPushButton("Salir", self)
        salir_btn.setFixedSize(100, 25)  # Establece el tamaño del botón
        salir_btn.clicked.connect(self.salir)

        # Cambia el tamaño de la fuente de los campos de texto
        font = QFont()
        font.setPointSize(14)  # Ajusta el tamaño de la fuente a 14
        self.usuario_edit.setFont(font)
        self.contrasena_edit.setFont(font)

        # Coloca los widgets en un layout de cuadrícula (grid)
        layout = QGridLayout()
        layout.addWidget(logo_label, 0, 0, 1, 2, alignment=Qt.AlignCenter)
        layout.setRowStretch(1, 1)  # Añade una fila para estirar en la parte superior
        layout.addWidget(usuario_label, 2, 0)
        layout.addWidget(self.usuario_edit, 2, 1)
        layout.addWidget(contrasena_label, 3, 0)
        layout.addWidget(self.contrasena_edit, 3, 1)
        layout.setRowStretch(4, 1)  # Añade una fila de estiramiento entre los campos de texto y los botones
        layout.addWidget(iniciar_sesion_btn, 5, 0, alignment=Qt.AlignRight)  # Alinea el botón a la derecha
        layout.addWidget(salir_btn, 5, 1, alignment=Qt.AlignLeft)  # Alinea el botón a la izquierda
        layout.setRowStretch(6, 1)  # Añade una fila para estirar en la parte inferior
        layout.setColumnStretch(2, 1)
        layout.setVerticalSpacing(20)  # Aumenta el espacio vertical entre los widgets

        # Establece el espacio horizontal entre los widgets a 0
        layout.setSpacing(0)

        # Establece el ancho de la primera columna de la cuadrícula
        layout.setColumnMinimumWidth(0, int(self.width() / 2))

        # Alinea los widgets horizontalmente al centro
        layout.setAlignment(Qt.AlignHCenter)

        self.setLayout(layout)

# HEADER
def init_header(self):
        header = QFrame(self)
        header.setGeometry(0, 0, self.width(), 100)
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
        fecha = QDateTime.currentDateTime().toString("dd-MM-yyyy")
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

# PRINCIPAL TABLE
def init_table(self):
    self.table = QTableWidget(self)
    self.table = QTableWidget(self)
    table_width = int(self.width() * 3 / 4)
    self.table.setGeometry(0, 140, table_width, self.height() - 160)
    self.table.setColumnCount(6)
    self.table.setHorizontalHeaderLabels(["No.", "Código de Barras", "Producto", "Cant.", "Precio Venta", "Precio Total"])
    header = self.table.horizontalHeader()

    # Establecer el modo de redimensionamiento y el ancho personalizado para las columnas "No." y "Cant."
    header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
    header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
    self.table.setColumnWidth(0, 50)  # Ancho de la columna "No."
    self.table.setColumnWidth(3, 50)  # Ancho de la columna "Cant."

    # Establecer el modo de redimensionamiento QHeaderView.Stretch para las otras columnas
    for col_index in [1, 2, 4, 5]:
        header.setSectionResizeMode(col_index, QHeaderView.Stretch)

# MENU BUTTON
def init_button_menu(self):
    button_menu = QFrame(self)
    button_menu.setGeometry(0, 100, self.width(), 40)

    button_layout = QHBoxLayout(button_menu)
    button_layout.setContentsMargins(0, 0, 0, 0)

    def create_tool_button(icon_path, tooltip_text):
        tool_button = QToolButton(button_menu)
        icon = QIcon(icon_path)
        tool_button.setIcon(icon)
        tool_button.setIconSize(QSize(32, 32))
        tool_button.setToolTip(tooltip_text)
        return tool_button

    usuarios_button = create_tool_button("img/icons8-grupo-de-usuarios-hombre-y-mujer-48.png", "Usuarios")
    addproductos_button = create_tool_button("img/icons8-addproduct.png", "Agregar Producto")
    editproductos_button = create_tool_button("img/icons8-editproduct.png", "Editar Producto")
    deleteproductos_button = create_tool_button("img/icons8-deleteproduct.png", "Eliminar Producto")
    stock_button = create_tool_button("img/icons8-almacén-48.png", "Stock")
    reportes_button = create_tool_button("img/icons8-pdf-48.png", "Reportes")
    ventas_button = create_tool_button("img/icons8-caja-registradora-48.png", "Ventas")
    logout_button = create_tool_button("img/icons8-salida-48.png", "Cerrar Sesión")

    button_layout.addWidget(usuarios_button)
    button_layout.addWidget(addproductos_button)
    button_layout.addWidget(editproductos_button)
    button_layout.addWidget(deleteproductos_button)
    button_layout.addWidget(stock_button)
    button_layout.addWidget(ventas_button)
    button_layout.addWidget(reportes_button)
    button_layout.addWidget(logout_button)

    spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)  # Agregar un "spacer" expansible
    button_layout.addItem(spacer)  # Añadir el "spacer" al layout

    button_menu.setLayout(button_layout)

    # usuarios_button.clicked.connect(self.abrir_ventana_agregar_producto) CODIGO PARA GESTIONAR USUARIOS
    addproductos_button.clicked.connect(self.abrir_ventana_agregar_producto)
    editproductos_button.clicked.connect(self.abrir_ventana_modificar_producto)
    deleteproductos_button.clicked.connect(self.abrir_ventana_eliminar_producto)
    logout_button.clicked.connect(self.cerrar_sesion)
    reportes_button.clicked.connect(self.show_reports_window)

# PDF WINDOWS
def show_reports_window(self):
    reports_window = QDialog(self)
    reports_window.setWindowTitle("Reportes")
    reports_window.setFixedSize(300, 200)

    stock_report_button = QPushButton("Reporte Stock")
    sales_report_button = QPushButton("Reporte Ventas")

    layout = QVBoxLayout()
    layout.addWidget(QLabel("Seleccione el tipo de reporte:"))
    layout.addWidget(stock_report_button)
    layout.addWidget(sales_report_button)

    reports_window.setLayout(layout)

    stock_report_button.clicked.connect(self.generate_stock_report)
    sales_report_button.clicked.connect(self.generate_sales_report)

    reports_window.exec_()

# PDF GENERATES (SALES - STOCK)
def generate_stock_report(self):
    pdf_file = f"stock_report_{time.strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf_path = os.path.join(os.path.expanduser('~'), 'Desktop', pdf_file)

    # Aquí puedes agregar la lógica para obtener los datos del stock y generar el contenido del PDF
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 750, "Reporte de Stock")
    c.save()

    QMessageBox.information(self, "Éxito", f"Reporte de stock generado exitosamente en {pdf_path}")

def generate_sales_report(self):
    pdf_file = f"sales_report_{time.strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf_path = os.path.join(os.path.expanduser('~'), 'Desktop', pdf_file)

    # Aquí puedes agregar la lógica para obtener los datos de las ventas y generar el contenido del PDF
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 750, "Reporte de Ventas")
    c.save()

    QMessageBox.information(self, "Éxito", f"Reporte de ventas generado exitosamente en {pdf_path}")

# RIGHT SIDE BUTTONS (COBRAR)
def init_right_side_buttons(self):
    # Crear un QFrame para contener los botones
    buttons_frame = QFrame(self)
    buttons_frame.setGeometry(int(self.width() * 3 / 4), 140, int(self.width() / 4), self.height() - 160)

    # Crear un QVBoxLayout para alinear los botones verticalmente
    buttons_layout = QVBoxLayout(buttons_frame)

    # Crear los botones y agregarlos al layout
    hola_button = QPushButton("REMOVER ITEM F4", buttons_frame)
    chau_button = QPushButton("CHAU", buttons_frame)
    gracias_button = QPushButton("GRACIAS", buttons_frame)

    cobrar_button = QPushButton("COBRAR", buttons_frame)
    cobrar_button.clicked.connect(self.show_payment_window)  # Conectar el botón "COBRAR" a la función show_payment_window
    buttons_layout.addWidget(cobrar_button)

    buttons_layout.addWidget(hola_button)
    buttons_layout.addWidget(chau_button)
    buttons_layout.addWidget(gracias_button)
    buttons_layout.addWidget(cobrar_button)

    # Aplicar el layout al QFrame
    buttons_frame.setLayout(buttons_layout)

# PAYMENT WINDOW
def show_payment_window(self):
    payment_window = QDialog(self)
    payment_window.setWindowTitle("Pago")
    payment_window.setFixedSize(600, 400)  # Cambiar el tamaño de la ventana
    payment_window.setStyleSheet("background-color: #F1F6F9;")  # Cambiar el color de fondo

    # Crear el QLabel para mostrar el mensaje "TOTAL:"
    total_label = QLabel("TOTAL:")
    total_label.setAlignment(Qt.AlignCenter)

    # Layout superior
    top_layout = QVBoxLayout()
    top_layout.addWidget(total_label)

    # Línea divisoria
    divider = QFrame()
    divider.setFrameShape(QFrame.HLine)
    divider.setFrameShadow(QFrame.Sunken)
    divider.setStyleSheet("color: #BDBDBD;")

    # Crear botones de pago y agregarles iconos y estilos
    button_style = """
        QPushButton {
        font: bold 14px;
        color: white;
        border: 1px solid #BDBDBD;
        border-radius: 5px;
        padding: 5px;
        background-color: #3F51B5;
        }
        QPushButton:hover {
        background-color: #5C6BC0;
        }
        QPushButton:pressed {
        background-color: #3949AB;
        }
        """

    cash_button = QPushButton("Efectivo")
    cash_button.setIcon(QIcon("img/icons8-efectivo-96.png"))  # Ruta a la imagen de efectivo
    cash_button.setStyleSheet(button_style)
    credit_debit_button = QPushButton("Débito/Crédito")
    credit_debit_button.setIcon(QIcon("img/icons8-visa-96.png"))  # Ruta a la imagen de débito/crédito
    credit_debit_button.setStyleSheet(button_style)
    transfer_button = QPushButton("Transferencia")
    transfer_button.setIcon(QIcon("img/icons8-edificio-del-banco-96.png"))  # Ruta a la imagen de transferencia
    transfer_button.setStyleSheet(button_style)

    # Layout inferior
    bottom_layout = QHBoxLayout()
    bottom_layout.addWidget(cash_button)
    bottom_layout.addWidget(credit_debit_button)
    bottom_layout.addWidget(transfer_button)

    # Layout principal
    main_layout = QVBoxLayout()
    main_layout.addLayout(top_layout)
    main_layout.addWidget(divider)
    main_layout.addLayout(bottom_layout)

    # Espaciadores
    spacer_top = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
    spacer_bottom = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
    main_layout.insertSpacerItem(0, spacer_top)
    main_layout.insertSpacerItem(-1, spacer_bottom)

    # Aplicar el layout a la ventana de pago
    payment_window.setLayout(main_layout)

    # Mostrar la ventana de pago
    payment_window.exec_()
