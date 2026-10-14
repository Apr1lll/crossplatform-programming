n = 3
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

maximum = a[0][2]
for i in range(n):
    if maximum < a[i][2]:
        maximum = a[i][2]
print('Максимальный в 3 столбце:', maximum)

maximum = a[1][0]
for j in range(n):
    if maximum < a[1][j]:
        maximum = a[1][j]
print('Максимальный во второй строке:', maximum)
