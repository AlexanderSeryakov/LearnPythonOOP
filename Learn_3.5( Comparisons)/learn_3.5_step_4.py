class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            object.__setattr__(self, key, value)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    def get_volume(self):
        return self.a*self.b*self.c

    def __gt__(self, other):
        return self.get_volume() > other.get_volume()

    def __ge__(self, other):
        return self.get_volume() >= other.get_volume()


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)), ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)), ShopItem('табуретка', 2000.99,
                                                                                  Dimensions(500, 200, 200))]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)

assert len(lst_shop) == 4, "число элементов в lst_shop не равно 4"

lst_sp = []
lst_sp.append(ShopItem('кеды', 1024, Dimensions(40, 30, 120)))
lst_sp.append(ShopItem('зонт', 500.24, Dimensions(10, 20, 50)))
lst_sp.append(ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)))
lst_sp.append(ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200)))

lst_sp_sorted = ['зонт', 'кеды', 'табуретка', 'холодильник']
s = [x.name for x in lst_shop_sorted]
assert lst_sp_sorted == s, "список lst_shop_sorted сформирован неверно"

d1 = Dimensions(40, 30, 120)
d2 = Dimensions(40, 30, 120)
d3 = Dimensions(30, 20, 100)
assert d1 <= d2, "неверно отработал оператор <="
assert d3 <= d2, "неверно отработал оператор <="
assert d3 < d2, "неверно отработал оператор <"

d2.a = 10
d2.b = 10
d2.c = 10
assert d2 < d1, "неверно отработал оператор < после изменения объема через объекты-свойства a, b, c"
