f1 = open('task_5.txt','w')

var_list = list(range(0, 20))
for i in var_list:
    f1.write(str(i) + ' ')
f1.close()

f1 = open('task_5.txt','r')
string_list = f1.readline()

sum = 0
for i in string_list.split():
    sum = sum + int(i)

print(sum)
f1.close()