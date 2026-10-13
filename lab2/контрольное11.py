def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


n = int(input("Введите число: "))

if n < 0:
    print("Факториал для отрицательных чисел не определён")
else:
    print(f"{n}! = {factorial(n)}")