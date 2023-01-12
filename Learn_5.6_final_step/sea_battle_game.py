from random import randint, choice


class ConstCoords:
    """На уровне класса объявлены 3 атрибута: _neigh, _neigh_tp_1, _neigh_tp_2
    Минимальный набор соседних точек для кораблей на 1 палубу - _neigh,
    для вертикальных (tp=2) - _neigh_tp_2, для горизонтальных (tp=1) - _neigh_tp_1"""
    _neigh = (-1, -1), (0, -1), (1, -1), (-1, 0), (-1, 1), (1, 1), (0, 1), (1, 0)  # (x, y)
    _neigh_tp_1 = (-1, -1), (0, -1), (1, -1), (-1, 0), (-1, 1), (1, 1), (0, 1)
    _neigh_tp_2 = (-1, -1), (0, -1), (1, -1), (-1, 0), (-1, 1), (1, 1), (1, 0)


class Ship(ConstCoords):
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1] * self._length

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                if go == 1:
                    return tuple((self._length, i) for i in range(-1, 2))
                return tuple((- 2, i) for i in range(-1, 2))
            if self._tp == 2:
                if go == 1:
                    return tuple((i, -2) for i in range(-1, 2))
                return tuple((i, self._length + 1) for i in range(-1, 2))

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
                return not (self._y + 1 < ship._y or ship._y + 1 < self._y)

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
                return not (self._x + 1 < ship._x or ship._x + 1 < self._x)

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
                return not (self._y + 1 < ship._y or ship._y + ship._length < self._y)
        if self._tp == 2:
            if self._x in range(ship._x - 1, ship._x + ship._length + 1):
                return not (self._y + self._length < ship._y or ship._y + 1 < self._y)
        return False

    def is_out_pole(self, size):
        return not 0 <= self._x + self._length <= size if self._tp == 1 else not 0 <= self._y + self._length <= size


class GamePole(ConstCoords):
    """Класс, описывающий игровое поле. В его экземплярах происходит расстановка кораблей случ.образом,
    перемещение и т.д"""

    def __init__(self, size):
        self._size = size
        self._pole = [[0 for _ in range(self._size)] for _ in range(self._size)]

    """Функция, в которой происходит расстановка кораблей на игровом поле. 
    А также объявляется лок.атрибут(список) - self._ships, содержащий в себе корабли, 
    которые будут присутствовать на игровом поле"""

    def init(self):
        self._ships = [Ship(4, tp=randint(1, 2)) for j in range(1)] + [Ship(3, tp=randint(1, 2)) for j in range(2)] + \
                      [Ship(2, tp=randint(1, 2)) for j in range(3)] + [Ship(1, tp=randint(1, 2)) for j in range(4)]

        # Запускаем цикл со счётчиком n; С помощью него выбираем текущий корабль ship из списка self._ships.
        # Устанавливаем для него случайные начальные координаты в корректном диапазоне, далее считываем значения
        # координат в переменные х, у для удобства дальнейшего использования. Если длина корабля равна 1,
        # то проверяем на наличие другого корабля только точки из self._neigh, иначе определяем ориентацию
        # корабля (tp) и в зависимости от этого также задаем набор точек для проверки.
        n = 0
        while n < len(self._ships):
            ship = self._ships[n]
            ship.set_start_coords(randint(0, self._size - 1), randint(0, self._size - 1))

            # Проверяем, занята ли клетка с координатами, которые мы получили случайным образом.
            # Если занята - пропускаем шаг итерации и определяем новые координаты.
            if self._pole[ship._y][ship._x] == 1:
                continue
            x, y = ship.get_start_coords()
            if ship._length == 1:
                neighboring = self._neigh
            else:
                if ship._tp == 1:

                    # extreme_point_x - крайняя точка справа для горизонтальных кораблей,
                    # которую необходимо проверить на "Открытость".
                    # length_points - набор точек, расположенных вдоль корабля
                    # по всей его длине на единицу выше или ниже от у корабля.
                    # neighboring - итоговый список точек для конкретного корабля, у которых проверяем "Открытость".
                    # Оборачиваем всё это в set, чтобы избежать дублирования координат.
                    extreme_point_x = ((ship._length, 0),)
                    length_points = tuple((1 + i, n) for i in range(ship._length) for n in (-1, 1))
                    neighboring = set(self._neigh_tp_1 + length_points + extreme_point_x)
                else:
                    extreme_point_y = ((0, ship._length),)
                    length_points = tuple((n, 1 + i) for i in range(1, ship._length) for n in (-1, 1))
                    neighboring = set(self._neigh_tp_2 + length_points + extreme_point_y)

            # проходимся по всем соседним
            # клеткам на всей длине корабля и проверяем, пустые ли они. Если хотябы в одной клетке будет единица,
            # то сумма будет больше 0, тогда условие станит истинным и мы пропустим один шаг итерации.
            # Т.е в этом месте корабль мы не можем разместить, поэтому будут выбраны другие координаты на след. шаге.
            if sum((self._pole[y + j][x + i] for i, j in neighboring
                    if 0 <= y + j < self._size and 0 <= x + i < self._size)) > 0:
                continue

            # Проверяем, не выйдет ли наш корабль за пределы игрового поля.
            # И если не выходит, то "Ставим" корабль на поле.
            if ship._tp == 1:
                if self._size < x + ship._length:
                    continue
                else:
                    self._pole[y][x: x + ship._length] = ship._cells
            else:
                if self._size < y + ship._length:
                    continue
                else:
                    for i in range(ship._length):
                        self._pole[y + i][x] = ship._cells[i]
            n += 1

    def move_ships(self):
        n = 0
        if n:
            for ship in self._ships:
                go = choice([-1, 1])
                coords = ship.move(go)
                x, y = ship.get_start_coords()
                if sum((self._pole[y + j][x + i] for i, j in coords
                        if 0 <= y + j < self._size and 0 <= x + i < self._size)) == 0:
                    if ship._tp == 1 and go == 1:
                        ship._cells.insert(0, 0)
                        self._pole[y][x: x + len(ship._cells)] = ship._cells
        else:
            return

    def show(self):
        for row in self._pole:
            print(row)

    def get_ships(self):
        return self._ships

    def get_pole(self):
        return tuple(tuple(row) for row in self._pole)


#pole = GamePole(8)
#pole.init()
#pole.show()
#pole.move_ships()
#print()
#pole.show()

#s1 = Ship(3, 2, 6, 2)
#s2 = Ship(2, 1, 6, 6)
#s3 = Ship(1, 1, 8, 1)
#print(s1.is_collide(s3))  # False
#print(s1.is_collide(s2))  # False
ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"

ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(
    s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

pole_size_8 = GamePole(8)
pole_size_8.init()
