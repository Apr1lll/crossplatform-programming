matrix = [
    [2, 4, 6],
    [9, 7, 8],
    [1, 10, 15]
]

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

for i in range(3):
    for j in range(3):
        if is_prime(matrix[i][j]):
            matrix[i][j] = 0
print(matrix)

transposed = []
for j in range(3):
    row = []
    for i in range(3):
        row.append(matrix[i][j])
    transposed.append(row)
print(transposed)

m = transposed
det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
     - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
     + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
print(det)