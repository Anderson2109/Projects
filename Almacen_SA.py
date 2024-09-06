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
        self.capacidad_total = self.altura * self.anchura * self.largura
        self.capacidad_disponible = self.capacidad_total * 0.80
        self.items = []