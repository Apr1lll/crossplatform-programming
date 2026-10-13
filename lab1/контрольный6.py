a = float(input("Введите сторону A коробки: "))
b = float(input("Введите сторону B коробки: "))
c = float(input("Введите сторону C коробки: "))

m = float(input("Введите ширину двери M: "))
k = float(input("Введите высоту двери K: "))

sides = sorted([a, b, c])

if sides[0] <= m and sides[1] <= k or sides[0] <= k and sides[1] <= m:
    print("Коробка пройдёт в дверь")
else:
    print("Коробка не пройдёт в дверь")