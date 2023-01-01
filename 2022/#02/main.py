#
# Reto #2
# LA SUCESIÓN DE FIBONACCI# Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...
#

num0 = 0
num1 = 1

for counter in range(51):
    print(num0)
    
    fib = num0 + num1
    num0 = num1
    num1 = fib