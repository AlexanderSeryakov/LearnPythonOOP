"""Объявите класс PrimaryKey, который должен работать совместно с менеджером контекста следующим образом:

with PrimaryKey() as pk:
    raise ValueError

где pk - ссылка на объект класса PrimaryKey.
Класс PrimaryKey должен в момент входа в менеджер контекста выводить
на экран сообщение "вход", а при завершении работы менеджера контекста выводить тип возникшего исключения.

Класс PrimaryKey следует реализовать так, чтобы менеджер контекста сам обрабатывал возникшее исключение."""


class PrimaryKey:
    def __enter__(self):
        print("вход")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)

        return True

with PrimaryKey() as pk:
    raise ValueError
