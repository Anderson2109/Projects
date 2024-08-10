numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

cuadrado_producto = (numero1 * numero2) ** 2

if numero2 != 0:
    doble_cociente = 2 * (numero1 / numero2)
else:
    doble_cociente = "Error: División por cero"

cuadruple_diferencia = 4 * (numero1 - numero2)

cuadrado_suma = (numero1 + numero2) ** 2

print(f"El cuadrado del producto es: {cuadrado_producto}")
print(f"El doble del cociente es: {doble_cociente}")
print(f"El cuádruple de la diferencia es: {cuadruple_diferencia}")
print(f"El cuadrado de la suma es: {cuadrado_suma}")