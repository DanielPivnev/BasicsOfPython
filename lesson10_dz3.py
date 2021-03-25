class Cell:
    def __init__(self, n):
        self.cell_number = n

    def __mul__(self, other):
        return self.cell_number * other.cell_number

    def __truediv__(self, other):
        return round(self.cell_number / other.cell_number)

    def __add__(self, other):
        return self.cell_number + other.cell_number

    def __sub__(self, other):
        return self.cell_number - other.cell_number if self.cell_number > other.cell_number else 'Вычитание ' \
                                                                                                       'невозможно ' \
                                                                                                       'так как ' \
                                                                                                       'резултат ' \
                                                                                                       'меньше нуля'

    @staticmethod
    def make_order(cell_number, cell_in_a_line):
        a = cell_number // cell_in_a_line
        b = cell_number % cell_in_a_line
        txt = ''
        while a > 0:
            for _ in range(cell_in_a_line):
                txt += '*'
            txt += '\n'
            a -= 1
        for _ in range(b):
            txt += '*'

        return txt


a = Cell(15000)
b = Cell(2000)
print(a + b)
print(a * b)
print(a - b)
print(a / b)

b = Cell(20000)
print(a - b)

print(Cell.make_order(100, 10))
