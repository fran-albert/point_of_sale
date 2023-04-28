from servicios.categoria_service import CategoriaService
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

# Crear una instancia de QApplication
app = QApplication([])

categoria_service = CategoriaService()

categorias = categoria_service.obtenerCategorias()

# Crear una instancia de QTableWidget con dos columnas y el número de filas igual a la longitud de la lista de datos
table = QTableWidget(len(categorias), 2)

# Definir los encabezados de las columnas
table.setHorizontalHeaderLabels(["Descripción", "Categoría"])

# Agregar los elementos a la tabla
for i, (descripcion, categoria) in enumerate(categorias):
    item_descripcion = QTableWidgetItem(descripcion)
    item_categoria = QTableWidgetItem(categoria)
    table.setItem(i, 0, item_descripcion)
    table.setItem(i, 1, item_categoria)

# Mostrar la tabla en pantalla
table.show()

# Ejecutar la aplicación
app.exec_()