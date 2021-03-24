import abc


class Cloths:
    def __init__(self, n):
        self.clothes_name = n

    @abc.abstractmethod
    def material_amount(self):
        pass


class Caot(Cloths):
