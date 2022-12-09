"""Вам необходимо создать простую программу по учету семейного бюджета. Для этого в программе объявите два класса с именами:

Budget - для управления семейным бюджетом;
Item - пункт расходов бюджета.

Объекты класса Item должны создаваться командой:

it = Item(name, money)
где name - название статьи расхода; money - сумма расходов (вещественное или целое число).

Соответственно, в каждом объекте класса Item должны формироваться локальные атрибуты name и money с переданными
значениями. Также с объектами класса Item должны выполняться следующие операторы:

s = it1 + it2 # сумма для двух статей расходов
и в общем случае:

s = it1 + it2 + ... + itN # сумма N статей расходов
При суммировании оператор + должен возвращать число - вычисленную сумму по атрибутам money соответствующих объектов класса Item.

Объекты класса Budget создаются командой:

my_budget = Budget()
А сам класс Budget должен иметь следующие методы:

add_item(self, it) - добавление статьи расхода в бюджет (it - объект класса Item);
remove_item(self, indx) - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
get_items(self) - возвращает список всех статей расходов (список из объектов класса Item).
"""


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        m = self.money
        m = m + other
        return m

    def __radd__(self, other):
        return self + other


class Budget:
    def __init__(self):
        self.items_lst = []

    def __len__(self):
        return len(self.items_lst)

    def add_item(self, it):
        self.items_lst.append(it)

    def remove_item(self, indx):
        self.items_lst.pop(indx)

    def get_items(self):
        return self.items_lst


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

assert len(my_budget) == 4, 'Неверно добавлены элементы в список расходов'

my_budget.remove_item(0)

assert len(my_budget) == 3, 'Неверно добавлены элементы в список расходов'

my_budget.add_item(Item("Изучаем Python", 2500))

assert len(my_budget) == 4, 'Неверно добавлены элементы в список расходов'

# вычисление общих расходов
total_price = 0
for x in my_budget.get_items():
    total_price = total_price + x

assert total_price == 9000.11, "Неверно вычисляется сумма"
