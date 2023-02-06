from src.Rectangle import Rectangle


class Square(Rectangle):
    name = 'Square'

    def __init__(self, a):
        self.a = a
        self.b = a


squ = Square(10)
print(squ.name)
print(squ.area)
print(squ.perimeter)

