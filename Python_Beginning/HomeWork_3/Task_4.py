def my_func(x, y):
    if abs(y) > 1:
        y = abs(y) - 1
        return 1 / x * my_func(x, y)
    else:
        return 1 / x

print(my_func(2, -5))
