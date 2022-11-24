class Point:
    def __set_name__(self, owner, name):
        self.name = '__'+name
        self.min = owner.MIN_DIMENSION
        self.max = owner.MAX_DIMENSION

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.min <= value <= self.max:
            setattr(instance, self.name, value)


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    a = Point()
    b = Point()
    c = Point()
    d = Point()
    key = Point()

    def __init__(self, a, b, c, d, key):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.key = key

    def __setattr__(self, key, value):
        if key in ['MIN_DIMENSION', 'MAX_DIMENSION']:
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        super().__setattr__(key, value)


dm = Dimensions(50, 70, 10, 90, 150)


print(dm.__dict__)
