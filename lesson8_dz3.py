def type_logger(func):
    def wrapper(*args):
        x = args[0]
        m = f'{x}: {type(x)}'
        return m
    return wrapper


@type_logger
def calc_cube(x):
    return x**3


print(calc_cube(5))
