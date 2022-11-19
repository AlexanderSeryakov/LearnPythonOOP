""" Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:

em = EmailValidator() # None
В самом классе реализовать следующие методы класса (@classmethod):

get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False"""

from random import randint as rdi


class EmailValidator:
    __CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._@'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        email_1 = ''
        for i in range(rdi(1, 101)):
            index = rdi(0, len(cls.__CHARS) - 2)
            email_1 += cls.__CHARS[index]
        return email_1 + '@gmail.com'

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            type_check = all(map(lambda x: x in cls.__CHARS, email))  # True/False
            at_count = email.count('@')  # must be 1
            len_check = len(email.split('@')[0]) < 101 and len(email.split('@')[1]) < 51 and 0 < email.split('@')[1].count(
                '.') if len(email.split('@')) > 1 else False
            double_dot_count = email.count('..')
            return type_check and at_count == 1 and len_check and not double_dot_count
        return False

    @staticmethod
    def __is_email_str(email):
        return type(email) == str




