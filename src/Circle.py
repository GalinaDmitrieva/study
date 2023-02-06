import math
from src.Figure import Figure


class Circle(Figure):
    name = 'Circle'

    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        if self.r > 0:
            return math.pi * math.pow(self.r, 2) * self.get_area()
        else:
            raise ValueError('impossible to calculate')

    @property
    def perimeter(self):
        if self.r > 0:
            return 2 * math.pi * self.r * self.get_perimeter()
        else:
            raise ValueError('impossible to calculate')


