import os

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class Almacen:
    def __init__(self, id, nombre, altura, largura, anchura):
        self.id = id
        self.nombre = nombre
        self.altura = altura
        self.largura = largura
        self.anchura = anchura
        self.capacidad_total = altura * largura * anchura
        self.capacidad_ocupada = 0
        self.items = []

    def capacidad_disponible(self):
        return self.capacidad_total - self.capacidad_ocupada
    
class Item:
    contador_id = 1

    def __init__(self, descripcion, area):
        self.id = Item.contador_id
        Item.contador_id += 1
        self. descripcion = descripcion
        self.area = area

class Sistema_Gestion_Almacen:
    def __init__(self, empleado):
        self.empleado = empleado
        self.almacenes = []

    def registrar_almacen(self):
        try:
            nombre = input("Ingrese el nombre del almacén: ")
            altura = float(input("Ingrese la altura del almacén: "))
            largura = float(input("Ingrese la largura del almacén: "))
            anchura = float(input("Ingrese la anchura del almacén: "))
            id = len(self.almacenes) + 1
            almacen = Almacen(id, nombre, altura, largura, anchura)
            self.almacenes.append(almacen)
            print("Almacén registrado exitosamente.")
        except ValueError:
            print("Error, Asegúrese de ingresar valores numéricos correctos. ")
    
    def registrar_item(self, id_almacen, descripcion, area):
        almacen = self.buscar_almacen(id_almacen)
        if almacen:
            if almacen.capacidad_disponible() >= area * 1.2:
                item = Item(descripcion, area)
                almacen.items.append(item)
                almacen.capacidad_ocupada += area
                print("Ítem registrado exitosamente.")
            else:
                print("No hay suficiente capacidad en el almacén para registrar el ítem.")
        else:
            print("Almacén no encontrado.")

    def retirar_item(self, id_almacen, id_item):
        almacen = self.buscar_almacen(id_almacen)
        if almacen:
            item = self.buscar_item(almacen, id_item)
            if item:
                almacen.items.remove(item)
                almacen.capacidad_ocupada -= item.area
                print("Ítem retirado exitosamente.")
            else:
                print("Ítem no encontrado.")
        else:
            print("Almacén no encontrado.")

    def buscar_almacen(self, id_almacen):
        for almacen in self.almacenes:
            if almacen.id == id_almacen:
                return almacen
            return None
        
    def buscar_item(self, almacen, id_item):
        for item in almacen.items:
            if item.id == id_item:
                return item
            return None

    def mostrar_almacenes(self):
        for almacen in self.almacenes:
            print(f"ID: {almacen.id}, Nombre: {almacen.nombre}, Capacidad total: {almacen.capacidad_total} m³, Capacidad disponible: {almacen.capacidad_disponible()} m³")

    def mostrar_items(self, id_almacen):
        almacen = self.buscar_almacen(id_almacen)
        if almacen:
            print(f"Ítems en el almacén {almacen.nombre}:")
            for item in almacen.items:
                print(f"ID: {item.id}, Descripción: {item.descripcion}, Área: {item.area} m²")
        else:
            print("Almacén no encontrado.")

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

def main():
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    empleado = Empleado(nombre_empleado)
    sistema = Sistema_Gestion_Almacen(empleado)

    while True:
        sistema.limpiar_pantalla()
        print("Sistema de Gestión de Almacenes")
        print("1. Registrar Almacén")
        print("2. Registrar Ítem")
        print("3. Retirar Ítem")
        print("4. Mostrar Almacenes")
        print("5. Mostrar Ítems en un Almacén")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            sistema.registrar_almacen()
        elif opcion == '2':
            id_almacen = int(input("Ingrese el ID del almacén: "))
            descripcion = input("Ingrese la descripción del ítem: ")
            area = float(input("Ingrese el área del ítem (en metros cuadrados): "))
            sistema.registrar_item(id_almacen, descripcion, area)
        elif opcion == '3':
            id_almacen = int(input("Ingrese el ID del almacén: "))
            id_item = int(input("Ingrese el ID del ítem: "))
            sistema.retirar_item(id_almacen, id_item)
        elif opcion == '4':
            sistema.mostrar_almacenes()
        elif opcion == '5':
            id_almacen = int(input("Ingrese el ID del almacén: "))
            sistema.mostrar_items(id_almacen)
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
        
        input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()