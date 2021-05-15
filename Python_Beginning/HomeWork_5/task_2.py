f = open("task_2.txt", 'r')
string_list = f.readlines()
i = 1

for line in string_list:
    print('String ' + str(i) + ': ', len(line.split()), line)
    i += 1

f.close()