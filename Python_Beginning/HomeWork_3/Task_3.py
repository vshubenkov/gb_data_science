def my_func(var_1, var_2, var_3):
    var_temp_list = [var_1, var_2, var_3]
    var_max_1 = max(var_temp_list)
    check = var_temp_list.remove(var_max_1)
    var_max_2 = max(var_temp_list)
    return var_max_1 + var_max_2, check


print(my_func(1, 2, 3))