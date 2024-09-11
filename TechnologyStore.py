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

#Actualizar el stock
def update_stock(product_id, quantity_change):
    data = load_products()
    for category in data:
        for product in data[category]:
            if product["id_producto"] == product_id:
                if product["cantidad_disponible"] + quantity_change < 0:
                    print("No hay suficiente stock.")
                    return
                product["Cantidad_disponible"] += quantity_change
                save_products(data)
                print(f"Stock actualizado para el producto ID {product_id}.")
                return
            print("Producto no encontrado.")

#Verificar el stock
def check_stock(product_id):
    data = load_products()
    for category in data:
        for product in data[category]:
            if product["id_producto"] == product_id:
                return product["Cantidad_disponible"]
    return None

#Ejemplo de uso de las funciones
if __name__ == "__main__":

#Agregar un producto
    add_product("computadoras", 101, "Pc Gaming", 1200, ["Intel i7", "16GB RAM", "1TB SSD"], 10)

#Actualizar stock (vender 2 unidades)
    update_stock(101, -2)

#Verificar stock
    stock = check_stock(101)
    if stock is not None:
        print(f"Stock disponible para el producto ID 101: {stock}")
    else:
        print(f"Producto no encontrado.")