class Stationary:
    def __init__(self, t, d):
        self.title = t
        self.draw = d

    def drawing(self):
        print(f'Отрисовка началась, вы рисуети {self.title} {self.draw}')


class Pen(Stationary):
    def drawing(self):
        print(f'Отрисовка началась, вы рисуети корандашом {self.title} {self.draw}. '
              f'У вас это подучается рслвать корондашом красиво')


class Pencil(Stationary):
    def drawing(self):
        print(f'Отрисовка началась, вы выбрали карадаш {self.title} и рисунте {self.draw}. '
              f'У вас это подучается прекрасно')


class Handle(Stationary):
    def drawing(self):
        print(f'Отрисовка началась, у вас в руках маркер {self.title} и ваш стиль рисование {self.draw}. '
              f'У вас это подучается прекрасна')


hadle1 = Handle('Масте1', 'Натурализм')
pencil1 = Pencil('Castel', 'Яблоко')
pen1 = Pen('абвгд', 'Машину')
pen1.drawing()
hadle1.drawing()
pencil1.drawing()
