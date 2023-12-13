@echo off

rem busca la ruta de application
rem ejemplo: set "ruta=C:\Users\tinch\OneDrive\Documentos\point_of_sale_py\application"
set "ruta=C:\Users\tinch\OneDrive\Documentos\point_of_sale_py\application"

cd "%ruta%"

rem Tamaño de la ventana de logs
mode con: cols=40 lines=10

rem ejecuto script en python
python Login.py