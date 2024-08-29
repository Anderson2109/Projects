productos = {
    1: {"descripcion": "Arroz", "precio": 50},
    2: {"descripcion": "Habichuelas", "precio": 80},
    3: {"descripcion": "Aceite", "precio": 300},
    4: {"descripcion": "Pollo", "precio": 85},
    5: {"descripcion": "Lechuga", "precio": 80}
}

carrito = []

def mostrar_menu():
    print("Menú:")
    for id, producto in productos.items():
        print(f"{id}. {producto['descripcion']} -> RD${producto['precio']}")

def agregar_producto_al_carrito():
    mostrar_menu()
    try:
        id_producto = int(input("Ingrese el ID del producto: "))
        if id_producto in productos:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad > 0:
                for producto in carrito:
                    if producto["id"] == id_producto:
                        producto["cantidad"] += cantidad
                        return
                carrito.append({"id": id_producto, "descripcion": productos[id_producto]["descripcion"], "precio": productos[id_producto]["precio"], "cantidad": cantidad})
            else:
                print("No se permiten cantidades negativas.")
        else:
            print("ID de producto no válido.")
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número.")

def imprimir_factura():
    print("\nFactura:")
    print("{:<5} {:<15} {:<15} {:<10} {:<15}".format("ID", "Descripción", "Precio Unitario", "Cantidad", "Precio Total"))
    subtotal = 0
    for producto in carrito:
        precio_total = producto["precio"] * producto["cantidad"]
        print("{:<5} {:<15} RD${:<13} {:<10} RD${:<15}".format(producto['id'], producto['descripcion'], producto['precio'], producto['cantidad'], precio_total))
        subtotal += precio_total
    impuestos = subtotal * 0.18
    total = subtotal + impuestos
    print(f"\nSubtotal: RD${subtotal:.2f}")
    print(f"Impuestos (18%): RD${impuestos:.2f}")
    print(f"Total: RD${total:.2f}")
<<<<<<< HEAD

def main():
    continuar = True
    while continuar:
        agregar_producto_al_carrito()
        respuesta = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
        continuar = (respuesta == "s")
    imprimir_factura()

if __name__ == "__main__":
    main()
=======

def main():
    continuar = True
    while continuar:
        agregar_producto_al_carrito()
        respuesta = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
        continuar = (respuesta == "s")
    imprimir_factura()

if __name__ == "__main__":
    main()

>>>>>>> c4ef8992222fcff4abfcde48f8bb88ce07ce25be
