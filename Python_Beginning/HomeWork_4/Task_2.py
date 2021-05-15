var_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

var_generator = (i for en, i in enumerate(var_list) if en != 0 and i > var_list[en - 1])

for i in var_generator:
    print(i)