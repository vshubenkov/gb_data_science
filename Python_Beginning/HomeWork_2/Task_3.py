var_month_nr = int(input("Введите номер месяца от 1 до 12: "))
var_list = ['зима', 'весна', 'лето', 'осень']

if var_month_nr == 12 or var_month_nr <= 2:
    print(var_list[0])
elif var_month_nr > 2 and var_month_nr <= 5:
    print(var_list[1])
elif var_month_nr > 5 and var_month_nr <= 8:
    print(var_list[2])
elif var_month_nr > 8 and var_month_nr <= 11:
    print(var_list[3])

# if var_month_nr in [12,1,2]:
#     print(var_list[0])
# elif var_month_nr in [3,4,5]:
#     print(var_list[1])

var_dict = {12: 'зима', 1: 'зима', 2: 'зима',
            3: 'весна', 4: 'весна', 5: 'весна',
            6: 'лето', 7: 'лето', 8: 'лето',
            9: 'осень', 10: 'осень', 11: 'осень'}

# var_dict = {зима: [12, 1, 2],
#             3: 'весна', 4: 'весна', 5: 'весна',
#             6: 'лето', 7: 'лето', 8: 'лето',
#             9: 'осень', 10: 'осень', 11: 'осень'}

print(var_dict[var_month_nr])