class ClsCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print("Car went", "Speed:" + str(self.speed))

    def stop(self):
        self.speed = 0
        print("Car stopped")

    def direction(self, direction):
        print("Car turned to the" + direction)

    def show_speed(self):
        print("Car speed:", self.speed)

class ClsTownCar(ClsCar):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            print("Car speed more than 60:" + str(self.speed))
        else:
            print("Car speed:" + str(self.speed))

class ClsWorkCar(ClsCar):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Car speed more than 40:" + str(self.speed))
        else:
            print("Car speed:" + str(self.speed))

class ClsSportCar(ClsCar):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class ClsPoliceCar(ClsCar):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class ClsPoliceCar(ClsCar):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


ObjTownCar = ClsTownCar(50, "Red", "Lada", False)
ObjTownCar.show_speed()
ObjTownCar.go(70)
ObjTownCar.show_speed()
ObjTownCar.stop()
ObjTownCar.show_speed()

print("===================")

ObjWorkCar = ClsWorkCar(20, "Red", "Lada", False)
ObjWorkCar.show_speed()
ObjWorkCar.go(70)
ObjWorkCar.show_speed()
ObjWorkCar.stop()
ObjWorkCar.show_speed()
