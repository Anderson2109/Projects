class Almacen:
    def __init__(self, id_almacen, nombre, altura, anchura, largura):
        self.id_almacen = id_almacen
        self.nombre = nombre
        self.altura = altura
        self.anchura = anchura
        self.largura = largura
        self.capacidad_total = self.altura * self.anchura * self.largura
        self.capacidad_disponible = self.capacidad_total * 0.80 
        self.items = []

    def agregar_item(self, item):
        if item.area <= self.capacidad_disponible:
            self.items.append(item)
            self.capacidad_disponible -= item.area
            print(f"Item {item.descripcion} agregado al almacén {self.nombre}.")
        else:
            print(f"Capacidad insuficiente para el item {item.descripcion}.")

    def retirar_item(self, item_id):
        for item in self.items:
            if item.id_item == item_id:
                self.capacidad_disponible += item.area
                self.items.remove(item)
                print(f"Item {item.descripcion} retirado del almacén {self.nombre}.")
                return
        print(f"Item con id {item_id} no encontrado en el almacén {self.nombre}.")

    def mostrar_informacion(self):
        print(f"Almacén: {self.nombre} (ID: {self.id_almacen})")
        print(f"Capacidad total: {self.capacidad_total} m3")
        print(f"Capacidad disponible: {self.capacidad_disponible} m3")
        print("Items almacenados:")
        for item in self.items:
            print(f"  - {item.descripcion} (Área: {item.area} m2)")

class item:
    def __init__(self, id_item, descripcion, area):
        self.id_item = id_item
        self.descripcion = descripcion
        self.area = area

class empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def registrar_item(self, item, almacen):
        almacen.agregar_item(item)

    def retirar_item(self, item_id, almacen):
        almacen.retirar_item(item_id)