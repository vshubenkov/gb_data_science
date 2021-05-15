from itertools import count
from itertools import cycle


for el in count(7):
    if el > 15:
        break
    else:
        print(el)


var = "abcdefj"
с = 0
for el in cycle(var):
    if с > len(var) - 1:
        break
    print(el)
    с += 1

