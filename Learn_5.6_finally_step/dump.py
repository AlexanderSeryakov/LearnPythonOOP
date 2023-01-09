from random import randint


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1] * self._length

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            if self._tp == 2:
                self._y += go

    def set_start_coords(self, x, y):
        self._x, self._y = x, y

    def get_start_coords(self):
        return self._x, self._y

    def is_collide(self, ship):
        if self._tp == ship._tp:
            # В этом блоке идёт, если выражение в скобках даёт True, то корабли ТОЧНО не пересекаются,
            # а если False, то возможно пересечение, поэтому ставлю not,
            # чтобы при False перейти внутрь условия для доп.проверки
            if self._tp == 1 and not (self._x + self._length + 1 < ship._x or ship._x + ship._length + 1 < self._x):
                return  # Тут должна быть проверка на пересечение по у
            if self._tp == 2 and not (self._y + self._length + 1 < ship._y or ship._y + ship._length + 1 < self._y):
                return  # Тут должна быть проверка на пересечение по у
        # В этом блоке идёт проверка сначала по Х, входит ли Х ship в диапазон недопустимых клеток для self._x,
        # и если это так, то сравниваются оси Y этих кораблей. В скобках проверяется, что корабли НЕ пересекаются,
        # поэтому ставим not. Ведь, если верны все предыдущие условия, то выражение в скобках точно определяет,
        # могут корабли пересекаться или нет.
        # В итоге получаем булево значение True - если они пересекаются.
        if self._tp == 1:
            if ship._x in range(self._x - 1, self._x + self._length + 2):
                return not (self._y + 1 < ship._y or ship._y + ship._length + 1 < self._y)

    def is_out_pole(self, size):
        return not 0 <= self._x + self._length < size if self._tp == 1 else not 0 <= self._y + self._length < size


class GamePole:
    """Класс, описывающий игровое поле. В его экземплярах происходит расстановка кораблей случ.образом,
    перемещение и т.д
    На уровне класса объявлены 3 атрибута: _neigh, _neigh_tp_1, _neigh_tp_2
    Минимальный набор соседних точек для кораблей на 1 палубу - _neigh,
    для вертикальных (tp=2) - _neigh_tp_2, для горизонтальных (tp=1) - _neigh_tp_1"""
    _neigh = (-1, -1), (0, -1), (1, -1), (-1, 0), (-1, 1), (1, 1), (0, 1), (1, 0)  # (x, y)
    _neigh_tp_1 = (-1, -1), (0, -1), (1, -1), (-1, 0), (-1, 1), (1, 1), (0, 1)
    _neigh_tp_2 = (-1, -1), (0, -1), (1, -1), (-1, 0), (-1, 1), (1, 1), (1, 0)

    def __init__(self, size):
        self._size = size
        self._pole = [[0 for _ in range(self._size)] for _ in range(self._size)]

    """Функция, в которой происходит расстановка кораблей на игровом поле. 
    А также объявляется лок.атрибут(список) - self._ships, содержащий в себе корабли, 
    которые будут присутствовать на игровом поле"""
    def init(self):
        self._ships = [Ship(4, tp=randint(1, 2)) for j in range(1)] + [Ship(3, tp=randint(1, 2)) for j in range(2)] + \
                      [Ship(2, tp=randint(1, 2)) for j in range(3)] + [Ship(1, tp=randint(1, 2)) for j in range(4)]
        n = 0
        while n < len(self._ships):
            ship = self._ships[n]
            ship.set_start_coords(randint(0, self._size - 1), randint(0, self._size - 1))
            x, y = ship.get_start_coords()
            if ship._length == 1:
                neighboring = self._neigh
            else:
                if ship._tp == 1:
                    neighboring = self._neigh_tp_1 + tuple((ship._length, i) for i in range(-1, 2))
                else:
                    neighboring = self._neigh_tp_2 + tuple((n, 1 + i) for n in (-1, 1) for i in range(1, 3))
            if self._pole[y][x] == 1 or sum((self._pole[y + j][x + i] for i, j in neighboring
                                             if 0 <= y + j < self._size and 0 <= x + i < self._size)) > 0:
                continue
            if ship._tp == 1:
                if x + ship._length > self._size - 1:
                    continue
                self._pole[y][x: x + ship._length] = ship._cells
            else:
                if y + ship._length > self._size - 1:
                    continue
                for i in range(ship._length):
                    self._pole[y + i][x] = ship._cells[i]
            n += 1

    def draw(self):
        for row in self._pole:
            print(row)


pole = GamePole(10)
pole.init()

s1 = Ship(4, 1, 1, 5)
s2 = Ship(3, 2, 3, 1)
print(s1.is_collide(s2))  # True
