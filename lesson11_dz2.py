import traceback


class ZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    number1 = float(input('Enter the first number for the division: '))
    number2 = float(input('Enter the second number for the division: '))
    if number1 == 0 or number2 == 0:
        raise ZeroDivision('You cannot divide by zero')
    result = number1/number2
except ValueError as v_err:
    print('Enter please the next time a  just number.', traceback.format_exc())
except ZeroDivision as z_err:
    print(z_err)
else:
    print(f'The result is: {result}')
