"""Объявите в программе класс FloatValidator, объекты которого создаются командой:

fv = FloatValidator(min_value, max_value)
где min_value, max_value - минимальное и максимальное допустимое значение (диапазон [min_value; max_value]).

Объекты этого класса предполагается использовать следующим образом:

fv(value)
где value - проверяемое значение. Если value не вещественное число или не принадлежит диапазону [min_value; max_value],
то генерируется исключение командой:

raise ValueError('значение не прошло валидацию')

По аналогии, объявите класс IntegerValidator, объекты которого создаются командой:

iv = IntegerValidator(min_value, max_value)

и используются командой:

iv(value)

Здесь также генерируется исключение:

raise ValueError('значение не прошло валидацию')

если value не целое число или не принадлежит диапазону [min_value; max_value].

После этого объявите функцию с сигнатурой:

def is_valid(lst, validators): ...

где lst - список из данных; validators - список из объектов-валидаторов
(объектов классов FloatValidator и IntegerValidator).

Эта функция должна отбирать из списка все значения, которые прошли хотя бы по одному валидатору.
И возвращать новый список с элементами, прошедшими проверку."""


class Validator:
    _valid_type = None

    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    def __call__(self, value):
        if type(value) != self._valid_type or not self._min_value <= value <= self._max_value:
            raise ValueError('значение не прошло валидацию')
        return value


class FloatValidator(Validator):
    _valid_type = float


class IntegerValidator(Validator):
    _valid_type = int


def is_valid(lst, validators):
    def validate(validator, value):
        try:
            return validator(value)
        except ValueError:
            pass

    return [item for item in lst for validator in validators if validate(validator, item)]

