class cls_road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_material(self, depth=5):
        self.__mass_const = 25
        return self._length * self._width * self.__mass_const * depth


obj_road = cls_road(1000, 6)
print(obj_road.mass_material(), "tons")
