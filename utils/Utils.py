from PyQt5.QtWidgets import QMenuBar, QMenu, QAction, QGraphicsView, QGraphicsScene, QLabel, QWidget,QLineEdit, QDialog, QTableWidget, QMessageBox, QToolButton, QSpacerItem, QSizePolicy, QHeaderView, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QFrame,  QTabWidget
from PyQt5.QtGui import QPixmap, QFont, QIcon, QImage
from PyQt5.QtCore import Qt, QDateTime, QSize
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Spacer
from reportlab.lib import colors
from servicios.vendedor_service import VendedorService
from servicios.producto_service import ProductoService
from servicios.categoria_service import CategoriaService
from servicios.producto_vendido_service import ProductoVendidoService
from servicios.proveedor_service import ProveedorService
from servicios.ticket_service import TicketService
from application.categorias.lista_categorias import ListaCategoriasDialog
from reportlab.lib.styles import getSampleStyleSheet
import os, time, traceback, io, fitz
import datetime


class Utils:
    nombre_usuario = ""
    id_usuario = None
    # Pantalla de componentes Login
    def create_login_ui(self):

            logo = QPixmap("utils/img/logo2.0.jpg").scaled(300, 250, Qt.KeepAspectRatio)
            logo_mask = logo.createMaskFromColor(Qt.white)
            logo.setMask(logo_mask)
            logo_label = QLabel(self)
            logo_label.setPixmap(logo)

            self.usuario_edit = QLineEdit(self)
            usuario_label = QLabel("Usuario:", self)
            self.usuario_edit.returnPressed.connect(self.enter_pressed)  

            self.contrasena_edit = QLineEdit(self)
            self.contrasena_edit.setEchoMode(QLineEdit.Password)
            contrasena_label = QLabel("Contraseña:", self)
            self.contrasena_edit.returnPressed.connect(self.enter_pressed)  

            iniciar_sesion_btn = QPushButton("Entrar", self)
            iniciar_sesion_btn.setFixedSize(100, 25)  
            iniciar_sesion_btn.clicked.connect(self.iniciar_sesion)

            salir_btn = QPushButton("Salir", self)
            salir_btn.setFixedSize(100, 25)  
            salir_btn.clicked.connect(self.salir)

            font = QFont()
            font.setPointSize(14)  
            self.usuario_edit.setFont(font)
            self.contrasena_edit.setFont(font)

            layout = QGridLayout()
            layout.addWidget(logo_label, 0, 0, 1, 2, alignment=Qt.AlignCenter)
            layout.setRowStretch(1, 1)  
            layout.addWidget(usuario_label, 2, 0)
            layout.addWidget(self.usuario_edit, 2, 1)
            layout.addWidget(contrasena_label, 3, 0)
            layout.addWidget(self.contrasena_edit, 3, 1)
            layout.setRowStretch(4, 1)  
            layout.addWidget(iniciar_sesion_btn, 5, 0, alignment=Qt.AlignRight) 
            layout.addWidget(salir_btn, 5, 1, alignment=Qt.AlignLeft)  
            layout.setRowStretch(6, 1) 
            layout.setColumnStretch(2, 1)
            layout.setVerticalSpacing(20)  

            layout.setSpacing(0)
            layout.setColumnMinimumWidth(0, int(self.width() / 2))
            layout.setAlignment(Qt.AlignHCenter)
            self.setLayout(layout)

    # PDF GENERATES (SALES - STOCK)
    def show_pdf_preview(main_window, pdf_buffer, table_data, headers):
        try:
            pdf_buffer.seek(0) 

            doc = fitz.open("pdf", pdf_buffer.getvalue())
            page = doc.load_page(0)  
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  
            img = QImage(pix.samples, pix.width, pix.height, QImage.Format_RGB888)  
            image = QPixmap.fromImage(img)  

            scene = QGraphicsScene()
            scene.addPixmap(image)
            view = QGraphicsView(scene)

            preview_dialog = QDialog(main_window)
            preview_dialog.setWindowTitle("Vista Previa")
            preview_dialog.setFixedSize(1000, 700)

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
            view.setScene(None) 
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

        styles = getSampleStyleSheet()
        elements.append(Paragraph(title, styles['Heading1']))

        current_date = datetime.datetime.now().strftime('%d/%m/%Y')
        elements.append(Paragraph(f"Fecha: {current_date}", styles['Normal']))

        if data:
            table = Table(data)

            # Estilos de la tabla
            table.setStyle(TableStyle([
                # Encabezado
                ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  
                ('FONTSIZE', (0, 0), (-1, 0), 14),  
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  
                ('TOPPADDING', (0, 0), (-1, 0), 12),  

                # Cuerpo de la tabla
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige), 
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),  
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  
                ('FONTSIZE', (0, 1), (-1, -1), 12),  
                ('PADDING', (0, 1), (-1, -1), 8),  

                # Bordes
                ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkgrey), 
                ('LINEABOVE', (0, 1), (-1, -1), 1, colors.lightgrey),  
            ]))

            elements.append(Spacer(1, 24))
            elements.append(table)


        footer = f"Generado por Point Of Sale - {current_date}"
        elements.append(Spacer(1, 24))
        elements.append(Paragraph(footer, styles['Normal']))

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

            stock_data = producto_service.obtenerProductos()

            data = [['Código', 'Producto', 'Cantidad', 'Precio Compra', 'Precio Venta', 'Categoria', 'Proveedor']]
            for producto in stock_data:
                nombre_del_proveedor = proveedor_nombre_map.get(int(producto.proveedor), "Proveedor Desconocido")
                data.append([producto.codigo, producto.nombre, producto.cantStock, producto.precioCompra, "{:.2f}".format(float(producto.precioVenta)), categoria_descripcion_map.get(producto.categoria, "Desconocida"), nombre_del_proveedor])

            pdf_buffer = Utils.generate_pdf(main_window, "Reporte de Stock", data)

            stock_headers = ["ID", "Producto", "Cantidad", "Precio Compra", "Precio Venta", "Categoria", "Proveedor"]
            stock_data_for_preview = [[producto.codigo, producto.nombre, producto.cantStock, producto.precioCompra, producto.precioVenta, categoria_descripcion_map.get(producto.categoria, "Desconocida"), nombre_del_proveedor] for producto in stock_data]
            
            Utils.show_pdf_preview(main_window, pdf_buffer, stock_data_for_preview, stock_headers)
        except Exception as e:
            print("Error al generar el reporte de stock:")
            QMessageBox.critical(main_window, "Error", f"Ocurrió un error al generar el reporte de stock: {e}")

    def generate_sales_report(main_window, fechaDesde, fechaHasta, nombre_vendedor):
        try:
            ticket_service = TicketService()
            tickets = ticket_service.obtenerTickets(fechaDesde, fechaHasta)
            if len(tickets) > 0:
                producto_vendido_service = ProductoVendidoService()
                vendedor_service = VendedorService()

                data = [['ID Ticket', 'Fecha', 'Código de Barras', 'Producto', 'Cantidad', 'Precio Venta', 'Vendedor', 'Forma de Pago', 'Total Venta']]
                
                for ticket in tickets:
                    productos_vendidos = producto_vendido_service.obtenerProductosVendidos(ticket.id_ticket)
                    nombre_vendedor = vendedor_service.obtenerNombrePorId(ticket.id_vendedor)
                    for producto_vendido in productos_vendidos:
                        if ticket.tipo_de_pago == 0:
                            metodo_pago = 'Efectivo'
                        elif ticket.tipo_de_pago == 1:
                            metodo_pago = 'Tarjeta'
                        elif ticket.tipo_de_pago == 2:
                            metodo_pago = 'Transferencia'
                        else:
                            metodo_pago = str(ticket.tipo_de_pago)
                        data.append([ticket.id_ticket, ticket.fecha, producto_vendido.codigo, producto_vendido.producto_vendido, producto_vendido.cantidad_vendida, producto_vendido.precio_venta, nombre_vendedor, metodo_pago, ticket.total])

                pdf_buffer = Utils.generate_pdf(main_window, "Reporte de Ventas", data)

                stock_headers = ['ID Ticket', 'Fecha', 'Código de Barras', 'Producto', 'Cantidad', 'Precio Venta', 'Vendedor', 'Forma de Pago', 'Total Venta']
                stock_data = data[1:] 

                Utils.show_pdf_preview(main_window, pdf_buffer, stock_data, stock_headers)
            else:
                    QMessageBox.critical(main_window, "Error", f"En el período {fechaDesde} - {fechaHasta} no hubo ventas.")
        except Exception as e:
                print("Error al generar el reporte de ventas:")
                QMessageBox.critical(main_window, "Error", f"Ocurrió un error al generar el reporte de ventas: {e}")

            

    def generate_minimum_stock_report(main_window):
        try:
            categoria_service = CategoriaService()
            categorias = categoria_service.obtenerCategorias()
            categoria_descripcion_map = {categoria.id: categoria.descripcion for categoria in categorias}

            proveedor_service = ProveedorService()
            proveedores = proveedor_service.obtenerProveedores()
            proveedor_nombre_map = {proveedor.id: proveedor.nombre for proveedor in proveedores}

            producto_service = ProductoService()
            stock_data = producto_service.obtenerProductosStockMinimo()

            data = [['Código', 'Producto', 'Cantidad', 'Precio Compra', 'Precio Venta', 'Categoria', 'Proveedor']]
            for producto in stock_data:
                nombre_del_proveedor = proveedor_nombre_map.get(int(producto.proveedor), "Proveedor Desconocido")
                data.append([producto.codigo, producto.nombre, producto.cantStock, producto.precioCompra, "{:.2f}".format(float(producto.precioVenta)), categoria_descripcion_map.get(producto.categoria, "Desconocida"), nombre_del_proveedor])

            pdf_buffer = Utils.generate_pdf(main_window, "Reporte de Stock", data)

            stock_headers = ["ID", "Producto", "Cantidad", "Precio Compra", "Precio Venta", "Categoria", "Proveedor"]
            stock_data_for_preview = [[producto.codigo, producto.nombre, producto.cantStock, producto.precioCompra, producto.precioVenta, categoria_descripcion_map.get(producto.categoria, "Desconocida"), nombre_del_proveedor] for producto in stock_data]
            
            Utils.show_pdf_preview(main_window, pdf_buffer, stock_data_for_preview, stock_headers)
        except Exception as e:
            print("Error al generar el reporte de stock:")
            QMessageBox.critical(main_window, "Error", f"Ocurrió un error al generar el reporte de stock: {e}")

    @staticmethod
    def obtener_rol(dni):
        vendedor_service = VendedorService()
        return vendedor_service.obtenerRol(dni)
    
    @staticmethod
    def obtener_nombre_usuario(dni):
        vendedor_service = VendedorService()
        nombre_usuario = vendedor_service.obtenerNombre(dni)
        Utils.id_usuario = vendedor_service.obtenerId(dni)
        return nombre_usuario
    



