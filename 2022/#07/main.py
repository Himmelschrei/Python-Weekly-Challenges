#
# Reto #7
# CONTANDO PALABRAS
#
# Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
#

def count_words(text):
    counter = dict()
    words = text.lower().split()

    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    print_counter(counter)

def print_counter(counter):
    for word in counter:
        if (counter[word] == 1):
            print(f"The word '{word}' appears once in the given text.")
        else:
            print(f"The word '{word}' appears {counter[word]} times in the given text")

text = str(input("Please type the desire text: "))
count_words(text)