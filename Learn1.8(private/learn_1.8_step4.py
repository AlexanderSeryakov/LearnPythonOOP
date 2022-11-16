"""Объявите класс с именем Money и определите в нем следующие переменные и методы:

- приватная локальная переменная money (целочисленная) для хранения количества денег (своя для каждого объекта класса Money);
- публичный метод set_money(money) для передачи нового значения приватной локальной переменной money (изменение выполняется только если метод check_money(money) возвращает значение True);
- публичный метод get_money() для получения текущего объема средств (денег);
- публичный метод add_money(mn) для прибавления средств из объекта mn класса Money к средствам текущего объекта;
- приватный метод класса check_money(money) для проверки корректности объема средств в параметре money (возвращает True, если значение корректно и False - в противном случае).

Проверка корректности выполняется по критерию: параметр money должен быть целым числом, больше или равным нулю."""

class Money:
    def __init__(self, money):
        self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()

    @classmethod
    def __check_money(cls, money):
        return type(money) == int and -1 < money

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120
print(m1, m2)
