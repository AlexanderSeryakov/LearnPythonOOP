"""Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса должны создаваться командой:

dt = DeltaClock(clock1, clock2)
где clock1, clock2 - объекты другого класса Clock для хранения текущего времени. Эти объекты должны создаваться командой:

clock = Clock(hours, minutes, seconds)
где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные числа).

В классе Clock также должен быть (по крайней мере) один метод (возможны и другие):

get_time() - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).

После создания объекта dt класса DeltaClock, с ним должны выполняться команды:

str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
Если разность получается отрицательной, то разницу времен считать нулевой.

Пример использования классов (эти строчки в программе писать не нужно):

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
Обратите внимание, добавляется незначащий ноль, если число меньше 10."""


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.time = hours*3600 + minutes*60 + seconds

    def get_time(self):
        return self.time


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.time_1 = clock1.get_time()
        self.time_2 = clock2.get_time()

    def get_delta(self):
        return self.time_1 - self.time_2

    def __str__(self):
        hour = self.get_delta() // 3600
        minutes = (self.get_delta() - hour*3600) // 60
        seconds = self.get_delta() - hour*3600 - minutes*60
        return f"{hour:02}: {minutes:02}: {seconds:02}" if 0 < self.get_delta() else f"00: 00: 00"

    def __len__(self):
        return self.get_delta()

dt = DeltaClock(Clock(2, 45, 0), Clock(10, 15, 0))
print(dt)

