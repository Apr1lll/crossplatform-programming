n = int(input('Введите нечетный порядок матрицы: '))
while n % 2 == 0:
    print('Порядок должен быть нечетным')
    n = int(input('Введите нечетный порядок матрицы: '))

A = []
for i in range(n):
    row = input().split()
    for j in range(n):
        row[j] = float(row[j])
    A.append(row)

maxi = 0
maxj = 0
for i in range(n):
    if A[i][i] > A[maxi][maxj]:
        maxi = i
        maxj = i
    if A[i][n - 1 - i] > A[maxi][maxj]:
        maxi = i
        maxj = n - 1 - i

c = n // 2
A[maxi][maxj], A[c][c] = A[c][c], A[maxi][maxj]

print('Новая матрица:')
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
