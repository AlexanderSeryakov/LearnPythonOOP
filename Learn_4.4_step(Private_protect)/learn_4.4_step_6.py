"""Объявите класс Furniture (мебель), объекты которого создаются командой:

f = Furniture(name, weight)
где name - название предмета (строка); weight - вес предмета (целое или вещественное число).

В каждом объекте класса Furniture должны создаваться защищенные локальные атрибуты с именами _name и _weight.
В самом классе Furniture нужно объявить приватные методы:

__verify_name() - для проверки корректности имени;
__verify_weight() - для проверки корректности веса.

Метод __verify_name() проверяет, что имя должно быть строкой, если это не так, то генерируется исключение командой:

raise TypeError('название должно быть строкой')
Метод __verify_weight() проверяет, что вес должен быть положительным числом (строго больше нуля), если это не так, то
генерируется исключение командой:

raise TypeError('вес должен быть положительным числом')
Данные методы следует вызывать всякий раз при записи новых значений в атрибуты _name и _weight (а также при их создании).

На основе базового класса Furniture объявить следующие дочерние классы:

Closet - для представления шкафов;
Chair - для представления стульев;
Table - для представления столов.

Объекты этих классов должны создаваться командами:

obj = Closet(name, weight, tp, doors)   # tp: True - шкаф-купе; False - обычный шкаф; doors - число дверей (целое число)
obj = Chair(name, weight, height)       # height - высота стула (любое положительное число)
obj = Table(name, weight, height, square) # height - высота стола; square - площадь поверхности (любые положительные числа)
В каждом объекте этих классов должны создаваться соответствующие защищенные атрибуты:

- в объектах класса Closet: _name, _weight, _tp, _doors
- в объектах класса Chair: _name, _weight, _height
- в объектах класса Table: _name, _weight, _height, _square

В каждом классе (Closet, Chair, Table) объявить метод:

get_attrs()
который возвращает кортеж из значений локальных защищенных атрибутов объектов этих классов.

Пример использования классов (эти строчки в программе писать не нужно):

cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно."""


class Furniture:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def __setattr__(self, key, value):
        if key == '_name':
            self.__verify_name(value)
        if key == '_weight':
            self.__verify_weight(value)
        super().__setattr__(key, value)

    def __verify_name(self, name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')
        return

    def __verify_weight(self, weight):
        if weight < 0:
            raise TypeError('вес должен быть положительным числом')
        return


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return self._name, self._weight, self._tp, self._doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return self._name, self._weight, self._height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return self._name, self._weight, self._height, self._square
