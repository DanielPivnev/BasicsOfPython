def val_cheker(x):
    def _logger(func):
        def wrapper(*args):
            result = args[0]
            if x > 0 and result > 0:
                result = func(result)
                return result
            else:
                raise ValueError
        return wrapper
    return _logger


@val_cheker(x=1)
def calc_cube(x):
    return x**3


print(calc_cube(4))
