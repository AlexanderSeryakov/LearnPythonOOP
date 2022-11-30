""" Объявите класс-декоратор InputValues с параметром render - функция или объект для преобразования данных из строк
в другой тип данных. Чтобы реализовать такой декоратор в инициализаторе __init__() следует указать параметр render,
а магический метод __call__() определяется как функция-декоратор:

class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        # здесь строчки программы

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            # здесь строчки программы
        return wrapper
В качестве рендера объявите класс с именем RenderDigit, который бы преобразовывал строковые данные в целые числа.
Объекты этого класса создаются командой:

render = RenderDigit()
и применяются следующим образом:

d1 = render("123")   # 123 (целое число)
d2 = render("45.54")   # None (не целое число)
d3 = render("-56")   # -56 (целое число)
d4 = render("12fg")  # None (не целое число)
d5 = render("abc")   # None (не целое число)
Декорируйте стандартную функцию input декоратором InputValues и объектом рендера класса RenderDigit так, чтобы на
выходе при вводе целых чисел через пробел возвращался список из введенных значений. А на месте не целочисленных данных
- значение None.

Например, при вводе строки:

"1 -5.3 0.34 abc 45f -5"

должен возвращаться список:

[1, None, None, None, None, -5]

Назовите декорированную функцию input_dg и вызовите ее командой:

res = input_dg()
Выведите результат res на экран."""


class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return list(map(self.render, func.split()))

        return wrapper


class RenderDigit:
    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except ValueError:
            return None

render = RenderDigit()
input_dg = InputValues(render)(input())
res = input_dg()
print(res)
