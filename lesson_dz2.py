class Road:
    def __init__(self, w, l):
        self._weidth = w
        self._length = l

    def asphalt_mass_pro_quadrat_meter(self):
        print(1 * 1 * 25 * 0.01, 'T')

    def asphalt_all_mass(self):
        print(self._length * self._weidth * 25 * 0.01, 'T')


road1 = Road(250, 10)
road1.asphalt_mass_pro_quadrat_meter()
road1.asphalt_all_mass()
