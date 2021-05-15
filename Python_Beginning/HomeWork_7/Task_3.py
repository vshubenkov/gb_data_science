class ClsCell():
    def __init__(self, in_cells_count):
        self.in_cells_count = in_cells_count

    def __add__(self, other):
        return ClsCell(self.in_cells_count + other.in_cells_count)

    def __sub__(self, other):
        in_cells_count = self.in_cells_count - other.in_cells_count
        if in_cells_count >= 0:
            return ClsCell(in_cells_count)
        else:
            return f'Exception, result cell contains less 0 cells'

    def __mul__(self, other):
        return ClsCell(self.in_cells_count * other.in_cells_count)

    def __truediv__(self, other):
        return ClsCell(self.in_cells_count // other.in_cells_count)

    def make_order(self, parameter):
        string = ''
        idx = 0
        if self.in_cells_count <= parameter:
            return str('*' * self.in_cells_count) + '\n'
        else:
            while idx < self.in_cells_count // parameter:
                string = string + str('*' * parameter) + '\n'
                idx += 1
            return string + str('*' * (self.in_cells_count - parameter * idx))


objCell_1 = ClsCell(5)
objCell_2 = ClsCell(10)
objCell_3 = ClsCell(2)
objCell_4 = ClsCell(15)
objCell_5 = ClsCell(25)


objCell_6 = objCell_1 + objCell_2
print(objCell_6.in_cells_count)
print(objCell_6.make_order(5))

