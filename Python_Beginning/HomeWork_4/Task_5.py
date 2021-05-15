from functools import reduce


def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el + el


var_generator = [i for i in range(99, 1001) if i % 2 == 0]
print(var_generator)

print(reduce(my_func, var_generator))