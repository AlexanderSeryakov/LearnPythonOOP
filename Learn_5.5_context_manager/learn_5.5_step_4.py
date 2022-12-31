"""Вам поручено разработать класс DatabaseConnection для управления подключением к базе данных. Объекты этого класса
создаются командой:

conn = DatabaseConnection()

В самом классе необходимо объявить метод:

def connect(self, login, password): ...

для подключения к БД. В данной реализации этот метод должен устанавливать локальный атрибут _fl_connection_open в
значение True:

_fl_connection_open = True

и генерировать исключение с помощью собственного класса ConnectionError унаследованного от базового класса Exception.

Также в классе DatabaseConnection должен быть метод:

def close(self): ...

для закрытия соединения. В этом методе нужно атрибут _fl_connection_open установить в значение False.

Метод close() необходимо вызывать всякий раз после завершения работы с БД, вне зависимости от того,
произошли какие-либо исключения или нет.

Этот функционал (автоматическое закрытие соединения с БД) предполагается реализовывать посредством менеджера контекста
 с использованием класса DatabaseConnection следующим образом:

with DatabaseConnection() as conn:
    # операторы менеджера контекста
Пропишите дополнительно в классе DatabaseConnection необходимые магические методы для такого его использования
совместно с оператором with.

P.S. В программе нужно объявить только класс. На экран ничего выводить не нужно."""


class DatabaseConnection:
    def __init__(self):
        self._fl_connection_open = False

    def connect(self, login, password):
        self._fl_connection_open = True
        raise ConnectionError

    def close(self):
        self._fl_connection_open = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False


c = DatabaseConnection()

try:
    c.connect('aaa', 'bbb')
except ConnectionError:
    assert c._fl_connection_open
else:
    assert False, "не сгенерировалось исключение ConnectionError"

try:
    with DatabaseConnection() as conn:
        conn.connect('aaa', 'bbb')
except ConnectionError:
    assert True
else:
    assert False, "не сгенерировалось исключение ConnectionError"

assert conn._fl_connection_open == False, "атрибут _fl_connection_open принимает значение True, а должно быть False"
