m = int(input('Введите количество строк'))
n = int(input('Введите количество столбцов'))
a = []
for i in range(m):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    a.append(b)
print('Исходный массив:')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

for i in range(m):
    for j in range(n):
        if a[i][j] < 0:
            a[i][j] = 0
        elif a[i][j] > 0:
            a[i][j] = 1

print('Измененный массив:')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
