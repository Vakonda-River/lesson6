class Stationery:
    title: str
    _message = "Start draw."

    def draw(self):
        print(self._message)

class Pencil(Stationery):
    title = 'Pen'
    _message = f"{title} - draw on the paper."

class Pen(Stationery):
    title = 'Pencil'
    _message = f"{title} - draw in the work book."

class Handle(Stationery):
    title = 'Handle'
    _message = f"{title} - draw on the desk."


items = [Pencil(), Pen(), Handle()]
for item in items:
    item.draw()
