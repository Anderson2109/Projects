import json
import os
import random
from datetime import datetime

# Función para limpiar la pantalla (para Windows y Unix)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clase para la gestión de productos
class Product:
    def __init__(self, id_producto, nombre, precio, caracteristicas, cantidad_disponible):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.caracteristicas = caracteristicas
        self.cantidad_disponible = cantidad_disponible

    def __repr__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Precio: {self.precio} RD$, Cantidad: {self.cantidad_disponible}"

# Clase para manejar la tienda (almacén y ventas)
class Store:
    def __init__(self):
        self.products = self.load_products()
        self.sales = self.load_sales()
        self.changes_log = self.load_changes_log()
        self.user_session = None  # Sesión de usuario
        self.categories = list(self.products.keys())  # Obtener categorías desde los productos
        self.client_id_counter = max([sale['id_cliente'] for sale in self.sales], default=999) + 1

    # Cargar productos desde productos.json
    def load_products(self):
        if not os.path.exists('productos.json'):
            with open('productos.json', 'w') as file:
                json.dump({}, file)
        with open('productos.json', 'r') as file:
            data = json.load(file)
        # Convertir productos en instancias de Product
        return {category: [Product(**prod) for prod in prods] for category, prods in data.items()}

    # Guardar productos en productos.json
    def save_products(self):
        data = {category: [prod.__dict__ for prod in prods] for category, prods in self.products.items()}
        with open('productos.json', 'w') as file:
            json.dump(data, file, indent=4)

    # Cargar ventas desde ventas.json
    def load_sales(self):
        if not os.path.exists('ventas.json'):
            with open('ventas.json', 'w') as file:
                json.dump([], file)
        with open('ventas.json', 'r') as file:
            return json.load(file)

    # Guardar ventas en ventas.json
    def save_sales(self):
        with open('ventas.json', 'w') as file:
            json.dump(self.sales, file, indent=4)

    # Cargar el log de cambios desde cambios_almacen.json
    def load_changes_log(self):
        if not os.path.exists('cambios_almacen.json'):
            with open('cambios_almacen.json', 'w') as file:
                json.dump([], file)
        with open('cambios_almacen.json', 'r') as file:
            return json.load(file)

    # Guardar log de cambios
    def save_changes_log(self):
        with open('cambios_almacen.json', 'w') as file:
            json.dump(self.changes_log, file, indent=4)

    # Método para listar categorías con ID
    def show_categories_with_id(self):
        clear_screen()
        print("Categorías disponibles:")
        for index, category in enumerate(self.categories, 1):
            print(f"{index}. {category.capitalize()}")

    # Mostrar productos por categoría
    def show_products_by_category(self, category):
        clear_screen()  # Limpiar pantalla antes de mostrar productos
        print(f"Productos en la categoría: {category.capitalize()}")
        if category in self.products:
            found = False
            for product in self.products[category]:
                print(product)
                found = True
            if not found:
                print("No hay productos en esta categoría.")
        else:
            print("Categoría no encontrada.")

    # Agregar productos (desde el almacén)
    def add_product(self, category, name, price, characteristics, quantity):
        if not name or price <= 0 or quantity < 0:
            print("Entrada inválida. Asegúrese de que el nombre no esté vacío, el precio y la cantidad sean válidos.")
            return
        
        product_id = random.randint(1000, 9999)
        new_product = Product(product_id, name, price, characteristics, quantity)
        if category not in self.products:
            self.products[category] = []
        self.products[category].append(new_product)
        self.save_products()
        print(f"Producto {name} agregado exitosamente con ID {product_id}.")
        if self.user_session:  # Solo registrar cambio si hay sesión
            self.log_change(self.user_session['nombre'], f"Agregó producto {name} (ID {product_id}) en categoría {category}.")

    # Eliminar producto
    def delete_product(self, category, product_id):
        clear_screen()  # Limpiar pantalla antes de eliminar producto
        if category in self.products:
            self.products[category] = [prod for prod in self.products[category] if prod.id_producto != product_id]
            self.save_products()
            print(f"Producto ID {product_id} eliminado exitosamente.")
            if self.user_session:  # Solo registrar cambio si hay sesión
                self.log_change(self.user_session['nombre'], f"Eliminó producto ID {product_id} de la categoría {category}.")
        else:
            print("Categoría no encontrada.")

    # Eliminar categoría
    def delete_category(self, category):
        clear_screen()  # Limpiar pantalla antes de eliminar categoría
        if category in self.products:
            del self.products[category]
            self.save_products()
            print(f"Categoría {category} eliminada exitosamente.")
            if self.user_session:  # Solo registrar cambio si hay sesión
                self.log_change(self.user_session['nombre'], f"Eliminó la categoría {category}.")
        else:
            print("Categoría no encontrada.")

    # Actualizar stock
    def update_stock(self, product_id, quantity_change):
        clear_screen()  # Limpiar pantalla antes de actualizar stock
        if self.user_session is None:
            print("Debe iniciar sesión antes de actualizar el stock.")
            return

        for category, products in self.products.items():
            for product in products:
                if product.id_producto == product_id:
                    if product.cantidad_disponible + quantity_change < 0:
                        print("No hay suficiente stock.")
                        return
                    product.cantidad_disponible += quantity_change
                    self.save_products()
                    if self.user_session:  # Solo registrar cambio si hay sesión
                        self.log_change(self.user_session['nombre'], f"Actualización de stock: Producto ID {product_id}, Cambio: {quantity_change}")
                    print(f"Stock actualizado para el producto ID {product_id}.")
                    return
        print("Producto no encontrado.")

    # Verificar stock de un producto
    def check_stock(self, product_id):
        for products in self.products.values():
            for product in products:
                if product.id_producto == product_id:
                    return product.cantidad_disponible
        return None

    # Registrar cambios en el almacén
    def log_change(self, employee_name, change_description):
        log_entry = {
            "empleado": employee_name,
            "cambio": change_description,
            "fecha": datetime.now().isoformat()  # Fecha y hora del cambio
        }
        self.changes_log.append(log_entry)
        self.save_changes_log()

    # Registrar venta
    def register_sale(self, client_name, products):
        clear_screen()  # Limpiar pantalla antes de registrar venta
        # Eliminado el chequeo de autenticación
        client_id = self.client_id_counter
        self.client_id_counter += 1
        total = 0
        for product in products:
            stock = self.check_stock(product["id_producto"])
            if stock is None or stock < product["cantidad"]:
                print(f"No hay suficiente stock para el producto ID {product['id_producto']}.")
                return
            total += self.get_product_price(product["id_producto"]) * product["cantidad"]
        sale = {
            "id_cliente": client_id,
            "nombre_cliente": client_name,
            "productos": products,
            "total": total,
            "fecha": datetime.now().isoformat()  # Fecha y hora de la venta
        }
        self.sales.append(sale)
        self.save_sales()
        print(f"Venta registrada para el cliente {client_name} con ID {client_id}.")
        for product in products:
            self.update_stock(product["id_producto"], -product["cantidad"])
        self.show_invoice(sale)  # Mostrar factura

    # Mostrar factura
    def show_invoice(self, sale):
        clear_screen()  # Limpiar pantalla antes de mostrar factura
        print("Factura")
        print("-" * 30)
        print(f"ID Cliente: {sale['id_cliente']}")
        print(f"Nombre Cliente: {sale['nombre_cliente']}")
        print("Productos:")
        for product in sale["productos"]:
            print(f"  ID: {product['id_producto']}, Cantidad: {product['cantidad']}, Precio Unitario: {self.get_product_price(product['id_producto'])} RD$")
        print(f"Total: {sale['total']} RD$")
        print(f"Fecha: {sale['fecha']}")
        print("-" * 30)

    # Obtener precio de producto
    def get_product_price(self, product_id):
        for products in self.products.values():
            for product in products:
                if product.id_producto == product_id:
                    return product.precio
        return None

    # Buscar factura por ID de cliente o nombre
    def search_invoice(self, search_term):
        found = False
        for sale in self.sales:
            if str(sale['id_cliente']) == search_term or sale['nombre_cliente'].lower() == search_term.lower():
                self.show_invoice(sale)
                found = True
                break
        if not found:
            print("Factura no encontrada.")

    # Reporte de ventas
    def generate_sales_report(self):
        clear_screen()  # Limpiar pantalla antes de mostrar el reporte
        print("Reporte de Ventas")
        print("-" * 30)
        if not self.sales:
            print("No se han registrado ventas.")
        else:
            for sale in self.sales:
                print(f"ID Cliente: {sale['id_cliente']}")
                print(f"Nombre Cliente: {sale['nombre_cliente']}")
                print("Productos:")
                for product in sale["productos"]:
                    print(f"  ID: {product['id_producto']}, Cantidad: {product['cantidad']}, Precio Unitario: {self.get_product_price(product['id_producto'])} RD$")
                print(f"Total: {sale['total']} RD$")
                print(f"Fecha: {sale['fecha']}")
                print("-" * 30)
        input("Presione Enter para continuar...")

    # Autenticación del almacén
    def authenticate_warehouse(self):
        clear_screen()
        print("Inicio de sesión del almacén")
        username = input("Usuario: ")
        password = input("Contraseña: ")
        if username == 'admin' and password == 'admin21':
            self.user_session = {'nombre': 'Administrador'}
            print("Inicio de sesión exitoso.")
        else:
            print("Usuario o contraseña incorrectos.")
            self.user_session = None

