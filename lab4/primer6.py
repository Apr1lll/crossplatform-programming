A = [[1, 2, 3, 4], [5, 6, 7, 8]]
print('Массив A:')
for i in A:
    print(' '.join(list(map(str, i))))
s=0
for i in range(len(A)):
    for j in range(len(A[i])):
        s += A[i][j]
print("Пример 1. Сумма элементов: ", s)
s=0
for row in A:
    for elem in row:
        s += elem
print("Пример 2. Сумма элементов: ", s)

