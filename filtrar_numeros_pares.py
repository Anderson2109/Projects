def filter_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

lista_numeros = [1, 2, 3, 4, 5, 6]
print(filter_even_numbers(lista_numeros))