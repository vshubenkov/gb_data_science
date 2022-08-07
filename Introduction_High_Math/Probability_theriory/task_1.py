import random as rnd

#Четные красные, не четные черные, Зеро


for _ in range(50):
    step = rnd.randint(0, 37)
    if step == 0:
        print("Zero")
    elif step % 2 == 0:
        print("Red")
    else:
        print("Black")
    print(step)



