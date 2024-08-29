def fibonacci(n):
    a, b = 0, 1
    secuencia = []
    for _ in range (n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia
n = int(input("Ingrese el valor de la sucesion de fibonacci que desea:"))

fibonacci_secuencia = fibonacci(n)
print("Los primeros", n, "valores de la sucesion de fibonacci son:", fibonacci_secuencia)