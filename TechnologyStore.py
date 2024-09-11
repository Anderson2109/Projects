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

#Aplicar descuento al producto
def apply_discount(product_id):
    data = load_products()
    for category in data:
        for product in data[category]:
            if product["id_producto"] == product_id:

                #Verificar si el producto tiene un descuento               
                if "descuento" in product:
                    discount = product["descuento"]
                    original_price = product["precio"]

                    #Si el descuento es porcentual
                    if discount["tipo"] == "porcentual":
                        discount_amount = original_price * (discount["valor"] / 100)
                        final_price = original_price - discount_amount
                        print(f"Descuento aplicado: {discount['valor']}%")
                    
                    #Si el descuento es una cantidad fija
                    elif discount["tipo"] == "cantidad_fija":
                        final_price = original_price - discount["valor"]
                        print(f"Descuento aplicado: ${discount['valor']}")

                    #Si el descuento es una oferta especial
                    elif discount["tipo"] == "oferta":
                        final_price = original_price
                        print(f"Oferta especial aplicada: {discount['descripcion']}")

                    #Asegurarse de que el precio final no sea menor a cero
                    final_price = max(0, final_price)
                    print(f"Precio final del producto: ${final_price}")
                    return final_price
                else:
                    print("Este producto no tiene descuento.")
                    return product["precio"]
                
    print("Producto no encontrado.")
    return None

#Agregar descuento al producto
def add_discount_to_product(product_id, discount_type, discount_value, description=None):
    data = load_products()
    for category in data:
        for product in data[category]:
            if product["id_producto"] == product_id:
                product["descuento"] = {
                    "tipo": discount_type,
                    "valor": discount_value,
                    "descripcion": description
                }
                save_products(data)
                print(f"Descuento aplicado al producto {product_id}.")
                return
    print("Producto no encontrado.")

#Ejemplo de uso de las funciones
if __name__ == "__main__":

    #Agregar un descuento porcentual a un producto
    add_discount_to_product(101, "porcentual", 10)

    #Agregar un descuento por cantidad fija a un producto
    add_discount_to_product(102, "cantidad_fija", 50)

    #Aplicar descuento al producto y mostrar precio final
    final_price = apply_discount(101)
    print(f"Precio final del producto con descuento: ${final_price}")