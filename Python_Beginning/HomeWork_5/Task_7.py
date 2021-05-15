import json

dict_firm_up, dict_firm_down = {}, {}
average_profit = 0
dict_average_profit = {}

with open("task_7.txt") as f_obj:
    for line in f_obj:
        print(line.split()[0], line.split()[2], line.split()[3])
        dict_firm_up[line.split()[0]] = int(line.split()[2]) - int(line.split()[3])

    idx_firms_up = 0
    for key in dict_firm_up:
        if dict_firm_up[key] > 0:
            average_profit = dict_firm_up[key] + average_profit
            idx_firms_up += 1

    if idx_firms_up > 0:
        dict_average_profit["average_profit"] = average_profit / idx_firms_up
    else:
        dict_average_profit["average_profit"] = "no firms_up"

    list_json = [dict_firm_up, dict_average_profit]

with open('task_7_out.json', 'w') as f:
    json.dump(list_json, f)