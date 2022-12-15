class Box:
    def __init__(self):
        self.items = []

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items):
        self.__items = items

    def add_thing(self, obj):
        self.items.append(obj)

    def get_things(self):
        return self.items

    def __eq__(self, other):
        if len(self.items) == len(other.items):
            lst1 = sorted(self.items)
            lst2 = sorted(other.items)
            res_lst = [item_1 for item_1 in lst1 for item_2 in lst2 if item_1 == item_2]
            return len(res_lst) == len(lst1)
        return False


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, mass):
        self.__mass = mass

    def __eq__(self, other):
        return (self.name.lower(), self.mass) == (other.name.lower(), other.mass)

    def __lt__(self, other):
        return self.mass < other.mass

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('МЕЛ', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
print(res)


