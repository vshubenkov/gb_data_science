import re

dict_number = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}

f1 = open("task_4_in.txt", 'r')
string_list = f1.readlines()
f1.close()

f2 = open("task_4_out.txt", 'w')

for i in string_list:
    if int(re.findall(r'\d', i)[0]) in dict_number:
        f2.write(i.replace(re.findall(r'^\w+', i)[0], dict_number[int(re.findall(r'\d', i)[0])]))

f2.close()
