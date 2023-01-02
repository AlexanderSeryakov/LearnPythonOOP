""" Объявите класс Box3D для представления прямоугольного параллелепипеда (бруска), объекты которого создаются командой:

box = Box3D(width, height, depth)
где width, height, depth - ширина, высота и глубина соответственно (числа: целые или вещественные)

В каждом объекте класса Box3D должны создаваться публичные атрибуты:

width, height, depth - ширина, высота и глубина соответственно.

С объектами класса Box3D должны выполняться следующие операторы:

box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = 3 * box2    # Box3D: width=6, height=12, depth=18
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box2 % 3    # Box3D: width=2, height=1, depth=0
При каждой арифметической операции следует создавать новый объект класса Box3D с соответствующими значениями локальных
атрибутов."""


class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        self.attrs = [self.width, self.height, self.depth]

    def __add__(self, other):
        other_arrrs = [other.width, other.height, other.depth]
        return self.__class__(*list(map(sum, zip(self.attrs, other_arrrs))))

    def __sub__(self, other):
        other_arrrs = [other.width, other.height, other.depth]
        return self.__class__(*list(map(lambda x: x[0] - x[1], zip(self.attrs, other_arrrs))))

    def __mul__(self, other):
        return self.__class__(*[x * other for x in self.attrs])

    def __rmul__(self, other):
        return self * other

    def __floordiv__(self, other):
        return self.__class__(*list(map(lambda x: x // other, self.attrs)))  # Вариант реализации без list comprehension

    def __mod__(self, other):
        return self.__class__(*[x % other for x in self.attrs])

