pos = 0
neg = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n > 0:
        pos += n
    else:
        neg += n
print('Сумма положительных:', pos)
print('Сумма отрицательных:', neg)
