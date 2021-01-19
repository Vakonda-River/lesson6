class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage,"bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}{self.position}"

    def get_total_income(self):
       return sum(self._income.values())

#---
one_w = 1000;two_w = 2000
one_b = 500;two_b = 4000
#---
one = Position("Vasilij", "Pupkin", ", (Driver) =",one_w, one_b)
print(one.get_full_name(), one.get_total_income())

two = Position("Isold", "Ivanov", ", (Speaker)  =", two_w, two_b)
print(two.get_full_name(), two.get_total_income())
