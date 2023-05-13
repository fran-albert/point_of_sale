from PyQt5.QtWidgets import QMenuBar, QMenu, QAction, QGraphicsView, QGraphicsScene, QLabel, QWidget,QLineEdit, QDialog, QTableWidget, QMessageBox, QToolButton, QSpacerItem, QSizePolicy, QHeaderView, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QFrame,  QTabWidget
from PyQt5.QtGui import QPixmap, QFont, QIcon, QImage
from PyQt5.QtCore import Qt, QDateTime, QSize
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from servicios.producto_service import ProductoService
from servicios.categoria_service import CategoriaService
from servicios.proveedor_service import ProveedorService
from application.categorias.abm_categorias import ABMCategoriasWindow
from reportlab.lib.styles import getSampleStyleSheet
import fitz, os, time, traceback, io



class Utils:
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

    # PDF GENERATES (SALES - STOCK)
    def show_pdf_preview(main_window, pdf_buffer, table_data, headers):
        try:
            pdf_buffer.seek(0)  # Asegurarse de que el puntero esté al inicio del archivo

            # Convertir el PDF a una imagen utilizando PyMuPDF
            doc = fitz.open("pdf", pdf_buffer.getvalue())
            page = doc.load_page(0)  # Carga la primera página
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Renderiza la página a un pixmap con un factor de zoom de 2
            img = QImage(pix.samples, pix.width, pix.height, QImage.Format_RGB888)  # Crea una QImage a partir de los datos de imagen del pixmap
            image = QPixmap.fromImage(img)  # Convierte la QImage a QPixmap

            # Crear un QGraphicsView y QGraphicsScene para mostrar la imagen
            scene = QGraphicsScene()
            scene.addPixmap(image)
            view = QGraphicsView(scene)

            preview_dialog = QDialog(main_window)
            preview_dialog.setWindowTitle("Vista Previa")
            preview_dialog.setFixedSize(800, 400)

            save_pdf_button = QPushButton("Guardar PDF")

            def save_pdf():
                pdf_file = f"report_{time.strftime('%Y%m%d_%H%M%S')}.pdf"
                pdf_path = os.path.join(os.path.expanduser('~'), 'Desktop', pdf_file)

                with open(pdf_path, 'wb') as f:
                    f.write(pdf_buffer.getbuffer())

                QMessageBox.information(main_window, "Éxito", f"PDF guardado exitosamente en {pdf_path}")
                preview_dialog.accept()

            save_pdf_button.clicked.connect(save_pdf)

            layout = QVBoxLayout()
            layout.addWidget(view)
            layout.addWidget(save_pdf_button)
            preview_dialog.setLayout(layout)

            result = preview_dialog.exec()
            view.setScene(None)  # Elimina la referencia a la escena antes de cerrar el diálogo
            return True if result == QDialog.Accepted else False
        except Exception as e:
            print("Error al mostrar la vista previa del PDF:")
            traceback.print_exc()  # Imprimir el traceback de la excepción
            QMessageBox.critical(main_window, "Error", f"Ocurrió un error al mostrar la vista previa del PDF: {e}")
            return False
        
    def generate_pdf(main_window, title, data=None):
        pdf_buffer = io.BytesIO()

        doc = SimpleDocTemplate(pdf_buffer, pagesize=landscape(letter))
        elements = []

        # Título del reporte
        title = title
        elements.append(Paragraph(title, getSampleStyleSheet()['Heading1']))

        # Tabla de datos
        if data:
            table = Table(data)

            # Estilos de la tabla
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))

            elements.append(table)

        # Generar el PDF
        doc.build(elements)

        pdf_buffer.seek(0)
        return pdf_buffer

    def generate_stock_report(main_window):
        try:
            categoria_service = CategoriaService()
            categorias = categoria_service.obtenerCategorias()
            categoria_descripcion_map = {categoria.id: categoria.descripcion for categoria in categorias}

            proveedor_service = ProveedorService()
            proveedores = proveedor_service.obtenerProveedores()
            proveedor_nombre_map = {proveedor.id: proveedor.nombre for proveedor in proveedores}

            producto_service = ProductoService()

            # Obtener datos del stock desde la base de datos
            stock_data = producto_service.obtenerProductos()


            # Preparar datos para la tabla en el reporte
            data = [['Código', 'Producto', 'Cantidad', 'Precio Compra', 'Precio Venta', 'Categoria', 'Proveedor', 'Fecha Vencimiento']]
            for producto in stock_data:
                nombre_del_proveedor = proveedor_nombre_map.get(int(producto.proveedor), "Proveedor Desconocido")
                data.append([producto.codigo, producto.nombre, producto.cantStock, producto.precioCompra, "{:.2f}".format(float(producto.precioVenta)), categoria_descripcion_map.get(producto.categoria, "Desconocida"), nombre_del_proveedor, producto.fechaVenc])

            pdf_buffer = Utils.generate_pdf(main_window, "Reporte de Stock", data)

                    # Preparar datos para mostrar en el visor de PDF
            stock_headers = ["ID", "Producto", "Cantidad", "Precio Compra", "Precio Venta", "Categoria", "Proveedor", "Fecha Vencimiento"]
            stock_data_for_preview = [[producto.codigo, producto.nombre, producto.cantStock, producto.precioCompra, producto.precioVenta, categoria_descripcion_map.get(producto.categoria, "Desconocida"), nombre_del_proveedor, producto.fechaVenc] for producto in stock_data]
            
            Utils.show_pdf_preview(main_window, pdf_buffer, stock_data_for_preview, stock_headers)
        except Exception as e:
            print("Error al generar el reporte de stock:")
            QMessageBox.critical(main_window, "Error", f"Ocurrió un error al generar el reporte de stock: {e}")

    def generate_sales_report(main_window):

        try:
            # Datos de ejemplo para la tabla
            data = [['Producto', 'Cantidad', 'Precio'],
                    ['Producto 1', '10', '100'],
                    ['Producto 2', '5', '150'],
                    ['Producto 3', '8', '200']]

            pdf_buffer = Utils.generate_pdf(main_window, "Reporte de Ventas", data)

            stock_headers = ["ID", "Producto", "Cantidad"]
            stock_data = [
                [1, "Producto 1", 10],
                [2, "Producto 2", 5],
                [3, "Producto 3", 20]
            ]

            Utils.show_pdf_preview(main_window, pdf_buffer, stock_data, stock_headers)
        except Exception as e:
            print("Error al generar el reporte de ventas:")
            #traceback.print_exc()  # Imprimir el traceback de la excepción
            QMessageBox.critical(main_window, "Error", f"Ocurrió un error al generar el reporte de ventas: {e}")

