my_list_1 = [7, 5, 3, 3, 2]
my_list_2 = my_list_1.copy()
var = True

while var:
    print(my_list_2)
    var_input = int(input())
    if var_input:
        var = True
        for ind, el in enumerate(my_list_1):
            if var_input >= el:
                my_list_2.insert(ind, var_input)
                break
            elif var_input < el and ind == len(my_list_1) - 1:
                my_list_2.append(var_input)
        my_list_1 = my_list_2.copy()
    else:
        var = False

# my_list_1.append(var_input)
# my_list_1.sort()
# my_list_1.reverse()