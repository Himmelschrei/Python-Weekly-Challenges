#
# Reto #4
# ÁREA DE UN POLÍGONO
# Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.
#

class Polygon(object):
    def __init__(self, area, type):
        self.area = area
        self.type = type
    
    def get_area(self):
        return self.area

    def get_type(self):
        return self.type
    
    def ask_type():
        type = str(input("What type of Polygon do you want to calculate the area from? ")).lower()
        return type

    def print_area():
        type = Polygon.ask_type()
        if (type == "triangle"):
            area = Triangle.calc_triangle()
        elif (type == "square"):
            area = Square.calc_size()
        elif (type == "rectangle"):
            area = Rectangle.calc_size()
        else:
            print("The chosen type is not valid.")
            Polygon.print_area()

        print(f"The {type} has an area of {area:g}")
        exit()

class Triangle(Polygon):
    def __init__(self, area, type):
        super().__init__(area, type)
    
    type = "triangle"

    def ask_size():
        height = float(input("Please enter the height of the triangle: "))
        base = float(input("Please enter the base of the triangle: "))
        return height, base
    
    def calc_triangle():
        h, b = Triangle.ask_size()
        return (h * b) / 2

class Square(Polygon):
    def __init__(self, area, type):
        super().__init__(area, type)

    type = "square"

    def ask_size():
        side = float(input("Please enter the length of the square's sides: "))
        return side

    def calc_size():
        s = Square.ask_size()
        return s ** 2

class Rectangle(Polygon):
    def __init__(self, area, type):
        super().__init__(area, type)
    
    type = "rectangle"

    def ask_size():
        length = float(input("Please enter the length of the rectangle: "))
        width = float(input("Please enter the width of the rectangle: "))
        return length, width
    
    def calc_size():
        l, w = Rectangle.calc_size()
        return l * w

Polygon.print_area()
    