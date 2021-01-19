import itertools
import time

class TrafficLight:
    __color: str
    __time: dict

    def __init__(self, red_time, yellow_time, green_time):
        self.__time = {"red": red_time, "yellow": yellow_time, "green": green_time}

    def run(self):
        for mode, timer in itertools.cycle(self.__time.items()):
            self.__color = mode

            for second in range(timer):
                print(f" {self} [{second + 1}] ")
                time.sleep(1)

    def __repr__(self):
        return f" Work time = {self.__color} "

col_gr = int(input("Input work-time to green: "))

traffic_work = TrafficLight(7,2,col_gr)
traffic_work.run()


