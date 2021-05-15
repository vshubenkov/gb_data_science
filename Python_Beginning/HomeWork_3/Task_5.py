b = 0
flag = True
var_input_list = [0]


def func_check_symbol(var_1):
    if var_1 == 'x':
        return None
    else:
        return var_1


while var_input_list and flag:
    var_input = input("Введите числа через пробел, для выхода введите x: ")
    var_input_list = var_input.split(' ')
    for i in var_input_list:
        if func_check_symbol(i):
            b = b + int(i)
        else:
            flag = False
            break
    print("Сумма: ", b)


print(b)

