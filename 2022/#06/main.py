#
# Reto #6
# INVIRTIENDO CADENAS
# 
# Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#

def revert_text_s(text):
    return text[::-1]

def revert_text_r(text):
    if text == "":
        return text
    else:
        return text[-1] + revert_text_r(text[:-1])

text = str(input("Please enter the desired text: "))

print(revert_text_s(text))
print(revert_text_r(text))