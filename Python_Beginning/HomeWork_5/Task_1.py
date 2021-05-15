out_f = open("task_1.txt", "w")
var_input = str(input("Введите строку: "))

while var_input:
    out_f.write(var_input + '\n')
    var_input = str(input("Введите строку: "))

out_f.close()