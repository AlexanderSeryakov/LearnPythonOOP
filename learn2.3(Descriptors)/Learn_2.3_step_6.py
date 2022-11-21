""" Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения. При записи
вещественного числа должна выполняться проверка на вещественный тип данных. Если проверка не проходит, то генерировать
исключение командой:

raise TypeError("Присваивать можно только вещественный тип данных.")
Объявите класс Cell, в котором создается объект value дескриптора FloatValue. А объекты класса Cell должны создаваться командой:

cell = Cell(начальное значение ячейки)
Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:

table = TableSheet(N, M)
Каждая ячейка этой таблицы должна быть представлена объектом класса Cell, работать с вещественными числами через объект
value (начальное значение должно быть 0.0).

В каждом объекте класса TableSheet должен формироваться локальный атрибут:

cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).

Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3. Запишите в эту таблицу числа от 1.0 до 15.0
(по порядку).
"""


class FloatValue:

    @classmethod
    def check_float(cls, value):
        if type(value) is float:
            return 1
        raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_float(value)
        setattr(instance, self.name, value)


class Cell:

    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, n, m):
        self.string = n
        self.column = m
        self.cells = [[Cell() for _ in range(self.column)] for _ in range(self.string)]

    def fill_value(self, start, end):
        while start <= end:
            for row in self.cells:
                for column in row:
                    column.value = start
                    start += 1.0

    def draw_value_cells(self):
        for row in self.cells:
            for column in row:
                print(column.value)


table = TableSheet(5, 3)
table.fill_value(1.0, 15.0)
table.draw_value_cells()
assert isinstance(table, TableSheet)
assert len(table.cells) == 5 and len(table.cells[0]) == 3

assert type(table.cells) == list

res = [int(x.value) for row in table.cells for x in row]
assert res == list(range(1, 16))

table.cells[0][0].value = 1.0
x = table.cells[1][0].value

try:
    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"