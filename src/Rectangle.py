from src.Figure import Figure


class Rectangle(Figure):

    name = 'Rectangle'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        if (self.a > 0) and (self.b > 0):
            return self.a * self.b * self.get_area()
        else:
            raise ValueError('impossible to calculate')

    @property
    def perimeter(self):
        if (self.a > 0) and (self.b > 0):
            return (self.a + self.b) * 2 * self.get_perimeter()
        else:
            raise ValueError('impossible to calculate')
