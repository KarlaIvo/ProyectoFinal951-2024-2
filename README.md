<h1 align="center"> Proyecto final para Programación para la Extracción de Datos 2024-2 </h1>
   <p align="center">
   <img src="assets/imagenes/bc.png">
   </p>

## Índice
1. [Introducción](#introducción)
2. [Integrantes](#Integrantes)
3. [Partes del proyecto](#Partes-del-proyecto)
4. [Empresa](#Empresa)
6. [Instrucciones](#Instrucciones)
7. [Librerias](#Librerias)

## Introducción
En este proyecto realizamos todo el proceso desde buscar una pagina y extraer datos de ella hasta realizar dashboards de los datos que se extrajeron, con los cuales se respondieron preguntas que se generaron acerca de informacion la pagina (en nuestro caso la pagina de Beauty Creations)

## Integrantes:
- Maria Fernanda Hernandez Aleman
- Karla Ivonne Zavala Bojorquez

## Partes del proyecto
- Extraccion de datos
- Transformacion de datos
- Visualizacion de datos

## Empresa
Beauty Creations, una empresa mexicana dedicada a la creacion y produccion de productos cosmeticos principalmente, con la mision de aumentar la confianza de los consumidores.

## Instrucciones
1. `Paso`: Acceder a el codigo de <a href="Web_Scraping_bc.py">Web Scrapper</a> para obtener los datos de la pagina <a href="https://beautycreationscosmetics.com.mx/">Beauty Creations</a>
2. `Paso`: Acceder al codigo de <a href="Clean_bc.py">Limpieza y Normalizacion</a> para realizar la limpieza y normalizacion de los datos
3. `Paso`: Para configurar la Base de Datos: Acceder al codigo de <a href="beauty_creations.sql">Base de Datos</a> para importar la base.
   - Usar un gestor de base de datos como MySQL Workbench para importar el archivo <a href="beauty_creations.sql">Base de Datos</a>.
4. `Paso`: Actualizar los Detalles de Conexión
   - Editar el archivo <a href="funcion_python_sql.py">Funcion Python</a> para actualizar los detalles de conexión a la base de datos en la función "conectar()".
   - def conectar():
    return mysql.connector.connect(
        - host='localhost',  # Cambiar esto si tu base de datos no está en localhost
        - user='root',       # Cambiar esto por tu nombre de usuario
        - password='Asdf123', # Cambiar esto por tu contraseña
         <br>database='beauty_creations'
    )
5. `Paso`: Acceder al codigo de <a href="assets/datasets/Clean_bc_accessories.csv">Accessories</a>, <a href="assets/datasets/Clean_bc_bundles.csv">Bundles</a> y <a href="assets/datasets/Clean_bc_collabs.csv">Collabs</a> en caso de tardarse mucho el WebScrapper
6. `Paso`: Acceder al codigo de <a href="assets/style.css">style.css</a> ,al de <a href="menu.py">Menu</a>, luego al de <a href="welcome.py">Welcome</a>, depues a los de <a href="dashboard_uno.py">Dashboard1</a>, <a href="dashboard_dos.py">Dashboard2</a> y <a href="dashboard_tres.py">Dashboard3</a>
7. `Paso`: Dar Run en el archivo de <a href="menu.py">Menu</a>
8. `Paso`: Visualizar los Dashboards



## Librerias
Las librerias usadas a lo largo del proyecto fueron:
- time
- pandas
- selenium import webdriver
- selenium.webdriver.chrome.service
- selenium.webdriver.chrome.options
- selenium.webdriver.common.by
- selenium.webdriver.support.ui
- selenium.webdriver.support
- webdriver_manager.chrome import ChromeDriverManager
- bs4 import BeautifulSoup
- dash_bootstrap_components
- dash import Input, Output, dcc, html, Dash, callback
- plotly.express



