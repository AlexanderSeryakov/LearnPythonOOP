"""Вам поручается создать программу по учету книг (библиотеку). Для этого необходимо в программе объявить два класса:

Lib - для представления библиотеки в целом;
Book - для описания отдельной книги.

Объекты класса Book должны создаваться командой:

book = Book(title, author, year)
где title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).

Объекты класса Lib создаются командой:

lib = Lib()
Каждый объект должен содержать локальный публичный атрибут:

book_list - ссылка на список из книг (объектов класса Book). Изначально список пустой.

Также объекты класса Lib должны работать со следующими операторами:

lib = lib + book # добавление новой книги в библиотеку
lib += book

lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book

lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= indx
При реализации бинарных операторов + и - создавать копии библиотек (объекты класса Lib) не нужно.

Также с объектами класса Lib должна работать функция:

n = len(lib) # n - число книг
которая возвращает число книг в библиотеке."""


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Book):
            self.book_list.remove(other)
        else:
            self.book_list.pop(other)
        return self

    def __len__(self):
        return len(self.book_list)


lib = Lib()

lib = lib + Book('Процесс', 'Кафка', 2020) # добавление новой книги в библиотеку

lib += Book('Три товарища', 'Ремарк', 2021)

lib += Book('Бесы', 'Достоевский', 2022)

lib += Book('1984', 'Оруэлл', 2022)

lib -= 1

print(lib.book_list)
