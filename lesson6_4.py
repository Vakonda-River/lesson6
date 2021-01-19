class Car:
    speed: float
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed: float, color: str, name: str,) -> None:
        self.speed = speed
        self.color = color
        self.name = name
        self.over_s = ' Over speed'
        self.place = ' near the pump'

    def go(self):
        print(f"{self.name}: start")

    def stop(self):
        print(f"{self.name}: stop {self.place}")

    def turn(self, direction: str):
        print(f"{self.name}: turn to the {direction}")

    def show_speed(self):
        print(f"{self.name}: speed = {self.speed} km/h")

    def show_color(self):
        print(f"{self.color}")

    def polis(self):
        print(f"{self.name}: Police car")

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.name}({self.color}):{self.over_s} ")

class SportCar(Car):
    def show_speed(self):
        print(f"{self.name}({self.color}) ")

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.name}({self.color}):{self.over_s}")

class PoliceCar(Car):
    is_police: bool = True
    if is_police:
        def show_speed(self):
            print(f"{self.name}({self.color}): Police car")

cars = [
    TownCar(100, 'silver', 'Kia'),
    SportCar(200, 'red', 'Audi'),
    WorkCar(70, 'white', 'Golf'),
    PoliceCar(100, 'black', 'Ford'),
]

cars[0].go()
cars[0].turn(" left")
cars[1].go()
cars[3].turn(" right")
cars[2].stop()

for car in cars:
    car.show_speed()

