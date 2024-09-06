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