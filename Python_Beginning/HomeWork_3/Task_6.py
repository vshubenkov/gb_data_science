def int_func(var):
    return var.title()

print(int_func("sdfsdf sdfsdf . 2323 sfdf"))


var_1 = 15
var_list = [var_1]
print(var_list, id(var_list[0]), id(var_1))
var_1 = 20
print(var_list, id(var_list[0]), id(var_1))
