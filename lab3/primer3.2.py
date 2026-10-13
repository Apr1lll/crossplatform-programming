import random
Sum = 0
while True:
    a = random.randint(0, 10)
    print(a)
    if a == 5:
        break
    Sum += a
print(Sum)