# Utils.py
def create_main_window_menu(parent):
    menu_bar = parent.menuBar()

    menu_menu = QMenu("Menú", parent)
    menu_bar.addMenu(menu_menu)

    vendedores_action = QAction(QIcon("utils/img/icons8-grupo-de-usuarios-hombre-y-mujer-48.png"),"Vendedores", parent)
    menu_menu.addAction(vendedores_action)

    categorias_action = QAction(QIcon("utils/img/icons8-almacén-48.png"),"Categorias", parent)
    menu_menu.addAction(categorias_action)

    productos_action = QAction(QIcon("utils/img/icons8-almacén-48.png"),"Productos", parent)
    menu_menu.addAction(productos_action)

    proveedores_action = QAction(QIcon("utils/img/icons8-proveedor-48.png"),"Proveedores", parent)
    menu_menu.addAction(proveedores_action)

    ordenes_action = QAction(QIcon("utils/img/icons8-recibo-48.png"),"Órdenes de Compra", parent)
    menu_menu.addAction(ordenes_action)

    movimientos_menu = QMenu("Movimientos", parent)
    menu_bar.addMenu(movimientos_menu)

    ventas_action = QAction(QIcon("utils/img/icons8-caja-registradora-48.png"), "Ventas", parent)
    movimientos_menu.addAction(ventas_action)

    reportes_menu = QMenu("Reportes", parent)
    menu_bar.addMenu(reportes_menu)

    reporte_stock_minimo_action = QAction(QIcon("utils/img/icons8-pdf-48.png"), "Reporte de Stock Mínimo", parent)
    reportes_menu.addAction(reporte_stock_minimo_action)

    reporte_stock_action = QAction(QIcon("utils/img/icons8-pdf-48.png"), "Reporte de Stock", parent)
    reportes_menu.addAction(reporte_stock_action)

    reporte_ventas_action = QAction(QIcon("utils/img/icons8-pdf-48.png"), "Reporte de Ventas", parent)
    reportes_menu.addAction(reporte_ventas_action)

    cerrar_sesion_action = QAction("Cerrar Sesión", parent)
    menu_bar.addAction(cerrar_sesion_action)

    reporte_stock_action.triggered.connect(parent.generate_stock_report_wrapper)
    reporte_ventas_action.triggered.connect(parent.generate_sales_report_wrapper)
    reporte_stock_minimo_action.triggered.connect(parent.generate_minimum_stock_report_wrapper)
    categorias_action.triggered.connect(parent.show_categories_window)
    productos_action.triggered.connect(parent.show_products_window)
    proveedores_action.triggered.connect(parent.show_proveedores_window)
    ventas_action.triggered.connect(parent.show_ventas_window)
    ordenes_action.triggered.connect(parent.show_ordenes_window)
    vendedores_action.triggered.connect(parent.show_vendedores_window)
    cerrar_sesion_action.triggered.connect(parent.cerrar_sesion)

