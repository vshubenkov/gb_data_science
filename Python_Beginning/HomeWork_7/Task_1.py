import random
import functools

class ClsMatrix:
    def __init__(self, matrix):
        self.attr_matrix = matrix

    def __str__(self):
        temp_string = ''
        for i in self.attr_matrix:
            idx = str(i)
            temp_string = temp_string + idx + "\n"

        temp_string = temp_string[:-1]
        return temp_string

    def __add__(self, other):
        temp_list_1 = []
        temp_list_2 = []

        def sum(a, b):
            for idx1, idx2 in zip(a, b):
                for idx1_1, idx2_2 in zip(idx1, idx2):
                    temp_list_1.append(idx1_1 + idx2_2)
                temp_list_2.append(temp_list_1.copy())
                temp_list_1.clear()
            return temp_list_2
        try:
            if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q, ClsMatrix.MatrixShape(self), ClsMatrix.MatrixShape(other)), True):
                return ClsMatrix(sum(self.attr_matrix, other.attr_matrix))
            else:
                return ("Размер матриц не одинаковый")
        except TypeError:
            return ("Размер матриц не одинаковый")

    def MatrixShape(val):
        if val.attr_matrix and val.attr_matrix[0]:
            return [len(val.attr_matrix), len(val.attr_matrix[0])]
        else:
            return None

def FuncMatrixCreation(a, b):
     '''
     :param a: strings
     :param b: columns
     :return: list - matrix
     '''
     idx_strings = 0
     idx_columns = 0
     matrix = list()
     temp_list = list()
     while idx_strings < a:
         while idx_columns < b:
             temp_list.insert(idx_columns, random.randrange(1, 100))
             idx_columns += 1
         matrix.insert(idx_strings, temp_list.copy())
         temp_list.clear()
         idx_columns = 0
         idx_strings += 1

     return matrix


ObjMatrix_1 = ClsMatrix(FuncMatrixCreation(3, 1))
ObjMatrix_2 = ClsMatrix(FuncMatrixCreation(3, 3))

a = ClsMatrix.MatrixShape(ObjMatrix_1)
b = ClsMatrix.MatrixShape(ObjMatrix_2)
print(a, b)
ObjMatrix_3 = ObjMatrix_1 + ObjMatrix_2

print(ObjMatrix_1)
print('+')
print(ObjMatrix_2)
print('=')
print(ObjMatrix_3)
