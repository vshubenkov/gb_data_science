import time

class TrafficLight:

    def change_light(self, state="red"):
        if state == "red":
            self.__color = "red"
            self.print_state()
            time.sleep(1)
            self.change_light("yellow")
        elif state == "yellow":
            self.__color = "yellow"
            self.print_state()
            time.sleep(1)
            self.change_light("green")
        elif state == "green":
            self.__color = "green"
            self.print_state()
            time.sleep(1)
            self.change_light("red")

    def print_state(self):
        print(self.__color)

obj_light = TrafficLight()
obj_light.change_light()