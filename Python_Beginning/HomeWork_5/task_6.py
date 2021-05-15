import re
f = open("task_6.txt", 'r')
string_list = f.readlines()
i = 1

school_subj_dict = {}

for line in string_list:
    print('String ' + str(i) + ': ', line.split())
    temp_gen = (int(re.findall(r'\d+', i1)[0]) for i1 in line.split() if re.findall(r'\d+', i1))

    summa = 0
    for idx, current in enumerate(temp_gen):
        if idx == 0:
            summa = current
        elif idx >= 1:
            summa = summa + current

    school_subj_dict[line.split()[0]] = summa
    print(school_subj_dict[line.split()[0]])
    i += 1


print(school_subj_dict)
f.close()
