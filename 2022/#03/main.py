#
# Reto #3
# ¿ES UN NÚMERO PRIMO?# Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.
#

def is_prime(num):
    if (num < 2):
        return False
    
    for i in range(2, num):
        if (num % i == 0):
            return False
    
    return True

for num in range(1, 101):
    if(is_prime(num)):
        print(num)