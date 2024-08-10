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

def imprimir_factura():
    print("Factura:")
    print("ID\tDescripción\tPrecio Unitario\tCantidad\tPrecio Total")
    subtotal = 0
    for producto in carrito:
        precio_total = producto["precio"] * producto["cantidad"]
        print(f"{producto['id']}\t{producto['descripcion']}\tRD${producto['precio']}\t{producto['cantidad']}\tRD${precio_total}")
        subtotal += precio_total
    impuestos = subtotal * 0.18
    total = subtotal + impuestos
    print(f"Subtotal: RD${subtotal:.2f}")
    print(f"Impuestos (18%): RD${impuestos:.2f}")
    print(f"Total: RD${total:.2f}")

def main():
    while True:
        agregar_producto_al_carrito()
        respuesta = input("¿Desea agregar otro producto? (s/n): ")
        if respuesta.lower() != "s":
            break
    imprimir_factura()

if __name__ == "__main__":
    main()
