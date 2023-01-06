class Vector:
    def __init__(self, *args):
        self.coords = args

    def __add__(self, other):
        self.compare_size(other)
        return self.__class__(*map(sum, zip(self.coords, other.coords)))

    def __sub__(self, other):
        self.compare_size(other)
        return self.__class__(*map(lambda x: x[0] - x[1], zip(self.coords, other.coords)))

    def __mul__(self, other):
        self.compare_size(other)
        return self.__class__(*map(lambda x: x[0] * x[1], zip(self.coords, other.coords)))

    def compare_size(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.compare_size(other)
            return self + other
        else:
            self.coords = tuple(x + other for x in self.coords)
        return self

    def __isub__(self, other):
        if isinstance(other, self.__class__):
            self.compare_size(other)
            return self - other
        else:
            self.coords = tuple(x - other for x in self.coords)
        return self

    def __eq__(self, other):
        self.compare_size(other)
        return all(map(lambda x: x[0] == x[1], zip(self.coords, other.coords)))


v1 = Vector(1, 1, 1)
v2 = Vector(2, 0, 2)
v1 -= v2
print(v1 != v2)
