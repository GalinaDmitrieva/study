import math
from src.Figure import Figure


class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def triangle_exist(self):
        if (self.a + self.b <= self.c) or (self.b + self.c <= self.a) or (self.c + self.a <= self.b) \
                or (self.a <= 0) or (self.b <= 0) or (self.c <= 0):
            raise ValueError('Triangle does not exist')
        else:
            return 1

    @property
    def perimeter(self):
        if self.triangle_exist():
            return (self.a + self.b + self.c) * self.get_perimeter()
        else:
            raise ValueError('Triangle does not exist')

    def half_perimeter(self):
        return self.perimeter / 2

    @property
    def area(self):
        if self.triangle_exist():
            return math.sqrt(self.half_perimeter() * (self.half_perimeter() - self.a) * (self.half_perimeter() - self.b) * (
                self.half_perimeter() - self.c)) * self.get_area()
        else:
            raise ValueError('Triangle does not exist')
