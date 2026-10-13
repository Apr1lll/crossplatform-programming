def diff(a, b):
    if a > b:
        return a - b
    else:
        return b - a

for i in range(1, 4):
    print(f"\n--- Пара чисел №{i} ---")
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    result = diff(x, y)
    print(f"Модуль разности |{x} - {y}| = {result}")