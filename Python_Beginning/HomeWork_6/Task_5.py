class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Draw has been started")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Pen draw has been started - " + self.title)


objPen = Pen("Pen")
objPen.draw()