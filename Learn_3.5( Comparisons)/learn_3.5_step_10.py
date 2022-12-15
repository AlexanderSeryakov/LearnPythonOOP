"""Объявите в программе класс с именем Box (ящик), объекты которого должны создаваться командой:

box = Box()
А сам класс иметь следующие методы:

add_thing(self, obj) - добавление предмета obj (объект другого класса Thing) в ящик;
get_things(self) - получение списка объектов ящика.

Для описания предметов необходимо объявить еще один класс Thing. Объекты этого класса должны создаваться командой:

obj = Thing(name, mass)
где name - название предмета (строка); mass - масса предмета (число: целое или вещественное).
Объекты класса Thing должны поддерживать операторы сравнения:

obj1 == obj2
obj1 != obj2
Предметы считаются равными, если у них одинаковые названия name (без учета регистра) и массы mass.

Также объекты класса Box должны поддерживать аналогичные операторы сравнения:

box1 == box2
box1 != box2
Ящики считаются равными, если одинаковы их содержимое (для каждого объекта класса Thing одного ящика и можно найти
 ровно один равный объект из второго ящика).
 P.S. В программе только объявить классы, выводить на экран ничего не нужно."""


class Box:
    def __init__(self):
        self.items = []

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items):
        self.__items = items

    def add_thing(self, obj):
        self.items.append(obj)

    def get_things(self):
        return self.items

    def __eq__(self, other):
        if len(self.items) == len(other.items):
            lst1 = sorted(self.items)
            lst2 = sorted(other.items)
            res_lst = [item_1 for item_1 in lst1 for item_2 in lst2 if item_1 == item_2]
            return len(res_lst) == len(lst1)
        return False


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, mass):
        self.__mass = mass

    def __eq__(self, other):
        return (self.name.lower(), self.mass) == (other.name.lower(), other.mass)

    def __lt__(self, other):
        return self.mass < other.mass
