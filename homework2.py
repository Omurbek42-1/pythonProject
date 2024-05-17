import math

class Figure:
    unit = "cm"

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement abstract method")

    def info(self):
        raise NotImplementedError("Subclasses must implement abstract method")

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Circle radius: {self.__radius}{self.unit}, area: {area:.2f}{self.unit}².")

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return (self.__side_a * self.__side_b) / 2

    def info(self):
        area = self.calculate_area()
        print(f"RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit}, area: {area:.2f}{self.unit}².")

# Создание объектов
circles = [Circle(2), Circle(3)]
triangles = [RightTriangle(5, 8), RightTriangle(3, 4), RightTriangle(6, 7)]

# Вывод информации
for circle in circles:
    circle.info()

for triangle in triangles:
    triangle.info()
