"""Объявите класс DateString для представления дат, объекты которого создаются командой:

date = DateString(date_string)
где date_string - строка с датой в формате:

"DD.MM.YYYY"

здесь DD - день (целое число от 1 до 31); MM - месяц (целое число от 1 до 12); YYYY - год (целое число от 1 до 3000).
Например:

date = DateString("26.05.2022")
или

date = DateString("26.5.2022") # незначащий ноль может отсутствовать
Если указанная дата в строке записана неверно (не по формату), то генерировать исключение с помощью собственного класса:

DateError - класс-исключения, унаследованный от класса Exception.

В самом классе DateString переопределить магический метод __str__() для формирования строки даты в формате:

"DD.MM.YYYY"

(здесь должны фигурировать незначащие нули, например, для аргумента "26.5.2022"
должна формироваться строка "26.05.2022")

Далее, в программе выполняется считывание строки из входного потока командой:

date_string = input()
Ваша задача создать объект класса DateString с аргументом date_string и вывести объект на экран командой:

print(date) # date - объект класса DateString
Если же произошло исключение, то вывести сообщение (без кавычек):

"Неверный формат даты"

Sample Input:

1.2.1812
Sample Output:

01.02.1812"""


class DateError(Exception):
    pass


class DateString:
    def __init__(self, date_string):
        self._date_lst = self._validate_data(date_string)

    def _validate_data(self, date_string):
        ds = [int(x) for x in date_string.split('.')]
        if len(ds) != 3 or not 1 <= ds[0] <= 31 or not 1 <= ds[1] <= 12 or not 1 <= ds[2] <= 3000:
            raise DateError('Invalid date-format. Correct format: DD.MM.YYYY')
        return ds

    def __str__(self):
        return f"{self._date_lst[0]:02}.{self._date_lst[1]:02}.{self._date_lst[2]:02}"

date_string = input()
try:
    print(DateString(date_string))
except DateError:
    print("Неверный формат даты")
