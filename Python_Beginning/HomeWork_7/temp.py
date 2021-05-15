import functools

list_1 = [1, 2, 3, 3, 6, 7]
list_2 = [1, 3, 3, 3, 6, 7]

list_help = map(lambda p, q: p == q, list_1, list_2)

if functools.reduce(lambda x, y: x and y, list_help, True):
    print("Списки одинаковые")
else:
    print("Списки не одинаковые")

def addition(n, n1):
    return n + n1

for i in map(lambda p, q: p == q, list_1, list_2):
    print(i)

# print(list(map(lambda p, q: p == q, list_1, list_2)))