var_generator = (i for i in range(19, 240) if i % 20 == 0 or i % 21 == 0)

for i in var_generator:
    print(i)