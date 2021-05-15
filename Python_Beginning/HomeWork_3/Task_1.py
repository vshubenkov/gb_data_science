def func_del(arg_1, arg_2):
    try:
        return arg_1/arg_2
    except ZeroDivisionError:
        return None

var_1 = input("Введите число 1: ")
var_2 = input("Введите число 2: ")
while var_1 and var_2:
    print(func_del(int(var_1), int(var_2)))
    var_1 = input("Введите число 1: ")
    var_2 = input("Введите число 2: ")