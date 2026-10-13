import math

def show_menu():
    print("\n=== Инженерный калькулятор ===")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("6. Квадратный корень (sqrt)")
    print("7. Синус (sin)")
    print("8. Косинус (cos)")
    print("9. Тангенс (tan)")
    print("10. Натуральный логарифм (ln)")
    print("11. Десятичный логарифм (log10)")
    print("12. Факториал (!)")
    print("0. Выход")


def calculate():
    while True:
        show_menu()
        choice = input("Выберите операцию: ")

        # Выход
        if choice == "0":
            print("До свидания!")
            break

        elif choice in ("6", "7", "8", "9", "10", "11", "12"):
            try:
                x = float(input("Введите число: "))

                if choice == "6":
                    if x < 0:
                        print("Ошибка: корень из отрицательного числа")
                    else:
                        print(f"√{x} = {math.sqrt(x)}")

                elif choice == "7":
                    print(f"sin({x}) = {math.sin(x)}")

                elif choice == "8":
                    print(f"cos({x}) = {math.cos(x)}")

                elif choice == "9":
                    print(f"tan({x}) = {math.tan(x)}")

                elif choice == "10":
                    if x <= 0:
                        print("Ошибка: логарифм определён только для x > 0")
                    else:
                        print(f"ln({x}) = {math.log(x)}")

                elif choice == "11":
                    if x <= 0:
                        print("Ошибка: логарифм определён только для x > 0")
                    else:
                        print(f"log10({x}) = {math.log10(x)}")

                elif choice == "12":
                    if x < 0 or x != int(x):
                        print("Ошибка: факториал определён только для целых неотрицательных чисел")
                    else:
                        print(f"{int(x)}! = {math.factorial(int(x))}")

            except ValueError:
                print("Ошибка: нужно ввести число")

        elif choice in ("1", "2", "3", "4", "5"):
            try:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))

                if choice == "1":
                    print(f"{a} + {b} = {a + b}")
                elif choice == "2":
                    print(f"{a} - {b} = {a - b}")
                elif choice == "3":
                    print(f"{a} * {b} = {a * b}")
                elif choice == "4":
                    if b == 0:
                        print("Ошибка: деление на ноль")
                    else:
                        print(f"{a} / {b} = {a / b}")
                elif choice == "5":
                    print(f"{a} ^ {b} = {a ** b}")

            except ValueError:
                print("Ошибка: нужно ввести числа")

        else:
            print("Ошибка: неизвестная операция")


calculate()