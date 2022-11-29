"""Объявите класс DigitRetrieve для преобразования данных из строки в числа. Объекты этого класса создаются командой:

dg = DigitRetrieve()
Затем, их предполагается использовать, например следующим образом:

d1 = dg("123")   # 123 (целое число)
d2 = dg("45.54")   # None (не целое число)
d3 = dg("-56")   # -56 (целое число)
d4 = dg("12fg")  # None (не целое число)
d5 = dg("abc")   # None (не целое число)
То есть, целые числа в строке следует приводить к целочисленному типу данных, а все остальные - к значению None.

С помощью объектов класса DigitRetrieve должно выполняться преобразование чисел из списка строк следующим образом:

st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
P.S. На экран ничего выводить не нужно. """


class DigitRetrieve:
    def __call__(self, x, *args, **kwargs):
        try:
            return int(x)
        except ValueError:
            return None
