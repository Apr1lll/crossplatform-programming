n = 5
A = []
for i in range(n):
    row = input().split()
    for j in range(len(row)):
        row[j] = int(row[j])
    A.append(row)
print(A)
