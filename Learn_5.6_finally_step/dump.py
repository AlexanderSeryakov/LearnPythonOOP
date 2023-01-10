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

            if self._tp == 1 and not (self._x + self._length < ship._x or ship._x + ship._length < self._x):
                # Проверяем Y-координату кораблей. Если Y + 1 одного корабля, строго меньше Y второго корабля,
                # то они точно не пересекаются по оси Y. А в прошлом условии мы уже проверили, что и по оси X
                # они также ТОЧНО не пересекаются. Выходит, если выполнение программы дойдет до этого блока,
                # значит корабли ТОЧНО не пересекаются.

                return not(self._y + 1 < ship._y or ship._y + 1 < self._y)
            # В данном случае имеем 2 корабля с вертикальной ориентацией. Для начала проверим, могут ли они
            # пересекаться или нет.
            # Если выражение self._y + self._length + 1 < ship._y or ship._y + ship._length + 1 < self._y
            # вернёт True, значит корабли ТОЧНО не пересекаются. А если False, то возможно пересечение.
            # Поэтому ставим not для перехода в следующий блок для доп.проверки.

            if self._tp == 2 and not (self._y + self._length < ship._y or ship._y + ship._length < self._y):
                # Блок с доп.проверкой кораблей с вертикальной ориентацией на их пересечение. Здесь получаем
                # окончательный результат, пересекаются корабли или нет. Если выражение в скобках выдаст True,
                # значит корабли ТОЧНО не пересекаются. А если False, ТОЧНО пересекаются. Нам же нужно вернуть True,
                # если есть пересечение, поэтому ставим not.

                return not(self._x + 1 < ship._x or ship._x + 1 < self._x)

        # Сюда мы попадаем в случае, если ориентации кораблей не равны (т.е кто-то горизонтальный, кто-то вертикальный)
        # и уточняем, что ориентация корабля, для которого запущена проверка - горизонтальная (self._tp == 1),
        # если это так, значит ориентация второго корабля вертикальная (ship._tp == 2).
        # В этом блоке идёт проверка сначала по Х, входит ли ship._x в диапазон недопустимых клеток для self._x,
        # и если это так, то сравниваются оси Y этих кораблей. В скобках проверяется, что корабли НЕ пересекаются,
        # поэтому ставим not. Ведь, если верны все предыдущие условия, то выражение в скобках точно определяет,
        # могут корабли пересекаться или нет.
        # В итоге получаем булево значение True - если они пересекаются.
        if self._tp == 1:
            if ship._x in range(self._x - 1, self._x + self._length + 1):
                return not (self._y + 1 < ship._y or ship._y + ship._length< self._y)
        if self._tp == 2:
            if self._x in range(ship._x - 1, ship._x + ship._length + 1):
                return not (self._y + self._length < ship._y or ship._y + 1 < self._y)
        return False

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


s1 = Ship(3, 2, 6, 2)
s2 = Ship(2, 1, 6, 6)
s3 = Ship(1, 1, 8, 1)
print(s1.is_collide(s3))  # False
print(s1.is_collide(s2))  # False
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"
