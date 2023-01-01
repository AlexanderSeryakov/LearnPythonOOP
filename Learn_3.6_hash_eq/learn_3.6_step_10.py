""" Объявите класс с именем Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)
где a, b, c - длины сторон треугольника (числа: целые или вещественные). В классе Triangle объявите следующие
дескрипторы данных:

a, b, c - для записи и считывания длин сторон треугольника.

При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное).
Иначе, генерируется исключение командой:

raise ValueError("длины сторон треугольника должны быть положительными числами")
Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника. То есть,
должны выполняться условия:

a < b+c; b < a+c; c < a+b

Иначе генерируется исключение командой:

raise ValueError("с указанными длинами нельзя образовать треугольник")
Наконец, с объектами класса Triangle должны выполняться функции:

len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)), где p -
полупериметр треугольника).

P.S. На экран ничего выводить не нужно, только объявить класс Triangle."""


from math import sqrt


class Descriptor:
    def __set_name__(self, owner, name):
        self.name = '_'+name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_type(value)
        setattr(instance, self.name, value)

    @staticmethod
    def verify_type(value):
        if type(value) not in (int, float):
            raise ValueError("длины сторон треугольника должны быть положительными числами")


class Triangle:
    a = Descriptor()
    b = Descriptor()
    c = Descriptor()

    def __init__(self, a, b, c):
        if not (a < b+c and b < a+c and c < a+b):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        self.a = a
        self.b = b
        self.c = c

    def __len__(self):
        return sum((self.a, self.b, self.c))

    def __call__(self):
        p = len(self)/2
        return sqrt(p * (p-self.a) * (p-self.b) * (p-self.c))


tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"

