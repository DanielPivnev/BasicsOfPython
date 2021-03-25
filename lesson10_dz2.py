import abc


class Clothes:
    def __init__(self, n):
        self.clothes_name = n

    @abc.abstractmethod
    def material_amount(self, x):
        pass


class Coat(Clothes):
    def material_amount(self, v):
        return v/6.5+0.5


class Costume(Clothes):
    def material_amount(self, h):
        return 2*h+0.3


a = Costume('Mike')
b = a.material_amount(16)
print(b)
c = Coat('abc')
d = c.material_amount(28)
print(d)