# HEADER
def init_header(parent, width, nombre_usuario, menu_bar_height):
    parent_width = width
    header = QFrame(parent)
    header.move(0, menu_bar_height)
    header.setFixedHeight(100)
    header.setMinimumWidth(parent_width)
    header.setMaximumWidth(parent_width)

    header.setStyleSheet("background-color: #F9F5EB;")

    left_layout = QVBoxLayout()
    user_label = QLabel(f"Vendedor: {nombre_usuario}", header)
    user_label.setStyleSheet("color: black;")
    left_layout.addWidget(user_label, alignment=Qt.AlignTop | Qt.AlignLeft)

    center_layout = QVBoxLayout()
    logo_label = QLabel(header)
    pixmap = QPixmap("utils/img/logosinfondo.png").scaled(300, 250, Qt.KeepAspectRatio)
    logo_label.setPixmap(pixmap)
    logo_label.setAlignment(Qt.AlignCenter)
    center_layout.addWidget(logo_label)

    right_layout = QGridLayout()

    fecha = QDateTime.currentDateTime().toString("dd-MM-yyyy")
    fecha_num_label = QLabel(fecha, header)
    fecha_num_label.setStyleSheet("color: black;")
    right_layout.addWidget(fecha_num_label, 0, 1, Qt.AlignTop | Qt.AlignRight)

    location_label = QLabel("Rosario, Argentina", header)
    location_label.setStyleSheet("color: black;")
    right_layout.addWidget(location_label, 1, 0, 1, 2, Qt.AlignTop | Qt.AlignRight)

    bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
    right_layout.addItem(bottom_spacer, 2, 0, 1, 2)

    main_layout = QHBoxLayout(header)
    main_layout.addLayout(left_layout)
    main_layout.setStretchFactor(left_layout, 1)
    main_layout.addLayout(center_layout)
    main_layout.setStretchFactor(center_layout, 1)
    main_layout.addLayout(right_layout)
    main_layout.setStretchFactor(right_layout, 1)
    header.setLayout(main_layout)


