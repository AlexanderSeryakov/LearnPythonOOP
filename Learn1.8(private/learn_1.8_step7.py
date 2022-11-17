""" Объявите класс Line для описания линии на плоскости, объекты которого предполагается создавать командой:

line = Line(x1, y1, x2, y2)
При этом в объекте line должны создаваться следующие приватные локальные свойства:

__x1, __y1 - начальная координата;
__x2, __y2 - конечная координата.

В самом классе Line должны быть реализованы следующие сеттеры и геттеры:

set_coords(self, x1, y1, x2, y2) - для изменения координат линии;
get_coords(self) - для получения кортежа из текущих координат линии.

А также метод:

draw(self) - для отображения в консоли списка текущих координат линии (в одну строчку через пробел)."""


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1, self.__y1 = x1, y1
        self.__x2, self.__y2 = x2, y2

    def set_coords(self, x1, y1, x2, y2):
        self.__x1, self.__y1 = x1, y1
        self.__x2, self.__y2 = x2, y2

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(*[x for x in self.get_coords()])

l1 = Line(1, 1, 2, 3)
print(l1.get_coords())
l1.draw()
