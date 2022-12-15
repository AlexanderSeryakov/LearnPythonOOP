"""Необходимо объявить класс Body (тело), объекты которого создаются командой:

body = Body(name, ro, volume)
где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное);
volume - объем тела  (число: вещественное или целочисленное).

Для объектов класса Body должны быть реализованы операторы сравнения:

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5
Масса тела вычисляется по формуле:

m = ro * volume

P.S. В программе только объявить класс, выводить на экран ничего не нужно."""


class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def get_weight(self):
        return self.ro * self.volume

    @staticmethod
    def check_type(other):
        return other if isinstance(other, (int, float)) else other.get_weight()

    def __eq__(self, other):
        return self.get_weight() == self.__class__.check_type(other)

    def __gt__(self, other):
        return self.__class__.check_type(other) < self.get_weight()

    def __lt__(self, other):
        return self.__class__.check_type(other) > self.get_weight()
