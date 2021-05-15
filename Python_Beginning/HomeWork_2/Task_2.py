var_list = input().split()

i = 0
print(var_list)
if len(var_list) > 1:
     while i < len(var_list):
         try:
             var_list[i],  var_list[i+1] = var_list[i+1], var_list[i]
         except IndexError:
             break
         i += 2
print(var_list)


i = 0

#Another method:
if len(var_list) % 2:
    while i < len(var_list) - 1:
        var_list[i],  var_list[i+1] = var_list[i+1], var_list[i]
        i += 2
else:
    while i < len(var_list):
        var_list[i],  var_list[i+1] = var_list[i+1], var_list[i]
        i += 2
print(var_list)

#Another method:
for i in range(0, len(var_list) - 1, 2):
    var_list[i],  var_list[i+1] = var_list[i+1], var_list[i]

print(var_list)

