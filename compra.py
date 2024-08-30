def __init__(self, Id, Descripción, Precio, Cantidad, Impuesto):
    self.id = Id
    self.descripción = Descripción
    self.precio = Precio
    self.cantidad = Cantidad
    self.impuesto = Impuesto

def calcular_impuesto(self):
    if self.impuesto == "01":
        return self.precio * 0.18
    elif self.impuesto == "02":
        return self.precio * 0.16
    else:
        return 0

from datetime import datetime

class Factura:
    contador_id = 1

    def __init__(self, cliente):



        self.id = Factura.contador_id
        Factura.contador_id += 1
        self.fecha = datetime.now().strftime('%d/%m/%Y %H:%M')
        self.cliente = cliente
        self.productos = []
    
    def agregar_producto(self, producto, cantidad):
        for p in self.productos:
            if p["producto"].id == producto.id:
                p["cantidad"] += cantidad
                return
        self.productos.append({"producto": producto, "cantidad": cantidad})
    
    def calcular_subtotal(self):
        return sum(p["producto"].precio * p["cantidad"] for p in self.productos)

    def calcular_impuestos(self):
        return sum(p["producto"].calcular_impuesto() * p["cantidad"] for p in self.productos)

    def calcular_total(self):
        return self.calcular_subtotal() + self.calcular_impuestos()

    def imprimir_factura(self):
        print(f"\nCliente: {self.cliente}")
        print(f"ID: {self.id}")
        print(f"Fecha: {self.fecha}")
        print("{:<5} {:<15} {:<15} {:<10} {:<15}".format("ID", "Descripción", "Precio Unitario", "Cantidad", "Precio Total"))
        for p in self.productos:
            producto = p["producto"]
            cantidad = p["cantidad"]
            precio_total = producto.precio * cantidad
            print("{:<5} {:<15} RD${:<13} {:<10} RD${:<15}".format(producto.id, producto.descripcion, producto.precio, cantidad, precio_total))
        print(f"\nSubtotal: RD${self.calcular_subtotal():.2f}")
        print(f"Impuestos: RD${self.calcular_impuestos():.2f}")
        print(f"Total: RD${self.calcular_total():.2f}")

class pos:
    def __init__(self):
        self.inventario = {}
        self.facturas = []

    def agregar_producto_inventario(self, Producto):
        self.inventario[Producto.id] = Producto

    def mostrar_menu(self):
        print("Menú:")
        for Id, producto in self.inventario.items():
            print(f"{Id}. {producto.descripcion} -> RD${producto.precio} (stock: {producto.cantidad})")

    def vender(self):
        Carrito = Factura(input("Ingrese el nombre del cliente: "))
        Continuar = True
        while Continuar:
            self.mostrar_menu()
            id_producto = int(input("Ingrese el Id del producto: "))
            if id_producto in self.inventario:
                Producto = self.inventario[id_producto]
                Cantidad = int(input(f"Ingrese la cantidad de {Producto.descripcion}: "))
                if Cantidad > 0 and Cantidad <= Producto.cantidad:
                    Carrito.agregar_producto(Producto, Cantidad)
                    Producto.cantidad -= Cantidad
                else:
                    print("Cantidad no válida.")
            else:
                print("Id de producto no válido.")

            Respuesta = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
            Continuar = (Respuesta == "s")
        
        Carrito.imprimir_factura()
        self.facturas.append(Carrito)