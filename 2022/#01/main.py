#
# Reto #1
# ¿ES UN ANAGRAMA?
# Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.
#

word1 = str(input("Please enter the first word: "))
word2 = str(input("Please enter the second word: "))

word1 = word1.lower()
word2 = word2.lower()

if (word1 == word2):
    print("Both words are the same, so they don't count as an anagram.")
else:
    word1 = sorted(word1)
    word2 = sorted(word2)
    print("Word 1 after sorting: ", word1)
    print("Word 2 after sorting: ", word2)
    
    if (word1 == word2):
        print("The words are anagrams.")
    else:
        print("The words aren't anagrams.")