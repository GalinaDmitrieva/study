geometric_figures = ['Triangle',
                     'Circle',
                     'Rectangle',
                     'Square']


class Figure:

    name = None

    def get_area(self):
        return 1

    def get_perimeter(self):
        return 1

    def add_area(self, k):
        if k.name in geometric_figures:
            return self.area + k.area
        else:
            raise ValueError('not geometric figure')
