import time


class TrafficLight:
    __color = 'red'

    def start_traffic(self):
        print(self.__color)
        start1 = time.perf_counter()
        start2 = time.perf_counter()
        start3 = time.perf_counter()
        start4 = time.perf_counter()

        while True:
            if start1 - time.perf_counter() <= -7 and start1 - time.perf_counter() > -7.001:
                self.__color = 'yellow'
                print(self.__color)
                start1 = 0
            if start2 - time.perf_counter() <= -9 and start2 - time.perf_counter() > -9.001:
                self.__color = 'green'
                print(self.__color)
                start2 = 0
            if start4 - time.perf_counter() <= -16 and start4 - time.perf_counter() >= -16.001:
                self.__color = 'yellow'
                print(self.__color)
                start4 = 0
            if start3 - time.perf_counter() <= -18 and start3 - time.perf_counter() >= -18.001:
                self.__color = 'red'
                print(self.__color)
                start1 = time.perf_counter()
                start2 = time.perf_counter()
                start3 = time.perf_counter()
                start4 = time.perf_counter()


light1 = TrafficLight()
light1.start_traffic()
