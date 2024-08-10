import os

productos = {
    1: {"descripcion": "Arroz", "precio": 50},
    2: {"descripcion": "Habichuelas", "precio": 80},
    3: {"descripcion": "Aceite", "precio": 300},
    4: {"descripcion": "Pollo", "precio": 85},
    5: {"descripcion": "Lechuga", "precio": 80}
}

carrito = []

def limpiar_pantalla():

    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():

    print("Menú de Productos:")
    for ID in productos:
        info = productos[ID]
        print(f"{ID}. {info['descripcion']} -> RD${info['precio']}")

def agregar_producto(ID, cantidad):

    encontrado = False
    for item in carrito:
        if item['id'] == ID:
            item['cantidad'] += cantidad
            encontrado = True
            break
    if not encontrado:
        carrito.append({
            'id': ID,
            'descripcion': productos[ID]['descripcion'],
            'precio': productos[ID]['precio'],
            'cantidad': cantidad
        })

def punto_de_venta():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        try:
            id_producto = int(input("Ingrese el ID del producto: "))
            if id_producto not in productos:
                print("ID no válido. Intente de nuevo.")
                continue
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")
            continue
        
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad < 0:
                print("Cantidad no puede ser negativa. Intente de nuevo.")
                continue
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")
            continue
        
        agregar_producto(id_producto, cantidad)
        
        otra_compra = input("¿Desea añadir otro producto? (si/no): ").strip().lower()
        if otra_compra != 'si':
            break
    
    imprimir_factura()

def imprimir_factura():
    subtotal = 0

    print("\nFactura:")
    print("ID | Descripción   | Precio Unidad | Cantidad | Precio Total")
    for item in carrito:
        precio_total = item['precio'] * item['cantidad']
        subtotal += precio_total
        print(f"{item['id']}  | {item['descripcion']:<14} | RD${item['precio']:<12} | {item['cantidad']:<8} | RD${precio_total}")
    
    impuestos = subtotal * 0.18
    total = subtotal + impuestos
    
    print("\nSubtotal: RD$", subtotal)
    print("Impuestos (18%): RD$", impuestos)
    print("Total: RD$", total)

punto_de_venta()
