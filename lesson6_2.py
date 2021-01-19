class Road:
    __mass: float = 25
    _length: float
    _width: float

    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width
        self._name = 'Asphalt voiume'

    def calculate(self, depth):
        return (self._length * self._width * self.__mass * depth) / 1000

    def name(self):
        self.name = 'Asphalt voiume ='
        return f"{self.name} "

road = Road(20, 5000)
calculation = road.calculate(5)
name_r = road.name()
print(f"{name_r}{calculation} tonns")

