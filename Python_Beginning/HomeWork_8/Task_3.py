class OwnError(Exception):
    def __init__(self, txt, i):
        self.txt = txt + ' ' + i


result_list = []
flag = True
while flag:
    inp_data = input("Введите список чисел: ")
    inp_list = inp_data.split()
    for i in inp_list:
        try:
            if isinstance(i, str):
                if i == 'stop':
                    flag = False
                    continue
                else:
                    if not i.isdigit():
                        raise OwnError("Вы ввели не число", i)
        except OwnError as err:
            print(err)
        else:
            result_list.append(i)
        finally:
            print(result_list)