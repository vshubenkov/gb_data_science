var_benefit = int(input("Введите показатель выручки:"))
var_lost = int(input("Введите показатель издержек:"))

if var_benefit > var_lost:
    print("Выручка больше издержек")
    print("Рентабельность фирмы:" + str(((var_benefit - var_lost)/var_benefit)*100))
    var_employe = int(input("Введите количество сотрудников:"))
    print((var_benefit - var_lost)/var_employe)
elif var_lost > var_benefit:
    print("Издержеки больше выручки")
else:
    print("Фирма работает в ноль")


