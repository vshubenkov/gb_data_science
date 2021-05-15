var_input = int(input("Введите число:"))

var_input = str(var_input)
var_max, i = 0, 0

while i < len(var_input):
    if int(var_input[i]) > var_max:
        var_max = int(var_input[i])
    i += 1

print(var_max)