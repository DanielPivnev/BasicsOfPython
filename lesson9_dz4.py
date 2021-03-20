class Car:
    def __init__(self, s, c, n, p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p

    def go(self):
        print('Go-go')

    def stop(self):
        print('stop')

    def turn(self, d):
        print(f'Your turned to {d} directiion')

    def show_speed(self):
        print(f'{self.speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы привысили скорость, ваша скорость {self.speed}')
        else:
            print(f'{self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы привысили скорость, ваша скорость {self.speed}')
        else:
            print(f'{self.speed}')


