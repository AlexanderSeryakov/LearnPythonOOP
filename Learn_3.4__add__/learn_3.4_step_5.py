"""Объявите класс с именем ListMath, объекты которого можно создавать командами:

lst1 = ListMath() # пустой список
lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и вещественные числа,
остальные игнорировать (если указываются в списке). Например:

lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
В каждом объекте класса ListMath должен быть публичный атрибут:

lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).

Также с объектами класса ListMath должны работать следующие операторы:

lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0
При использовании бинарных операторов +, -, *, / должны формироваться новые объекты класса ListMath с новыми списками,
прежние списки не меняются.

При использовании операторов +=, -=, *=, /= значения должны меняться внутри списка текущего объекта
(новый объект не создается).

P.S. В программе достаточно только объявить класс. На экран ничего выводить не нужно."""


class ListMath:
    def __init__(self, lst_in=None):
        if lst_in is None:
            lst_in = []
        self.lst_math = [x for x in lst_in if type(x) in (int, float)]

    def __add__(self, other):
        return ListMath([x + other for x in self.lst_math])

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.lst_math = [x + other for x in self.lst_math]
        return self

    def __sub__(self, other):
        return ListMath([x - other for x in self.lst_math])

    def __rsub__(self, other):
        return ListMath([other - x for x in self.lst_math])

    def __isub__(self, other):
        self.lst_math = [x - other for x in self.lst_math]
        return self

    def __mul__(self, other):
        return ListMath([x * other for x in self.lst_math])

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.lst_math = [x * other for x in self.lst_math]
        return self

    def __truediv__(self, other):
        return ListMath([x / other for x in self.lst_math])

    def __rtruediv__(self, other):
        return ListMath([other / x for x in self.lst_math])

    def __itruediv__(self, other):
        self.lst_math = [x / other for x in self.lst_math]
        return self


lst = ListMath([1, 3, 4])
res = 12/lst

assert res.lst_math == [12.0, 4.0, 3.0], 'Неверно обработано деление числа на каждый элемент списка'

lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)

assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"

assert lst1.lst_math == [] and lst2.lst_math == [1, 2, -5, 7], "неверные значения в списке объекта класса ListMath"

res1 = lst2 + 76
lst = ListMath([1, 2, 3])
lst += 5
assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71, 83], "неверные значения, полученные при операциях сложения"

lst = ListMath([0, 1, 2])
res3 = lst - 76
res4 = 7 - lst
assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [7, 6, 5], "неверные значения, полученные при операциях вычитания"

lst -= 3
assert lst.lst_math == [-3, -2, -1], "неверные значения, полученные при операции вычитания -="

lst = ListMath([1, 2, 3])
res5 = lst * 5
res6 = 3 * lst
lst *= 4
assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6, 9], "неверные значения, полученные при операциях умножения"
assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"

lst = lst / 2
lst /= 13.0