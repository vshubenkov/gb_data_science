from abc import ABC, abstractmethod

class AbstractClassClothes(ABC):
    @abstractmethod
    def CreationCost(self):
        pass


class ClsClothes(AbstractClassClothes):
    def __init__(self, type):
        self.type = type

    @property
    def CreationCost(self):
        pass


class ClsCoat(ClsClothes):
    def __init__(self, type, V):
        super().__init__(type)
        self.V = V

    @property
    def CreationCost(self):
        return self.V / 6.5 + 0.5


class ClsSuite(ClsClothes):
    def __init__(self, type, H):
        super().__init__(type)
        self.H = H

    @property
    def CreationCost(self):
        return 2 * self.H + 0.3


ObjCoat_1 = ClsCoat('coat', 20)
print(ObjCoat_1.CreationCost)

ObjSuite_1 = ClsSuite('suite', 20)
print(ObjSuite_1.CreationCost)

