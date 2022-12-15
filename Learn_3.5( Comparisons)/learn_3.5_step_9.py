class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def get_weight(self):
        return self.ro * self.volume

    @staticmethod
    def check_type(other):
        return other if isinstance(other, (int, float)) else other.get_weight()

    def __eq__(self, other):
        return self.get_weight() == self.__class__.check_type(other)

    def __gt__(self, other):
        return self.__class__.check_type(other) < self.get_weight()

    def __lt__(self, other):
        return self.__class__.check_type(other) > self.get_weight()

body1 = Body('Name', 5.5, 50)
body2 = Body('Cock', 10, 20)
print(body2.check_type(10))

print(body1 > body2)  # True, если масса тела body1 больше массы тела body2
print(body1 == body2) # True, если масса тела body1 равна массе тела body2
print(10 < body1)     # True, если масса тела body1 меньше 10
print(body2 == 5)    # True, если масса тела body2 равна 5
