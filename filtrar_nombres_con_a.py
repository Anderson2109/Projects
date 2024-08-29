def filter_names_starting_with_a(names):
    return [name for name in names if name.startswith('A')]

lista_nombres = ["Ana", "Anderson", "Martin", "Juana", "Pablo"]
print(filter_names_starting_with_a(lista_nombres))