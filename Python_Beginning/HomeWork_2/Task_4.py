var_input = str(input("Enter string of several words: "))
var_list = var_input.split()
print(var_list)
for i in var_list:
    print(i[:10])