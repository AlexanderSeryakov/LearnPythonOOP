""" Объявите в программе класс MailBox (почтовый ящик), объекты которого создаются командой:

mail = MailBox()
Каждый объект этого класса должен содержать локальный публичный атрибут:

inbox_list - список из принятых писем.

Также в классе MailBox должен присутствовать метод:

receive(self) - прием новых писем

Этот метод должен читать данные из входного потока командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
В результате формируется список lst_in из строк. Каждая строка записана в формате:

"от кого; заголовок; текст письма"

Например:

sc_lib@list.ru; От Балакирева; Успехов в IT!
mail@list.ru; Выгодное предложение; Вам одобрен кредит.
mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.

Каждая строчка списка lst_in должна быть представлена объектом класса MailItem, объекты которого создаются командой:

item = MailItem(mail_from, title, content)
где mail_from - email отправителя (строка); title - заголовок письма (строка), content - содержимое письма (строка).
В каждом объекте класса MailItem должны формироваться соответствующие локальные атрибуты
(с именами: mail_from, title, content). И дополнительно атрибут is_read (прочитано ли) с начальным значением False.

В классе MailItem должен быть реализован метод:

set_read(self, fl_read) - для отметки, что письмо прочитано (метод должен устанавливать атрибут is_read = fl_read,
если True, то письмо прочитано, если False, то не прочитано).

С каждым объектом класса MailItem должна работать функция:

bool(item)
которая возвращает True для прочитанного письма и False для непрочитанного.

Вызовите метод:

mail.receive()
Отметьте первое и последнее письмо в списке mail.inbox_list, как прочитанное (используйте для этого метод set_read).
Затем, сформируйте в программе список (глобальный) с именем inbox_list_filtered из прочитанных писем,
используя стандартную функцию filter() совместно с функцией bool() языка Python.

P.S. На экран ничего выводить не нужно.

Sample Input:

sc_lib@list.ru; От Балакирева; Успехов в IT!
mail@list.ru; Выгодное предложение; Вам одобрен кредит.
mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить."""

import sys


class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        lst_in = [MailItem(*x.split('; ')) for x in lst_in]
        self.inbox_list = self.inbox_list + lst_in


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)

inbox_list_filtered = list(filter(bool, mail.inbox_list))

assert len(inbox_list_filtered) == 2, 'Неверно создан список inbox_list_filtered'
assert inbox_list_filtered[0].is_read, 'Неверно установлен статус о прочтении письма'

assert mail.inbox_list[-1].is_read, 'Неверно отрабатывает метод set_read'
assert not mail.inbox_list[1].is_read, 'Неверно отрабатывает метод set_read'

assert mail.inbox_list[1].title == 'Выгодное предложение', 'Неверно отрабатывает метод receive'
