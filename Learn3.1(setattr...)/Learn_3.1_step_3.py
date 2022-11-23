"""Объявите класс Book для представления информации о книге. Объекты этого класса должны создаваться командами:

book = Book()
book = Book(название, автор, число страниц, год издания)
В каждом объекте класса Book автоматически должны формироваться следующие локальные свойства:

title - заголовок книги (строка, по умолчанию пустая строка);
author - автор книги (строка, по умолчанию пустая строка);
pages - число страниц (целое число, по умолчанию 0);
year - год издания (целое число, по умолчанию 0).

Объявите в классе Book магический метод __setattr__ для проверки типов присваиваемых данных локальным свойствам title,
author, pages и year. Если типы не соответствуют локальному атрибуту (например, title должна ссылаться на строку,
а pages - на целое число), то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
Создайте в программе объект book класса Book для книги:

автор: Сергей Балакирев
заголовок: Python ООП
pages: 123
year: 2022"""


class Book:
    def __init__(self, title='', author='', page=0, year=0):
        self.title = title
        self.author = author
        self.page = page
        self.year = year

    def get_error(self):
        raise TypeError("Неверный тип присваиваемых данных.")

    def __setattr__(self, key, value):
        if key in ('title', 'author'):
            return object.__setattr__(self, key, value) if type(value) == str else self.get_error()
        if key in ('page', 'year'):
            return object.__setattr__(self, key, value) if type(value) == int else self.get_error()


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
