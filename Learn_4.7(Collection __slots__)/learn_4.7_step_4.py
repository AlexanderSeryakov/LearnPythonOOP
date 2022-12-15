""" Объявите класс Person, в объектах которого разрешены только локальные атрибуты с именами (ограничение задается
через коллекцию __slots__):

_fio - ФИО сотрудника (строка);
_old - возраст сотрудника (целое положительное число);
_job - занимаемая должность (строка).

Сами объекты должны создаваться командой:

p = Person(fio, old, job)
Создайте несколько следующих объектов этого класса с информацией:

Суворов, 52, полководец
Рахманинов, 50, пианист, композитор
Балакирев, 34, программист и преподаватель
Пушкин, 32, поэт и писатель

Сохраните все эти объекты в виде списка с именем persons."""


class Person:
    __slots__ = ('_fio', '_old', '_job')

    def __init__(self, fio, old, job):
        self._fio = fio
        self._old = old
        self._job = job

humans = """Суворов, 52, полководец
Рахманинов, 50, пианист, композитор
Балакирев, 34, программист и преподаватель
Пушкин, 32, поэт и писатель"""

persons = [Person(*x.split(', ', maxsplit=2)) for x in humans.splitlines()]

# Tests

assert len(persons) == 4, 'Неправильно сформирован список persons'
assert all(map(lambda obj: isinstance(obj, Person), persons)), 'Элементы списка persons должны быть объектами класса Person'

human_1 = Person('Name', 22, 'Developer')
try:
    human_1.mood = 'fine'
    assert False, 'Неверно объявлена коллекция __slots__'
except AttributeError:
    assert True
