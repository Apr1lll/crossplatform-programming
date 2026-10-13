import math

a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

if a + b > c and a + c > b and b + c > a:
    # Периметр
    perimeter = a + b + c

    p = perimeter / 2

    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print(f"Периметр треугольника: {perimeter}")
    print(f"Площадь треугольника: {area}")
else:
    print("Ошибка: треугольник с такими сторонами не существует")