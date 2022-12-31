"""Объявите класс Box (ящик), объекты которого создаются командой:

box = Box(name, max_weight)
где name - название ящика (строка); max_weight - максимальный суммарный вес вещей в ящике (любое положительное число).

В каждом объекте этого класса должны формироваться локальные атрибуты:

_name - ссылка на параметр name;
_max_weight - ссылка на параметр max_weight;
_things - список из вещей, хранящиеся в ящике (изначально пустой список).

В классе Box объявите метод:

def add_thing(self, obj)

для добавления новой вещи в ящик, где obj - кортеж из двух значений:

(название_вещи, вес_вещи)

Если в момент добавления новой вещи суммарный вес всех вещей в ящике становится больше величины _max_weight,
то генерировать исключение командой:

raise ValueError('превышен суммарный вес вещей')

Затем, объявите еще один класс BoxDefender, который должен работать совместно с менеджером контекста следующим образом
(эти строчки в программе не писать):

box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))

with BoxDefender(box) as b:
    b.add_thing(("зонт", 346.6))
    b.add_thing(("шина", 500))
    ...
Здесь b - это ссылка на объект класса Box. Если при добавлении вещей возникает исключение ValueError,
то объект box должен оставаться без изменений (с теми вещами, что были до вызова менеджера контекста).
Иначе, все добавленные вещи остаются в объекте box.

P.S. В программе только объявить классы. Выводить что-либо на экран и использовать классы не нужно."""


from copy import deepcopy


class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []

    def add_thing(self, obj):
        if self._max_weight < sum(map(lambda x: x[1], self._things)) + obj[1]:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)


class BoxDefender:
    def __init__(self, def_cls):
        self.__def_cls = def_cls

    def __enter__(self):
        self.__temp_cls = deepcopy(self.__def_cls)
        return self.__temp_cls

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__def_cls._things = self.__temp_cls._things
        return False

#  Tests

b = Box('name', 2000)
assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"

b.add_thing(("1", 100))
b.add_thing(("2", 200))

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 1000))
        bb.add_thing(("4", 1900))
except ValueError:
    assert len(b._things) == 2

else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 100))
except ValueError:
    assert False, "возникло исключение ValueError, хотя, его не должно было быть"
else:
    assert len(b._things) == 3, "неверное число элементов в списке _things"
