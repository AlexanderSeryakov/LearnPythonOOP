"""Объявите класс Animal (животное), объекты которого создаются командой:

an = Animal(name, kind, old)
где name - название животного (строка); kind - вид животного (строка); old - возраст (целое число).
В каждом объекте этого класса должны создаваться соответствующие приватные атрибуты: __name, __kind, __old.

В классе Animal должны быть объявлены объекты-свойства для изменения и считывания приватных атрибутов:

name - для работы с приватным атрибутом __name;
kind - для работы с приватным атрибутом __kind;
old - для работы с приватным атрибутом __old.

Создайте в программе список с именем animals, который содержит три объекта класса Animal со следующими данными:

Васька; дворовый кот; 5
Рекс; немецкая овчарка; 8
Кеша; попугай; 3

P.S. В программе нужно объявить только класс и создать список animals. На экран выводить ничего не нужно."""


class Animal:
    def __init__(self, name, kind, old):
        self.name = name
        self.kind = kind
        self.old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind):
        self.__kind = kind

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old


animals = [Animal('Васька', 'дворовый кот', 5), Animal('Рекс', 'немецкая овчарка', 8), Animal('Кеша', 'попугай', 3)]

