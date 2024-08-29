def filter_logs_words(words):
    return [word for word in words if len(word) > 5]

lista_palabras = ["Hola", "profesor", "Adrian", "Fondeur"]
print(filter_logs_words(lista_palabras))