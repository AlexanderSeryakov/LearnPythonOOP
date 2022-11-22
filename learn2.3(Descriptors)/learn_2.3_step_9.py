"""Необходимо объявить класс Bag (рюкзак), объекты которого будут создаваться командой:

bag = Bag(max_weight)
где max_weight - максимальный суммарный вес вещей, который выдерживает рюкзак (целое число).

В каждом объекте этого класса должен создаваться локальный приватный атрибут:

__things - список вещей в рюкзаке (изначально список пуст).

Сам же класс Bag должен иметь объект-свойство:

things - для доступа к локальному приватному атрибуту __things (только для считывания, не записи).

Также в классе Bag должны быть реализованы следующие методы:

add_thing(self, thing) - добавление нового предмета в рюкзак (добавление возможно, если суммарный вес
(max_weight) не будет превышен, иначе добавление не происходит);
remove_thing(self, indx) - удаление предмета по индексу списка __things;
get_total_weight(self) - возвращает суммарный вес предметов в рюкзаке.

Каждая вещь описывается как объект класса Thing и создается командой:

t = Thing(название, вес)
где название - наименование предмета (строка); вес - вес предмета (целое или вещественное число).

В каждом объекте класса Thing должны формироваться локальные атрибуты:

name - наименование предмета;
weight - вес предмета.

Пример использования классов (эти строчки в программе писать не нужно):

bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")"""


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, weight):
        self.max_weight = weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def get_sum(self, thing_add):
        return sum(thing.weight for thing in self.things) + thing_add.weight <= self.max_weight

    def add_thing(self, thing):
        self.things.append(thing) if self.get_sum(thing) else print('Вес добавляемого предмета превышает вместимость!')

    def remove_thing(self, indx):
        try:
            self.things.pop(indx)
        except IndexError:
            print('Неверный индекс!')

    def get_total_weight(self):
        return sum(thing.weight for thing in self.things)


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()

assert w == 720, 'Неверно подсчитан вес предметов'
