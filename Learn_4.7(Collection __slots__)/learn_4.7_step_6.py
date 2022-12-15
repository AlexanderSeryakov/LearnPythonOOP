"""Объявите класс с именем Star (звезда), в объектах которого разрешены только локальные атрибуты с именами
(ограничение задается через коллекцию __slots__):

_name - название звезды (строка);
_massa - масса звезды (любое положительное число); часто измеряется в массах Солнца;
_temp - температура поверхности звезды в Кельвинах (любое положительное число).

Объекты этого класса должны создаваться командой:

star = Star(name, massa, temp)
На основе класса Star объявите следующие дочерние классы:

WhiteDwarf - белый карлик;
YellowDwarf - желтый карлик;
RedGiant - красный гигант;
Pulsar - пульсар.

В каждом объекте этих классов должны быть разрешены (дополнительно к атрибутам базового класса Star) только следующие
локальные атрибуты:

_type_star - название типа звезды (строка);
_radius - радиус звезды (любое положительное число); часто измеряется в радиусах Солнца.

Соответственно, объекты этих классов должны создаваться командой:

star = Имя_дочернего_класса(name, massa, temp, type_star, radius)
Создайте в программе следующие объекты звезд:

RedGiant: Альдебаран; 5; 3600; красный гигант; 45
WhiteDwarf: Сириус А; 2,1; 9250; белый карлик; 2
WhiteDwarf: Сириус B; 1; 8200; белый карлик; 0,01
YellowDwarf: Солнце; 1; 6000; желтый карлик; 1

Все эти объекты сохраните в виде списка stars. Затем, с помощью функций isinstance() и filter()
сформируйте новый список с именем white_dwarfs, состоящий только из белых карликов (WhiteDwarf).

P.S. В программе следует объявить только классы и создать списки. На экран выводить ничего не нужно."""


class Star:
    __slots__ = ('_name', '_massa', '_temp')

    def __init__(self, name, massa, temp):
        self._name = name
        self._massa = massa
        self._temp = temp


class DifferentStars(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class WhiteDwarf(DifferentStars):
    __slots__ = ()


class YellowDwarf(DifferentStars):
    __slots__ = ()


class RedGiant(DifferentStars):
    __slots__ = ()


class Pulsar(DifferentStars):
    __slots__ = ()

stars = [RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
         WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
         WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
         YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)]

white_dwarfs = list(filter(lambda obj: isinstance(obj, WhiteDwarf), stars))
