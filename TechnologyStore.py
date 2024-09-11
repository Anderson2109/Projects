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

#Guardar datos de productos en el archivo JSON   
def save_products(data):
    with open(PRODUCTS_FILE, 'w') as file:
        json.dump(data, file, indent=4)

#Agregar producto
def add_product(category, product_id, name, price, characteristics, quantify):
    data = load_products()
    product = {
        "id_producto": product_id,
        "nombre": name,
        "precio": price,
        "caracteristicas": characteristics,
        "cantidad_disponible": quantify
    }

#Añadir el producto a la categoría correspondiente
    if category in data:
        data[category].append(product)
        save_products(data)
        print(f"Producto {name} agregado con éxito.")
    else:
        print(f"Categoría {category} no encontrada.")