var_a = int(input())
var_b = int(input())
i = 1

while var_a <= var_b:
    print(i, "-й день:", var_a, "км")
    var_a = var_a + (var_a / 100) * 10
    i += 1

print(i, "-й день:", var_a, "км")