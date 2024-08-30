class Producto:
    def __init__(self, id, descripcion, precio, cantidad, impuesto):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        self.impuesto = impuesto

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

class POS:
    def __init__(self):
        self.inventario = {}
        self.facturas = []

    def agregar_producto_inventario(self, producto):
        self.inventario[producto.id] = producto

    def mostrar_menu(self):
        print("Menú:")
        for id, producto in self.inventario.items():
            print(f"{id}. {producto.descripcion} -> RD${producto.precio}")

    def vender(self):
        carrito = Factura(input("Ingrese el nombre del cliente: "))
        continuar = True
        while continuar:
            self.mostrar_menu()
            id_producto = int(input("Ingrese el ID del producto: "))
            if id_producto in self.inventario:
                producto = self.inventario[id_producto]
                cantidad = int(input(f"Ingrese la cantidad de {producto.descripcion}: "))
                if cantidad > 0 and cantidad <= producto.cantidad:
                    carrito.agregar_producto(producto, cantidad)
                    producto.cantidad -= cantidad
                else:
                    print("Cantidad no válida.")
            else:
                print("ID de producto no válido.")

            respuesta = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
            continuar = (respuesta == "s")
        
        carrito.imprimir_factura()
        self.facturas.append(carrito)

def main():
    pos = POS()

    pos.agregar_producto_inventario(Producto(1, "Arroz", 50, 100, "01"))
    pos.agregar_producto_inventario(Producto(2, "Habichuelas", 80, 50, "01"))
    pos.agregar_producto_inventario(Producto(3, "Aceite", 300, 30, "02"))
    pos.agregar_producto_inventario(Producto(4, "Pollo", 85, 20, "01"))
    pos.agregar_producto_inventario(Producto(5, "Lechuga", 80, 60, "00"))

    pos.vender()

if __name__ == "__main__":
    main()