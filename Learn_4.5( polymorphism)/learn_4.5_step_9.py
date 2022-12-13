"""Вам поручают разработать класс для представления маршрутов в навигаторе. Для этого требуется объявить класс с именем
Track, объекты которого могут создаваться командами:

tr = Track(start_x, start_y)
tr = Track(pt1, pt2, ..., ptN)
где start_x, start_y - начальная координата маршрута (произвольные числа); pt1, pt2, ..., ptN - набор из произвольного
числа точек (координат) маршрута (объекты класса PointTrack).

При передаче аргументов (start_x, start_y) координата должна представляться первым объектом класса PointTrack. Наборы
всех точек (объектов PointTrack) должны сохраняться в локальном приватном атрибуте объекта класса Track:

__points - список из точек (координат) маршрута.

Далее, каждая точка (координата) должна определяться классом PointTrack, объекты которого создаются командой:

pt = PointTrack(x, y)
где x, y - числа (целые или вещественные). Если передается другой тип данных, то должно генерироваться исключение командой:

raise TypeError('координаты должны быть числами')
В классе PointTrack переопределите магический метод __str__, чтобы информация об объекте класса возвращалась в виде строки:

"PointTrack: <x>, <y>"

Например:

pt = PointTrack(1, 2)
print(pt) # PointTrack: 1, 2
В самом классе Track должно быть свойство (property) с именем:

points - для получения кортежа из точек маршрута.

Также в классе Track должны быть методы:

def add_back(self, pt) - добавление новой точки в конец маршрута (pt - объект класса PointTrack);
def add_front(self, pt) - добавление новой точки в начало маршрута (pt - объект класса PointTrack);
def pop_back(self) - удаление последней точки из маршрута;
def pop_front(self) - удаление первой точки из маршрута."""


class PointTrack:
    def __init__(self, x, y):
        if not all(map(lambda coord: type(coord) in (int, float), (x, y))):
            raise TypeError('координаты должны быть числами')
        self._x = x
        self._y = y

    def __str__(self):
        return f"PointTrack: {self._x}, {self._y}"


class Track:
    def __init__(self, *args):
        self._points = []
        if all(map(lambda x: type(x) in (int, float), args)):
            self._points.append(PointTrack(*args))
        else:
            list(map(lambda point_tr_obj: self._points.append(point_tr_obj), args))

    @property
    def points(self):
        return tuple(self._points)

    def add_back(self, pt):
        self._points.append(pt)

    def add_front(self, pt):
        self._points.insert(0, pt)

    def pop_back(self):
        self._points.pop()

    def pop_front(self):
        self._points = self._points[1:]
