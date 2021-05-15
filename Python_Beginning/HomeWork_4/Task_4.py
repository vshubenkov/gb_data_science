var_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def func_generator(var_list):
    flag = False
    for en1, el1 in enumerate(var_list):
        for en2, el2 in enumerate(var_list):
            if en1 != en2 and el1 == el2:
                flag = False
                break
            else:
                flag = True
        if flag:
            yield el1
        flag = False

for i in func_generator(var_list):
    print(i)

