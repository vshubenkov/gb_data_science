my_dict = {'key': []}
temp_list = my_dict.get('key')
my_dict.update({'key': temp_list.append('123')})  # Дополняем.
#my_dict.update({'another_key': 'yet_another_value'})  # Обновляем.

print(my_dict)