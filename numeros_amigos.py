def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

numero1 = int(input("Ingrese el primer número:"))
numero2 = int(input("Ingrese el seungo número:"))

if suma_divisores(numero1) == numero2 and suma_divisores(numero2) == numero1:
    print(f"{numero1} y {numero2} son números amigos.")
else:
    print(f"{numero1} y {numero2} no son números amigos.")