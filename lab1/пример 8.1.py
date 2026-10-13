n = int(input("Введите количество элементов: "))
a = []

for i in range(n):
    x = float(input(f"Введите элемент {i + 1}: "))
    a.append(x)

average = sum(a) / n

print("Среднее арифметическое =", average)
print("Максимальное значение =", max(a))
print("Минимальное значение =", min(a))