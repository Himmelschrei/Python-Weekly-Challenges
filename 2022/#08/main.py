#
# Reto #8
# DECIMAL A BINARIO
#
# Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#

def main():    
    choice = input("What conversion do you want to make? \n 1. Decimal to binary \n 2. Binary to decimal \n E. Exit \n")

    match choice:
        case '1':
            d_b_converter()
        case '2':
            b_d_converter()
        case 'e':
            quit()
        case _:
            print("Please choose a valid option.")
            main()

def b_d_converter():
    binary = int(input("Please enter the desired decimal number you want to convert: "))
    blist = [int(x) for x in str(binary)]
    rlist = list()

    for i in blist:
        rlist = [i] + rlist

    power = 1
    dec = 0
    for i in rlist:
        i *= power
        dec += i
        power *= 2

    print(f"The binary number {binary} equals {dec} in decimal system.")


def d_b_converter():
    dec = int(input("Please enter a desired decimal number you want to convert: "))
    ori = dec
    binary = []

    while (dec > 0):
        rest = int(float(dec % 2))
        binary.append(rest)
        dec = (dec - rest) / 2
    
    sbinary = ""
    
    for i in binary[::-1]:
        sbinary = sbinary + str(i)
    
    print(f"The decimal number {ori} equals {sbinary} in binary system.")

main()