# Utils.py
def create_main_window_menu(parent):
    menu_bar = parent.menuBar()

    archivo_menu = QMenu("Archivo", parent)
    menu_bar.addMenu(archivo_menu)

    menu_menu = QMenu("Menú", parent)
    menu_bar.addMenu(menu_menu)

    clientes_action = QAction(QIcon("img/icons8-grupo-de-usuarios-hombre-y-mujer-48.png"),"Clientes", parent)
    menu_menu.addAction(clientes_action)

    categorias_action = QAction(QIcon("img/icons8-almacén-48.png"),"Categorias", parent)
    menu_menu.addAction(categorias_action)

    productos_action = QAction(QIcon("img/icons8-almacén-48.png"),"Productos", parent)
    menu_menu.addAction(productos_action)

    proveedores_action = QAction(QIcon("img/icons8-proveedor-48.png"),"Proveedores", parent)
    menu_menu.addAction(proveedores_action)

    usuarios_action = QAction(QIcon("img/icons8-grupo-de-usuarios-hombre-y-mujer-48.png"),"Usuarios", parent)
    menu_menu.addAction(usuarios_action)

    movimientos_menu = QMenu("Movimientos", parent)
    menu_bar.addMenu(movimientos_menu)

    ventas_action = QAction(QIcon("img/icons8-caja-registradora-48.png"), "Ventas", parent)
    movimientos_menu.addAction(ventas_action)

    reportes_menu = QMenu("Reportes", parent)
    menu_bar.addMenu(reportes_menu)

    reporte_stock_action = QAction(QIcon("img/icons8-pdf-48.png"), "Reporte de Stock", parent)
    reportes_menu.addAction(reporte_stock_action)

    reporte_ventas_action = QAction(QIcon("img/icons8-pdf-48.png"), "Reporte de Ventas", parent)
    reportes_menu.addAction(reporte_ventas_action)

    configuracion_menu = QMenu("Configuración", parent)
    menu_bar.addMenu(configuracion_menu)

    acerca_menu = QMenu("Acerca", parent)
    menu_bar.addMenu(acerca_menu)

    reporte_stock_action.triggered.connect(parent.generate_stock_report_wrapper)
    reporte_ventas_action.triggered.connect(parent.generate_sales_report_wrapper)
    categorias_action.triggered.connect(parent.show_categories_window)
    productos_action.triggered.connect(parent.show_products_window)
    proveedores_action.triggered.connect(parent.show_proveedores_window)
    ventas_action.triggered.connect(parent.show_ventas_window)

# HEADER
def init_header(parent, width, username, menu_bar_height):
    parent_width = width
    header = QFrame(parent)
    header.move(0, menu_bar_height)
    header.setFixedHeight(100)
    header.setMinimumWidth(parent_width)
    header.setMaximumWidth(parent_width)

    header.setStyleSheet("background-color: #F9F5EB;")

    # Lado izquierdo
    left_layout = QVBoxLayout()
    user_label = QLabel(f"User: {username}", header)
    user_label.setStyleSheet("color: black;")
    left_layout.addWidget(user_label, alignment=Qt.AlignTop | Qt.AlignLeft)

    # Centro: Logo
    center_layout = QVBoxLayout()
    logo_label = QLabel(header)
    pixmap = QPixmap("img/logosinfondo.png").scaled(300, 250, Qt.KeepAspectRatio)
    logo_label.setPixmap(pixmap)
    logo_label.setAlignment(Qt.AlignCenter)
    center_layout.addWidget(logo_label)

    # Lado derecho
    right_layout = QGridLayout()

    # Fecha
    fecha = QDateTime.currentDateTime().toString("dd-MM-yyyy")
    fecha_num_label = QLabel(fecha, header)
    fecha_num_label.setStyleSheet("color: black;")
    right_layout.addWidget(fecha_num_label, 0, 1, Qt.AlignTop | Qt.AlignRight)

    # Location
    location_label = QLabel("Rosario, Argentina", header)
    location_label.setStyleSheet("color: black;")
    right_layout.addWidget(location_label, 1, 0, 1, 2, Qt.AlignTop | Qt.AlignRight)

    # Spacer
    bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
    right_layout.addItem(bottom_spacer, 2, 0, 1, 2)

    # Layout principal
    main_layout = QHBoxLayout(header)
    main_layout.addLayout(left_layout)
    main_layout.setStretchFactor(left_layout, 1)
    main_layout.addLayout(center_layout)
    main_layout.setStretchFactor(center_layout, 1)
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


