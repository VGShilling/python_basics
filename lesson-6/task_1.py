from time import sleep
from itertools import count


class TrafficLight:
    def __init__(self):
        self.__color = 'красный'

    def running(self):
        run_dict = {'красный': 7, 'желтый': 2, 'зеленый': 10}
        for key, value in run_dict.items():
            self.__color = key
            print(f'Горит {self.__color}')
            for el in count(1):
                if el > value:
                    break
                else:
                    print(el)
                    sleep(1)


traffic_lights = TrafficLight()
traffic_lights.running()
