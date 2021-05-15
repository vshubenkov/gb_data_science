import re

f = open("task_3.txt", 'r')
string_list = f.readlines()
sum = 0

for line in string_list:
#    print('String ' + str(i) + ': ', len(line.split()), line)
    var_zp = line.split()
    if int(re.search(r'[0-9]+', var_zp[1]).group()) <= 30000:
        print('Employee who has zp less than 30000rub: ' + var_zp[0])
    sum = sum + int(re.search(r'[0-9]+', var_zp[1]).group())

print('Middle zp of all employees:' + str(sum/len(string_list)))

f.close()