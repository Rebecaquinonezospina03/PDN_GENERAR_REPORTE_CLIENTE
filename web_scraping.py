import requests
from bs4 import BeautifulSoup
import pandas as pd

nombre = list()
apellido = list()
correo = list()
telefono = list()
fecha_de_pedido = list()
tipo_producto = list()

url = 'http://127.0.0.1:8000/'
html_doc = requests.get(url)


soup = BeautifulSoup(html_doc.text, 'html.parser')

tabla = soup.find('table')
filas = (tabla.find_all('tr'))

for fila in filas:
    celdas = fila.find_all('td')
    print(celdas)

    if len(celdas)>0:
        nombre.append(celdas[0].string)
        apellido.append(celdas[1].string)
        correo.append(celdas[2].string)
        telefono.append(celdas[3].string)
        fecha_de_pedido.append(celdas[4].string)
        tipo_producto.append(celdas[5].string)

# Convertir las listas a un DataFrame y guardar en un archivo CSV
df = pd.DataFrame({
    'Nombres': nombre,
    'Apellidos': apellido,
    'Correo': correo,
    'Telefono': telefono,
    'Fecha De Pedido': fecha_de_pedido,
    'Producto': tipo_producto
})

df.to_csv('clientes.csv', index=False, encoding='utf-8')
