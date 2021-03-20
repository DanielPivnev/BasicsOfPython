class Worker:
    def __init__(self,n, sn, p, w):
        self.name = n
        self.surename = sn
        self.position = p
        self._income = {
            'wage': w,
            'bonus': 0
        }


class Position(Worker):
    def get_total_income(self, bonus):
        self._income['bonus'] = bonus
        print(self._income['wage'] + self._income['bonus'])

    def get_full_name(self):
        print(f'{self.name} {self.surename}')


worker1 = Position('Vladimir', 'Pivnev', 'Chef', 1000000000)
worker1.get_total_income(21000000000)
worker1.get_full_name()
