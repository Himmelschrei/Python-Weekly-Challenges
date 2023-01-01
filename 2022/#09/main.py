#
# Reto #9
# CÓDIGO MORSE

# Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
#

import re

def check(text):
    for character in text:
        if character.isdigit() or character.isalpha():
            return True
    return False
        

def decode(text):
    alttext = ""

    nmdict = dict({"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
                    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
                    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", 
                    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
                    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
                    "Z": "--..", "1": ".----", "2": "..---", "3": "...--",
                    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
                    "8": "---..", "9": "----.", "0": "-----", ",": "--..--",
                    ".": ".-.-.-", "?": "..--..", "\"": ".-..-.",
                    ":": "---...", "'": ".----.", "-": "-....-", "/": "-..-.",
                    "(": "-.--.", ")": "-.--.-", " ": " "})

    mndict = dict((reversed(item) for item in nmdict.items()))
    mndict[""] = " "

    if (check(text) == True):
        # normal --> morse
        for i in text:
            alttext += nmdict[i]
    else:
        textl = text.split(" ")
        print(textl)
        for i in textl:
            alttext += mndict[i]
        alttext = alttext.replace("  ", " ")
    
    print(alttext)

print("--- Latin alphabet - Morse code translator ---")
text = str(input("Please enter the desired text to convert: ")).upper()
decode(text)