# Función principal del menú de la tienda
def main():
    store = Store()
    clear_screen()
    print("Bienvenido a Technology Store")
    input("Presione Enter para continuar...")
    
    while True:
        clear_screen()
        print("Menú Principal")
        print("1. Gestionar almacén")
        print("2. Venta de Productos")
        print("3. Buscar Factura")
        print("4. Reporte de Ventas")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            store.authenticate_warehouse()
            if store.user_session is None:
                continue
            while True:
                clear_screen()
                print("Gestionar almacén")
                print("1. Mostrar Categorías")
                print("2. Agregar Producto")
                print("3. Eliminar Producto")
                print("4. Eliminar Categoría")
                print("5. Volver al Menú Principal")

                product_choice = input("Seleccione una opción: ")

                if product_choice == "1":
                    store.show_categories_with_id()
                    input("Presione Enter para continuar...")
                elif product_choice == "2":
                    store.show_categories_with_id()
                    category_id = int(input("Ingrese el ID de la categoría: ")) - 1
                    if category_id < 0 or category_id >= len(store.categories):
                        print("Categoría no válida.")
                        continue
                    category = store.categories[category_id].lower()
                    while True:
                        name = input("Ingrese el nombre del producto: ")
                        price = float(input("Ingrese el precio del producto: "))
                        characteristics = input("Ingrese las características del producto: ")
                        quantity = int(input("Ingrese la cantidad disponible: "))
                        store.add_product(category, name, price, characteristics, quantity)
                        more = input("¿Desea agregar otro producto? (s/n): ").lower()
                        if more != 's':
                            break
                elif product_choice == "3":
                    store.show_categories_with_id()
                    category_id = int(input("Ingrese el ID de la categoría: ")) - 1
                    if category_id < 0 or category_id >= len(store.categories):
                        print("Categoría no válida.")
                        continue
                    category = store.categories[category_id].lower()
                    product_id = int(input("Ingrese el ID del producto a eliminar: "))
                    store.delete_product(category, product_id)
                elif product_choice == "4":
                    category = input("Ingrese la categoría a eliminar: ").lower()
                    store.delete_category(category)
                elif product_choice == "5":
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")

        elif choice == "2":
            clear_screen()
            print("Venta de Productos")
            client_name = input("Ingrese el nombre del cliente: ")
            products = []
            while True:
                clear_screen()
                store.show_categories_with_id()
                category_id = int(input("Seleccione una categoría por ID: ")) - 1
                if category_id < 0 or category_id >= len(store.categories):
                    print("Categoría no válida.")
                    continue
                category = store.categories[category_id].lower()
                store.show_products_by_category(category)
                product_id = int(input("Ingrese el ID del producto: "))
                quantity = int(input("Ingrese la cantidad: "))
                
                # Verifica el stock y agrega el producto a la lista
                if store.check_stock(product_id) is None or store.check_stock(product_id) < quantity:
                    print(f"No hay suficiente stock para el producto ID {product_id}.")
                    input("Presione Enter para intentar de nuevo...")
                    continue
                
                products.append({"id_producto": product_id, "cantidad": quantity})
                more = input("¿Desea agregar otro producto? (s/n): ").lower()
                if more != 's':
                    break
            
            store.register_sale(client_name, products)
            input("Presione Enter para volver al menú principal...")

        elif choice == "3":
            search_term = input("Ingrese el ID o nombre del cliente para buscar la factura: ")
            store.search_invoice(search_term)
            input("Presione Enter para volver al menú principal...")

        elif choice == "4":
            store.generate_sales_report()

        elif choice == "5":
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()