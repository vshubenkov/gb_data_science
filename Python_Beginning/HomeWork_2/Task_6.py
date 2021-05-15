
var_list = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]
# var_check = input('Enter yes/no to add new product: ')
#
# while var_check == 'yes':
#     var_product_name = input("Enter the name of the product: ")
#     var_product_cost = int(input("Enter the cost of the " + var_product_name + ": "))
#     var_product_count = int(input("Enter the count of the " + var_product_name + ": "))
#     var_product_unit = input("Enter the unit of the " + var_product_name + ": ")
#     var_list.append((len(var_list) + 1, {'название':var_product_name, 'цена': var_product_cost,
#                                      'количество': var_product_count, 'eд': var_product_unit}))
#     var_check = input('Enter yes/no to add new product: ')
#
# print(var_list)

var_dict_analysis = {"название": [], "цена": [], "количество": [], "eд": []}
# var_list_name = []
# var_list_cost = []
# var_list_cout = []
# var_list_unit = []

# for i in var_list:
#     var_list_name.append(i[1].get("название"))
#     var_list_cost.append(i[1].get("цена"))
#     var_list_cout.append(i[1].get("количество"))
#     var_list_unit.append(i[1].get("eд"))
#
# var_list_name = list(set(var_list_name))
# var_list_cost = list(set(var_list_cost))
# var_list_cout = list(set(var_list_cout))
# var_list_unit = list(set(var_list_unit))
#
# var_dict_analysis.update({"название": var_list_name})
# var_dict_analysis.update({"цена": var_list_cost})
# var_dict_analysis.update({"количество": var_list_cout})
# var_dict_analysis.update({"eд": var_list_unit})


for el, info_dict in var_list:
    for key, value in info_dict.items():
        var_dict_analysis[key].append(value)

print(var_dict_analysis)