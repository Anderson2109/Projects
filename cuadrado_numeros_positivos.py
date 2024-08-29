def square_positive_numbers (numbers):
    return [n**2 for n in numbers if n > 0]

lista_numeros = [-1, 2, -3, -4, 5, -6, 7, -8]
print(square_positive_numbers(lista_numeros))