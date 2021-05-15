var_ss_input = int(input("Введите число:"))

var_hh = var_ss_input // (3600)
var_mm = (var_ss_input // 60) % 60
var_ss = var_ss_input % 60

def get_time(var):
    if var <= 9:
        return str('0' + str(var))
    else:
        return str(var)

print(f"{get_time(var_hh)}:{get_time(var_mm)}:{get_time(var_ss)}")