"""Необходимо объявить функцию-декоратор class_log для класса, которая бы создавала логирование вызовов методов класса.
Например следующие строчки программы:

vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value
декорируют класс Vector и в список vector_log добавляются имена методов, которые были вызваны при использовании этого
класса. В частности, после выполнения команд:

v = Vector(1, 2, 3)
v[0] = 10
в списке vector_log должны быть два метода:

['__init__', '__setitem__']

Ваша задача реализовать декоратор с именем class_log."""


def class_log(lst):
    def log_methods(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, log_method_decorator(v))

        return cls

    def log_method_decorator(func):
        def wrapper(*args, **kwargs):
            lst.append(func.__name__)
            return func(*args, **kwargs)
        return wrapper

    return log_methods


vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value
