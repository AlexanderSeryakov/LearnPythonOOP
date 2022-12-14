"""Объявите класс Book со следующим набором сеттеров и геттеров:

set_title(self, title) - запись в локальное приватное свойство __title объектов класса Book значения title;
set_author(self, author) - запись в локальное приватное свойство __author объектов класса Book значения author;
set_price(self, price) - запись в локальное приватное свойство __price объектов класса Book значения price;
get_title(self) - получение значения локального приватного свойства __title объектов класса Book;
get_author(self) - получение значения локального приватного свойства __author объектов класса Book;
get_price(self) - получение значения локального приватного свойства __price объектов класса Book;

Объекты класса Book предполагается создавать командой:

book = Book(автор, название, цена)
При этом, в каждом объекте должны создаваться приватные локальные свойства:"""


class Book:
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


bk1 = Book('Л.Н. Толстой', 'Война и мир: том первый', 400)
print(bk1.title, bk1.author, bk1.price)  # Война и мир: том первый Л.Н. Толстой 400
bk1.title = ('Война и мир: том второй')
bk1.author = ('Л.Н. Толстой, С.А. Толстая')
bk1.price = (550)
print(bk1.title, bk1.author, bk1.price)  # Война и мир: том второй Л.Н. Толстой, С.А. Толстая 550
