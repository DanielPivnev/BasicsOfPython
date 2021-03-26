class ComplexNumber:
    def __init__(self, a, bi):
        self.a = a
        self.bi = bi

    def __add__(self, other):
        return [self.a + other.a, self.bi + other.bi]

    def __mul__(self, other):
        return [self.a * other.a, self.bi * other.bi]


complex_num1 = ComplexNumber(5, 7)
complex_num2 = ComplexNumber(7, 9)
result = complex_num1*complex_num2
print(f'({complex_num1.a} + {complex_num1.bi}i) * ({complex_num2.a} + {complex_num2.bi}i) = {result[0]} + {result[1]}i')
result = complex_num1+complex_num2
print(f'{complex_num1.a} + {complex_num1.bi}i + {complex_num2.a} + {complex_num2.bi}i = {result[0]} + {result[1]}i')