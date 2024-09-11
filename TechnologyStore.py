import json
import os

#Ruta del archivo json donde se almacenaran los productos
PRODUCTS_FILE = 'productos.json'

#Cargar datos de productos desde el archivo JSON
def load_products():
    if not os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, 'w') as file:
            json.dump({"computadoras": [], "laptops": [], "oficina": [], "almacenamiento": [], "imagenes_sonido": [], "celulares": [], "tablets": []}, file)
    with open(PRODUCTS_FILE, 'r') as file:
        return json.load(file)