import math


def ask_yes_no(question):
    while True:
        answer = input(f"{question} (да/нет): ").strip().lower()
        if answer in ("да", "д", "yes", "y"):
            return True
        elif answer in ("нет", "н", "no", "n"):
            return False
        else:
            print("Пожалуйста, ответьте 'да' или 'нет'.")


def main():
    print("=== Угадай фигуру ===")
    print("Загадайте одну из фигур: круг, квадрат, треугольник, прямоугольник.\n")

    if not ask_yes_no("У вашей фигуры есть углы?"):
        r = float(input("Введите радиус круга: "))
        area = math.pi * r ** 2
        print(f"\nВы загадали КРУГ.")
        print(f"Площадь круга: S = π·R² = {area:.4f}")

    else:
        corners = int(input("Сколько углов у фигуры? (3 или 4): "))

        if corners == 3:
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))
            c = float(input("Введите сторону c: "))

            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
                area = math.sqrt(p * (p - a) * (p - b) * (p - c))
                print(f"\nВы загадали ТРЕУГОЛЬНИК.")
                print(f"Площадь по формуле Герона: S = {area:.4f}")
            else:
                print("\nОшибка: треугольник с такими сторонами не существует.")

        elif corners == 4:
            if ask_yes_no("У фигуры все стороны равны?"):
                a = float(input("Введите сторону квадрата: "))
                area = a ** 2
                print(f"\nВы загадали КВАДРАТ.")
                print(f"Площадь квадрата: S = a² = {area:.4f}")
            else:
                a = float(input("Введите длину прямоугольника: "))
                b = float(input("Введите ширину прямоугольника: "))
                area = a * b
                print(f"\nВы загадали ПРЯМОУГОЛЬНИК.")
                print(f"Площадь прямоугольника: S = a·b = {area:.4f}")

        else:
            print("Не удалось определить фигуру: у фигуры должно быть 3 или 4 угла.")


main()