class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = [0, 1, 2, 0, 'a']

for i in inp_data:
    try:
        i = int(i)
        if i == 0:
            raise OwnError("Вы ввели 0! Делить на ноль нельзя")
    except ValueError:
        print("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        print(f"Все хорошо. Ваше число: {i}, на него можно делить")