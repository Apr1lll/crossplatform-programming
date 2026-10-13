a = [0, 1, 2, 3, 4, 10, 13, 21, 34, 55, 89, 100, 16]

print("Элементы меньше 35:")
for x in a:
    if x < 35:
        print(x)

print("Чётные элементы меньше 35:")
for x in a:
    if x < 35 and x % 2 == 0:
        print(x)