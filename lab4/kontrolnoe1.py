n = int(input('Введите порядок матрицы: '))
A = []
for i in range(n):
    row = input().split()
    for j in range(n):
        row[j] = int(row[j])
    A.append(row)

for i in range(n):
    maximum = A[i][0]
    for j in range(n):
        if A[i][j] > maximum:
            maximum = A[i][j]
    print('Наибольший в строке', i + 1, ':', maximum)

for j in range(n):
    minimum = A[0][j]
    for i in range(n):
        if A[i][j] < minimum:
            minimum = A[i][j]
    print('Наименьший в столбце', j + 1, ':', minimum)
